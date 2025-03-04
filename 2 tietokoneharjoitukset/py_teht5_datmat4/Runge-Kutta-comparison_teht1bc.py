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
    return y + x

# Define the exact solution function
def exact_solution(x):
    return np.exp(x) - x - 1

# Set initial conditions and parameters
initial_y = 0  # Initial value of y at x=0
x_interval = (0, 1)  # Interval for x
step_size = 0.2  # Step size for x

# Solve the differential equation using Runge-Kutta method
results_rk = runge_kutta_method(equation, initial_y, x_interval, step_size)

# Calculate exact solution values
# exact_values = [(x, exact_solution(x)) for x, _ in results_rk]
x2=np.arange(0, 1.01, 0.01)
y_values_exact = exact_solution(x2)
# Display the results
print("Results using Runge-Kutta method with a step size of 0.2:")
for x, y in results_rk:
    print(f"x = {x:.6f}, y = {y:.6f}")

# Plot the results
plt.plot([x for x, _ in results_rk], [y for _, y in results_rk], label='Runge-Kutta')
plt.plot(x2, y_values_exact, label='Exact Solution', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of y\' = y + x using Runge-Kutta method')
plt.legend()
plt.show()
