# "Avoid unnecessary work by deferring it until the result is needed."

# local transform - movement of object - moving a hand

# world transform - movement of object and all related objects in hierarchy - moving a hand in a moving car

# "We need the world transform for every object in the world every frame, so even though there are only a handful of matrix
# multiplications per model, it’s on the hot code path where performance is critical."

# SLOW!
# "The simplest approach is to calculate transforms on the fly while rendering.
# Each frame, we recursively traverse the scene graph starting at the top of the hierarchy. "

# "The obvious answer is to cache it. "
