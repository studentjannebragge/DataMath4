import numpy as np

# Define the system of equations
def equations(vars):
    x, y = vars
    eq1 = y * x**3 - x * y**2 + 2
    eq2 = x + y + x * y - 5
    return np.array([eq1, eq2])

# Compute the Jacobian matrix
def jacobian(vars):
    x, y = vars
    df1_dx = 3 * x**2 * y - y**2
    df1_dy = x**3 - 2 * x * y
    df2_dx = 1 + y
    df2_dy = x + x

    return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])

# Newton-Raphson method
def newton_raphson(initial_guess, tol=1e-6, max_iterations=100):
    vars = np.array(initial_guess)

    for iteration in range(max_iterations):
        f = equations(vars)
        J = jacobian(vars)

        # Update using the inverse of the Jacobian matrix
        # vars -= np.linalg.solve(J, f)
        
        # Directly perform matrix operations without linalg.inv or np.dot
        det_J = J[0, 0] * J[1, 1] - J[0, 1] * J[1, 0]
        J_inv = np.array([[J[1, 1], -J[0, 1]], [-J[1, 0], J[0, 0]]]) / det_J

        vars -= np.array([f[0] * J_inv[0, 0] + f[1] * J_inv[0, 1], f[0] * J_inv[1, 0] + f[1] * J_inv[1, 1]])


        # Check for convergence
        #if np.linalg.norm(f, ord=np.inf) < tol:
        if np.max(np.abs(f)) < tol:
            print(f"Converged to solution after {iteration + 1} iterations.")
            return vars

    print("Newton-Raphson method did not converge within the maximum number of iterations.")
    return None

# Initial guess
initial_guess = [1.0, 1.0]

# Apply the Newton-Raphson method
solution = newton_raphson(initial_guess)

if solution is not None:
    print("Approximate solution:", solution)