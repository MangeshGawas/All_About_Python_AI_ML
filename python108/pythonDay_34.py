#Day 34
# Class and static method in python

class MyClass:
    class_variable = 10

    @classmethod
    def class_method(cls):
        return f"Class variable value:{cls.class_variable}"
    
# call class method using class name
print(MyClass.class_method())


class MyClass2:
    @staticmethod
    def static_method():
        return "This is the static method"
    
print(MyClass2.static_method())