# "Provide a global point of access to a service without coupling users to the concrete class that implements it."

# static class and singleton work but also introduce coupling

# "phone book" - "a convenient single place where we control how we’re found."

# "The core difficulty with a service locator is that it takes a dependency — a bit of coupling between
#  two pieces of code — and defers wiring it up until runtime. This gives you flexibility,
#  but the price you pay is that it’s harder to understand what your dependencies are by reading the code."

# "The Unity framework uses this pattern in concert with the Component pattern in its GetComponent() method."

def main():
    pass


if __name__ == "__main__":
    main()


class ExampleService:
    def __init__(self) -> None:
        pass


class NullService:
    def __init__(self) -> None:
        pass

    def do_something(self):
        pass
