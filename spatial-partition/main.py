# "Efficiently locate objects by storing them in a data structure organized by their positions."

# ex RTS games

# simple 1d rendidion - units on a line
# array sort by unit location -> binary search (takes search from O(n^2) to O(n log n)
# pigeonhole? -> O(n)?

# "For a set of objects, each has a position in space. Store them in a spatial data structure
# that organizes the objects by their positions. This data structure lets you efficiently query
# for objects at or near a location. When an object’s position changes, update the spatial data structure
# so that it can continue to find the object."

# used in static situations (game world) as well
# used when "you have a set of objects that each have some kind of position and that you are doing enough
# queries to find objects by location that your performance is suffering."

# "FIXED GRID"

# grid - array of pointers (cells)
# cell - doubly linked list, holds most recently added unit as head

# partitions the battlefield into smaller battlefields, check (in unit range/vision)
# adjacent cells as well for enemies to hit
# on moving into new cells, unit will be moved into the correct cell list
# old check 4 of the 8 surrounding cells to prevent double checks

# i think this means that if unit a sees unit b, they effectively both see eachother
# otherwise units would only be able to see and attack from one direction

# Grid
# Quadtree
# BSP
# k-d tree
# Bounding volume hierarchy
