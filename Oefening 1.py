vijhanden = ["Goblin", "Draak", "Trol"]
goud = 0
wapen =str(input("kies een wapen, (zwaard, boog of toverstok):"))
import random
print("Je wordt aangevallen door een", random.choice(vijhanden))
actie = str(input("wil je vechten of vluchten"))

if actie in "vechten"and wapen in "zwaard" and "Goblin":
    print("Je hebt het gevecht gewonnen")
if actie in "vluchten":
        print("Je bent gevlucht")
else:
    print("Je hebt het gevecht verloren")

if actie in "vechten"and wapen in "boog" and "Trol":
    print("Je hebt het gevecht gewonnen")
if actie in "vluchten":
        print("Je bent gevlucht")
else:
    print("Je hebt het gevecht verloren")

if actie in "vechten"and wapen in "toverstok" and "Draak":
    print("Je hebt het gevecht gewonnen")
if actie in "vluchten":
      print("Je bent gevlucht")
else:
    print("Je hebt het gevecht verloren")

if "Je hebt het gevecht gewonnen":
    goud +=1
    print("goud is", goud)