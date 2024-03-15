class Singleton:
    # Static variable single_instance of type Singleton
    _single_instance = None

    # Declaring a variable of type String
    def __init__(self):
        self.s = "Hello I am a string part of Singleton class"

    # Static method to create instance of Singleton class
    @staticmethod
    def singleton():
        # To ensure only one instance is created
        if Singleton._single_instance is None:
            Singleton._single_instance = Singleton()
        return Singleton._single_instance


# Main class
class GFG:
    # Main driver method
    @staticmethod
    def main():
        # Instantiating Singleton class with variable x
        x = Singleton.singleton()

        # Instantiating Singleton class with variable y
        y = Singleton.singleton()

        # Instantiating Singleton class with variable z
        z = Singleton.singleton()

        # Now changing variable of instance x via upper() method
        x.s = x.s.upper()

        # Print and display commands
        print("String from x is", x.s)
        print("String from y is", y.s)
        print("String from z is", z.s)
        print("\n")

        # Now again changing variable of instance z via lower() method
        z.s = z.s.lower()

        print("String from x is", x.s)
        print("String from y is", y.s)
        print("String from z is", z.s)


# Call the main function
if __name__ == "__main__":
    GFG.main()
