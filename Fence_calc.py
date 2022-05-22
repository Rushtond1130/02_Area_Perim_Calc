# Functions

#  check if more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please Enter A NUMBER That Is More Than Zero."
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # check if more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    

# Main routine how spell plz help

# Introduction
print()
print("***** Fence Cost Calculator *****")
print()

bye_message = ("Thank-you For Using The Fence Cost Calculator.")
yn_enter = False 

# Start calc loop

keep_going = "y"
while keep_going == "y":

    print("Please Answer Some Questions Regarding Your Fence. :)")

    width = num_check("width (m): ")
    length = num_check("length(m): ")
    fence_price_m = num_check ("Fencing price /m :$")

    perimeter = (width + length) * 2 

    full_fence_cost = (perimeter * fence_price_m)


    print ()
    print("Total Fence Cost:$ {:.2f} ".format(full_fence_cost))
    print()
    print ("*-"*30) 
    keep_going = input("Would You Like To Keep Going? y/n :") .lower()
    print ()

    if keep_going == ("y") : 
        yn_enter = True
     
    if keep_going == ("n"):
        yn_enter = True
        print (bye_message)

    if yn_enter == False:
        print ("Invalid Input.")
        print ("Goodbye :)")



        
    
    