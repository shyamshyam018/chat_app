def generate_pascals_triangle(n):
    pascal_triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        pascal_triangle.append(row)

    return pascal_triangle

def print_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

try:
    num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
    if num_rows <= 0:
        print("Please enter a positive integer.")
    else:
        pascal_triangle = generate_pascals_triangle(num_rows)
        print_pascals_triangle(pascal_triangle)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
