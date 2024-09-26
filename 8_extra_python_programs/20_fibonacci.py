#Write a python program to print the fibonacci series using iterative method

n_terms = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series = []
a, b = 0, 1
for _ in range(n_terms):
    fibonacci_series.append(a)
    a, b = b, a + b
print("Fibonacci series:", fibonacci_series)

