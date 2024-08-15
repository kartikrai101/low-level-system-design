
# The Singleton Pattern: https://blog.algomaster.io/p/singleton-design-pattern

# Single Underscore (_method): Indicates a protected method, a convention to suggest it should not be accessed from outside the class.
# Double Underscore (__method): Triggers name mangling to provide a stronger indication of privacy. This makes the method harder to access from outside the class but does not make it truly private.
# cls: Refers to the class and is used to access or modify class-level attributes or methods
# *args: Allows passing a variable number of positional arguments
# **kwargs: Allows passing a variable number of keyword arguments.
class DatabaseConnection:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):  # overriding the 'new' method that creates new instance of the class when called
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Private method to simulate establishing a database connection
        print("Database connection established.")

    def query(self, sql):
        # Simulate a database query
        print(f"Executing query: {sql}")

# Example usage
if __name__ == "__main__":
    # Creating the first instance of DatabaseConnection
    db1 = DatabaseConnection()
    db1.query("SELECT * FROM users")

    # Attempting to create a second instance of DatabaseConnection
    db2 = DatabaseConnection()
    db2.query("SELECT * FROM products")

    # Check if both references are the same instance
    if db1 is db2:
        print("Both references point to the same database connection instance.")
    else:
        print("Different instances of database connection.")


# Examples of systems that implement the Singleton Pattern are:
# 1. ParkingLot -> to ensure only one instance of the parking lot exists. It maintains a list of levels and provides methods to park and unpark vehicles.