import numpy as np

def bisection_method(func, a, b, tol=1e-6, max_iterations=100):
    """
    Bisection method for finding a zero of a function within a given interval.

    Parameters:
    - func: The function for which to find the zero.
    - a, b: The interval [a, b] in which to search for the zero.
    - tol: Tolerance for stopping criteria (default: 1e-6).
    - max_iterations: Maximum number of iterations (default: 100).

    Returns:
    - root: The estimated zero.
    - iterations: Number of iterations performed.
    """

    if func(a) * func(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    iterations = 0

    while (b - a) / 2 > tol and iterations < max_iterations:
        c = (a + b) / 2
        if func(c) == 0:
            return c, iterations
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    return (a + b) / 2, iterations

# Define the function
def f(x):
    # return x**3 - 3
    # return np.log(x)+x
    return x-np.e**(-(x**2)) 
# Set the interval [lower_bound, upper_bound]
# lower_bound = 0
# upper_bound = 3
# lower_bound = 0.1
# upper_bound = 1
lower_bound = 0
upper_bound = 1

# Apply the bisection method
zero_estimate, num_iterations = bisection_method(f, lower_bound, upper_bound)

print("Estimated zero:", zero_estimate)
print("Number of iterations:", num_iterations)

# luonnollinen logaritmi, esim. luvusta 2:
test=np.log(2)
# Neperin luku e:
euler_number = np.e
