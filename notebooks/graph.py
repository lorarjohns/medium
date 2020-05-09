# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: 'Python 3.6.8 64-bit (''venv-sci'': venv)'
#     name: python36864bitvenvscivenv55fc700d3ea9447888c06400e9b2b088
# ---

import pygraphviz as pgv

G=pgv.AGraph(strict=False,directed=True,pad=0.5,
            nodesep='1',ranksep='.1')

G.graph_attr['label']='How to recover your Jupyter Notebook\n(@rayljohns)'
G.graph_attr['splines']='ortho'
G.node_attr['shape']='box'
G.node_attr['style']='rounded'
G.edge_attr['color']='blue'

G.add_node('start', shape='box', style='rounded,bold')
G.add_node('a', shape='box', label='How much did you lose?')
G.add_edge('start', 'a')

G.add_node('b', label='A few cells', style='filled,rounded', fillcolor='yellow')
G.add_node('c', label='A whole notebook', style='filled,rounded', fillcolor='orange')
G.add_node('d', label='More than one\nnotebook', style='filled,rounded', fillcolor='red')
G.add_edge('a','b')
G.add_edge('a','c')
G.add_edge('a','d')

G.add_node('e', label='Is the notebook \nstill running?')
G.add_edge('b','e')
G.add_node('f', label='Use In[] or %history\nmagic to recover the\nlast few cells', color='green')
G.add_edge('e','f', label='yes')

G.add_node('g', label='Is the kernel\nstill running?')
G.add_edge('e','g',label='no')
G.add_edge('c', 'g')

G.add_node('h', label='write session history\nto disk with\n%notebook filename.ipynb\nor %history -f filename.py', color='green')
G.add_edge('g', 'h', label='yes')

G.add_node('i', label='Use sqlite3 to\naccess IPython\nhistory database')
G.add_edge('g','i',label='no')
G.add_edge('d','i')

G.add_node('j', label='Can you eyeball it?')
G.add_edge('i','j')
G.add_node('k', label='Use SQL to\nselect rows\nthat match\n criteria\nin history table')
G.add_edge('j','k',label='yes')

G.add_node('l', label='Join tables on\n session ID\nand filter\n with SQL')
G.add_edge('j','l',label='no')

G.add_node('m', label='Export SQL results\nto .py file', color='green')
G.add_edge('k','m')
G.add_edge('l','m')

G.add_node('n', label='Convert .py file\nto .ipynb\nwith jupytext', style='bold,rounded', color='blue')
G.add_edge('m','n')
G.add_edge('h', 'n')

G.add_node('o', label='finish!',style='bold,rounded')
G.add_edge('n','o')

G.layout(prog='dot')
#G.layout()

G.draw('file.png')

neato, dot, twopi, circo, fdp, nop, wc, acyclic, gvpr, gvcolor, ccomps, sccmap, tred, sfdp, unflatten.
