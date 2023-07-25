#!/usr/bin/python

from dataclasses import dataclass
from datetime import date

@dataclass
class FoodItem:
    name: str
    category: str  # => better to have some enums/other object for type of food
    expiration_date: date
