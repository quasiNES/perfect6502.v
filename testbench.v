module testbench;

    reg clock0;
    reg reset;
    wire [7:0] data;

    Perfect6502 perfect6502 ( 
        .reset(reset),
        .ready(1'b1),
        .clock0(clock0),
        .clock1(),
        .clock2(),
        .irq(1'b1),
        .nmi(1'b1),
	.so(1'b0),
        .sync(),
        .readNotWrite(),
        .address(),
        .data()
    );

    // assign data = perfect6502.readNotWrite ? 8'b0 : 8'hzz;

    initial begin
        forever begin
	    clock0 = 1'b0; #1;
	    clock0 = 1'b1; #1;
	end
    end

    initial begin
        $dumpfile("perfect.vcd");
	$dumpvars(0); //, clock0, reset, perfect6502.clock1, perfect6502.clock2, perfect6502.address);
        reset = 1'b0; #20;
	reset = 1'b1; #10;
	$finish;
    end
endmodule
