# Function to print a lower triangular pattern
def lower_triangular(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print("* ", end="")
		print("\r")

# Example: Print a lower triangular  with 5 rows
n = 5
lower_triangular(n)
