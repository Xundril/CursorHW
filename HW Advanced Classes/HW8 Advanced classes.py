from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
import uuid
import time


class Animal(ABC):
    def __init__(self, strength: int, speed: int):
        self.id = None
        self.max_strength = strength
        self.current_strength = strength
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError('Your method is not implemented')

class Predator(Animal):
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
                prey.current_strength = 0
            else:
                print('Predator did not caught prey')
                self.current_strength = self.current_strength - 0.3 * self.max_strength
                prey.current_strength = prey.current_strength - 0.3 * prey.max_strength

    def __str__(self):
        return f'{self.__class__.__name__}'

class Herbivorous(Animal):
    def eat(self, forest: Forest):
        print('Herbivorous eating...')
        tmp = self.current_strength
        self.current_strength = min(self.current_strength + self.max_strength * 0.5, self.max_strength)
        print(f'Herbivorous restored {self.current_strength - tmp} strength')

    def __str__(self):
        return f'{self.__class__.__name__}'

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

    def __iter__(self):
        self.num = 0
        self.animal_item = list(self.animals.values())
        return self

    def __next__(self):
        self.num += 1
        if self.num <= len(self.animal_item):
            return self.animal_item[self.num - 1]
        else:
            raise StopIteration

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


## Output (one of random results):

# There is new animal Predator
# There is new animal Herbivorous
# There is new animal Herbivorous
# There is new animal Herbivorous
# There is new animal Herbivorous
# There is new animal Predator
# There is new animal Predator
# There is new animal Herbivorous
# There is new animal Predator
# There is new animal Predator
# The hunt was unsuccessful
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey
# Predator eating...
# Predator restored 0 strength
# Predator is removed from forest
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 17.5 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# The hunt was unsuccessful
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 21.299999999999997 strength
# Herbivorous eating...
# Herbivorous restored 14.0 strength
# Herbivorous eating...
# Herbivorous restored 25.200000000000003 strength
# Predator did not caught prey
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator did not caught prey
# Predator is removed from forest
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 21.299999999999997 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 25.200000000000003 strength
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 26.4 strength
# Predator did not caught prey
# Predator is removed from forest
# Predator is removed from forest
# Predator did not caught prey
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Herbivorous eating...
# Herbivorous restored 42.0 strength
# Herbivorous eating...
# Herbivorous restored 0 strength
# Predator is removed from forest
# Predators is gone!
