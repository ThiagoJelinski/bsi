from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, value1: int, value2: int) -> None:
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
        self._value1 = 0
        self._value2 = 0

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self._value1, self._value2)

    def set_values(self, value1: int, value2: int) -> None:
        self._value1 = value1
        self._value2 = value2
        self.notify_observers()

class DivisionObserver(Observer):
    def update(self, value1: int, value2: int) -> None:
        if value2 == 0:
            print("Error: Division by zero.")
            return
        result = value1 // value2
        print(f"Division: {value1} // {value2} = {result}")

class ModuloObserver(Observer):
    def update(self, value1: int, value2: int) -> None:
        if value2 == 0:
            print("Error: Modulo by zero.")
            return
        result = value1 % value2
        print(f"Modulo: {value1} % {value2} = {result}")

class MultiplicationObserver(Observer):
    def update(self, value1: int, value2: int) -> None:
        result = value1 * value2
        print(f"Multiplication: {value1} * {value2} = {result}")

def main():
    calculator = Calculator()

    division_observer = DivisionObserver()
    modulo_observer = ModuloObserver()
    multiplication_observer = MultiplicationObserver()

    calculator.register_observer(division_observer)
    calculator.register_observer(modulo_observer)
    calculator.register_observer(multiplication_observer)

    calculator.set_values(10, 2)
    calculator.set_values(15, 4)

if __name__ == "__main__":
    main()

#2

from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, news: str) -> None:
        pass

class IObservable(ABC):
    @abstractmethod
    def subscribe(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

class Reuters(IObservable):
    def __init__(self):
        self._observers = []
        self._latest_news = ""

    def subscribe(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: IObserver) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, news: str) -> None:
        self._latest_news = news
        self.notify_observers()

class NewsChannel(IObserver):
    def __init__(self, name: str):
        self.name = name

    def update(self, news: str) -> None:
        print(f'{self.name} recebeu uma atualização: {news}')

def main():
    reuters = Reuters()

    cnn = NewsChannel("CNN")
    fox_news = NewsChannel("Fox News")
    bbc = NewsChannel("BBC")

    reuters.subscribe(cnn)
    reuters.subscribe(fox_news)
    reuters.subscribe(bbc)

    reuters.add_news("Notícia urgente: Evento inesperado aconteceu!")

    reuters.unsubscribe(fox_news)

    reuters.add_news("Atualização: Mais detalhes sobre o evento.")

if __name__ == "__main__":
    main()
