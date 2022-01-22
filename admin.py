from registeredcustomer import *
from allcustomer import *

def admin_menu():
    while True:
        try:
            option = int(input("\n*-------------------------\n"
                               "   Welcome to AIRLINE ADMIN SYSTEM MENU  \n"
                               "-------------------------*\n"
                               "1. Add flight schedules \n"
                               "2. Modify flight schedules\n"
                               "3. Display all records\n"
                               "4. Log Out\n"
                               "*-------------------------\n"
                               "Please select one option: "))
            if option == 1:
                add_flight()
            elif option == 2:
                modify_flight_schedules_menu()
            elif option == 3:
                display_records_menu()
            elif option == 4:
                print("Successfully Exit AIRLINE ADMIN SYSTEM")
                exit()
            else:
                print("Please select option 1-4!")
                print("Try again!")
                admin_menu()

            break

        except ValueError:
            print("Not a valid input! please try again!")


def show_airline():  # All airlines schedules
    totalrow = sum(1 for _ in open('Available_Flight_Schedules.txt'))  # To get how many lines in the text file
    # Interface Header
    print("*", "-" * 217, "*")
    print(
        "|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAir Malaysia Group (AMG) All Airlines\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("-" * 221)
    print(
        "|No.|\tFlight Number:\t\t|\tFrom:\t\t\t\t\t\t\t\t|\tTo:\t\t\t\t\t\t\t\t\t\t|\tDepart Date:\t|\tTime:\t|\tReturn Date:\t|\tTime:\t|\tPrice\t|\tFlight Duration (in hours)\t|")
    print("-" * 221)
    # Record
    for row in range(totalrow):
        print("\n", "{:<10}".format(row + 1), end="")  # Row Numbers
        for col in range(1):
            file = open('Available_Flight_Schedules.txt', 'r')
            line = file.readlines()[row]
            data = list(line.replace("\n", "").split(";"))  # To separate data one by one
            print("{:<20}".format(data[0]), end="")
            print("{:<20}".format(data[1]), end="")
            print("({:<11})\t\t".format(data[2]), end="")
            print("{:<20}".format(data[3]), end="")
            print("({:<16})\t\t".format(data[4]), end="")
            print("{:<20}".format(data[5]), end="")
            print("{:<12}".format(data[7]), end="")
            print("{:<20}".format(data[6]), end="")
            print("{:<12}".format(data[8]), end="")
            print("{:<20}".format(data[9]), end="")
            print("{:<20}".format(data[10]), end="")
    print("\n")
    print("*", "-" * 217, "*")
    print("*", "-" * 217, "*")


def add_flight():
    show_airline()
    file = open("Available_Flight_Schedules.txt", "r")
    print("\n" * 3)
    while True:
        try:
            option = int(input('*------------------\n'
                               '1.Add more flight?\n'
                               '2.Back to menu\n'
                               '------------------*\n'
                               'Enter option: '))
            if option == 1:
                break

            elif option == 2:
                admin_menu()

        except ValueError:
            print("Not a valid input! please try again!")

    while True:
        try:
            flight_id = int(input("Flights no: AMG"))
            break
        except ValueError:
            print("Not a valid input! please try again!")
    from_place = choosing_place()
    to_place = choosing_place()
    print(f"Place Chosen From: {from_place}   To: {to_place}")
    full_depart_date, full_return_date = prompt_flight_date_menu2()
    while True:
        try:
            depart_time = input("Depart Time: ")
            break
        except ValueError:
            print("Not a valid input! please try again!")
    while True:
        try:
            return_time = input("Return Time: ")
            break
        except ValueError:
            print("Not a valid input! please try again!")
    while True:
        try:
            price = input("Price: MYR ")
            break
        except ValueError:
            print("Not a valid input! please try again!")
    while True:
        try:
            flight_duration = float(input("Flight Duration: "))
            break
        except ValueError:
            print("Not a valid input! please try again!")

    get_data = ("AMG" + str(flight_id) + ";" + from_place + ";" + to_place + ";" + full_depart_date + ";" + full_return_date
                + ";" + depart_time + ";" + return_time + ";" + "MYR" + price + ";" + str(flight_duration))

    for line in file:
        if get_data in line:
            print("The flight already exists on the database!")
            while True:
                try:
                    option = int(input("*---------------------\n"
                                       "1.Retry\n"
                                       "2.Back\n"
                                       "---------------------*\n"
                                       "Select an option: "))

                    if option == 1:
                        add_flight()
                    elif option == 2:
                        admin_menu()
                    else:
                        print("Input does not exist! Try Again!")

                except ValueError:
                    print("Input does not exist! Try Again!")
    file.close()
    db = open("Available_Flight_Schedules.txt", "a")
    db.write("AMG" + str(flight_id) + ";" + from_place + ";" + to_place + ";" + full_depart_date + ";" +
             full_return_date + ";" + depart_time + ";" + return_time + ";" + "MYR" + price + ";" +
             str(flight_duration) + "\n")
    db.close()
    print("Airline Details")
    print("New Airline is successfully updated into the system.!")
    print("Redirecting back to Menu...")
    while True:
        try:
            option = int(input('*------------------\n'
                               '1.Add more flight?\n'
                               '2.Back to menu\n'
                               '------------------*\n'
                               'Enter option: '))
            if option == 1:
                add_flight()

            elif option == 2:
                admin_menu()

        except ValueError:
            print("Not a valid input! please try again!")


def modify_flight_schedules_menu():
    while True:
        try:
            option = int(input("\n*-------------------------\n"
                               "1. Change flight schedules\n"
                               "2. Cancel flight schedules\n"
                               "3. Back to menu\n"
                               "*-------------------------\n"
                               "Please select one option: "))
            if option == 1:
                change_flight_schedules()
            elif option == 2:
                cancel_flight_schedules()
            elif option == 3:
                print("Backing to ADMIN MENU")
                admin_menu()
            else:
                print("Please Insert 1-3 ONLY!\n")

        except ValueError:
            print("Input does not exist! Try Again!")


def change_flight_schedules():
    show_airline()
    file = open("Available_Flight_Schedules.txt", "r")
    total_line = 0
    data = file.read()
    data_list = data.split("\n")

    for i in data_list:
        if i:
            total_line += 1

    while True:
        try:
            line = int(input("Please select the flight you wish to modify: ")) - 1
            break
        except ValueError:
            print("Not a valid input! please try again!")

    if line >= total_line:
        print("Out of Range")
        print("Try again!")
        change_flight_schedules()

    while True:
        try:
            flight_id = int(input("Flights no: "))
            break
        except ValueError:
            print("Not a valid input! please try again!")
    from_place = choosing_place()
    to_place = choosing_place()
    print(f"Place Chosen From: {from_place}   To: {to_place}")
    full_depart_date, full_return_date = prompt_flight_date_menu2()
    while True:
        try:
            depart_time = input("Depart Time: ")
            break
        except ValueError:
            print("Not a valid input! please try again!")
    while True:
        try:
            return_time = input("Return Time: ")
            break
        except ValueError:
            print("Not a valid input! please try again!")
    while True:
        try:
            price = input("Price: MYR ")
            break
        except ValueError:
            print("Not a valid input! please try again!")
    while True:
        try:
            flight_duration = float(input("Flight Duration: "))
            break
        except ValueError:
            print("Not a valid input! please try again!")
    text = ("AMG" + str(flight_id) + ";" + from_place + ";" + to_place + ";" + full_depart_date + ";" +
            full_return_date + ";" + depart_time + ";" + return_time + ";" + "MYR" + price + ";" +
            str(flight_duration) + "\n")
    replace_line(file, line, text)
    file.close()
    while True:
        try:
            option = int(input('*------------------\n'
                               '1.Modify more flight\n'
                               '2.Back to menu\n'
                               '------------------*\n'
                               'Enter option: '))
            if option == 1:
                modify_flight_schedules_menu()
            elif option == 2:
                admin_menu()
        except ValueError:
            print("Not a valid input! please try again!")


def cancel_flight_schedules():
    show_airline()
    file = open("Available_Flight_Schedules.txt", "r")
    total_line = 0

    while True:
        try:
            line = int(input("Please select the flight you wish to cancel: ")) - 1
            break
        except ValueError:
            print("Not a valid input! please try again!")

    lines = file.readlines()
    data = file.read()
    data_list = data.split("\n")
    file.close()

    for i in data_list:
        if i:
            total_line += 1

    if line <= total_line:
        print("Out of Range")
        print("Try again!")
        cancel_flight_schedules()

    del lines[line]

    new_file = open("Available_Flight_Schedules.txt", "w+")

    for line in lines:
        new_file.write(line)
    new_file.close()
    while True:
        try:
            option = int(input('*------------------\n'
                               '1.Modify more flight\n'
                               '2.Back to menu\n'
                               '------------------*\n'
                               'Enter option: '))
            if option == 1:
                modify_flight_schedules_menu()
            elif option == 2:
                admin_menu()
        except ValueError:
            print("Not a valid input! please try again!")


def display_records_menu():
    while True:
        try:
            option = int(input("\n*-------------------------\n"
                               "1. Flight schedules by flight number\n"
                               "2. Flight booked by customer\n"
                               "3. Summary of Total tickets sold \n"
                               "4. Back to Main Menu\n"
                               "*-------------------------\n"
                               "Please select one option: "))
            if option == 1:
                by_flight_number()
            elif option == 2:
                booked_by_customer()
            elif option == 3:
                summary_total_ticket_sold()
            elif option == 4:
                print("Backing to ADMIN MENU")
                admin_menu()
            else:
                print("Please Insert 1-3 ONLY!\n")

        except ValueError:
            print("Input does not exist! Try Again!")


def by_flight_number():
    file = open("Available_Flight_Schedules.txt", "r")
    total_row = 0
    print()
    print("-" * 220)
    while True:
        try:
            user_prompt_flight_id = int(input("Enter the flight ID you wish to check: AMG"))
            print("-" * 220)
            print()
            break
        except ValueError:
            print("Not a valid input! please try again!")
    final_user_prompt_flight_id = str("AMG" + str(user_prompt_flight_id))
    print("-" * 220)
    print("No.\t Flight ID\t\tFrom\t\t\t\t\t  To\t\t\t\t\t\t\t\t Depart Date & Time\t\t\t\t Return Date & Time\t\t\t\tPrice\t\t   Flight Duration(hrs)")
    print("-" * 220)
    for line in file:
        if final_user_prompt_flight_id in line:
            total_row += 1
            temp = line.replace("\n", "").strip("")
            temp2 = list(temp.split(";"))
            price_convert = int(temp2[9].strip("MYR"))
            print("{:<5}".format(total_row), end="")
            print("{:<15}".format(temp2[0]), end="")
            print(f"{temp2[1]}", end=", ")
            print("{:<15}".format(temp2[2]), end="")
            print(f"{temp2[3]}", end=", ")
            print("{:<20}".format(temp2[4]), end="")
            print(f"{temp2[5]}", end="|")
            print("{:<15}".format(temp2[7]), end="")
            print(f"{temp2[6]}", end="|")
            print("{:<15}".format(temp2[8]), end="")
            print("{:<15}".format("MYR" + str(price_convert)), end="")
            print(temp2[10], end="\n")
    print()
    print("-" * 220)
    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Search More?\n'
                            '2.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                display_records_menu()
            elif opt == 1:
                display_records_menu()
            else:
                print("Please select option 1!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def booked_by_customer():
    file = open("booking_data.txt", "r")
    total_row = 0
    print("-" * 220)
    print("No.\t Username\t\t\t Full Name \t\t\t\t\t\t\tFlight ID\t   From\t\t\t\t\t\t\t\t To\t\t\t\t\t\t  Depart Date&Time\t\t\t\tReturn Date&Time\t\t\tAdult\t  Child\t\tInfant ")
    print("-" * 220)
    for line in file:
        total_row += 1
        temp = line.replace("\n", "").strip("")
        temp2 = list(temp.split(";"))
        print("{:<5}".format(total_row), end="")
        print("{:<20}".format(temp2[0]), end="")
        print("{:<35}".format(temp2[2]), end="")
        print("{:<15}".format(temp2[1]), end="")
        print(f"{temp2[3]}", end=", ")
        print("{:<20}".format(temp2[4]), end="")
        print(f"{temp2[5]}", end=", ")
        print("{:<17}".format(temp2[6]), end="")
        print("{:<30}".format(temp2[7]), end="")
        print("{:<30}".format(temp2[8]), end="")
        print("{:<10}".format(temp2[9]), end="")
        print("{:<10}".format(temp2[10]), end="")
        print((temp2[11]), end="\n")
    print()
    print("-" * 220)
    file.close()

    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                display_records_menu()
            else:
                print("Please select option 1!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def summary_total_ticket_sold():
    file = open("booking_data.txt", "r")
    total_adult_count = 0
    total_child_count = 0
    total_infant_count = 0
    total_total_price_in_ticket = 0
    total_total_seat_class_price = 0
    total_total_add_baggage_price = 0
    total_total_seating_price = 0
    total_total_insurance = 0
    total_income = 0
    total_rewards_points = 0

    for line in file:
        temp = line.replace("\n", "").strip("")
        temp2 = list(temp.split(";"))
        adult_count = int(temp2[9])
        total_adult_count += adult_count
        child_count = int(temp2[10])
        total_child_count += child_count
        infant_count = int(temp2[11])
        total_infant_count += infant_count
        total_price_in_ticket = float(temp2[22])
        total_total_price_in_ticket += total_price_in_ticket
        total_seat_class_price = float(temp2[14])
        total_total_seat_class_price += total_seat_class_price
        total_add_baggage_price = float(temp2[16])
        total_total_add_baggage_price += total_add_baggage_price
        total_seating_price = float(temp2[18])
        total_total_seating_price += total_seating_price
        total_insurance = float(temp2[20])
        total_total_insurance += total_insurance
        total_income = float(
            total_total_price_in_ticket + total_total_seat_class_price + total_total_add_baggage_price + total_total_seating_price + total_total_insurance)
        rewards_points = float(temp2[24])
        total_rewards_points += rewards_points
    print("\n--------------------------------------------------------------------------------------------\n"
          "                                 Summary of Total Ticket Sold\n"
          "--------------------------------------------------------------------------------------------")
    print(f'Total Passengers: \n'
          f'Adult: {total_adult_count}      Child: {total_child_count}      Infant: {total_infant_count}\n'
          '--------------------------------------------------------------------------------------------\n'
          f'The total prices earn in ticket: {total_total_price_in_ticket}\n'
          '--------------------------------------------------------------------------------------------\n'
          f'The total seat class incomes is: MYR {total_total_seat_class_price}\n'
          f'The total add baggage incomes is: MYR {total_total_add_baggage_price}\n'
          f'The total seating incomes is: MYR {total_total_seating_price}\n'
          f'The total insurance incomes is: MYR {total_total_insurance}\n'
          '--------------------------------------------------------------------------------------------\n'
          f'UP-to-date Profit: MYR {total_income}\n'
          f'UP-to-date total rewards point given: {total_rewards_points} Points\n'
          '--------------------------------------------------------------------------------------------')
    print()
    file.close()
    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                display_records_menu()
            else:
                print("Please select option 1!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")
