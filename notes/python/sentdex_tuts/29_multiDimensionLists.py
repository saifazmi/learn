# Multi-dimensional Lists

# Example of a 2D list

x = [[5,6],[6,7],[7,2],[2,5]]

print(x[1])
print(x[1][0])

# Example of a 3D list

y = [[[5,6],[6,6]],[[6,6],[7,8]],[7,2],[2,5]]
print(y[0])
print(y[0][1])
print(y[0][1][0])

# Organising syntactically busy piece of code like above

z = [
     [[5,6],[6,6]],
     [[6,6],[7,8]],
      [7,2],[2,5]
    ]
print(z[0])
print(z[0][1])
print(z[0][1][0])
