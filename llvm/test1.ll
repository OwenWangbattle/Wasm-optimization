	.text
	.file	"test1.c"
	.globaltype	__stack_pointer, i32
	.functype	__original_main () -> (i32)
	.functype	printf (i32, i32) -> (i32)
	.functype	main (i32, i32) -> (i32)
	.section	.text.__original_main,"",@
	.hidden	__original_main                 # -- Begin function __original_main
	.globl	__original_main
	.type	__original_main,@function
__original_main:                        # @__original_main
	.functype	__original_main () -> (i32)
	.local  	i32
# %bb.0:
	global.get	__stack_pointer
	i32.const	16
	i32.sub 
	local.tee	0
	global.set	__stack_pointer
	local.get	0
	i64.const	515396075525
	i64.store	0
	i32.const	.L.str
	local.get	0
	call	printf
	drop
	local.get	0
	i32.const	16
	i32.add 
	global.set	__stack_pointer
	i32.const	0
                                        # fallthrough-return
	end_function
                                        # -- End function
	.section	.text.main,"",@
	.hidden	main                            # -- Begin function main
	.globl	main
	.type	main,@function
main:                                   # @main
	.functype	main (i32, i32) -> (i32)
# %bb.0:
	call	__original_main
                                        # fallthrough-return
	end_function
                                        # -- End function
	.type	.L.str,@object                  # @.str
	.section	.rodata..L.str,"S",@
.L.str:
	.asciz	"Factorial of %d is %d\n"
	.size	.L.str, 23

	.globl	__main_void
	.type	__main_void,@function
	.hidden	__main_void
.set __main_void, __original_main
	.ident	"clang version 18.1.2-wasi-sdk (https://github.com/llvm/llvm-project 26a1d6601d727a96f4301d0d8647b5a42760ae0c)"
	.no_dead_strip	__indirect_function_table
	.section	.custom_section.producers,"",@
	.int8	1
	.int8	12
	.ascii	"processed-by"
	.int8	1
	.int8	5
	.ascii	"clang"
	.int8	95
	.ascii	"18.1.2-wasi-sdk (https://github.com/llvm/llvm-project 26a1d6601d727a96f4301d0d8647b5a42760ae0c)"
	.section	.rodata..L.str,"S",@
	.section	.custom_section.target_features,"",@
	.int8	2
	.int8	43
	.int8	15
	.ascii	"mutable-globals"
	.int8	43
	.int8	8
	.ascii	"sign-ext"
	.section	.rodata..L.str,"S",@
