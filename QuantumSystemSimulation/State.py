import random
from enum import Enum


class State(Enum):
    DEGREE0 = 0
    DEGREE90 = 1
    DEGREE45 = 2
    DEGREE135 = 3

    def state_to_bit(state):
        if state in [State.DEGREE0, State.DEGREE45]:
            return 0
        else:
            return 1


