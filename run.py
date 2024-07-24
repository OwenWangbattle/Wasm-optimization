import subprocess
import time

# 路径到您的 WebAssembly 文件
wasm_file = "/mnt/home/wce/Test/wasm-opt/hello_optimized.wasm"

# 记录开始时间
start_time = time.time()

# 运行 WebAssembly 模块
result = subprocess.run(["wasmtime", wasm_file], capture_output=True, text=True)

# 记录结束时间
end_time = time.time()

# 计算运行时间
elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒

# 打印输出和运行时间
print(result.stdout)
print(f"Elapsed time: {elapsed_time:.2f} ms")