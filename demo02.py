"""
    异常处理
        不是解决语法错误,而是解决逻辑错误
        逻辑错误:运行时,可能由于数值超过有效范围而带来错误
        异常现象：程序不再向下执行,而是不断向上翻
        处理目的：将异常流程改为正常流程
        核心价值：保障程序按照既定流程继续执行
"""


# 语法错误
# print(qtx) # NameError

# 写法1："包治百病" (民间流行)
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print("每人分%d个苹果"%result)
#     except Exception:
#         print("程序出错啦")

# 写法2:"对症下药" (官方建议)
# def div_apple(apple_count):
#     try:
#         # ValueError
#         person_count = int(input("请输入人数："))
#         # ZeroDivisionError
#         result = apple_count / person_count
#         print("每人分%d个苹果"%result)
#     except ValueError:
#         print("不能输入非整数")
#     except ZeroDivisionError:
#         print("不能输入零")

# 写法3:无论是否异常,一定执行的逻辑
# def div_apple(apple_count):
#     try:
#         # 打开文件(开门)
#         # 处理文件(错误)
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print("每人分%d个苹果"%result)
#     finally:
#         # 关闭文件(关门)
#         print("对自己好一点")

# 写法4: 没有发生错误执行的逻辑
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print("每人分%d个苹果" % result)
#     except Exception:
#         print("出错啦")
#     else:
#         print("没有发生错误执行的逻辑")


# 综合:
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print("每人分%d个苹果" % result)
    except Exception:
        print("分苹果失败")
    else:
        print("分苹果成功")
    finally:
        print("分任务结束")



if __name__ == '__main__':
    div_apple(10)

    print("后续逻辑")
