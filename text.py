import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Training data for XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([[0], [1], [1], [0]])

# Initialize random weights
weights_input_hidden = np.random.randn(2, 2)
weights_hidden_output = np.random.randn(2, 1)

# Sigmoid activation and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Train the neural net
learning_rate = 0.5
for epoch in range(5000):
    # Forward pass
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)

    # Calculate error
    error = y - final_output

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    d_hidden = np.dot(d_output, weights_hidden_output.T) * sigmoid_derivative(hidden_output)

    # Update weights
    weights_hidden_output += np.dot(hidden_output.T, d_output) * learning_rate
    weights_input_hidden += np.dot(X.T, d_hidden) * learning_rate

# Test results
print("🧠 Trained Neural Network Results:")
for i in range(len(X)):
    print(f"Input: {X[i]} → Predicted: {final_output[i][0]:.3f}")
