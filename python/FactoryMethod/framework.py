from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def _method1(self):
        pass

    @abstractmethod
    def _method2(self):
        pass

    @abstractmethod
    def _method3(self):
        pass


class Creator(metaclass=ABCMeta):
    def create(self) -> Product:
        product = self._factory_method()
        return product

    @abstractmethod
    def _factory_method(self) -> Product:
        pass
