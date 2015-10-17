from enum import Enum


class Apple:
    class AppleState(Enum):
        fresh = 1
        eaten = 2

    def __init__(self):
        self.state = Apple.AppleState.fresh

    def eat(self):
        self.state = Apple.AppleState.eaten
