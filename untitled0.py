# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:29:18 2024

@author: DELL
"""

from gurobipy import *
m = Model()
x1 = m.addVar(vtype= GRB.CONTINUOUS, lb=0.0)
x2 = m.addVar(vtype= GRB.CONTINUOUS, lb=0.0)

m.addConstr(3*x1 + 2*x2 <= 11)
m.addConstr(3*x2 <= 11)
m.addConstr(x1 <= 1)




m.setObjective(9*x1 + 17*x2, sense =GRB.MAXIMIZE)
m.update()
m.optimize()

print(x1.x, x2.x, m.objVal)