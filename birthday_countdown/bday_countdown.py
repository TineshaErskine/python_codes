import time
from datetime import date


play = 1
while play == 1:
    birth = input('When is your birthday? MM/DD/YYYY : ')

    try:

        len(birth) != 10
        b_month = int(birth[:2])
        b_day = int(birth[:5][3:])
        b_year = int(birth[6:])
        
        birthday = date(b_year,b_month,b_day)
        today = date.today()
        birth_month_day = date(today.year,b_month,b_day)
        
        print("Today's date: " + str(today))
        print("Your birthday: " + str(birthday))
        
        days_till_bd = abs(birth_month_day-today)
        
        if today.year <= birthday.year:
            print("There's no way you were born today, this year or in the future.")
        elif today == birth_month_day:
            print("\nHappy Birthday!!!")
        elif birth_month_day > today:
            print("Sorry, today is not your birthday.")
            if days_till_bd.days == 1:
                print(str(days_till_bd.days) + " day until your birthday.")
            else:    
                print(str(days_till_bd.days) + " days until your birthday.")
        else:
            print("Sorry, today is not your birthday.")
            print(str(365-days_till_bd.days) + " days until your birthday.")
        
        break
    #except (AttributeError, ValueError) as e:
    except ValueError:
        print("Please follow the correct formating.")
        try_again = input('Would you like to try again? Y or N: ')
    
    if  try_again == 'Y' or 'y':
        play = 1
    else:
        play = 2            
        break
