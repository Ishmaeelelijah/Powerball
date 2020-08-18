#Ishmaeel Elie
#Class one
#age player must enter his or her age
#if player is below the age indicated can not play lotto
name = input("Please enter your name:")
age = int(input(" Please enter your age:"))
if age <= 18:
 print("Tickets only sold and to be played for person 18 and over!!!")
 exit()
#if you are not 18 the code will not run
#code starts here
import random

lotto_numbers = []

for i in range(0, 6):
    num = random.randint(1, 50)
    lotto_numbers.append(num)
    while num in lotto_numbers:
        num = random.randint(1,49)



lotto_numbers.sort()

selection_num = []
#lucky number imputs and player must input 6 numbers
for i in range(0, 6):
    selection = int(input("Please enter a number between 1 and 49: "))
    selection_num.append(selection)

selection_num.sort()

correct_guesses = 0
if i in selection_num:
    if i in lotto_numbers:
        correct_guesses += 1
#prize list and how much a player can win
prize = 0
if correct_guesses == 6:

    prize += 10000000

elif correct_guesses == 5:

    prize += 8,584.00

elif correct_guesses == 4:

    prize += 2,384.00

elif correct_guesses == 3:
    prize +=  100.50

elif correct_guesses == 2:

    prize += 20.0

elif correct_guesses == 0:
    print("You did not win anything please try again next time\n")

#All the prints
file = open("Lotto_Plus_Draw.txt","w+") #oping up my answer in a text file
#this is the prize list to be won
print("This is the prize list according the the amount of numbers you get right",file=file)
print("Prediction are as followed: \n",file=file)
print("6 numbers correct","Prize-R10,000,000.00\n",file=file)
print("5 numbers correct","Prize-R8,584.00\n",file=file)
print("4 numbers correct","Prize-R2,384.00\n",file=file)
print("3 numbers correct","Prize- R100.50\n",file=file)
print("2 numbers correct","Prize-R20.00\n",file=file)
print("0 numbers correct","Prize-R0",file=file)

print("Players name and age is:",file=file)
print(name,",",age,file=file)
print( "Players lotto selection numbers:",file=file)
print(selection_num,file=file)
print("The lucky lotto numbers for this week is:",file=file)
print(lotto_numbers,file=file)
print("You have guessed ", str(correct_guesses), " number(s) correctly\n",file=file)

#date and time
import datetime
now = datetime.datetime.now()
print ("Time played lotto: ",file=file)
print (now.strftime("%Y-%m-%d %H:%M:%S"),file=file)
file.close()





