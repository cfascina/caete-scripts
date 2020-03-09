# Array with all PLSs - [c02, height, treetop_area]
arr_pls = [
    [102, 2.5, 27], # Dead (not considered)
    [836, 1.3, 44], # Tallest until here
    [950, 0.8, 18],
    [257, 4.7, 46], # Dead (not considered)
    [516, 3.5, 48], # Tallest until here
    [187, 1.2, 15], # Dead (not considered)
    [630, 7.7, 12], # Tallest until here
    [472, 6.0, 34],
    [721, 9.9, 15], # Tallest until here (*)
    [176, 6.5, 28], # Dead (not considered)

    # (*) This item won't be considered because when the loop gets to it,
    #     the 'total_treetop_area' will already be higher/equal to the
    #     cell_grid_area
]

# Save at 'arr_pls_alive' just the PLSs w/ co2 >= 300
arr_pls_alive = []

for pls in arr_pls:
    if(pls[0] >= 300):
        arr_pls_alive.append(pls)

# Set the total treetop area, initially as 0
total_treetop_area = 0;

# Set the tallets pls, initially as 0
tallest_pls = 0

# Set the cell grid area as 100m^2
cell_grid_area = 100

# Iterates through all the 'arr_pls_alive' items
# At each item, check if 'total_treetop_area' is lower than 'cell_grid_area'
# If it is, check if the current item is taller than the tallest found so far
# If it is:
#   Set the 'tallest_pls' with the new value
#   Set the heigh value of the current item to 0 (to be discarded in the next iteration)
#   Increase the 'total_treetop_area' with the treetop_area of the current item
for pls in arr_pls_alive:
    if(total_treetop_area < cell_grid_area):
        if(pls[1] > tallest_pls):
            tallest_pls = pls[1]
            pls[1] = 0
            total_treetop_area += pls[2]

# Display the results
print(f'tallest_pls: {tallest_pls}')
print(f'total_treetop_area: {total_treetop_area}')
