class MyClass:
    def __del__(self):
        print ("MyClass is being destroyed")

obj = MyClass()
del obj