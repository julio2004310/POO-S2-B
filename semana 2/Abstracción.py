from abc import ABC, abstractmethod


class Vehiculo(ABC):

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass
