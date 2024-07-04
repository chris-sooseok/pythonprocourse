class MyClass:
    def __init__(self):
        self.my_private_variable = 42

    def get_my_private_variable(self):
        return self.my_private_variable


class MyClass2(MyClass):

    def __init__(self):
        self.my_private_variable = 30

    def get_my_private_variable(self):
        return self.my_private_variable


my_instance = MyClass()
print(my_instance.get_my_private_variable())
print(my_instance.my_private_variable)


my_instance2 = MyClass()
print(my_instance2.get_my_private_variable())# Output: 42