import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def binomial_theorem(a, b, n):
    terms = []
    for k in range(n + 1):
        coefficient = binomial_coefficient(n, k)
        term = coefficient * (a ** (n - k)) * (b ** k)
        terms.append(term)
    return sum(terms)

def main():
    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        n = int(input("Enter the value of n: "))
        
        # Using binomial theorem
        result_binomial = binomial_theorem(a, b, n)
        
        # Direct computation
        result_direct = (a + b) ** n
        
        print(f"Result using Binomial Theorem: {result_binomial}")
        print(f"Result using direct computation: {result_direct}")
        
        if math.isclose(result_binomial, result_direct, rel_tol=1e-9):
            print("The Binomial Theorem is proven to be correct!")
        else:
            print("There is a discrepancy in the results.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
