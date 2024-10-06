# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
from InputFunction import get_triangle_sides
from  HypFinder import hyp
from Triangles import triangle_generator


# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

def weird_calculation():
    # get the length and width of the first triangle from the user
    get_triangle_sides()

    # work out the hyp
    
    hyp()

    # get the length and width of the second triangle from the user
    get_triangle_sides()

    # work out the hyp
    hyp()

    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    triangle_generator()
    
    
    hyp()

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
"""The input entered must be a number whether that's an integer or a float. A string 
or any other datatype will cause the program to crash. """
# 2. Validate the user's input based on your preconditions.
""" We could use .isdigit() to see if the input entered is an actual number. Using Boolean, a while loop
 and an if statement, we could make it so that if .isdigit() is proven false, the user has to 
 re-enter the values."""
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
"""It saves us having to write up the same exact piece of code with just different variable names. 
Thus, it makes the code appear a lot cleaner and saves us time codinf it up as well. We didn't have
to repeatedly code to ask for user inputs or calculate the hypotenuse instead, we simply summoned in
the same function repeatedly."""

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in. (DONE)
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
