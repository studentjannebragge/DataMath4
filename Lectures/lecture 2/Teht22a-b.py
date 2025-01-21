import numpy as np


def fixed_point_iteration(func, initial_guess, tol=1e-6, max_iterations=100):
    """
    Fixed-point iteration method for finding a root of a function.

    Parameters:
    - func: The function for which to find the root.
    - initial_guess: Initial guess for the root.
    - tol: Tolerance for stopping criteria (default: 1e-6).
    - max_iterations: Maximum number of iterations (default: 100).

    Returns:
    - root: The estimated root.
    - iterations: Number of iterations performed.
    """
    
    x = initial_guess

    for iteration in range(max_iterations):
        x_new = func(x)

        if abs(x_new - x) < tol:
            print(f"Converged to solution after {iteration + 1} iterations.")
            return x_new, iteration + 1
        
        x = x_new
        if x <= 0:
            x=0.0001
        if x > 20000:
            x=20000
                    

    print("Fixed-point iteration did not converge within the maximum number of iterations.")
    return None, max_iterations

# Define the function and its fixed-point equivalent
euler_number = np.e

def f(x):
    return  3*(x**2) - euler_number**x #  x**3 -x -1
        # f(x)=0 on alkuperäinen tehtävänanto
def g(x):
    # Rearrange f(x) = 0 to find g(x), joka on muodostettu f(x):stä, jolloin g(x) = x
    return  np.sqrt(0.333*euler_number**x) #  x**3 - 1

# Set the initial guess and interval [1, 2]
initial_guess = 1.5

# Apply the fixed-point iteration method
root_estimate, num_iterations = fixed_point_iteration(g, initial_guess)

print("Estimated root:", root_estimate)
print("Number of iterations:", num_iterations)

