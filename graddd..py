# Define the function that we're interested in minimizing
def function(x):
    return (x + 3)**2

# Define the gradient (derivative) of the function
def gradient(x):
    return 2 * (x + 3)

# Implement the gradient descent algorithm
def gradient_descent(starting_point, learning_rate, convergence_threshold, max_iterations):
    x = starting_point  # This is our starting value for 'x'
    
    # We will update 'x' iteratively
    for i in range(max_iterations):
        grad = gradient(x)  # Calculate the gradient at the current 'x'
        
        # Update 'x' by taking a step in the direction opposite to the gradient
        x = x - learning_rate * grad

        # If the gradient is small enough, we stop and consider we found the minimum
        if abs(grad) < convergence_threshold:
            break

    return x, i  # Return the position of the minimum and the number of iterations

# Set the parameters for the gradient descent
starting_point = 2.0  # This is our initial guess for 'x'
learning_rate = 0.1   # This determines how big a step we take on each iteration
convergence_threshold = 1e-6  # This tells us when to stop the algorithm
max_iterations = 10000  # We also stop if we reach this many iterations

# Run the gradient descent algorithm and print the results
minimum, num_iterations = gradient_descent(starting_point, learning_rate, convergence_threshold, max_iterations)
print(f"Local minimum occurs at x = {minimum}")
print(f"Number of iterations: {num_iterations}")
