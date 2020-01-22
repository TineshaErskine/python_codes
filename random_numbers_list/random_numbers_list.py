# PSEUDOCODE
#This program will take 12 random integers inclusive of 18-65 and add them to an empty list, nums
#It will then print the values on the same line
#It will sort the list and then print the sorted list on the same line using the unpack feature for tuples
#Then it will slice the first 8 elements of the sorted list nums, save it to a new list called start, and print them
#Then it will slice the last for elements of the sorted list nums, save it to a new list named finish, and print them
#It will then coun the amoun of even and odd integers from the list nums
#Then it will print the total count of each and return these totals
#Lastly it will print the 4th element in the sorted num list 


#import randonm to use its functions
import random


def main():

    #Create an empty list
    nums = []

    #Start a for loop to create and add random integers to the list
    for n in range(12):

        #pick a random number
        integer = random.randint(18,65)

        #add that number to the list
        nums.append(integer)
    
    #Start a for loop to print the integers in one line
    for integer in nums:
        print(integer, end=' ')
    
    #To move to another line
    print()

    #Sort the list
    nums.sort()

    #Convert list to a tuple
    nums_tuple = tuple(nums)

    #Unpack feature of tuples to print the sorted values
    print(*nums_tuple)

    #Create a new list
    start = []

    #Slice first 8 elements from sorted nums and save them to start list
    start = nums[:7]

    #Print start list
    print(start)

    #Create a new list
    finish = []

    #Slice the last 4 elements of the sorted nums list and save it to the finish list
    finish = nums[8:]

    #Print finish list
    print(finish)

    #Call the even_odd function
    even_odd(nums)



def even_odd(nums):

    #Declare an even counter variable
    evens = 0

    #Declare an odd counter variable
    odds = 0

    #Start a for loop to add the even and odd integers
    for n in nums:

        #start an if statement to see if integer is even or odd
        if (n % 2) == 0:

            #The integer is even
            evens+=1
        else:
            #The integer is odd
            odds+=1

    #Print the total of even and odds
    print("List had", evens, "evens and", odds, "odds")

    #Print the 4th element in the list
    print("The 4th element in sorted nums is", nums[3])
    
    #Return the even and odd variables
    return evens, odds


#Run the main method
main()
