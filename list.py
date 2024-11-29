
import random
import time

class Passenger:
    def __init__(self, name, start_floor):
        self.name = name
        self.start_floor = start_floor
        self.target_floor = random.randint(1, 10)

class Elevator:
    UP = '^'
    DOWN = 'v'
    
    def __init__(self):
        self.current_floor = 1
        self.passengers = []
        
    def move_to_floor(self, floor):
        print(f"Elevator is moving from floor {self.current_floor} to floor {floor}")
        time.sleep(1)
        self.current_floor = floor
    
    @property
    def direction(self):
        directions = []
        for passenger in self.passengers:
            if self.current_floor < passenger.target_floor:
                directions.append(f"{passenger.name}: {Elevator.UP}")
            elif self.current_floor > passenger.target_floor:
                directions.append(f"{passenger.name}: {Elevator.DOWN}")
            else:
                directions.append(f"{passenger.name} is already at the target floor.")
        return directions
    
    def drop_off_passengers(self):
        remaining_passengers = []
        for passenger in self.passengers:
            if self.current_floor == passenger.target_floor:
                print(f"{passenger.name} has reached the target floor {passenger.target_floor}.")
            else:
                remaining_passengers.append(passenger)
        self.passengers = remaining_passengers

passenger_names = ["Ali", "Leyla", "Murad", "Aysel"]
passengers = [Passenger(name, random.randint(1, 10)) for name in passenger_names]

elevator = Elevator()

elevator.passengers = passengers

for passenger in passengers:
    elevator.move_to_floor(passenger.start_floor)  
    print(f"Picked up {passenger.name} at floor {passenger.start_floor}. Target floor: {passenger.target_floor}")
    
    elevator.move_to_floor(passenger.target_floor)  
    elevator.drop_off_passengers()  
        

          

