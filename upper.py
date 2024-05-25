# Function to print upper triangular pattern
def upper_triangular(n):
	for i in range(n, 0, -1):
		for j in range(1, i + 1):
			print("* ", end="")
		print("\r")

# Example: upper triangular pattern with n = 5
n = 5
upper_triangular(n)
