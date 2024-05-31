from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from typing import FrozenSet
from automathon import DFA as DFA2

# TBD: find a way to remove the numbers inside the states (circles)
# test run
regex = "(a|b)*"
regex = "(bab|bbb)a*b*(a*|b*)(ba)*(aba)(bab|aba)*bb(a|b)*(bab|aba)(a|b)*"
nfa = NFA.from_regex(regex, input_symbols=frozenset(["a", "b"]))
dfa = DFA.from_nfa(nfa)
# print(dir(dfa))
""" print(set(dfa.states))
print(dfa.input_symbols)
print(dfa.transitions)
print(dfa.initial_state)
print(dfa.final_states) """

q = set(dfa.states)
sigma = set(dfa.input_symbols)
delta = set(dfa.transitions)
initial_state = dfa.initial_state
f = set(dfa.final_states)

automata = DFA2(q, sigma, delta, initial_state, f)
print(dir(automata))
# print(automata.view("test"))
automata.view(
    file_name="DFA Custom Styling",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)
# dfa.show_diagram(path="\img")