import shared_resource
import rock
# this folder contains my attempt/notes at implementing the flyweight design pattern in
# chapter 2 of https://gameprogrammingpatterns.com/contents.html
# comments will be braindead obvious, but are for note taking purposes


def main():
    # create instance of shared data object to be referenced by all other objects as a shared resource
    shared = shared_resource.SharedResource(
        "Grey", "hmm, I guess it has a rough texture")
    # create objects with shared data as param
    rock_one = rock.Rock(shared, 1, 1)
    rock_two = rock.Rock(shared, 2, 2)
    rock_three = rock.Rock(shared, 3, 3)
    # check all children reference same obj addressof()? or id()?

    pass


if __name__ == "__main__":
    main()
