import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

R = 1

def objective(h):
    return -(1/3) * np.pi * (2*R*h - h**2) * h  # Negative for minimization

# Bounds and constraints
bounds = [(0, 2*R)]
cons = ({'type': 'ineq', 'fun': lambda h: 2*R*h - h**2})  # Ensure x² >= 0

result = minimize(objective, x0=1, bounds=bounds, constraints=cons)
h_optimal = result.x[0]
x_optimal = np.sqrt(2*R*h_optimal - h_optimal**2)
V_optimal = -result.fun

print(f"Optimal height (h): {h_optimal}")
print(f"Optimal radius (x): {x_optimal}")
print(f"Maximum Volume (V): {V_optimal}")

# Visualization
h_values = np.linspace(0, 2*R, 100)
x_values = np.sqrt(2 * R * h_values - h_values**2)
V_values = (1/3) * np.pi * x_values**2 * h_values

plt.plot(h_values, V_values, label="Volume vs. Height")
plt.axvline(h_optimal, color='r', linestyle='--', label=f"Optimal h = {h_optimal:.3f}")
plt.xlabel("Height (h)")
plt.ylabel("Volume (V)")
plt.legend()
plt.grid(True)
plt.title("Optimization of Cone Volume inside a Sphere")
plt.show()
