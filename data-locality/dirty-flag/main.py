# "Avoid unnecessary work by deferring it until the result is needed."

# local transform - movement of object - moving a hand

# world transform - movement of object and all related objects in hierarchy - moving a hand in a moving car

# "We need the world transform for every object in the world every frame, so even though there are only a handful of matrix
# multiplications per model, it’s on the hot code path where performance is critical."

# SLOW! - not everything needs to be recalculated if it didn't move
# "The simplest approach is to calculate transforms on the fly while rendering.
# Each frame, we recursively traverse the scene graph starting at the top of the hierarchy. "

# "The obvious answer is to cache it. "
# " When we render, we only use the precalculated world transform.
# If the object never moves, the cached transform is always up to date and everything’s happy."
# the calculation is done recursively - or at least fully up the hierarchy tree - cache the position of something
# that would otherwise need to be calculated more than once -

# ex from book
# move ship
# recalc ship
# recalc nest
# recalc pirate
# recalc parrot

# move nest
# recalc nest
# recalc pirate
# recalc parrot

# move pirate
# recalc pirate
# recalc parrot

# move parrot
# recalc parrot
