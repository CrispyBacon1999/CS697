border = input("Border Character: ")
n = int(input("Base Width: "))

for i in range(n):
    if i < n - 1:
        # For top part of triangle
        # Calculate the amount of whitespace to put before
        # the edge of the triangle
        outer_whitespace = " " * (((n * 2) - (i * 2 + 1)) // 2)
        if i == 0:
            # Just use a border character as the middle
            # portion of the triangle for the tip
            tri = border
        else:
            # Calculate out the space that should be in
            # between the border characters to place the
            # right hand side at the correct place
            # (current row * 2 - 1) will calculate the space
            # Eg. row i=3, whitespace is 5 spaces
            tri = border + (" " * (i * 2 - 1)) + border
        print(outer_whitespace + tri)
    else:
        # For base of triangle
        print((border + " ") * n)

# Just for the fun of it, a one-line version,
# which is absolutely hideous, but works :)

# b = border
# print("\n".join([(b + " ")*n if i==n-1 else " "*(((n*2)-(i*2+1))//2)+b+(" "*(i*2-1))+(b if i>0 else "") for i in range(n)]))
