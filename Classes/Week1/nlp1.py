#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:11:44 2025

@author: josenino-mora
"""

from gurobipy import Model, GRB

# Create a Gurobi model
model = Model("Nonlinear_Program")

# Define variables
x1 = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="x1")
x2 = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="x2")

# Set objective function: 
model.setObjective(3*x1**2 - 4*x2, GRB.MAXIMIZE)

# Add constraints
model.addConstr(x1 * x2 <= 4, "nonlinear_constraint1")
model.addConstr(x1**2 + x2**2 <= 16, "nonlinear_constraint2")

# Solve the model
model.optimize()

# Print results
if model.status == GRB.OPTIMAL:
    print(f"Optimal solution: x1 = {x1.x}, x2 = {x2.x}")
    print(f"Optimal objective value: {model.objVal}")
else:
    print("No optimal solution found.")
    