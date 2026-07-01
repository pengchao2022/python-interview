# 定义一个 Person 类，以及它的两个子类 Male 和 Female。所有类都有一个 getGender 方法，在 Male 类中调用该方法会打印 "Male"，在 Female 类中调用该方法会打印 "Female"。

class Person(object):

    # 静态类 不需要初始化方法
    # 方法 一
    def getGender(self):
        return "Unknown"
    

# male 子类
class Male(Person):

    # 定义方法一
    def getGender(self):
        return "Male"
    

# female 子类
class Female(Person):

    # 定义方法一
    def getGender(self):
        return "Female"
    

# 创建对象 实例
aMale = Male()
aFemale = Female()

# 调用方法
person1 = aMale.getGender()
person2 = aFemale.getGender()

# 打印出来
print(person1)
print(person2)

