
.PHONY: all

all: testbench

perfect6502.v: generate.py perfect6502.py
	python3.6 generate.py perfect6502.py >perfect6502.v

testbench: testbench.v perfect6502.v
	iverilog -o testbench testbench.v perfect6502.v

