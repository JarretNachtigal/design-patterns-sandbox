# "each entity in the game should encapsulate its own behavior."

# "Once per frame, the game loop walks the collection and calls update()
#  on each object. This gives each one a chance to perform one frame’s worth
# of behavior. By calling it on all objects every frame,
# they all behave simultaneously."

# "Update methods work well when:

# - Your game has a number of objects or systems that need to run simultaneously.
# - Each object’s behavior is mostly independent of the others.
# - The objects need to be simulated over time."

# "If A comes before B in the list of objects, then when A updates, it will see B’s previous state. "
# "But when B updates, it will see A’s new state, since A has already been updated this frame."
# OR - double buffer

# each class will have or inherit an update() method

def main():
    pass


if __name__ == "__main__":
    main()
