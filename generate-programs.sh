#!/bin/bash

n=$1
output_dir="C_programs"
mkdir -p $output_dir

for ((i=1; i<=n; i++))
do
    csmith --max-funcs 5 --no-safe-math --max-expr-complexity 3  > $output_dir/program_$i.c
    echo "Generated program_$i.c"
done

