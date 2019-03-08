from .framework import Product, Creator


class ConcreteProduct(Product):
    # override
    def _method1(self):
        print('concrete method1')

    # override
    def _method2(self):
        print('concrete method2')

    # override
    def _method3(self):
        print('concrete method3')


class ConcreteCreator(Creator):
    # override
    def _factory_method(self) -> ConcreteProduct:
        print('concrete factory method')
        return ConcreteProduct()
