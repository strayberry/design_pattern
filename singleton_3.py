class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_Singleton__instance'):
            cls.__instance = super().__new__(cls, *args, **kw)
        print('实例化时打印实例 ID:', id(cls.__instance))
        return cls.__instance


s1 = Singleton()
s2 = Singleton()

print('s1 is s2:', s1 is s2)


#如果不重写类的 __new__ 方法，则默认调用 object 的同名方法并返回，也就是每次都会创建一个新的实例。重写的目的就是将一个实例固定到类属性中，然后每次创建实例时都返回这个属性值。这个方式思路简单，代码也很清晰。