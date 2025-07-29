from scipy.optimize import linprog

# Coefficients of the objective function (to be minimized, so negate profit)
c = [-60, -32.5]

# Coefficients of the inequality constraints (A_ub @ x <= b_ub)
A_ub = [
    [1, 0],    # Crude A availability: x_A <= 18000
    [0, 1],    # Crude B availability: x_B <= 32000
    [0.6, 0.85], # Gasoline market demand: 0.6*x_A + 0.85*x_B <= 20000
    [0.4, 0.15]  # Lube oil market demand: 0.4*x_A + 0.15*x_B <= 12000
]

# Right-hand side of the inequality constraints
b_ub = [18000, 32000, 20000, 12000]

# Bounds for the variables (x_A >= 0, x_B >= 0)
x_A_bounds = (0, None)
x_B_bounds = (0, None)
bounds = [x_A_bounds, x_B_bounds]

# Solve the linear programming problem using the 'highs' method (recommended for general LP)
# 'simplex' can also be used, but 'highs' is generally more performant.
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Print the results
if result.success:
    print(f"Optimization successful: {result.success}")
    print(f"Optimal barrels of Crude A to use: {result.x[0]:.2f}")
    print(f"Optimal barrels of Crude B to use: {result.x[1]:.2f}")
    print(f"Maximum profit: ${-result.fun:.2f}") # Negate result.fun to get max profit
    
    # Calculate quantities of products produced
    gasoline_produced = 0.6 * result.x[0] + 0.85 * result.x[1]
    lube_oil_produced = 0.4 * result.x[0] + 0.15 * result.x[1]
    
    print(f"\nGasoline produced: {gasoline_produced:.2f} barrels")
    print(f"Lube Oil produced: {lube_oil_produced:.2f} barrels")
else:
    print(f"Optimization failed: {result.message}")
