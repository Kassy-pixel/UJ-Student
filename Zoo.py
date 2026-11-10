class Cat:
    # TODO 1: add an extra parameter to the constructor to define the colour
    # of the cat and store it for use
    def __init__(self, name, color):
        self.name = name
        self.color = color
        

    def meow(self):
        print(f"Meow  my name is {self.name}")

    # TODO 2: Define a method called Jump that takes in a value and prints
    # "The {color} cat jumps x meters high"
    # NOTE: the {color} part refers to the colour attribute you defined
    # in the constructor above.
    def Jump(self, x):
        print(f"The {self.color} cat jumps {x} meters high")


def demo():
    cat1 = Cat("sussie", "black")

    cat2 = Cat("Bob", "orange")

    # TODO 3: Create a new cat object with name JOHN and colour purple
    cat3 = Cat("JOHN", "purple")

    cat1.meow()
    cat2.meow()
    cat3.meow()

    cat1.name = "Tiffany"

    # TODO 4: Change the colour of cat 2 to be white and observe the change
    cat2.color = "white"

    cat1.meow()
    cat2.meow()
    cat3.meow()

    # TODO 5: Call the newly defined Jump method on each cat here
    # and observe what it prints
    cat1.Jump(2)
    cat2.Jump(3)
    cat3.Jump(5)

    # Leave this line as it is - it hands your cats to the marker.
    return locals()


# =====================================================================
#  DO NOT MODIFY ANYTHING BELOW THIS LINE
#  Press Enter when you click Run to see your program's output.
# =====================================================================
import io
import contextlib


def _colour(obj):
    for attr in ("color", "colour", "Color", "Colour"):
        if hasattr(obj, attr):
            return getattr(obj, attr)
    return None


def _jump(obj):
    for attr in ("Jump", "jump"):
        if hasattr(obj, attr):
            return getattr(obj, attr)
    return None


def _quiet(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        value = fn(*args)
    return buf.getvalue(), value


def _main():
    try:
        test = input().strip()
    except EOFError:
        test = ""

    if test in ("", "demo"):
        demo()
        return

    try:
        if test == "1":
            c = Cat("Tester", "red")
            print(c.name, _colour(c))

        elif test == "2":
            c = Cat("Tester", "red")
            out, _ = _quiet(_jump(c), 7)
            print(out.strip())

        elif test == "3":
            _, made = _quiet(demo)
            cats = [v for v in made.values() if isinstance(v, Cat)]
            match = [c for c in cats
                     if c.name.upper() == "JOHN"
                     and str(_colour(c)).lower() == "purple"]
            print(len(match) >= 1)

        elif test == "4":
            _, made = _quiet(demo)
            print(str(_colour(made["cat2"])).lower())

        elif test == "5":
            out, _ = _quiet(demo)
            print("jumps" in out.lower())

        else:
            print("unknown test")

    except Exception as error:
        print("ERROR:", type(error).__name__)


if __name__ == "__main__":
    _main()