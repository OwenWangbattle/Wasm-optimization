import os

csmith_path = '/mnt/home/wce/csmith/src/csmith'
csmith_cmd = csmith_path + " --max-funcs 5 --no-safe-math --max-expr-complexity 3 > {}"
csmith_runtime = '/mnt/home/wce/csmith/runtime'

emcc_opt3_cmd = 'emcc -w -g -O3 -I' + csmith_runtime + ' {} -s WASM=1 -o {}'
emcc_opt0_cmd = 'emcc -w -g -O0 -I' + csmith_runtime + ' {} -s WASM=1 -o {}'

wasm_opt_cmd = 'wasm-opt {} -O3 --enable-sign-ext -o {}'

case_path = "/mnt/home/wce/Test/wasm-opt/testcases"

output_path = "/mnt/home/wce/Test/wasm-opt/result/output.txt"               # output file

outgraph_path = "/mnt/home/wce/Test/wasm-opt/result/graph.png"              # output graph