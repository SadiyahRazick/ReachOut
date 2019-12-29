'''
Design Project 2
This is getting out of hand
McMaster University

1P10
Group 22

Computing Group:

Lauren LaValley (400114232)
Sadiyah Razick (400142914)

Protoytping Group:
Raymond Tolentino (400134547)
Vivian Li (400120524)
Emily Yeo (400129107)  
                    
'''

import random
import sys
import math
import time
#Store Constants
length = 72 
gRatio = 11.25

#time = 1/output
#time/speed factor = newtime
#new time by num rotations=time for num rotations

#import RPi.GPIO as GPIO

#Subprogram 1
'''GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

aSpeed=12
aDir=5
GPIO.setup(aSpeed,GPIO.OUT)
GPIO.setup(aDir,GPIO.OUT)


def stop():
    pwmMotA=GPIO.PWM(12,50)
    pwmMotA.start(0)
##    GPIO.output(12,0)
##    GPIO.output(5,0)
                    
def counterclockwise():
    GPIO.output(12,1)
    GPIO.output(5,1)

def clockwise():
    GPIO.output(12,1)
    GPIO.output(12, 0)
               
def runMotors(a):
    counterclockwise()
    time.sleep(a)
    stop()'''
    
def sp1():
    #User Input
    infile = input('Please enter "textfile.txt": ') #Calls textfile with team numbers and corresponding, also checks for valid input
    if infile == "textfile.txt":
        List = []
        File = open(infile, 'r')
    else:
        print('Invalid entry')
        sp1()

    while True: #Asks user how long they want to run the motor, checks for valid input
        try:
            lengtht=float(input('How long do you want the motors to rotate for in seconds?'))
            break
        except ValueError:
            print("Sorry, that is not a valid length of time. Please input an amount of time in seconds.\n")
    while True:
        try:
            speedFactor=int(input('Enter the speed factor you want to mulitpy the output speed by:')) #Asks for speed factor, checks for valid input 
            break
        except ValueError:
            print ("The entry is invalid, enter a whole number speed factor you want to mulitpy the output speed") 
            
    teamNum = input('Please enter a team number from 1 to 23: ') #Asks for desired team number
    #Variables are defined 
    outSpeed = None
    check = True     
    while check== True:
        for a in range (23): 
            temp = File.readline().split() #file is read and corresponding team number and input speed are spilt into separate lines
            List.append(temp) #The team numbers and input speeds are stored in a list 
            if List[a][0] == teamNum: #Finds the team number in the list that corresponds to the inputted team number 
                inSpeed = List[a][1] #input speed is accessed from the list
                outSpeed = ((float(List [a][1]))/(gRatio*60)) #Outspeed is calculated using the team's input speed and our team's gear ratio 
                outSpeed = round(outSpeed, 3) #Calculated output speed is rounded to 3 decimal places
                '''speed=(outSpeed/(17/6))*100 #Speed of the motor is calculated
                pwmMotA=GPIO.PWM(12, 1000)
                pwmMotA.start(0)
                pwmMotA.ChangeDutyCycle(speed*speedFactor)
                runMotors(lengtht)'''
                NumRotationMotor=lengtht*(outSpeed*speedFactor)
                print('The other team number is: ' + List[a][0] + '\n\n The input speed of the other team is ' + inSpeed + ' rpm \n\n The output speed is' ,  (outSpeed),  'rps \n\n The gear reduction ratio is ' + str(gRatio))
                print("\nThe motor will rotate " + str(NumRotationMotor) + " times")
                check=False

        if outSpeed == None: #If no outspeed is given, an invalid team number was entered and the while loop returns 
            print('This team does not exist, please try again')
            teamNum = input('Please enter a team number from 1-23:')
            True

    anything = input('\nEnter anything to return to main menu: ')
    mainMenu()
    
#Subprogram 2
    

#Creating Text File to right outputs too
outFile = open("subprogram.txt", 'w')

import math

