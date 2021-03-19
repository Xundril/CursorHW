from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
import uuid
import time


class Animal(ABC):
    def __init__(self, strength: int, speed: int):
        self.id = None
        self.max_power = strength
        self.current_strength = 1
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError

class Predator(Animal):
    def __init__(self, strength: int, speed: int):
        super().__init__(strength, speed)
        self.id = None
        self.max_strength = strength
        self.current_strength = 2
        self.speed = speed

    def eat(self, forest: Forest):
        prey = random.choice(list(forest.animals.values()))
        if prey.id == self.id:
            print('The hunt was unsuccessful')
        else:
            if (self.speed > prey.speed) and (self.current_strength > prey.current_strength):
                print('Predator eating...')
                tmp = self.current_strength
                self.current_strength = min(self.current_strength + self.max_strength * 0.5, self.max_strength)
                print(f'Predator restored {self.current_strength - tmp} strength')
            else:
                print('Predator did not caught prey, both are tired')
                self.current_strength = self.current_strength - 0.3 * self.max_strength
                forest.animals[prey.id].current_strength = forest.animals[prey.id].current_strength - 0.3 * forest.animals[prey.id].max_strength

    def __str__(self):
        return f'{self.__class__.__name__}'

class Herbivorous(Animal):
    def __init__(self, strength: int, speed: int):
        super().__init__(strength, speed)
        self.id = None
        self.max_strength = strength
        self.current_strength = 1.5
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}'

    def eat(self, forest: Forest):
        print('Herbivorous eating...')
        tmp = self.current_strength
        self.current_strength = min(self.current_strength + self.max_strength * 0.5, self.max_strength)
        print(f'Herbivorous restored {self.current_strength - tmp} strength')


AnyAnimal: Any[Herbivorous, Predator]

class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print('There is new animal', animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(animal, 'is removed from forest')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        generated_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)), Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        generated_animal.id = uuid.uuid4()
        yield generated_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_strength < 1:
                animal_to_remove.append(animal.id)
        for animal_id in animal_to_remove:
            forest.remove_animal(forest.animals[animal_id])
        if not forest.any_predator_left():
            print('Predators is gone!')
            break
        for animal in forest.animals.values():
            animal.eat(forest=forest)
        time.sleep(1)


## Output (one of other results):

# There is new animal Predator
# There is new animal Herbivorous
# There is new animal Predator
# There is new animal Predator
# There is new animal Predator
# There is new animal Predator
# There is new animal Predator
# There is new animal Herbivorous
# There is new animal Herbivorous
# There is new animal Herbivorous
# Predator did not caught prey, both are tired
# Herbivorous eating...
# Herbivorous restored 43.0 strength
# Predator did not caught prey, both are tired
# Predator did not caught prey, both are tired
# Predator did not caught prey, both are tired
# Predator did not caught prey, both are tired
# Predator eating...
# Predator restored 35.5 strength
# Herbivorous eating...
# Herbivorous restored 44.5 strength
# Herbivorous eating...
# Herbivorous restored 18.0 strength
# Herbivorous eating...
# Herbivorous restored 44.5 strength
# Predator is removed from forest
# Predator is removed from forest
# Predator is removed from forest
# Predator is removed from forest
# Predator is removed from forest
# Herbivorous is removed from forest
# Herbivorous eating...
# Herbivorous restored 43.0 strength
# Predator eating...
# Predator restored 33.5 strength
# Herbivorous eating...
# Herbivorous restored 43.0 strength
# Herbivorous eating...
# Herbivorous restored 44.5 strength
# Herbivorous eating...
# Herbivorous restored 24.299999999999997 strength
# Predator did not caught prey, both are tired
# Herbivorous eating...
# Herbivorous restored 26.700000000000003 strength
# Herbivorous eating...
# Herbivorous restored 25.200000000000003 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey, both are tired
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 25.799999999999997 strength
# The hunt was unsuccessful
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey, both are tired
# Herbivorous eating...
# Herbivorous restored 26.700000000000003 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey, both are tired
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 26.700000000000003 strength
# Predator is removed from forest
# Predators is gone!