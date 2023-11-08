from sympy import symbols, solve

# Redefining the variables and the given equation
mu_n, C_ox, W_2, L_2, W_3, L_3, V_DD, V_t, V_X = symbols('mu_n C_ox W_2 L_2 W_3 L_3 V_DD V_t V_X')

# Given equation
equation = (mu_n*C_ox/2 * (W_2/L_2) / (mu_n*C_ox/2 * (W_3/L_3))) * (V_DD - V_X - V_t)**2 - (V_X - V_t)**2

# Solving for V_X
V_X_solution = solve(equation, V_X)
print(V_X_solution)