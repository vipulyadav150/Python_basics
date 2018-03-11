class Parent:


    def print_last_name(self):
        print("Yadav")


class child(Parent):

    def print_first_name(self):
        print("Vipulkumar")

    def print_last_name(self):
        print("NONE")


a = child()
a.print_first_name()
a.print_last_name()
b = Parent()
b.print_last_name()
