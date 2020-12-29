class Singleton:
    '''
    单例模式
    '''

    # 创建一个嵌套类
    class _A:
        def display(self):    # 1
            return id(self)

    _instance = None

    def __init__(self):    # 2
        __class__._instance = __class__._instance or __class__._A()

    def __getattr__(self, attr):    # 3
        return getattr(__class__._instance, attr)

    def __setattr__(self, attr, value):    # 4
        object.__setattr__(__class__._instance, attr, value)


if __name__ == '__main__':
    s1 = Singleton(); s2 = Singleton()    # 5

    print('id(s1):', id(s1))    # 6
    print('id(s2):', id(s2))

    print('s1.display():', s1.display())    # 7
    print('s2.display():', s2.display())

    s1.name = 'James'    # 8
    print('s1.name:', s1.name)
    print('s2.name:', s2.name)



# 1 创建一个嵌套类 _A，在类内部定义一个 display 方法，该方法返回 _A 类的实例的内存地址。

# 2 编写 Singleton 类的实例的初始化方法。创建 Singleton 类的实例后，执行此方法。方法内部是对类的操作，为类的 _instance 属性赋值一个 _A 的实例。第一次对 Singleton 进行实例化时会创建一个 _A 类的实例并赋值，以后不再变化。

# 3 编写 Singleton 类的实例获取属性的方法。Singleton 类内部故意不为自身的实例设置任何属性，结果就是调用实例的属性时最后落到此方法的头上。方法内部获取类属性 _instance 的同名属性，也就是 _A 类的实例的属性。

# 4 编写 Singleton 类的实例定义属性的方法。同样，此方法内部调用object.__setattr__ 方法为 Singleton._instance 也就是 _A 的实例定义属性。

# 5 为 Singleton 类创建两个实例以备测试。

# 6 打印两个实例的内存地址，它们的结果应该是不同的。

# 7 打印两个实例调用 display 方法的结果，实际上调用的都是Singleton._instance 的同名方法，结果应该是一样的。

# 8 其中一个实例定义 name 属性，然后两个实例获取该属性并打印，结果应该都是一样的。