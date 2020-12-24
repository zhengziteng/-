"""
    主动创造异常
        目的：为了快速传递错误信息
        语法：
            抛出
                raise 异常对象

            接收
                try:
                    .....
                except:
                    .....
"""


class Wife:
    def __init__(self, age=0):
        self.age = age # B

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):# C
        if 23 <= value <=30:
            self.__age = value
        else:
            # 主动创造异常
            raise Exception("我不要",1005)

while True:
    try:
        age = int(input("请输入年龄："))
        shuang_er = Wife(age)# A
        print(shuang_er.age)
        break
    except Exception as e: # 创建变量,关联raise后面的对象
        print(e.args)

print("后续逻辑")
