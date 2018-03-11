class Mario:
    def move(self):
        print("I am Moving")


class Shroom:
    def eat_shroom(self):
        print("i ate a shroom!")


class BigMario(Mario , Shroom):
    pass

a = BigMario()
a.eat_shroom()
a.move()
