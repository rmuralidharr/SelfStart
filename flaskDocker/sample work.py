

# def guard_zero(operate):
#     def inner(x, y):
#         if y == 0:
#             print("Cannot divide by 0.")
#             return
#         return operate(x, y)
#
#     return inner
#
#
# @guard_zero
# def divide(x, y):
#     return x / y
#
#
# print(divide(5, 0))

# y=0
# if y==0:
#     print("wow")
#     return

class food():
    # init method or constructor
    def __init__(self, fruit, color,wow):
        self.fruit = fruit
        self.color = color
        wow1=wow

    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color)
        # print(food.wow)

apple = food("apple", "red","sd")
grapes = food("grapes", "green","asd")

print(apple)
print(grapes)
apple.show()
grapes.show()