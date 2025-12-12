RTL=../rtl/fsm_rtl.sv
TB=../tb/tb_fsm_min.sv
OUT=build/tb.out

all: run

run:
	mkdir -p build
	iverilog -g2012 -o $(OUT) $(RTL) $(TB)
	vvp $(OUT)

clean:
	rm -rf build
