from enum import Enum


# 난이도 Enum (각 난이도의 행, 열)
class Difficulty(Enum):
    BEGINNER = 3, 3
    INTERMEDIATE = 6, 4
    EXPERT = 10, 5