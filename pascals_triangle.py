def generate_pascals_triangle(n):
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer.")
    
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

def display_pascals_triangle(triangle):
    for row in triangle:
        print(" " * (len(triangle) - len(row)), end="")
        print(" ".join(map(str, row)))

def main():
    try:
        n = int(input("Enter the number of rows for Pascal's Triangle: "))
        triangle = generate_pascals_triangle(n)
        display_pascals_triangle(triangle)
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
