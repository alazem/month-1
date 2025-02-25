class Vehicle:
    def __init__(self, make, model):
        self._make = make  
        self._model = model 
    
    def describe(self):
        return f"This is a {self._make} {self._model}."
    
    def get_make(self):
        return self._make
    
    def get_model(self):
        return self._model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors 
    
    def describe(self):
        return f"This car is a {self._make} {self._model} with {self._num_doors} doors."
    
    def get_num_doors(self):
        return self._num_doors

class Bike(Vehicle):
    def __init__(self, make, model, has_gears):
        super().__init__(make, model)
        self._has_gears = has_gears 
    
    def describe(self):
        gear_info = "with gears" if self._has_gears else "without gears"
        return f"This bike is a {self._make} {self._model} {gear_info}."
    
    def has_gears(self):
        return self._has_gears


def vehicle_info(vehicle):
    print(vehicle.describe())


car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "MT-07", True)


vehicle_info(car) 
vehicle_info(bike)  

