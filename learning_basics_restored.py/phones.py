class Phone:
    def __init__(self, model, model_num, color, phone_size):
     self.model = model
     self.model_num = model_num
     self.color = color
     self.phone_size = phone_size

    def describe(self):
       print(f"{self.color}, {self.phone_size}, {self.model}, {self.model_num}")
    def turn_on(self):
       print("You turned on your phone!") 
    def turn_off(self):
       print("You turned off your phone!")
   