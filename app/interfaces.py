from abc import ABCMeta, abstractmethod


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def modelIsChanged(self):
        pass


class IModelReading(metaclass=ABCMeta):
    @abstractmethod
    def randomNumber(self):
        pass

    @abstractmethod
    def attach(self, observer: IObserver):
        pass

    @abstractmethod
    def detach(self, observer: IObserver):
        pass


class IModelWriting(metaclass=ABCMeta):
    @abstractmethod
    def updateRandom(self):
        pass


class IController(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass
