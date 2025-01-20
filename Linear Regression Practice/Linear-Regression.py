import numpy as np

def compute_error_for_line_given_points(b, m, points):
    """ Compute the total error (Mean Squared Error) of the model """
    x = points[:, 0]
    y = points[:, 1]
    predictions = m * x + b
    error = np.mean((y - predictions) ** 2)
    return error

def step_gradient(b_current, m_current, points, learning_rate):
    """ Perform one step of gradient descent """
    x = points[:, 0]
    y = points[:, 1]
    
    # Compute gradients for b and m
    N = len(points)
    predictions = m_current * x + b_current
    error = y - predictions
    b_gradient = -2 * np.mean(error)
    m_gradient = -2 * np.mean(error * x)
    
    # Update parameters
    new_b = b_current - learning_rate * b_gradient
    new_m = m_current - learning_rate * m_gradient
    return new_b, new_m

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    """ Run gradient descent to minimize the error """
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learning_rate)
        
        # Optional: print the error every 100 iterations
        if i % 100 == 0:
            error = compute_error_for_line_given_points(b, m, points)
            print(f"Iteration {i}: Error = {error}")
    
    return b, m

def run():
    # Load dataset
    points = np.genfromtxt("data.csv", delimiter=",")
    
    # Set parameters
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    num_iterations = 1000

    # Print starting info
    print(f"Starting gradient descent at b = {initial_b}, m = {initial_m}")
    initial_error = compute_error_for_line_given_points(initial_b, initial_m, points)
    print(f"Initial error = {initial_error}")
    
    # Run gradient descent
    b, m = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    
    # Print the results
    final_error = compute_error_for_line_given_points(b, m, points)
    print(f"After {num_iterations} iterations, b = {b}, m = {m}, error = {final_error}")

if __name__ == '__main__':
    run()
