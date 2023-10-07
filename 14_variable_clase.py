"""Demostración variables de clase"""

class ExampleClass:

    counter = 0

    def __init__(self, val = 1):
        self.val = val
        ExampleClass.counter == 1

object_1 = ExampleClass()
object_2 = ExampleClass(2)
object_3 = ExampleClass(4)

print(object_1.val, object_1.counter)
print(object_2.val, object_2.counter)
print(object_3.val, object_3.counter)
      