import numpy as np

# Linear algebra practice
# Trying to understand matrix operations better

def matrix_multiply(A, B):
    """Multiply two matrices"""
    # Should I use np.dot or @ operator?
    # result = np.dot(A, B)
    result = A @ B
    return result

def transpose_matrix(A):
    """Transpose a matrix"""
    return A.T

def calculate_determinant(A):
    """Calculate determinant"""
    # TODO: implement this without using np.linalg.det
    # Want to understand the math better
    return np.linalg.det(A)

def inverse_matrix(A):
    """Calculate matrix inverse"""
    # TODO: add check for singular matrix
    try:
        return np.linalg.inv(A)
    except:
        print("Matrix is singular")
        return None

def solve_linear_system(A, b):
    """Solve Ax = b"""
    # TODO: is this the right function to use?
    x = np.linalg.solve(A, b)
    return x

# TODO: implement eigenvalue calculation
# def calculate_eigenvalues(A):
#     

# TODO: implement SVD decomposition
# Getting confused by the documentation

if __name__ == "__main__":
    # Test matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matrix A:")
    print(A)
    
    print("\nMatrix B:")
    print(B)
    
    # result = matrix_multiply(A, B)  # dimensions don't match? getting errors
    
    # TODO: add more test cases
    # TODO: add error handling for dimension mismatches
