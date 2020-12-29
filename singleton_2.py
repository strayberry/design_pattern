class SingletonDeco:
    """
    单例类装饰器
    """

    def __init__(self, cls):    # 1
        print('装饰器初始化')
        self._cls = cls

    def instance(self):    # 2
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
        return self._instance

    def __call__(self):    # 3
        return self.instance()


@SingletonDeco    # 4
class Singleton:

    def display(self):
        return id(self)


if __name__ == '__main__':
    s1 = Singleton()    # 5
    s2 = Singleton()
    print('id(s1):', s1.display())
    print('id(s2):', s2.display())
    print('s1 is s2:', s1 is s2)




# 1 类装饰器的初始化方法，将被装饰的类赋值给实例的 _cls 属性。

# 2 此方法用于给实例的 _instance 属性赋值，此方法的调用权交个了__call__ 方法，也就是说调用 SingletonDeco 类的实例时会执行 instance 方法并返回被装饰器装饰的类 Singleton 的实例。并且不论调用多少次，结果都是一样的。

# 3 类装饰器 SingletonDeco 的实例的调用接口。

# 4 使用类装饰器创建 Singleton 类，创建该类时，会执行SingletonDeco.__init__ 方法，并且将该类赋值给实例的 _cls 属性。此时 Singleton 这个变量就指向了 SingletonDeco 这个类的实例。如果要获取原 Singleton 类，就需要调用 Singleton 的 _cls 属性。此外原 Singleton 类为实例提供了 display 方法返回实例的内存地址。

# 5 调用 Singleton ，表面上看是对 Singleton 类进行实例化，实际上是调用 SingletonDeco 类的实例的 __call__ 方法。因为变量 Singleton 指向的就是 SingletonDeco 的实例。调用 __call__ 的结果就是调用 instance 方法，下一步就是对调用实例的 _cls 属性，而这个属性的值就是原 Singleton 类。综上所述，这个最终的调用结果还是原 Singleton 的实例。绕这么大一圈，一切都是为了在 instance 方法中实现唯一实例。