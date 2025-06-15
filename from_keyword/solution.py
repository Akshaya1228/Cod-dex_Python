# Write code below 💖

from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
randon_planet=ch(planets)

if randon_planet== 'Mercury':
  r=2440
elif randon_planet=='Venus':
  r=6052
elif randon_planet== 'Earth':
  r=6371
elif randon_planet=='Mars':
  r=3390
elif randon_planet=='Saturn':
  r=58232
else :
  print("Oops! An error occurred." )
area=4*pi*(r**2)
print(randon_planet,"area is",round(area))