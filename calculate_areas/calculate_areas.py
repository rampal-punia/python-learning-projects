'''Python Projects: Calculate the areas of polygons.
    => Display user the options for selecting area of required polygon.
    => As per the user selection, ask him the required parameters.
    => Show the area of required polygons.
    => Write separate functions to calculate the area of each polygon.
    => Validate the user input.
'''
import helper
while True:
    print("=======================================================")
    print("Option 1: Calculate the area of Right Angled Triangle.")
    print("Option 2: Calculate the area of Equilateral Triangle.")
    print("Option 3: Calculate the area of Square.")
    print("Option 4: Calculate the area of Rectangle.")
    print("Option 5: Calculate the area of Trapezium.")
    print("Option 6: Calculate the area of Parallelogram.")
    print("Option 7: Calculate the area of Rhombus.")
    print("Option 8: Calculate the area of Circle.")
    print("=======================================================")

    user_option = input("Select option: ")
    if user_option.isdigit() and int(user_option) in range(1, 9):
        if user_option == '1':
            height, base = input("Enter height, base (eg. 5, 7): ").split(', ')
            area = helper.right_triangle_area(height, base)
            print(
                f"The area of triangle with height {height}, and base {base}: {area:.2f}")

        elif user_option == '2':
            side = input("Enter side of equilateral triangle (eg. 5): ")
            area = helper.equilateral_area(side)
            print(
                f"The area of equilateral triangle with side {side}: {area:.2f}")

        elif user_option == '3':
            side = input("Enter side of square (eg. 5): ")
            area = helper.square_area(side)
            print(
                f"The area of square with side {side}: {area:.2f}")

        elif user_option == '4':
            height, width = input(
                "Enter height, width (eg. 5, 7): ").split(', ')
            area = helper.rectangle_area(height, width)
            print(
                f"The area of rectangle with height {height}, width {width}: {area:.2f}")

        elif user_option == '5':
            side1, side2, height = input(
                "Enter side1, side2, height (eg. 5, 7, 9): ").split(', ')
            area = helper.trapezium_area(side1, side2, height)
            print(
                f"The area of trapezium with side1 {side1}, side2 {side2}, height {height}: {area:.2f}")

        elif user_option == '6':
            base, height = input("Enter base, height (eg. 5, 7): ").split(', ')
            area = helper.parallelogram_area(base, height)
            print(
                f"The area of parallelogram with base {base} and height {height}: {area:.2f}")

        elif user_option == '7':
            diagonal1, diagonal2 = input(
                "Enter diagonal1, diagonal2 (eg. 5, 7): ").split(', ')
            area = helper.rhombus_area(diagonal1, diagonal2)
            print(
                f"The area of rhombus with diagonal1 {diagonal1} and diagonal2 {diagonal2}: {area:.2f}")

        elif user_option == '8':
            radius = input("Enter radius(eg. 5): ")
            area = helper.circle_area(radius)
            print(
                f"The area of circle with radius {radius}: {area:.2f}")

        is_continue = input("Do you want to continue?(yes/no): ")

        if is_continue.lower() == "yes":
            continue

        else:
            break

    else:
        print(
            f"**Expected option: 1, 2, 3, 4, 5, 6, but received {user_option}.")
        print("Please enter option again.")
        continue
