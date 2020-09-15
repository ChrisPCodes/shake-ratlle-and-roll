# Shake, Rattle and Roll
''' This program compares the relative strengths of two magnitudes given their magnitudes,
using the moment magnitude scale. In effort to start using more defined functions and main
to drive the program 
'''

# This function gets the magnitude from the user and returns a validated magnitude output
# By looping until the user enter an float greater than or equal to zero
def get_magnitude(number):
    magnitude = float(input(f"Please enter the magnitude for earthquake {number}: "))
    while magnitude < 0 :
        magnitude = float(input(f"Please enter the magnitude for earthquake {number}: "))
    return magnitude

# This function takes two magnitudes from the user and compares them using
# the moment magnitude scale returning the force
def compare_magnitudes(magnitude1, magnitude2):
    # Compares two magnitudes to return value f
    force = 10 ** ((1.5) * (magnitude1 - magnitude2) )
    return force
 
# This function checks whether the user wants to run the program again or quit
# if they type one it will return true in order to run again other wise it will return false and terminate

def get_run_again():
    run = int(input("Try again ? Type 1 for yes or 0 for no: "))
    if run == 1 :
        return True
    return False
        


# The main application
if __name__ == "__main__":
    run = 0 
    while run == 0 :
   # I stored varibles x and why as the user inputs for magnitude 1 and 2, so that I can print and compare them later in the program
        m1 = get_magnitude(1) 
        m2 = get_magnitude(2)

        force = compare_magnitudes(m1,m2)

        if m1 > m2 :
            print ("An earthquake of magnitude {} is {:.1f} times more powerful than an earthquake of magnitude {}.".format(m1, force, m2))
        elif m2 > m1 :
            force = (1/force)
            print("An earthquake of magnitude {} is {:.1f} times more powerful than an earthquake of magnitude {}.".format(m2, force, m1 ))

        if get_run_again() == True :
            run = 0 
        else : 
            run += 1

    print("\nBye!")