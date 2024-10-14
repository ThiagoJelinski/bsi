from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, valor1: int, valor2: int) -> None:
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

class Calculator(Subject):
    def __init__(self):
        self.observers = []
        self._valor1 = 0
        self._valor2 = 0

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self._valor1, self._valor2)

    def set_values(self, valor1: int, valor2: int) -> None:
        self._valor1 = valor1
        self._valor2 = valor2
        self.notify_observers()

class DivisionObserver(Observer):
    def update(self, valor1: int, valor2: int) -> None:
        if valor2 == 0:
            print("Erro: Divisão por zero.")
            return
        resultado = valor1 // valor2
        print(f"Divisão: {valor1} // {valor2} = {resultado}")

class ModuloObserver(Observer):
    def update(self, valor1: int, valor2: int) -> None:
        if valor2 == 0:
            print("Erro: Resto da divisão por zero.")
            return
        resultado = valor1 % valor2
        print(f"Resto da divisão: {valor1} % {valor2} = {resultado}")

class MultiplicationObserver(Observer):
    def update(self, valor1: int, valor2: int) -> None:
        resultado = valor1 * valor2
        print(f"Multiplicação: {valor1} * {valor2} = {resultado}")

def main():
    calculadora = Calculator()

    division_observer = DivisionObserver()
    modulo_observer = ModuloObserver()
    multiplication_observer = MultiplicationObserver()

    calculadora.register_observer(division_observer)
    calculadora.register_observer(modulo_observer)
    calculadora.register_observer(multiplication_observer)

    calculadora.set_values(10, 2)
    calculadora.set_values(15, 4)

if __name__ == "__main__":
    main()

