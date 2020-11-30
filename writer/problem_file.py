""" Writes the problem file.
"""

from typing import NamedTuple
from utils import depth, agts, nb_agts

""" Generates the string representing the goal.
"""
def str_goal(base):
    res = ''

    for d in range(0, depth()+1):
        res += '\t\t' + base.repr_depth(d) + '\n'

    return res

def numToAgnum(myString):
    digits=['0','1','2','3','4','5','6','7','8','9']
    resStr=''
    for i in range(1,len(myString)-1):
        if myString[i-1]==' ' and myString[i] in digits:
            resStr+="ag"+myString[i]
        else:resStr+=myString[i]
    return resStr


""" Generates the problem file (agents, initial state and goal).
"""
def print_problem_file(base, file):
    file.write(';; Gossip problem - PDDL problem file\n')
    file.write(';; depth ' + str(depth()) + ', ' + str(nb_agts()) + ' agents\n\n')

    file.write('(define (problem gossip)\n')
    file.write('\t(:domain gossip)\n\n')

    s_as_constant_gives_me_errors='\t\t' + ' '.join(str(atom) for atom in base.get_atoms_of_depth(0)) + '\n'
    s_as_constant_gives_me_errors=s_as_constant_gives_me_errors.replace('(','').replace(')','')
    file.write('\t(:objects ' + ' '.join("ag"+str(i) for i in agts()) +'\n'+s_as_constant_gives_me_errors+ ')\n\n')

    file.write('\t(:init\n')
    file.write('\t\t' + ' '.join(str(atom) for atom in base.get_atoms_of_depth(0)) + '\n')
    init_S='\t\t' + ' '.join(str(atom) for atom in base.get_atoms_of_depth(1) if atom.is_initial()) + '\n'
    init_S=numToAgnum(init_S)
    file.write(init_S)
    file.write('\t)\n\n')

    file.write('\t(:goal (and\n')
    goal_S=str_goal(base) + '\t))\n'
    goal_S=numToAgnum(goal_S)
    file.write(goal_S)

    file.write(')\n')