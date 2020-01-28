#!/usr/bin/env python3.7


class Piglet:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color


dennis = Piglet('185', 'brown')


@Piglet
def print_stuff():
    return(f'{self.weight}, {self.color}')


dennis.print_stuff()
