import dataclasses
from abc import ABC, abstractmethod

VEGETABLES = ['Black_prince']
FRUITS = ['Antonovka']

states = {'nothing': 0, 'flowering': 1, 'green': 2, 'red': 3, 'rotten': 4}


class GardenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'The garden has such vegetables: {self.vegetables}')
        print(f'Also garden has such fruits: {self.fruits}')
        print(f'And such pests: {self.pests}')
        print(f'The maintainer of the garden is {self.gardener}')


@dataclasses.dataclass()
class PlantsStates:
    nothing: int
    flowering: int
    green: int
    red: int
    rotten: int


class Vegetables(ABC):
    def __init__(self, states, _vegetable_type, name):
        self.states = states
        self._vegetable_type = None
        self.name = name

    @property
    def vegetable_type(self):
        return self._vegetable_type

    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if vegetable_type in VEGETABLES:
            self._vegetable_type = vegetable_type
            print('all ok')
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {vegetable_type}')


    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')


class Fruit(ABC):
    def __init__(self, states, _fruits_type, name):
        self.states = states
        self._fruits_type = None
        self.name = name

    @property
    def fruits_type(self):
        return self._fruits_type

    @fruits_type.setter
    def fruits_type(self, fruits_type):
        if fruits_type in FRUITS:
            self._fruits_type = fruits_type
            print('all ok')
        else:
            raise Exception(f'There is no such fruit in the list. '
                            f'Your fruit: {fruits_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('The method is missing.')


class Gardener(ABC):
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    @abstractmethod
    def harvest(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def poison_pests(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('The method is missing.')


class Pests(ABC):
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    @abstractmethod
    def eat(self):
        raise NotImplementedError('The method is missing.')


class Tomato(Vegetables):
    def __init__(self, index, vegetable_type, states, name):
        super(Tomato, self).__init__(states, vegetable_type, name)
        self.index = index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'{self.vegetable_type} {self.index} is {self.state}')

    def __repr__(self):
        return f'{self.vegetable_type} {self.index} is {self.state}'

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index, 'Black_prince', states, 'Cherry') for index in range(1, num + 1)]
        self.state = 0

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """
        all([True, True, True]) = True
        all([True, True, False]) = False
        :return:
        """
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def provide_harvest(self):
        self.tomatoes = []


class Apple(Fruit):
    def __init__(self, index, fruits_type, states, name):
        super(Apple, self).__init__(states, fruits_type, name)
        self.index = index
        self.fruits_type = fruits_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'{self.fruits_type} {self.index} is {self.state}')

    def __repr__(self):
        return f'{self.fruits_type} {self.index} is {self.state}'

class AppleTree:
    def __init__(self, num):
        self.apples = [Apple(index, 'Antonovka', states, 'King') for index in range(1, num + 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        """
        all([True, True, True]) = True
        all([True, True, False]) = False
        :return:
        """
        return all([apple.is_ripe() for apple in self.apples])

    def provide_harvest(self):
        self.apples = []


class StarGardener(Gardener):
    def __init__(self, name, plants):
        super(StarGardener, self).__init__(name, plants)
        self.name = name
        self.plants = plants

    def harvest(self):
        print('Gardener is harvesting...')
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.provide_harvest()
                print('Harvesting is finished.')
            else:
                print('Too early! Your plants is not ripe.')

    def handling(self):
        print('Gardner is working...')
        for plant in self.plants:
            plant.grow_all()
        print('Gardner is finished')

    def poison_pests(self):
        pests.quantity = 3
        print('Poisoning pests... \nThe Gardener poisoned all pests. \nFor now all pests - exterminated')

    def check_states(self):
        for all_plants in self.plants:
            if all_plants.state == 3:
                return True
            return False

    def __repr__(self):
        return f'{self.name}'

class Dangerous_Pests(Pests):

    def __init__(self, pests_type, quantity):
        super(Dangerous_Pests, self).__init__(pests_type, quantity)
        self.pests_type = pests_type
        self.quantity = quantity

    def eat(self):
        for pest in range(self.quantity):
            tomato_bush.tomatoes.pop(-1)
            if len(tomato_bush.tomatoes) == 0:
                break
        for pest in range(self.quantity):
            apple_tree.apples.pop(-1)
            if len(apple_tree.apples) == 0:
                break

    def __repr__(self):
        return f'{self.pests_type} is {self.quantity}'

if __name__ == '__main__':
    # Creating list of instances for vegetables and fruits, pests and gardener
    tomato_bush = TomatoBush(4)
    apple_tree = AppleTree(4)
    pests = Dangerous_Pests('aphid', 4)
    tom = StarGardener('Tom', [tomato_bush, apple_tree])
    tom.poison_pests()
    pests.eat()
    # creating only one garden instance with vegetables and fruits
    garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=tom)
    garden.show_the_garden()
    state = tom.check_states()
    if not state:
        tom.handling()
    for i in range(3):
        tom.handling()
    tom.harvest()

# Output:

# all ok
# all ok
# all ok
# all ok
# all ok
# all ok
# all ok
# all ok
# Poisoning pests...
# The Gardener poisoned all pests.
# For now all pests - exterminated
# The garden has such vegetables: [Black_prince 1 is 0]
# Also garden has such fruits: [Antonovka 1 is 0]
# And such pests: aphid is 3
# The maintainer of the garden is Tom
# Gardner is working...
# Black_prince 1 is 1
# Antonovka 1 is 1
# Gardner is finished
# Gardner is working...
# Black_prince 1 is 2
# Antonovka 1 is 2
# Gardner is finished
# Gardner is working...
# Black_prince 1 is 3
# Antonovka 1 is 3
# Gardner is finished
# Gardner is working...
# Black_prince 1 is 3
# Antonovka 1 is 3
# Gardner is finished
# Gardener is harvesting...
# Harvesting is finished.
# Harvesting is finished.