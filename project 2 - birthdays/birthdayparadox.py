import random

print('How many birthdays shall I generate? (Max 100)')
birthdays = int(input())

while(birthdays <= 1 or birthdays > 100):
    print('At least 2 birthdays, and no more than 100. Choose a valid number')
    birthdays = int(input())

date = [[0]*31,[0]*28,[0]*31,[0]*30,[0]*31,[0]*30,[0]*31,[0]*31,[0]*30,[0]*31,[0]*30,[0]*31]
months = {0:"Jan",1:"Feb",2:"Mar",3:"Apr",4:"May",5:"Jun",6:"Jul",7:"Aug",8:"Sep",9:"Oct",10:"Nov",11:"Dec"}

print(f'Here are {birthdays} birthdays:')
print_format = []
for i in range(birthdays):
    month = random.randint(0,11)
    if(month == 1): #february has 28 days - excluding leap year
        day = random.randint(0,27)
    elif(month == 0 or month ==  2 or month == 4 or month == 6 or month ==  7 or month == 9 or month == 11): # months with 31 days
        day = random.randint(0,30)
    else: #months with 30 days
        day = random.randint(0,29)
    date[month][day] +=1
    print_format.append(f'{months[month]} {day+1}')
print(", ".join(print_format))

print_format2 =[]
if not any(2 in month for month in date):
    print("In this simulation, no multiple people had a birthday on the same day")
else:
    for i in range (12):
        for j in range(len(date[i])):
            if(date[i][j] == 2):
                print_format2.append(f'{months[i]} {j+1}')
    print("In this simulation, multiple people have a birthday on: ", end ="")
    print(", ".join(print_format2))

matching_birthdays = 0
print(f'Generating {birthdays} random birthdays 100.000 times...')
input('Press Enter to begin...')
print("Let's run another 100.000 simulations.")
for i in range(0,100000):
    date = [[0] * len(month) for month in date]
    aux = 0
    if(i % 10000 == 0):
        print(f'{i} simulations run...')
    for i in range(birthdays):
        month = random.randint(0,11)
        if(month == 1):
            day = random.randint(0,27)
        elif(month == 0 or month ==  2 or month == 4 or month == 6 or month ==  7 or month == 9 or month == 11):
            day = random.randint(0,30)
        else:
            day = random.randint(0,29)
        date[month][day] +=1
    for i in range (12):
        for j in range(len(date[i])):
            if(date[i][j] == 2 and aux == 0):
                matching_birthdays +=1
                aux = 1

print(f'Out of 100.000 simulations of {birthdays} people, there was a matching birthday in that group {matching_birthdays} times.',end='')
prob = (matching_birthdays / 100000) * 100
print(f'This means that {birthdays} people have a {prob:.2f} % chance of having a matching birthday in their group.')
print("That's probably more than you would think!")
