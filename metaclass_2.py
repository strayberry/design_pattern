class BaseMeta(type):
    def __new__(metacls, name, bases, namespace, **kwargs):
        # 如果 name 不是基类的名字，那就是创建子类啦
        # 如果并且子类没有提供 bar 属性，那就不予创建这个子类
        if name != 'Base' and 'bar' not in namespace:
            raise TypeError('bad user class')
        return super().__new__(metacls, name, bases, namespace, **kwargs)

class Base(object, metaclass=BaseMeta):
    def foo(self):
        return self.bar()


if __name__ == '__main__':
    class Base1(Base):
        def bar(self):
            ...
    print('Base1 创建完成')

    class Base2(Base):
        ...
    print('Base2 创建完成')


#这会儿再将 Base 类作为父类创建子类时，子类就必须要提供 bar 属性了。
#执行脚本，Base1 类会成功创建 ，因为它提供了 bar 属性；而 Base2 不会创建成功，因为它没有 bar 属性：