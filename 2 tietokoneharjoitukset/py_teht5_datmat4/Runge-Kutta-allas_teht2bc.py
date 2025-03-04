import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_method(func, y0, x_range, h):
    results = []
    x_values = np.arange(x_range[0], x_range[1] + h, h)
    y = y0

    for x in x_values:
        results.append((x, y))
        k1 = h * func(x, y)
        k2 = h * func(x + h/2, y + k1/2)
        k3 = h * func(x + h/2, y + k2/2)
        k4 = h * func(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4)/6

    return results

# Define the differential equation function
def equation(x, y):
    return 1 - 1/40 * y

# Define the exact solution function
def exact_solution(x):
    return 40 - 20 * np.exp(-x/40)

# Set initial conditions and parameters
initial_y = 20  # Initial value of y at x=0
x_interval = (0, 150)  # Interval for x
step_size = 1  # Step size for x

# Solve the differential equation using Runge-Kutta method
results_rk = runge_kutta_method(equation, initial_y, x_interval, step_size)

# Calculate exact solution values
exact_values = [(x, exact_solution(x)) for x, _ in results_rk]

# Display the results
print("Results using Runge-Kutta method with a step size of 1:")
for (x_rk, y_rk), (x_exact, y_exact) in zip(results_rk, exact_values):
    print(f"x = {x_rk}, Approximation = {y_rk:.9f}, Exact Solution = {y_exact:.9f}")

# Plot the results
plt.plot([x for x, _ in results_rk], [y for _, y in results_rk], label='Runge-Kutta Method (Approximation)', marker='o')
plt.plot([x for x, _ in exact_values], [y for _, y in exact_values], label='Exact Solution', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation using Runge-Kutta Method and Exact Solution')
plt.legend()
plt.show()