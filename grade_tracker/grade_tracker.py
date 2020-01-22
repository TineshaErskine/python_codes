# PSEUDOCODE
#This program will have a method create() that will prompt the user to enter any number of course name
#It will then prompt them to enter the grade for that course
#It will write this data to a file named grades.txt
#To exit this loop of input the user will have the option to press enter instead of a course name
#Once Enter is pressed the file will be closed and a statement will print stating this
#It will also return the bool value true to the main function
#This program will also have a method retrieve() that will read the file grades.tx, print the course names and grades, and then calculate the average grade to 2 decimal places
#It will then return the vaiable used for the average to the main method


def main():

    #Call the create function
    create()

    #Call the retrieve function
    retrieve()




def create():

    #Open the file to write in it
    grades_file = open('grades.txt', 'w')

    #Prompt the user to to enter a course name
    course = input("Enter course name or Enter to quit: ")

    #Start a while loop
    while course != '':

        #Prompt the user for that course grade
        grade = input("Enter grade (integer) achieved: ")

        #Write that data to the file
        grades_file.write(course +'\n')
        grades_file.write(grade +'\n')

        #Prompt the user to to enter a course name
        course = input("Enter course name or Enter to quit: ")

    #close the file
    grades_file.close()

    #Print the statement that the file is closed 
    print("File was created and closed")

    #Return the bool value 
    return True


def retrieve():

    #Open the file
    grades_file = open('grades.txt', 'r')

    #declare a variable total to hold the total for thr grades
    total = 0.0

    #declare a variable counter to hold the amount of grades
    counter = 0

    #Print a statement before listing off course names and grades
    print("\nHere are your grades:")

    #read the first line of the file and set it to the course variable
    course = grades_file.readline()

    #Loop through the data and print the course and grade statements
    while course != '':

        #Read the next line which is grade
        grade = grades_file.readline()

        #Remove the newlines from fields
        course = course.rstrip('\n')
        grade = int(grade.rstrip('\n'))

        #Add the grade to the total
        total+=grade

        #Add 1 to the counter
        counter+=1

        #print the statement
        print(course, "score is", grade)

        #read the next line of the file and set it to the course variable
        course = grades_file.readline()

    #Calculate the avg grade
    avg_grade = total/counter

    #Print the avg grade
    print("Average grade among your courses is",format(avg_grade,'.2f') )

    #close file
    grades_file.close()

    #Return the variable for the avg grade
    return avg_grade



#call the main function
main()
