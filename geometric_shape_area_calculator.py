#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('Welcome to the geometric shape area calculator!')
    # User Options
    Circle = 1
    Rectangle = 2
    Triangle = 3

    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle = 1'+' '+'Rectangle = 2'+' '+'Triangle = 3')
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input("Select a shape by entering 1, 2, or 3")
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(isinstance(choice, int))
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input('What is the radius of the circle?')
        # TODO: Convert 'radius' to float.
        radius = float(radius)
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = circle_pi * radius * radius
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input('What is the length?')
        width = input('What is the width?')
        # TODO: Convert both 'length' and 'width' to float.
        length = float(length)
        width = float(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width
        area = length * width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input('What is the length of the base?')
        height = input('What is the height?')
        # TODO: Convert both 'base' and 'height' to float.
        base = float(base)
        height = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height
        area = 0.5 * base * height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print('Invalid choice .')
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
print('In Canvas navigate to modules and open the Live Classes with the corresponding date.\nTechnical assignments may be in any of the 3 sections of before, during and afterclass.\nClick the link to the assignment. This will open the github classroom page, accept the assignment, wait a moment and refresh the page,\nclick the url link to the assignments repo page.\nclick the carrot on the green code button and copy the url to clipboard. Open VSCode terminal and cd into the directory where\nI keep my JTC assignments enter git clone and paste the url, enter. From VSCode file menu/ open folder/ select assignment folder/ \nwork the assignment until it runs as expected and passes the unit test from the main folder/ git status file names in red/ git add filename.py\n/git status file names in green main branch upto date/ git commit -m"add working assignment _name code"/ git push. return to assignment\nrepo on github to check for the green check indicating the unit test passed.\ncopy url once more and paste it into the assignment page on canvas.')


if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
