# 基本数据类型
# 字符类型
string = 'abc'
print(string)
#  int类型
integer = 1
print(integer)
# 数组类型
array=[1,'a','2']
print(array)
array.append('c')
print(array)
print(array.pop())
print(array[2])
# 元组类型
tumple=(1,2,'c')
print(tumple)
# set类型
seta = set(array)
print(seta)
# 字典类型
mapDic={'1':'a',2:'c'}
print(mapDic)
mapDic['3']='e'
print(mapDic)
print(mapDic[2])
for i in mapDic:
    print(i)
print(mapDic['3'])



#顺序流程
print("请输入a")
a = input()
print("请输入b")
b = input()
print(a)
print(b)
print(a+b)

#判断流程
print("请输入")
selecter = input()
if(selecter == "a"):
    print("你输入的是：a")
elif (selecter == "b"):
    print("你输入的是：b")
else:
    print("你输入的不是：a和b")
#循环流程
print("请输入循环的次数")
count = int(input())
# while(count > 0):
#     print(print("第 %s 次"%(count)))
#     count=count-1

for i in range(0,count):
    print("第 %s 次"%(i+1))

# 异常控制流程
try:
    1/0
except BaseException:
    print(BaseException)

#面向对象
def method(a):
    a=str(a)
    print("方法接受到了参数"+a)
    return a + "1"

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayHello(self):
        print("hello"+self.name+self.age)

print(method(1))
tome = User('tome','10')
tome.sayHello()