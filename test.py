# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性，私有属性在类外部无法直接访问
#     __weight  = 0
#     #定义一个构造函数
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#        print(self.__weight)
#        print("%s 说 ：我%d岁。"%(self.name,self.age))
#
# #单继承示例
# class student(people):
#     grade = ''
#     #定义一个构造函数
#     def __init__(self,n,a,w,g):
#         #调用父类的构造函数
#         people.__init__(self,n,a,w)
#         self.grade = g
#         #覆写父类的方法
#     def speak(self):
#             print("%s 说：我%d岁了，在读%d年级"%(self.name,self.age,self.grade))
#
# s = student('ken',10,60,4)
# d = people('ton',5,50)
# d.speak()
# s.speak()


# total = 0  # 这是一个全局变量
#
#
# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2  # total在这里是局部变量.
#     print("函数内是局部变量 : ", total)
#     # return total
#
#
# # 调用sum函数
# sum(10, 20)
# print("函数外是全局变量 : ", total)
#

def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))



