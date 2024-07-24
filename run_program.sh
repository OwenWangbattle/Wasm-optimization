#!/bin/bash

start_time=$(date +%s%3N)

wasmtime time program_8.wasm

end_time=$(date +%s%3N)
elapsed=$(( end_time - start_time ))

echo "Elapsed time: ${elapsed}ms"