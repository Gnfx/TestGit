# Паттерн наблюдатель (observer)
from abc import ABC, abstractmethod


class SystemVideoSurveillance:
    def __init__(self):
        self.__observers = set()

    def attach(self, observer):
        self.__observers.add(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.make_photo()




class AbstractObserver(ABC):
    @abstractmethod
    def make_photo(self):
        pass


class Camera(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def make_photo(self):
        print(f"{self.__name} сделала фото")


cam1 = Camera("Камера 1")
cam2 = Camera("Камера 2")
cam3 = Camera("Камера 3")
cam4 = Camera("Камера 4")
systemVideoSurveillance = SystemVideoSurveillance()
systemVideoSurveillance.attach(cam1)
systemVideoSurveillance.attach(cam2)
systemVideoSurveillance.attach(cam3)
systemVideoSurveillance.attach(cam4)

# Кто-то позвонил в дверь
# systemVideoSurveillance.notify()


systemVideoSurveillance.detach(cam4)

systemVideoSurveillance.notify()




