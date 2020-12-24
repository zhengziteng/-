"""
    对时间处理的模块
    time
"""

import time

# 1. 人的时间：2020年10月27日 09:30
# 时间元组:年,月,日,时,分,秒,星期,年的第几天,夏令时
tuple_time = time.localtime()
print(tuple_time[0])  # 获取年
print(tuple_time[-3])  # 获取星期
print(tuple_time[3: 6])  # 获取时分秒

# 2. 机器时间:
# 时间戳：从1970年元旦到现在经过的秒数
print(time.time())  # 1603762810.9457989

# 3. 时间元组 <---> 时间戳
# 语法：时间元组 = time.localtime( 时间戳 )
print(time.localtime(1603762810.9457989))
# 语法：时间戳 = time.mktime( 时间元组 )
print(time.mktime(tuple_time))
# 语法：时间戳 = time.mktime(9个元素的元组)
print(time.mktime((2020, 10, 27, 9, 0, 0, 0, 0, 0)))

# 4. 时间元组<--->字符串
# 语法：字符串 = time.strftime(  "格式" ,时间元组)
print(time.strftime(  "%y/%m/%d %H:%M:%S" ,tuple_time))
# 2020/10/27 09:55:19
print(time.strftime(  "%Y/%m/%d %H:%M:%S" ,tuple_time))
# 下面代码含义：给整数占位
# "..%d..."%(100)
# 语法：时间元组 =time.strptime("时间字符串","格式")
print(time.strptime("2020/10/27 09:55:19","%Y/%m/%d %H:%M:%S"))