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

# next step

# "So far, we’ve pushed our behavior out to separate component classes, but we haven’t abstracted the behavior out.
# Bjorn still knows the exact concrete classes where his behavior is defined. Let’s change that.
# "We’ll take our component for handling user input and hide it behind an interface.
# We’ll turn InputComponent into an abstract base class"

# - essentially create an abstract class and and a concrete on PlayerInputComponent (extend) InputComponent <- (abstract)
# the Character class will send itself to the interfaced InputComponent which will have an update method
# def update(Character: character)
# components created this way are instantiated outside Character and passed in as params on creation
# this allows different inputcomponents to be used in the character ex: DemoInputController for the menu screen demo or a cpu

# after this, the Character class can be rebranded as a generic GameObject class holding component interfaces, as most of its
# behavior is defined in its components (other than position and velocity or other things needed to be shared between components)

# can used a factory method bjorn = GameObject.create_bjorn(#components) - returns GameObject bjorn

# the update() in the gameobject needs to care about the order of component.update() calls, or it may render data from last frame
# or some other bug
# it creates coupling, but there is also the option of giving the components references to eachother
# or Mediator pattern/ messaging event queue between them


def main():
    graphics = GraphicsComponent
    physics = PhysicsComponent
    sound = SoundsComponent
    character = Character()
    pass


if __name__ == "__main__":
    main()

# generic GameObject class - should replace Character in more mature implementation


class GameObject:
    def __init__(self) -> None:
        pass
    pass


class PhysicsComponent:
    def __init__(self) -> None:
        pass

    def update():
        pass


class GraphicsComponent:
    def __init__(self) -> None:
        pass

    def update():
        pass


class SoundsComponent:
    def __init__(self) -> None:
        pass

    def update():
        pass

# this can be changed to generic GameObject instance


class Character(GameObject):
    # each of these will be implemented and give their own update()
    def __init__(self, physics_component, graphics_component, sounds_component):
        # character specific values
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0
        self.velocity = 0

        self.physics_component = physics_component
        self.graphics_component = graphics_component
        self.sounds_component = sounds_component

    def update():
        # physics_component.update()
        # graphics_component.update()
        # sounds_component.update()
        pass
