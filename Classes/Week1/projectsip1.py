from gurobipy import *

m = 3 # number of years

n = 5 # number of projects

years = range(1, m+1) # list [1, ..., m]

projects = range(1, n+1)  # list [1, ..., n]

# primal objective coefficients

r_coeff = [20, 40, 20, 15, 30] 

# left-hand side (LHS) coefficients (matrix A)

A_coeff = [[5, 4, 3, 7, 8],
     [1, 7, 9, 4, 6],
     [8,  10, 2, 1, 10]]

# right-hand side (RHS) coefficients

b_coeff = [25, 25, 25]

r = {j : r_coeff[j-1] for j in projects}

A = {i : {j : A_coeff[i-1][j-1] for j in projects} 
    for i in years}

b = {i : b_coeff[i-1] for i in years}

model = Model('projectsip1')

# uncomment next line for linear relaxation (continuous variables)
# x = model.addVars(projects, name="x") # quantity produced

# uncomment next line for binary variables
x = model.addVars(projects, name="x", vtype=GRB.BINARY)

# uncomment next line for general integer variables
# x = model.addVars(projects, name="x", vtype=GRB.INTEGER)

# Budget capacity constraints
model.addConstrs((quicksum(A[i][j] * x[j] for j in projects)
                           <= b[i] 
                            for i in years))
# Variable upper bound constraints
model.addConstrs((x[j] <= 1 for j in projects))

# Objective
obj = quicksum(r[j] * x[j] for j in projects)

model.setObjective(obj, GRB.MAXIMIZE)

# disable Presolve
model.setParam(GRB.Param.Presolve, 0)
# disable Heuristics
model.setParam(GRB.Param.Heuristics, 0)
# disable Cuts
model.setParam(GRB.Param.Cuts, 0)
        
model.optimize()


# Display solution (print the name of each variable and the solution value)
print('--------------------------------')
print('\nOptimal solution:\n')

print('Variable Information:')
                 
for v in model.getVars():
    print("%s %s %8.2f" % 
              (v.Varname, "=", v.X))
    
    print(" ")
        
print('\nOptimal objective value: %g' % model.objVal)
