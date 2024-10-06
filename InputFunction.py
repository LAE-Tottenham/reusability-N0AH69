def get_triangle_sides():
    # Ask the user for input and ensure it's a valid float
    opp = float(input("Enter the length of the opposite side: "))
    adj = float(input("Enter the length of the adjacent side: "))
    return opp, adj  # Return the sides as a tuple

# For the first triangle
opp1, adj1 = get_triangle_sides()

# For the second triangle
opp2, adj2 = get_triangle_sides()

# For the third triangle
opp3, adj3 = get_triangle_sides()

# Print the results
print(f"Triangle 1: Opposite = {opp1}, Adjacent = {adj1}")
print(f"Triangle 2: Opposite = {opp2}, Adjacent = {adj2}")
print(f"Triangle 3: Opposite = {opp3}, Adjacent = {adj3}")