def sp2():
    outFile = open("subprogram.txt", 'w')
    while True: #these statments make sure the code is unable to be broken by entering letters or decimals into the inputs
        startPos = input('\nWhat is the starting position of the fingers? Enter "fully open" or "fully closed":')
        if startPos != 'fully open' and startPos != 'fully closed' : #if the starting position "does not" equal fully closed or fully open, then the program will continue to the else statement where it breaks
            print ("Your entry is invalid, please enter either 'fully open' or 'fully closed'")
        else:
            break

    while True:
        try:
            numRotations = int(input('Enter the number of rotations for motor: '))
            break
        except ValueError: #except ValueError is able to detect if the number inputted is not an integer and prints that it is an invalid input
            print ("The entry is invalid, enter a whole number of rotations for the motor:")
    while True:
        try:
            numIncrements = int(input('Enter the number of rotational increments to print to screen: '))
            break #this last break finishes the while loop as long as all the inputs are valid, once its broken the program continues to the for loop 
        except ValueError:
            print ("The entry is invalid, enter a whole number of rotational increments:")

    for i in range(numIncrements): #This for loop says to do whats within it every single numIncrement, which is a variable input. The for loop will stop running after all the increments have been printed, and the program will exit back to the main menu

        
        i += 1 # "i" is the number of increments given, and one more is added through every cycle of the loop
        totalAngleRotMotInc = (((numRotations*360)/numIncrements) * i) #this is the rotation of the motor per each increment that is given. 

        #Constants to be used in calculation of the thumb position
        angle1 = math.radians(270) - math.acos(53.5 / 68.033)
        angle2 = - math.acos(53.5 / 68.033)

        #Variables defined as none to begin, and then assigned values throughout the calculations
        gRatio = 11.25 
        relativeRotMot = None
        motDir = None
        xi_pos = None
        xt_pos = None
        yi_pos = None
        yt_pos = None

        if startPos == 'fully open':

                if ((totalAngleRotMotInc//1012.5) % 2) == 0: #Use the total rotation of the motor per increment to check the direction of the fingers
                        relativeRotMot = totalAngleRotMotInc % 1012.5 #our gear ratio x 90 degrees 
                        motDir = "Counterclockwise" #If even, the motor direction is ccw 
                        
                elif ((totalAngleRotMotInc//1012.5) % 2) == 1: #// is dividing the number without a remainder, modulus 2 is then dividing that number by 2, but only returning the remainder, so even numbers have a remainder of zero, and odd numbers have a remainder of 1
                        relativeRotMot = 1012.5 - (totalAngleRotMotInc % 1012.5)
                        motDir = "Clockwise" #If odd, the motor dir is cw

        elif startPos == 'fully closed':

                if ((totalAngleRotMotInc//1012.5) % 2) == 0:
                        relativeRotMot = totalAngleRotMotInc % 1012.5 #this takes the total angle the motor goes through and gives the remainder in degress, which is our realativeRotMot
                        motDir = "Clockwise" #If even, the motor direction is cw
                        
                elif ((totalAngleRotMotInc // 1012.5) % 2) == 1:
                        relativeRotMot = 1012.5 - (totalAngleRotMotInc % 1012.5)
                        motDir = "Counterclockwise" #If odd, the motor direction is ccw 
                        

        angleRotFingers = (relativeRotMot / gRatio) #calculates the angle of rotation of the fingers based on the angle of the motor and our gear ratio 
        if startPos == 'fully open': #Determines the x and y positions of the finger and thumb
                #Index Calculation
                xiPos = 68.033 * math.cos(math.radians(180 + angleRotFingers))
                yiPos = 68.033 * math.sin(math.radians(180 + angleRotFingers)) + 68.033
                #Thumb Calculation                
                xtPos = 68.033 * math.cos(angle2 - math.radians(angleRotFingers)) + 53.5
                ytPos = 68.033 * math.sin(angle2 - math.radians(angleRotFingers)) + 42
                

        elif startPos == 'fully closed': #Determines the x and y positions of the finger and thumb
                #Index Calculation
                xiPos = 68.033 * math.cos(math.radians(270 - angleRotFingers))
                yiPos = 68.033 * math.sin(math.radians(270 - angleRotFingers)) + 68.033
                #Thumb Calculation 
                xtPos = 68.033 * math.cos(angle1 + math.radians(angleRotFingers)) + 53.5
                ytPos = 68.033 * math.sin(angle1 + math.radians(angleRotFingers)) + 42



        #This prints all of our values stored from the previous calculations and prints them to both the screen and the outFile that its writing to. 
        print("\nIncrement:", str(i))
        outFile.write(str(i))
        outFile.write('\n')
        print("The direction of rotation of the motor is:", str(motDir))
        outFile.write(str(motDir))
        outFile.write('\n')
        print("The angle of rotation of the motor is:", str(relativeRotMot))
        outFile.write("The angle of rotation of the motor is " + str(relativeRotMot)+"\n")
        print("The angular rotation of the fingers is",str(angleRotFingers), "relative to the starting position")

        #Writes data to a textfile
        outFile.write("The angle of rotation of the motor is")
        outFile.write(str(angleRotFingers))
        outFile.write('\n')
        print("The position of the index finger", [round(xiPos,3),round(yiPos,3)])
        outFile.write("The position of the forefinger is ("+str(xiPos)+",(" +str(yiPos)+") \n")
        print("The position of the thumb is", [round(xtPos,3), round(ytPos,3)])
        outFile.write("The position of the thumb is ("+str(xtPos)+",(" +str(ytPos)+") \n\n")
    outFile.close()

    anykey = input('\nEnter anything to return to main menu: ')
    mainMenu()
 
#Subprogram 3
def sp3():
    print("Welcome! The object of this game is to guess which number you believe the computer program has selected. You will have three attempts to guess a correct number between 0 and 10. You lose once the fingers have shut.")
    attempts=1 #The number of attempts start at 1 
    generatedNumber=random.randint(0,10) #A random number is selected by the program, using the random integer library 
    while True: #Program asks the user to guess a number, checks for valid input
        try:
            guess =int(input("Pick a number between 0 and 10  :"))
            if guess < 0 or guess > 10:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
                print("Enter a whole number between 0-10.")

    while generatedNumber != guess and attempts < 3: #If the user's guess is wrong and they still have attempts left, the program gives a hint for their next guess

        if guess < generatedNumber:
            print(" Your guess is too low ") 
        elif guess > generatedNumber:
            print(" Your guess is too high ")
        guess = int(input("Guess a number between 0 and 10: ")),
        attempts += 1 #An unsuccessful attempt is added 
        
               
    if attempts >=3 and generatedNumber != guess: #The number of attempts was used up, and the user loses the game     
        print("You reached the maximum number of tries")
        print("The number was ",generatedNumber)

    if generatedNumber==guess: #Returns this statement if the user guesses the number under the 3 attempts 
        print("You guessed it! The number was " ,generatedNumber)   
    anything = input('\nEnter anything to return to main menu: ')
    mainMenu()

#Program Menu 
def mainMenu():
    print('Program Menu: \n\n 1. Subprogram 1 \n\n 2. Subprogram 2 \n\n 3. Subprogram 3 \n\n 4. Exit from program')
    selection = input('\nEnter choice: ')
    if selection =='1':
        sp1()
    if selection =='2':
        sp2()
    if selection =='3':
        sp3()
    if selection =='4':
        sys.exit()
    else:
        print('Invalid entry. Please enter 1-4')
        mainMenu()

#Home
mainMenu()



    
