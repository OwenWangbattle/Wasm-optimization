import os
import config
import subprocess
import sys
import re
import matplotlib.pyplot as plt
import math
def generate_testcases(n):
    for i in range(n):
        commandline = config.csmith_cmd.format(config.case_path + "/test{}.c".format(i))
        result = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
def compile_run(n):
    result = []
    for i in range(13):
        result.append(0)
    with open(config.output_path, 'w') as f:
            for i in range(n):
                print("Testcase {}".format(i))
                # Generate emcc -O0 testcases
                c_path1 = config.case_path + "/test{}.c".format(i)
                elf_path1 = config.case_path + "/test_O0_{}.wasm".format(i)
                commandline = config.emcc_opt0_cmd.format(c_path1, elf_path1)
                result3 = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out_path1 = config.case_path + "/test_O0_{}_opt.wasm".format(i)
                commandline = config.wasm_opt_cmd.format(elf_path1, out_path1)
                result3 = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                # Generate emcc -O3 testcases
                c_path2 = config.case_path + "/test{}.c".format(i)
                elf_path2 = config.case_path + "/test_O3_{}.wasm".format(i)
                commandline = config.emcc_opt3_cmd.format(c_path2, elf_path2)
                result3 = subprocess.run(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                    result[12] += 1
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
                    result[12] += 1
                    continue
                stderr_output2 = result2.stderr.decode('utf-8')
                user_time_match2 = re.search(r'(\d+\.\d+)user', stderr_output2)

                if user_time_match2:
                    user_time2 = float(user_time_match2.group(1))
                    print("Testcase {} User time 2: {}".format(i, float(user_time_match2.group(1))))
                else:
                    print("User time 2 not found in cycle {}".format(i))
                
                num = user_time2 / user_time1
                if num > 1.5:
                    result[11] += 1
                elif num < 0.5:
                    result[0] += 1
                else:
                    index = math.ceil((num - 0.5) / 0.1)
                    result[index] += 1
                print("Testcase {}: the execution time rate between emcc -O3 and emcc -O0 + wasm-opt -O3 is {}".format(i, num))
                f.write("Testcase {}: the execution time rate between emcc -O3 and emcc -O0 + wasm-opt -O3 is {}\n".format(i, num))
    f.close()
    return result       

def draw_graph(data, n):
    path = config.outgraph_path
    labels = ['<0.5', '0.5-0.6', '0.6-0.7', '0.7-0.8', '0.8-0.9', '0.9-1.0', '1.0-1.1', '1.1-1.2', '1.2-1.3', '1.3-1.4', '1.4-1.5', '>1.5', 'Timeout']
    sizes = data
    colors = 'blue'
        # 绘制直方图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, sizes, color=colors)
    plt.xlabel('Execution Time Ratio')
    plt.ylabel('Number of Test Cases')
    plt.title('Distribution of Execution Time Ratios')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, int(yval), ha='center', va='bottom')
    plt.text(0.95, 0.95, f'Total Samples: {n}', ha='right', va='top', transform=plt.gca().transAxes)
    plt.tight_layout()
    
    plt.savefig(path)
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python auto_test.py <testcase_num>")
        sys.exit(1)
    N = int(sys.argv[1])
    generate_testcases(N)
    result = compile_run(N)
    draw_graph(result, N)
    