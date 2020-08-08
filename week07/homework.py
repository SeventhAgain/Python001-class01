# -*- coding:utf-8 -*-
import abc
from enum import Enum, unique


@unique
class BodyType(Enum):
    small = '小'
    mid = '中'
    big = '大'


@unique
class AnimalType(Enum):
    eat_grass = '食草'
    eat_meat = '食肉'


@unique
class AnimalCharactor(Enum):
    is_mild = '温顺'
    is_violent = '凶猛'


class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, type, bodyType, charactor):
        self.type = type
        self.bodyType = bodyType
        self.charactor = charactor
        # 默认非凶猛动物
        self.is_violent = False
        if bodyType != BodyType.small.value \
                and type == AnimalType.eat_meat.value \
                and charactor == AnimalCharactor.is_violent.value:
            self.is_violent = True

    @property
    def isViolent(self):
        return self.is_violent


class Cat(Animal):
    cry = 'miao~'

    def __init__(self, name, type, bodyType, charactor):
        super().__init__(type, bodyType, charactor)
        self.name = name
        # 默认非宠物
        self.is_pet = False
        if charactor == AnimalCharactor.is_mild.value:
            self.is_pet = True

    @property
    def isPet(self):
        return self.is_pet


class Zoom(object):

    def __init__(self, name):
        self.animals = {}
        self.name = name

    def add_animal(self, obj):
        obj_hash = obj.__hash__()
        obj_class = type(obj).__name__
        if self.animals.get(obj_class) == None:
            self.animals[obj_class] = [obj_hash]
        else:
            class_arr = self.animals.get(obj_class)
            if obj_hash in class_arr:
                # 同一只猫（hash值相同） 不可重复添加
                print(f"{obj.name} exists!")
                return
            else:
                class_arr.append(obj_hash)

    @property
    def Cat(self):
        return self.animals[Cat.__name__]


if __name__ == '__main__':
    z = Zoom('时间动物园')

    # 添加 一只猫
    cat1 = Cat('cat1', '食肉', '小', '温顺')
    z.add_animal(cat1)
    print(cat1.__dict__)
    print(f'{cat1.name} {cat1.cry}')
    print(f'{cat1.name} is pet : {cat1.isPet}')
    print(f'{cat1.name} is violent : {cat1.isViolent}')

    # 测试添加同一只猫
    z.add_animal(cat1)

    # 再添加一只猫
    cat2 = Cat('cat2', '食肉', '中', '凶猛')
    z.add_animal(cat2)
    print(cat2.__dict__)
    print(f'{cat2.name} {cat2.cry}')
    print(f'{cat2.name} is pet : {cat2.isPet}')
    print(f'{cat2.name} is violent : {cat2.isViolent}')

    # 查看并打印 所有猫（hash）
    have_cat = getattr(z, 'Cat')
    print(have_cat)

    # 查看动物园所有动物
    print(z.animals)
