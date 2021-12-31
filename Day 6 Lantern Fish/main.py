
from typing import Optional
from functools import cache


class Fish(object):
    def __init__(self, timer:int, init_timer:int = 6):
        self.timer = timer
        self.init_timer = init_timer

    def reset(self):
        self.timer = self.init_timer

    def day_pass(self, days:int) -> Optional['Fish']:
        self.timer -= days
        if self.timer == -1:
            self.reset()
            return self.get_spawn()
        

    def get_spawn(self):
        return Fish(8, self.init_timer)

    def __str__(self):
        return f"Fish {self.init_timer}: {self.timer}"


def print_fishes(fishes:list):
    for fish in fishes:
        print(fish)

@cache
def new_fish_offsprings(days: int) -> int:
    acc = 1
    if days <= 0:
        return acc
    
    days -= 9
    acc += new_fish_offsprings(days)

    while(days - 7 > 0):
        days -= 7
        acc += new_fish_offsprings(days)
    return acc

def calculate_offspring(fish: Fish, days: int):
    # Current total fishes
    acc = 1

    # If there are no days
    if days <= fish.timer:
        return acc

    days -= fish.timer - 1
    acc += new_fish_offsprings(days)
    while days - 7 > 0:
        days -= 7
        acc += new_fish_offsprings(days)
    return acc

if __name__ == '__main__':
    with open('test_input.txt') as f:
        lines = f.read()
    fishes = list(map(lambda x: Fish(int(x)), lines.split(',')))
    
    DAYS = 3
    fish_c = 0

    for fish in fishes:
        r =  calculate_offspring(fish, DAYS)
        print(r)
        fish_c += r

    print(fish_c)