class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"Sound of {self.name} is: {self.name}! {self.name}!")

  def display_details(self):
    print(f"Entry Number: {self.entry}")
    print(f"Name: {self.name}")
    print(f"Type: {', '.join(self.types)}")
    print(f"Description: {self.description}")
    if self.is_caught:
      print(f"{self.name} has already been caught!")
    else:
      print(f"{self.name} has not been caught yet.")
    print("-" * 40)

# Pokémon objects
pikachu = Pokemon(25, 'Pikachu', ['Electric'],
                  'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.',
                  True)

charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'],
                    'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.',
                    False)

gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'],
                   'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.',
                   False)

# Interact with the Pokémon
pikachu.speak()
charizard.speak()
gyarados.speak()

pikachu.display_details()
charizard.display_details()
gyarados.display_details()