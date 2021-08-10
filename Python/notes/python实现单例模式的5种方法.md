# python实现单例模式的5种方法

- python实现单例模式的5种方法
  - [1. 使用模块](#1使用模块)
  - [2. 使用装饰器](#2使用装饰器)
  - [3. 使用类](#3使用类)
  - [4. 基于__new__方法实现](#4基于__new__方法实现)
  - [5. 使用元类](#5使用元类)
  - [总结](#总结)

单例模式是最常使用的一种设计模式，该模式的目的是确保在一个系统中，一个类只有一个实例，本文讨论python实现单例模式的5种方法。

## 1.使用模块

模块天然就是单例的，因为模块只会被加载一次，加载之后，其他脚本里如果使用import 二次加载这个模块时，会从sys.modules里找到已经加载好的模块，模块里的对象天然就是单例的，即使是在多线程环境下也是如此。

编写脚本my_singleton.py

```python
class Singleton():
    def __init__(self, name):
        self.name = name

    def do_something(self):
        pass

singleton = Singleton('模块单例')
```

在其他脚本里

```text
from my_singleton import singleton
```

在任何引用singleton的脚本里，singleton都是同一个对象，这就确保了系统中只有一个Singleton的实例。

这种方法是官方所推荐的，它简单，代码编写容易，不需要考虑多线程的问题，当然，你也可以挑刺说在其他脚本里，还是可以主动的创建Singleton的实例对象。没错，你想搞破坏，总是能找到方法，但设计模式的目的不是为了防止人为搞破坏，而是让系统解耦，让系统易于理解和工作。

## 2.使用装饰器

编写一个单例模式的装饰器，来装饰那些需要支持单例的类

```python
def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton_wrapper


@Singleton
class SingletonTest(object):
    def __init__(self, name):
        self.name = name


slt_1 = SingletonTest('第1次创建')
print(slt_1.name)
slt_2 = SingletonTest('第2次创建')
print(slt_1.name, slt_2.name)

print(slt_1 is slt_2)
```

程序输出结果

```text
第1次创建
第1次创建 第1次创建
True
```

创建slt_2 对象时，instance 字典中已经存在SingletonTest 这个key，因此直接返回了第一次创建的对象，slt_1 和 slt_2 是同一个对象。

在多线程环境下，这种设计方法是不安全的，多个线程同时判断cls是否在instance字典中，得到的返回结果都是False，于是这些线程都会去创建对象，为了避免这种情况，加上一把RLock锁

```python
from threading import RLock
single_lock = RLock()

def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        with single_lock:
            if cls not in instance:
                instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton_wrapper
```

## 3.使用类

```python
class Singleton(object):

    def __init__(self, name):
        self.name = name

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

single_1 = Singleton.instance('第1次创建')
single_2 = Singleton.instance('第2次创建')

print(single_1 is single_2)     # True
```

instance方法会先检查是否存在类属性_instance， 如果不存在，则创建对象，并返回。这个设计虽然实现了单例模式，但在多线程环境下不安全，多个线程同时检查Singleton类是否拥有_instance属性，得到的结果是否False， 则这些线程都会执行对象的创建工作，最后创建出来的对象才是最终的对象，为了在多线程环境下保证数据安全，在需要并发枷锁的地方加上RLock锁

```python
from threading import RLock
class Singleton(object):
    single_lock = RLock()

    def __init__(self, name):
        self.name = name

    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton.single_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance
```

## 4.基于__new__方法实现

__new__方法是构造函数，是真正的用来创建对象的，那么在创建对象的时候进行控制，不是更方便么

```python
from threading import RLock

class Singleton(object):
    single_lock = RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        with Singleton.single_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = object.__new__(cls)

        return Singleton._instance

single_1 = Singleton('第1次创建')
single_2 = Singleton('第2次创建')

print(single_1.name, single_2.name)   # 第2次创建 第2次创建
print(single_1 is single_2)     # True
```

这种方法同样实现了多线程环境下的安全的单例模式，但有一个小小的问题，第二次创建对象时，虽然返回了单例，但是修改了单例的name属性，前面已经介绍的三个方法，一旦单例对象被创建，此后的创建都返回第一次创建的对象且不会修改对象的属性。

之所有这样的差别，是因为前面三个方法，都只调用__new__方法一次，__new__方法创建对象后，会调用一次__init__来初始化对象，而方法4会多次调用__new__方法，虽然每次返回的都是同一个对象，但是会立即调用__init__方法，这样就修改了name属性，如果不希望name属性在多次创建对象过程中被修改，只需要做一个小小的修改即可

```python
    def __init__(self, name):
        if hasattr(self, 'name'):
            return
        self.name = name
```

一旦发现name属性已经被初始化，就不在执行初始化的代码。

## 5.使用元类

```python
from threading import RLock

class SingletonType(type):
    single_lock = RLock()

    def __call__(cls, *args, **kwargs):   # 创建cls的对象时候调用
        with SingletonType.single_lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)     # 创建cls的对象

        return cls._instance


class Singleton(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


single_1 = Singleton('第1次创建')
single_2 = Singleton('第2次创建')

print(single_1.name, single_2.name)     # 第1次创建 第1次创建
print(single_1 is single_2)     # True
```

在5种python实现单例模式的方法中，基于元类的实现，可能是最难理解的一个。

class Singleton(metaclass=SingletonType) 这行代码定义了一个类，这个类是元类SingletonType 的实例，是元类SingletonType的__new__构造出来的，Singleton是实例，那么Singleton('第1次创建')就是在调用元类SingletonType 的__call__方法，__call__方法可以让类的实例像函数一样去调用。

在__call__方法里，cls就是类Singleton，为了创建对象，使用super来调用__call__方法，而不能直接写成cls(*args, **kwargs), 这样等于又把SingletonType的__call__方法调用了一次，形成了死循环。

## 总结

5种方法，都可以实现多线程环境下的安全的单例模式，方法1最简单，无法避免人为的创建多个实例。其余的方法，可以避免人为的创建出多个实例，但需要在并发操作上加锁。