# "Components are basically plug-and-play for objects. They let us build complex entities with rich behavior
# by plugging different reusable component objects into sockets on the entity."

# "let’s try it with components. Our subclasses disappear completely.
# Instead, we have a single GameObject class and two component classes: PhysicsComponent and GraphicsComponent.
# A decoration is simply a GameObject with a GraphicsComponent but no PhysicsComponent.
# A zone is the opposite, and a prop has both components."

# "A single entity spans multiple domains."
# "The entity is reduced to a simple container of components."

# "The Component pattern adds a good bit of complexity over simply making a class and putting code in it.
# Each conceptual “object” becomes a cluster of objects that must be instantiated, initialized, and correctly wired together.
# Communication between the different components becomes more challenging, and controlling how they occupy memory is more complex."

# class Character will have an instance of PhysicsComponent, GraphicsComponent and delegate to them
# when needed inside the update() method

# "The Character class now basically does two things:
# - it holds the set of components that actually define it, and it holds the state that is shared across multiple domains.
# Position and velocity are still in the core Bjorn class for two reasons.
# First, they are “pan-domain” state — almost every component will make use of them,
# so it isn’t clear which component should own them if we did want to push them down.
#  - "Secondly, and more importantly, it gives us an easy way for the components to communicate
# without being coupled to each other."
