# "Provide a global point of access to a service without coupling users to the concrete class that implements it."

# static class and singleton work but also introduce coupling

# "phone book" - "a convenient single place where we control how we’re found."

# "The core difficulty with a service locator is that it takes a dependency — a bit of coupling between
#  two pieces of code — and defers wiring it up until runtime. This gives you flexibility,
#  but the price you pay is that it’s harder to understand what your dependencies are by reading the code."

# "The Unity framework uses this pattern in concert with the Component pattern in its GetComponent() method."

def main():
    locator = ServiceLocator()
    service_instance = ExampleService()
    locator.provide(service_instance)
    # this will be done where needed in the code base
    returned_service = locator.get_service()
    returned_service.do_something()


if __name__ == "__main__":
    main()


# this would be an audioengine or something that needs to be used
# in a bunch of places in the code
class ExampleService:
    def __init__(self) -> None:
        pass

    def do_something(self):
        pass


# prevent null return (in a language where that matters)
class NullService:
    def __init__(self) -> None:
        pass

    def do_something(self):
        pass


# return the instance of a service to many places in code base
class ServiceLocator:
    def __init__(self) -> None:
        # prevent null return (in a language where that matters)
        self.service = NullService()
        pass

    # this is the located service
    def provide(self, service):
        self.service = service

    def get_service(self):
        return self.service
