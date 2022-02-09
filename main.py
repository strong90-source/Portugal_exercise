print('''           
                  _                     _ 
                 | |                   | |
 _ __   ___  _ __| |_ _   _  __ _  __ _| |
| '_ \ / _ \| '__| __| | | |/ _` |/ _` | |
| |_) | (_) | |  | |_| |_| | (_| | (_| | |
| .__/ \___/|_|   \__|\__,_|\__, |\__,_|_|
| |                          __/ |        
|_|                         |___/       
''')
print("Welcome to Portugal.")
print("Your mission is to explore this country.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

question1 = input('Do you want to explore North or South of Portugal? Type "North" or "South"').lower()

if question1 == "north":
  print("You are in Porto now, let's eat some Francesinhas -> https://en.wikipedia.org/wiki/Francesinha")
elif question1 == "south":
  print("You are in Algarve now, voted Best Beach Destination in the world -> https://www.theportugalnews.com/news/2020-12-04/algarve-voted-best-beach-destination-in-the-world/56998")
else: 
  print("You are not in Portugal anymore! Hope to see you agian :)")

question2 = input('Would you like to visit Azores or Madeira??? Type "Azore" or "Madeira"').lower()

if question2 == "madeira":
  print("You are now in Madeira, find moure about this amazing place -> https://en.wikipedia.org/wiki/Madeira")
elif question2 == "azores":
  print("You are now in Madeira, find moure about this amazing place -> https://en.wikipedia.org/wiki/Azores")
else:
  print("You are not in Portugal anymore! Hope to see you agian :)")
