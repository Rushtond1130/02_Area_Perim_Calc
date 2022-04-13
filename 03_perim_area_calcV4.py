 # functions go here

 # checks input is a number more than zero
def num_check(question):

    valid = False
    while not valid:
        error = "Please Enter A NUMBER That Is More Than Zero."
        try:

            response = float(input(question))

            if response > 0:
                return response
            
            else:
                print(error)
                print ()

        except ValueError:
            print(error)
            print ()


# main routine goes here

# introduction 
print()
print("*====={Area perimeter calculator}=====*")
print()

# start of calculator loop

Thank_you = ("Thank you For Using Area Preimeter Calculator")

keep_going = "y"

yn_enter = False

bye_message = ("Goodbye, thank you for using area perimeter calculator.")

while keep_going == "y":

    width = num_check("width (m): ")
    height = num_check("height (m): ")

    # calculate area (width x height)
    area = width * height 

    # calculate perimeter (width x height) x2
    perimeter = 2 * (width + height)

    # output area and perimeter
    print ()
    print("Perimeter: {:.2f} Meters".format(perimeter))
    print("Area: {:.2f} square Meters".format(area))
    print()

    keep_going = input("Would You Like To Keep Going? y/n: ")

 # I could probably make this part better, but it was just an expiriment.

    if keep_going == ("y"):
        yn_enter = True
     
    if keep_going == ("n"):
        yn_enter = True
        print (bye_message)

    if yn_enter == False:
        print ("Invalid input.")
        print ("Goodbye :)")
        