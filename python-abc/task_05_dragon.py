class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):  # Note the order of inheritance
    def roar(self):
        print("The dragon roars!")
