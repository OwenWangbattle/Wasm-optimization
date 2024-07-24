import os
import config
import subprocess
import sys
import re

def generate_testcases(n):
    for i in range(n):
        commandline = config.csmith_cmd.format(config.case_path + "/test{}.c".format(i))
        result = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
def compile_run(n):
    with open(config.output_path, 'w') as f:
        for _ in range(3):
            for i in range(n):
                print("Testcase {}".format(i))
                # Generate emcc -O0 testcases
                c_path1 = config.case_path + "/test{}.c".format(i)
                elf_path1 = config.case_path + "/test_O0_{}.wasm".format(i)
                commandline = config.emcc_opt0_cmd.format(c_path1, elf_path1)
                result = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out_path1 = config.case_path + "/test_O0_{}_opt.wasm".format(i)
                commandline = config.wasm_opt_cmd.format(elf_path1, out_path1)
                result = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                # Generate emcc -O3 testcases
                c_path2 = config.case_path + "/test{}.c".format(i)
                elf_path2 = config.case_path + "/test_O3_{}.wasm".format(i)
                commandline = config.emcc_opt3_cmd.format(c_path2, elf_path2)
                result = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # out_path2 = config.case_path + "/test_O3_{}_opt.wasm".format(i)
                # commmandline = config.wasm_opt_cmd.format(elf_path2, out_path2) 
                # result = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print("Testcase {} compiled".format(i))
                user_time1 = 0
                user_time2 = 0
                command1 = "time wasmtime {}".format(out_path1)
                command2 = "time wasmtime {}".format(elf_path2)
                flag = False

                try:
                    result1 = subprocess.run(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
                except subprocess.TimeoutExpired:
                    print("Testcase {} timeout".format(i))
                    flag = True
                    continue
                stderr_output1 = result1.stderr.decode('utf-8')
                user_time_match1 = re.search(r'(\d+\.\d+)user', stderr_output1)
                if user_time_match1:
                    user_time1 = float(user_time_match1.group(1))
                    print("Testcase {} User time 1: {}".format(i, float(user_time_match1.group(1))))
                else:
                    print("User time 1 not found in cycle {}".format(i))

                try:
                    result2 = subprocess.run(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
                except subprocess.TimeoutExpired:
                    print("Testcase {} timeout".format(i))
                    flag = True
                    continue
                stderr_output2 = result2.stderr.decode('utf-8')
                user_time_match2 = re.search(r'(\d+\.\d+)user', stderr_output2)

                if user_time_match2:
                    user_time2 = float(user_time_match2.group(1))
                    print("Testcase {} User time 2: {}".format(i, float(user_time_match2.group(1))))
                else:
                    print("User time 2 not found in cycle {}".format(i))
                
                result = user_time2 - user_time1
                print("Testcase {}: the time difference between emcc -O0 and emcc -O3 is {}".format(i, result))
                f.write("Testcase {}: the time difference between emcc -O0 and emcc -O3 is {}\n".format(i, result))

    
    f.close()
            

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python auto_test.py <testcase_num>")
        sys.exit(1)
    N = int(sys.argv[1])
    generate_testcases(N)
    compile_run(N)
    