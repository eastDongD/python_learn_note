import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
#？？？？？？？？？？？？？？？此函数在类外吗
def student2dict(std):#为Student专门写一个转换函数，帮助json序列化
    return {  #返回一个dict，然后对dict序列化
    'name': std.name,
    'age': std.age,
    'score': std.score
    }

s = Student('Bob', 20, 88)
#print(json.dumps(s)) #报错无法执行，因为不知道如何序列化student
print(json.dumps(s, default=student2dict)) #告诉dumps用student2dict去序列化