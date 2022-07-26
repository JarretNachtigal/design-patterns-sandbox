# "Let’s say we unleash our team and get them writing superpower classes. What’s going to happen?
# - There will be lots of redundant code.
# - Every part of the game engine will get coupled to these classes.
# - When these outside systems need to change, odds are good some random superpower code will get broken.
# - It’s hard to define invariants that all superpowers obey."

# "We do (this) by making these operations protected methods of the Superpower base class.
# this = What we want is to give each of the gameplay programmers who is implementing a superpower a set of primitives they can play with.""

# "This pattern leads to an architecture where you have a shallow but wide class hierarchy.
# Your inheritance chains aren’t deep, but there are a lot of classes that hang off Superpower. "

# "For example, to let a power play sounds, we could add these directly to Superpower"
# "But if Superpower is already getting large and unwieldy, we might want to avoid that.
# Instead, we create a SoundPlayer class that exposes that functionality"
# - then instantiate sound_player in superpower parent and create getSoundPlayer()
