menu = "weihenstephan , tuborg , goldstar , carlsberg , blank and stella . "

name = input("""Welcome to NPK-Beer's
what is your name ?\n""")

order = input("Hi " + name + """ what beer would you like to drink ?
we got """ + menu + "\n" )

age = input("how old are you ?\n")

ligal = 18
import time 
if int(age) >= int(ligal):
    size = input("Ok ,what size would you like ? 1/2L or 1L " + order + "\n" )

else:
    print("Minimum Legal Drinking Age is 18")
    time.sleep(3)
    print("sorry")
    time.sleep(2)
    exit()
time = input("how many " + size + "-" + order + "s do you want ? ")


if order == "weihenstephan":
    price = 5
elif order == "tuborg":
    price = 8
elif order == "goldstar":
    price = 7
elif order == "carlsberg":
    price = 10
elif order == "blank":
     price = 9
elif order == "stella":
     price = 11

if size == "1L":
    price = float(price) * float(1.3)
tutal = float(price) * float(time) 

print("so the bill is " + str(tutal) + "$ \n\n") 
tip = input("would you like to tip the bartender ?\n")

if tip == "yes":
    import time
    percent = input("5% , 10% , 20%\n")
    if percent == "5%":
         percentt = 1.05
    elif percent == "10%":
        percentt = 1.1
    elif percent == "20%":
        percentt = 1.2
    tutalwithtip = float(tutal) * float(percentt)
    time.sleep(2)
    print("the tutal bill is " + str(tutalwithtip) + "$\n")    
else:
    import time
    time.sleep(2)
    print("kamtsan")
time.sleep(3)
print("thank you " + name + ", have a nice day !\n")
time.sleep(3)

