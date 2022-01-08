from typing import List
from random import randint

from app.interfaces import IModelReading, IModelWriting, IObserver


class Model(IModelReading, IModelWriting):
    __observers: List[IObserver] = []
    __randint: int

    def __init__(self):
        self.updateRandom()

    @property
    def randomNumber(self):
        return self.__randint

    def updateRandom(self):
        self.__randint = randint(0, 99)
        self.notify()

    def attach(self, observer: IObserver):
        self.__observers.append(observer)

    def detach(self, observer: IObserver):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.modelIsChanged()
