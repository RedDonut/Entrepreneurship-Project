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
plant_type = input("Name of Plant: ")
temperature = int(input("What is the surrounding temperature in Fahreneheit: "))
print("Amount of water needed weekly:")
print(str(plant_watering_inches[plant_type]) + " inch(es)")