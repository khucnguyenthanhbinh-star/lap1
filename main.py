class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
    
    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return cls(name, type, size // 2)
    
    def add_item(self, item_name: str):
        current_quantity = sum(self.items.values())
        if current_quantity < self.capacity:
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the store"
        return "Not enough capacity in the store"
    
    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"
    
    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
        
first_store = Store("First store", "Fruit and Veg", 20) 
second_store = Store.from_size("Second store", "Clothes", 500) 
print(first_store) 
print(second_store) 
print(first_store.add_item("potato")) 
print(second_store.add_item("jeans")) 
print(first_store.remove_item("tomatoes", 1)) 
print(second_store.remove_item("jeans", 1))

import math

class Integer:
    def __init__(self, value: int):
        self.value = value
    
    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(math.floor(value))
        return "value is not a float"
    
    @classmethod
    def from_roman(cls, value):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for char in reversed(value):
            curr_value = roman_map.get(char, 0)
            if curr_value >= prev_value:
                result += curr_value
            else:
                result -= curr_value
            prev_value = curr_value
        return cls(result)
    
    @classmethod
    def from_string(cls, value):
        try:
            return cls(int(value))
        except (ValueError, TypeError):
            return "wrong type"
    
    def add(self, integer):
        if isinstance(integer, Integer):
            return self.value + integer.value
        return "number should be an Integer instance"
        
first_num = Integer(10) 
second_num = Integer.from_roman("IV") 
 
print(Integer.from_float("2.6")) 
print(Integer.from_string(2.6)) 
print(first_num.add(second_num)) 

class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)
    
    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result
    
    @staticmethod
    def divide(*args):
        if not args:
            raise ValueError("No arguments provided")
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Division by zero")
            result /= num
        return result
    
    @staticmethod
    def subtract(*args):
        if not args:
            raise ValueError("No arguments provided")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
        
print(Calculator.add(5, 10, 4)) 
print(Calculator.multiply(1, 2, 3, 5)) 
print(Calculator.divide(100, 2)) 
print(Calculator.subtract(90, 20, -50, 43, 7)) 

class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False
    
    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.guests = people
            self.is_taken = True
        else:
            return f"Room number {self.number} cannot be taken"
    
    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:
            return f"Room number {self.number} is not taken"
            
