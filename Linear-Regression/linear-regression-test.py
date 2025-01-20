import unittest
import numpy as np
from linear_regression import compute_error_for_line_given_points, step_gradient, gradient_descent_runner

class TestLinearRegression(unittest.TestCase):

    def setUp(self):
        """Setup test data for use in various test cases"""
        # A small set of points for testing
        self.points = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])  # y = x + 1
        self.learning_rate = 0.0001
        self.initial_b = 0  # starting y-intercept
        self.initial_m = 0  # starting slope
        self.num_iterations = 100

    def test_compute_error_for_line_given_points(self):
        """Test the error computation function."""
        # Test for a line y = x + 1, the error should be 0 for these points.
        b = 1
        m = 1
        expected_error = 0  # Since the model perfectly fits the points
        error = compute_error_for_line_given_points(b, m, self.points)
        self.assertAlmostEqual(error, expected_error, places=2)

    def test_step_gradient(self):
        """Test the gradient calculation and update function."""
        b, m = 0, 0  # Initial values for b and m
        b_updated, m_updated = step_gradient(b, m, self.points, self.learning_rate)
        
        # Check if the updated values of b and m are different from initial (indicating learning)
        self.assertNotEqual(b_updated, b)
        self.assertNotEqual(m_updated, m)

    def test_gradient_descent_runner(self):
        """Test the gradient descent function with a small dataset."""
        b, m = gradient_descent_runner(self.points, self.initial_b, self.initial_m, self.learning_rate, self.num_iterations)
        
        # The final b and m values should be close to the expected values (since y = x + 1)
        expected_b = 1  # y = x + 1, so b should be around 1
        expected_m = 1  # slope should be 1
        
        self.assertAlmostEqual(b, expected_b, places=2)
        self.assertAlmostEqual(m, expected_m, places=2)

    def test_empty_data(self):
        """Test with an empty dataset (should raise an error)."""
        with self.assertRaises(ValueError):
            compute_error_for_line_given_points(0, 0, np.array([]))

    def test_single_data_point(self):
        """Test with a single data point (should not raise an error)."""
        points = np.array([[1, 2]])  # Single point, should be easy to compute
        b, m = gradient_descent_runner(points, 0, 0, self.learning_rate, self.num_iterations)
        
        # We expect the gradient descent to return a line close to the single point
        expected_b = 2  # y = x + 1, so for x = 1, y = 2
        expected_m = 1  # slope should be 1
        self.assertAlmostEqual(b, expected_b, places=2)
        self.assertAlmostEqual(m, expected_m, places=2)

if __name__ == '__main__':
    unittest.main()
