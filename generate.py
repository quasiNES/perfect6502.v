#! /usr/bin/env python3
"""\
module Perfect6502 ( 
    input  reset,
    input  ready,
    input  clock0,
    output clock1,
    output clock2,
    input irq,
    input nmi,
    input so,
    output sync,
    output readNotWrite,
    output [15:0] address,
    inout [7:0] data
);

    wire [{{ netlist.nodeIsPulledUp|length - 1 }}:0] nodes;

    {% for isPullUp in netlist.nodeIsPulledUp -%}
    {% if isPullUp != 0 -%}
    pullup (nodes[{{ loop.index0 }}]);
    {% endif %}
    {% endfor %}

    {% for t in netlist.transistors -%}
    tranif1 (nodes[{{ t.drain }}], nodes[{{ t.source }}],  nodes[{{ t.gate }}]);
    {% endfor %}

    supply0 gnd;
    supply1 vcc;
    assign nodes[{{ netlist.NamedNode.vss }}] = 1'b0;
    assign nodes[{{ netlist.NamedNode.vcc }}] = 1'b1;


    assign nodes[{{ netlist.NamedNode.res }}] = reset,
           nodes[{{ netlist.NamedNode.rdy }}] = ready,
           nodes[{{ netlist.NamedNode.clk0 }}] = clock0,
           clock1 = nodes[{{ netlist.NamedNode.clk1out }}],
           clock2 = nodes[{{ netlist.NamedNode.clk2out }}],
           nodes[{{ netlist.NamedNode.irq }}] = irq, 
           nodes[{{ netlist.NamedNode.nmi }}] = nmi,
           nodes[{{ netlist.NamedNode.so }}] = so;
     //      sync   =  nodes[];

     assign readNotWrite = nodes[{{ netlist.NamedNode.rw }}] ;
     assign address = {
         {% for idx in range(0, 16) | reverse -%}
         nodes[{{ netlist.NamedNode['ab%d' % idx] }}]{% if idx != 0 %}, {% endif %}
         {% endfor %}
     };

     assign data = {
         {% for idx in range(0, 8) | reverse -%}
         nodes[{{ netlist.NamedNode['db%d' % idx] }}]{% if idx != 0 %}, {% endif %}
         {% endfor %}
     };

endmodule
"""

from perfect6502 import Perfect6502
from jinja2 import Template

t = Template(__doc__)
r = t.render(netlist=Perfect6502)
print(r)






