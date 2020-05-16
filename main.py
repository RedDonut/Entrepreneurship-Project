def amount_of_water_needed_weekly():
  '''This takes in 2 inputs, the plant type and temperature and returns the amount of water needed weekly.'''

  #Dictionary of all crops and minimum amount of water needed per week in inches
  plant_watering_inches = {
    'Potato': 1.5,
    'Onion': 1,
    "Tomato": 1.25,
    "Cabbage": 1.5,
    "Green Bean": .5,
    "Carrot": 1,
    "Eggplant": 1,
    "Garlic": .75,
    "Ginger": 1
  }
  #input takes in the name of the plant
  plant_type = (input("Name of Plant: "))

  #This finds the plant in the dictionary and assigns the value to watering_amount
  watering_amount = plant_watering_inches.get(plant_type)

  #input takes in the temperature
  temperature = int(input("What is the surrounding temperature in Fahreneheit: "))

  #if temperature > 75 then add .1 inches of water per degree
  #If temperature too high or low, end process
  if temperature > 75 and temperature < 87:
    difference = temperature - 75
    total_amount_needed = watering_amount + (difference * .1)
  elif temperature < 60 or temperature >= 87:
    print("You will not be able to grow crops in this weather.")
    exit()
  elif temperature >= 60 and temperature <= 75:
    total_amount_needed = watering_amount

  #print final amount needed
  print("Amount of water needed weekly:", end=' ')
  print(total_amount_needed, end=" ")

  #inch for singular, inches for plural
  if total_amount_needed > 1:
    print("inches")
  else:
    print("inch")
amount_of_water_needed_weekly()