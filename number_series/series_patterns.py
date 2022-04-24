import helper_series

while True:
    print("==============================================")
    print("Select from the series to print.")
    print("Pattern 1. Square numbers.")
    print("Pattern 2. Add square number to the previous number.")
    print("Pattern 3. Add Squares plus one to previous number.")
    print("Pattern 4. Cube numbers.")
    print("Pattern 5. Add Cube plus one to previous number.")
    print("Pattern 6. Add odd numbers to previous number.")
    print("==============================================")

    pattern_option = input("Enter the option number: ")
    if pattern_option.isdigit() and int(pattern_option) in range(1, 7):
        num_element = input("Required elements in the pattern: ")

        if num_element.isdigit():
            num_element = int(num_element)

            if pattern_option == '1':
                pattern_list = helper_series.square_pattern(num_element)
                print(pattern_list)

            elif pattern_option == '2':
                pattern_list = helper_series.add_square_pattern(num_element)
                print(pattern_list)

            elif pattern_option == '3':
                pattern_list = helper_series.square_plus_one_pattern(
                    num_element)
                print(pattern_list)

            elif pattern_option == '4':
                pattern_list = helper_series.cube_pattern(num_element)
                print(pattern_list)

            elif pattern_option == '5':
                pattern_list = helper_series.cube_plus_one_pattern(num_element)
                print(pattern_list)

            elif pattern_option == '6':
                pattern_list = helper_series.add_odd_pattern(num_element)
                print(pattern_list)

            else:
                print(
                    f"Required options are: 1, 2, 3, 4, 5, 6, but received {pattern_option}.")

            is_continue = input("Do you want to continue?(yes/no): ")
            # YES, yES, Yes
            if is_continue.lower() == 'yes':
                continue

            elif is_continue.lower() == 'no':
                break
        else:
            print(
                f"**Expected 'number of element' to be a positive number but received {num_element}.")
            print("Please enter 'Required number of elements' again.")
            continue
    else:
        print(
            f"**Expected option must be positive number(1, 2, 3, 4, 5, 6) but received {pattern_option}.")
        print("Please enter pattern option again.")
        continue
