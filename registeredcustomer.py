from tools import *
from allcustomer import *

def regis_cus_menu(get_username):
    while True:
        try:
            select = int(input("\n*---------------------------------------\n"
                               "   Welcome to AIRLINE RESERVATIONS SYSTEM \n"
                               "-----------------------------------------*\n"
                               "1.My Account\n"
                               "2.My Booking\n"
                               "3.Add New Flight\n"
                               "4.My Points\n"
                               "5.Log Out\n"
                               "*-----------------------------------------\n"
                               "Please select one option: "))

            if select == 1:
                print_details(get_username)
            elif select == 2:
                print_booking(get_username)
            elif select == 3:
                add_new_flight(get_username)
            elif select == 4:
                print_points(get_username)
            elif select == 5:
                print("Successfully Exit Registered Customer Site")
                exit()
            else:
                print("Please select option 1-5!")
                print("Try again!")

        except ValueError:
            print("Not a valid input! please try again!")


def locate_username(get_username):
    file = open("customerdata2.txt", "r")

    index = 0

    for line in file:
        index += 1
        if get_username in line:
            break

    return index


def print_details(get_username):
    file = open("customerdata2.txt", "r")
    location = locate_username(get_username) - 1
    line = file.readlines()[location]
    print("\n*-------------\n"
          "    My Account\n"
          "---------------*")
    convert = str(line).replace("['", '').replace(r"\n'", '').replace("]", "")
    convert_back = list(convert.split(", "))
    username = convert_back[0]
    print("Username:", username)
    print("Password:", "********")
    email = convert_back[2]
    print("Email Address:", email)
    print("\n*-------------\n"
          "    Profile\n"
          "---------------*")
    name = convert_back[3]
    print("Name:", name)
    mobile_number = convert_back[4]
    print("Mobile Number:", mobile_number)
    dob = convert_back[5]
    print("Date of Birth:", dob)
    citizenship = convert_back[6]
    print("Citizenship:", citizenship)
    print("\n*---------------------------\n"
          "    Travel Document Details\n"
          "-----------------------------*")
    passport_id = convert_back[7]
    print("Passport_ID:", passport_id)
    print("\n*---------------\n"
          "    Emergency Contact\n"
          "------------------*")
    mobile_number2 = convert_back[8]
    print("Emergency Contact Number:", mobile_number2)
    relationship = convert_back[9]
    print("Relationship:", relationship)
    print("\n*-------------------\n"
          "    Payment Details\n"
          "---------------------*")
    card_id = convert_back[10]
    print("Credit / Debit Card ID:", card_id)
    ex_date = convert_back[11]
    print("Expiry Date:", ex_date)
    file.close()

    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Update Profile\n'
                            '2.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                update_profile(get_username)
            elif opt == 2:
                regis_cus_menu(get_username)
            else:
                print("Please select option 1-2!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def update_profile(get_username):
    file_name = "customerdata2.txt"
    line_num = locate_username(get_username) - 1
    file_name2 = "customerdata.txt"
    line_num2 = locate_username(get_username) - 1
    email = str(input("Email Address: "))
    pwd = str(input("Password: "))
    name = str(input("Full Name: "))
    mobile_number = str(input("Mobile Number: "))
    dob = str(input("Date of Birth(XX XX XXXX): "))
    citizenship = str(input("Citizenship: "))
    print("*" * 40)
    print("Travel Document Details")
    passport_id = str(input("Passport ID: "))
    print("*" * 40)
    print("Emergency Contact")
    mobile_number2 = str(input("Emergency Contact Number "))
    relationship = str(input("Relationship: "))
    print("*" * 40)
    print("Payment Details")
    card_id = str(input("Credit / Debit Card No: "))
    ex_date = str(input("Expiry Date: "))
    text = (get_username + ", " + pwd + ", " + email + ", " + name + ", " +
            mobile_number + ", " + dob + ", " + citizenship + ", " +
            passport_id + ", " + mobile_number2 + ", " + relationship + ", " +
            card_id + ", " + ex_date + "\n")
    text2 = (get_username + "\t\t" + pwd + "\n")
    replace_line(file_name, line_num, text)
    replace_line(file_name2, line_num2, text2)
    print("Your Profile is successfully updated into the system.!")
    print("Redirecting back to Menu...")
    regis_cus_menu(get_username)


def print_booking(get_username):
    file = open("booking_data2.txt", "r")
    total_row = 0
    long_line2()
    print(f"Username: {get_username}\t\t\t\t\t\t\t\t\t\t\t\tMy Booking")
    long_line2()
    print("No.\t  Flight ID  \t From\t\t\t\t\t\t  To\t\t\t\t\t\t Depart Date\t\t\t\t   Return Date\t\t\t\t Status")
    long_line2()
    for line in file:
        if get_username in line:
            total_row += 1
            temp = line.replace("\n", "").strip("")
            temp2 = list(temp.split(";"))
            print("\n", "{:<5}".format(total_row), end="")
            print("{:<15}".format(temp2[1]), end="")
            print(f"{temp2[3]}", end=", ")
            print("{:<15}".format(temp2[4]), end="")
            print(f"{temp2[5]}", end=", ")
            print("{:<19}".format(temp2[6]), end="")
            print("{:<30}".format(temp2[7]), end="")
            print("{:<26}".format(temp2[8]), end="")
            print(f"{temp2[9]}", end="\n")
    long_line2()
    file.close()

    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                regis_cus_menu(get_username)
            else:
                print("Please select option 1!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def add_new_flight(get_username):
    long_line()
    print(f"Username: {get_username}                    Add New Flights")
    long_line()
    while True:
        try:
            opt = int(input('*----------------------\n'
                            '1.One Way\n'
                            '2.Two Way\n'
                            '3.Backing to Main Menu\n'
                            '----------------------*\n'
                            'Enter option: '))
            if opt == 1:
                one_way(get_username)
            elif opt == 2:
                two_way(get_username)
            elif opt == 3:
                regis_cus_menu(get_username)
            else:
                print("Please select option 1-3!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def choosing_class():
    while True:
        try:
            opt = int(input('choose class\n'
                            '*------------------------\n'
                            '1.Economy --- MYR 0\n'
                            '2.Business --- MYR 100\n'
                            '3.First Class --- MYR 200\n'
                            '------------------------*\n'
                            'Enter option: '))

            if opt == 1:
                seat_class = "Economy"
                seat_class_price = 0
                return seat_class, seat_class_price
            elif opt == 2:
                seat_class = "Business"
                seat_class_price = 100
                return seat_class, seat_class_price
            elif opt == 3:
                seat_class = "First Class"
                seat_class_price = 200
                return seat_class, seat_class_price
            else:
                print("Please select option 1-3!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def add_more_checked_baggage_size():
    while True:
        try:
            opt = int(input('*------------------------------\n'
                            '1.Add More Checked Baggage Size\n'
                            '2.Continue\n'
                            '-------------------------------*\n'
                            'Enter option: '))

            if opt == 1:
                while True:
                    try:
                        opt2 = int(input('*------------------\n'
                                         '1.5 KG --- MYR 30\n'
                                         '2.10 KG --- MYR 45\n'
                                         '3.15 KG --- MYR 60\n'
                                         '4. Back to Menu\n'
                                         '------------------*\n'
                                         'Enter option: '))

                        if opt2 == 1:
                            more_size = "5 KG"
                            add_baggage_price = 30
                            return more_size, add_baggage_price
                        elif opt2 == 2:
                            more_size = "10 KG"
                            add_baggage_price = 45
                            return more_size, add_baggage_price
                        elif opt2 == 3:
                            more_size = "15 KG"
                            add_baggage_price = 60
                            return more_size, add_baggage_price
                        elif opt2 == 4:
                            break
                        else:
                            print("Please select option 1-4!")
                            print("Try again!")

                    except ValueError:
                        print("Input not valid! Try again!")

            elif opt == 2:
                more_size = 0
                add_baggage_price = 0
                return more_size, add_baggage_price
            else:
                print("Please select option 1-2!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def add_insurance():
    while True:
        try:
            opt = int(input('*------------------------\n'
                            '1.Add travel insurance? MYR 15\n'
                            '2.Continue\n'
                            '------------------------*\n'
                            'Enter option: '))

            if opt == 1:
                insurance = "Included"
                add_insurance_price = 15
                return insurance, add_insurance_price

            elif opt == 2:
                insurance = "No Included"
                add_insurance_price = 0
                return insurance, add_insurance_price
            else:
                print("Please select option 1-2!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def choosing_seat():
    while True:
        try:
            opt = int(input('choose seating\n'
                            '*------------------------\n'
                            '1.Random --- MYR 0\n'
                            '2.Window --- MYR 10\n'
                            '3.Aisle --- MYR 15\n'
                            '4.Extra Legroom --- MYR 20\n'
                            '------------------------*\n'
                            'Enter option: '))

            if opt == 1:
                seating = "Random"
                add_seating_price = 0
                return seating, add_seating_price
            elif opt == 2:
                seating = "Window"
                add_seating_price = 10
                return seating, add_seating_price
            elif opt == 3:
                seating = "Aisle"
                add_seating_price = 15
                return seating, add_seating_price
            elif opt == 4:
                seating = "Extra Legroom"
                add_seating_price = 20
                return seating, add_seating_price
            else:
                print("Please select option 1-4!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def choosing_place():
    file = open("Available_Destinations.txt", "r")
    print("Air Malaysia Group (AMG) Available Destinations:")
    num = 1
    list_country = []
    for line in file:
        line2 = line.replace("\n", "").replace(";", "")
        print(f"{num}. {line2}")
        list_country.append(line2.replace(" (", "; ").replace(")", ""))
        num += 1
    while True:
        try:
            option = int(input("Choose the place: "))
            break
        except ValueError:
            print("Not a valid input! please try again!")
    place = list_country[option - 1]
    print(place)
    return place


def payment_details():
    while True:
        try:
            full_name = str(input("Full Name: "))

            while True:
                try:
                    card_number = str(input("Card Number (Only 16 digits): "))
                    if len(card_number) == 16 and card_number.isdigit():
                        while True:
                            try:
                                cvv = str(input("CVV (Only 3 digits): "))
                                if len(cvv) == 3 and cvv.isdigit():
                                    while True:
                                        try:
                                            exp_month = str(input("Expiry Month (Only 2 digits Example: 01 - 12): "))
                                            if len(exp_month) == 2 and exp_month.isdigit():
                                                while True:
                                                    try:
                                                        exp_year = str(
                                                            input("Expiry Year (Only 2 digits Example: "
                                                                  "21,22,23,24,25): "))
                                                        if len(exp_year) == 2 and exp_year.isdigit():
                                                            return full_name, card_number, cvv, exp_month, exp_year
                                                        else:
                                                            print("Please Follow the Format!")
                                                            print("Try again!")
                                                    except ValueError:
                                                        print("Not a valid input! please try again!")
                                            else:
                                                print("Please Follow the Format!")
                                                print("Try again!")
                                        except ValueError:
                                            print("Not a valid input! please try again!")
                                else:
                                    print("Please Follow the Format!")
                                    print("Try again!")
                            except ValueError:
                                print("Not a valid input! please try again!")
                    else:
                        print("Please Follow the Format!")
                        print("Try again!")
                except ValueError:
                    print("Not a valid input! please try again!")
        except ValueError:
            print("Not a valid input! please try again!")


def one_way(get_username):
    file = open("Available_Flight_Schedules.txt", "r")
    from_place = choosing_place()
    to_place = choosing_place()
    print(f"Place Chosen From: {from_place}   To: {to_place}")
    full_depart_date = prompt_flight_date_menu1()
    get_data = (from_place + ";" + to_place + ";" + full_depart_date)
    total_row = 0
    total_list = []
    results = []
    long_line()
    print("Search Results")
    long_line()
    print("No.\t  Flight ID  \t From\t\t\t\t\t\t  To\t\t\t\t\t\t\t\tDepart Date & Time\t\t\t\t\t Price\n")
    long_line()
    for line in file:
        if get_data in line:
            total_row += 1
            temp = line.replace("\n", "").strip("")
            temp2 = list(temp.split(";"))
            print("\n", "{:<5}".format(total_row), end="")
            print("{:<15}".format(temp2[0]), end="")
            print(f"{temp2[1]}", end=", ")
            print("{:<15}".format(temp2[2]), end="")
            print(f"{temp2[3]}", end=", ")
            print("{:<26}".format(temp2[4]), end="")
            print(f"{temp2[5]}", end="|")
            print("{:<20}".format(temp2[7]), end="")
            print(temp2[9], end="\n")
            results.append(temp2)
            total_list.append(total_row)

    total_list_convert = str(total_list)

    long_line()
    print("Press ENTER if you wish to return!")
    option = str(input("Select an option: "))

    if option in total_list_convert:
        if option == "":
            add_new_flight(get_username)
        else:
            while True:
                try:
                    option_convert = int(option)
                    break
                except ValueError:
                    print("Not a valid input! please try again!")
            get_results = results[option_convert - 1]
            from_place2 = get_results[1] + ";" + get_results[2]
            to_place2 = get_results[3] + ";" + get_results[4]
            full_depart_date2 = get_results[5] + "|" + get_results[7]
            price2 = get_results[9].replace("MYR", "")
            convert_price2 = int(price2)
            print("\n*---------------------\n"
                  "     How Many Passenger\n"
                  "-----------------------*")
            while True:
                try:
                    adult_count = int(input("Adult (12 years and above): "))
                    break
                except ValueError:
                    print("Not a valid input! please try again!")

            while True:
                try:
                    child_count = int(input("Child (2 to 11 years): "))
                    break
                except ValueError:
                    print("Not a valid input! please try again!")

            while True:
                try:
                    infant_count = int(input("Infant (below 2 years): "))
                    break
                except ValueError:
                    print("Not a valid input! please try again!")

            total_passenger_count = adult_count + child_count
            adult_price = float(adult_count * convert_price2)
            child_price = float((convert_price2 / 2) * child_count)
            infant_price = 0
            total_price_in_ticket = adult_price + child_price + infant_price
            long_line()
            print("\n*-----------------------------\n"
                  "     Summary of Flight Booking:\n"
                  "-------------------------------*")
            print(f'Adult: {adult_count}      Child: {child_count}      Infant: {infant_count}\n'
                  f'From: {from_place2}              To: {to_place2}\n'
                  f'Depart Date: {full_depart_date2}\n'
                  f'Price per ticket: MYR {price2}\n'
                  f'Price in adult: MYR {price2} * {adult_count} = MYR {adult_price}\n'
                  f'Price in child (50% off): (MYR {price2} * {child_count}) / 2 = MYR {child_price}\n'
                  f'Price in infant (FREE): MYR {infant_price}.0\n'
                  f'Total price in ticket: MYR {total_price_in_ticket}\n'
                  f'Cabin Baggage Size (per passenger): 7 KG\n'
                  f'Checked Baggage Size (per passenger): 15 KG\n')
            long_line()
            seat_class_list = []
            total_seat_class_price = 0
            add_baggage_list = []
            total_add_baggage_price = 0
            seating_list = []
            total_seating_price = 0
            total_insurance = 0
            total_add_insurance = 0
            for i in range(total_passenger_count):
                print("\n*----------------\n"
                      f"Passenger {i + 1}\n"
                      "------------------*")
                seat_class, seat_class_price = choosing_class()
                more_size, add_baggage_price = add_more_checked_baggage_size()
                seating, add_seating_price = choosing_seat()
                insurance, add_insurance_price = add_insurance()
                long_line()
                print(f'Class: {seat_class}  Price: MYR {seat_class_price}')
                print(f'Seat: {seating}  Price: MYR {add_seating_price}')
                print(f'Add More Checked Baggage Size: {more_size}  Price: MYR {add_baggage_price}')
                print(f'Insurance: {insurance}  Price: MYR {add_insurance_price}')
                long_line()
                if insurance == "Included":
                    total_insurance += 1
                seat_class_list.append(seat_class)
                total_seat_class_price += seat_class_price
                add_baggage_list.append(more_size)
                total_add_baggage_price += add_baggage_price
                seating_list.append(seating)
                total_seating_price += add_seating_price
                total_add_insurance += add_insurance_price
            total_add_ons = float(total_seat_class_price + total_add_insurance + total_add_baggage_price + total_seating_price)
            final_price = float(total_price_in_ticket + total_add_ons)
            rewards_points = final_price * 10
            flight_id = get_results[0]
            print("\n" * 3)
            long_line()
            print("*----------------------------------\n"
                  "     Summary of Flight Booking:\n"
                  "----------------------------------*")
            print(f'Adult: {adult_count}      Child: {child_count}      Infant: {infant_count}\n'
                  f'From: {from_place}              To: {to_place}\n'
                  f'Depart Date: {full_depart_date2}\n'
                  f'Price per ticket: MYR {price2}\n'
                  f'Price in adult: MYR {price2} * {adult_count} = MYR {adult_price}\n'
                  f'Price in child (50% off): (MYR {price2} * {child_count}) / 2 = MYR {child_price}\n'
                  f'Price in infant (FREE): MYR {infant_price}.0\n'
                  f'Total price in ticket: MYR {total_price_in_ticket}\n'
                  f'Cabin Baggage Size: 7 KG\n'
                  f'Checked Baggage Size: 15 KG\n'
                  f'---------------------------------------------------------------------------------------------------'
                  f'----------------------------------\n'
                  f'Choosing Class List: {seat_class_list}\n'
                  f'Price: {total_seat_class_price}\n'
                  f'Add More Checked Baggage Size: {add_baggage_list}\n'
                  f'Price: MYR {total_add_baggage_price}\n'
                  f'Seat: {seating_list}\n'
                  f'Price: MYR {total_seating_price}\n'
                  f'Insurance: {total_insurance} Passenger included Travel Insurance\n'
                  f'Price: MYR {total_add_insurance}\n'
                  f'---------------------------------------------------------------------------------------------------'
                  f'----------------------------------\n'
                  f'Total Price in Ticket: MYR {total_price_in_ticket}\n'
                  f'Total Price in add_ons: MYR {total_add_ons}\n\n'
                  f'Final Price: MYR {final_price}\n'
                  f'Rewards Points: {rewards_points} Points\n\n'
                  f'---------------------------------------------------------------------------------------------------'
                  f'----------------------------------\n')
            while True:
                try:
                    option = int(input("*--------------------------------------\n"
                                       "            Payment Page\n"
                                       "---------------------------------------*\n"
                                       f"Total To Be Paid: MYR {final_price}\n"
                                       "Payment method will be online payment!\n"
                                       "*--------------------------------------\n"
                                       "1.Proceed\n"
                                       "2.Cancel Booking and back to main menu\n"
                                       "---------------------------------------*\n"
                                       "Select an option: "))
                    if option == 1:
                        full_name, card_number, cvv, exp_month, exp_year = payment_details()
                        print(f"Username: {get_username}\n\n"
                              f"Full Name: {full_name}\n"
                              f"Card Number: {card_number} CVV: {cvv}  Expiry Date: {exp_month}/ {exp_year}\n"
                              f"Total To Be Paid: RM{final_price}")
                        db = open("booking_data.txt", "a")
                        db.write(
                            get_username + ";" + flight_id + ";" + full_name + ";" + from_place2 + ";" +
                            to_place2 + ";" + full_depart_date2 + ";" + "     -     " + ";" + str(adult_count) + ";" +
                            str(child_count) + ";" + str(infant_count) + ";" + str(total_passenger_count) + ";" +
                            str(seat_class_list) + ";" + str(total_seat_class_price) + ";" + str(add_baggage_list) + ";" +
                            str(total_add_baggage_price) + ";" + str(seating_list) + ";" + str(total_seating_price) + ";" +
                            str(total_insurance) + ";" + str(total_add_insurance) + ";" + str(total_price_in_ticket) + ";" +
                            str(total_add_ons) + ";" + str(final_price) + ";" + str(rewards_points) + ";" + str(card_number) + ";" +
                            str(cvv) + ";" + str(exp_month) + ";" + str(exp_year) + "\n")
                        db.close()
                        db2 = open("booking_data2.txt", "a")
                        db2.write(
                            get_username + ";" + flight_id + ";" + full_name + ";" + from_place2 + ";" +
                            to_place2 + ";" + full_depart_date2 + ";" + "     -     " + ";" + "Check-IN OPEN" + "\n")
                        db2.close()
                        print("The booking has been received! Thank you for your purchase!")
                        print("Redirecting to Main menu!")
                        regis_cus_menu(get_username)
                    elif option == 2:
                        regis_cus_menu(get_username)
                    else:
                        print("Please select option 1-2!")
                        print("Try again!")

                except ValueError:
                    print("Not a valid input! please try again!")
        file.close()
    else:
        print("Invalid option!")
        input("Press enter to retry!")
        add_new_flight(get_username)


def two_way(get_username):
    file = open("Available_Flight_Schedules.txt", "r")
    from_place = choosing_place()
    to_place = choosing_place()
    print(f"Place Chosen From: {from_place}   To: {to_place}")
    full_depart_date, full_return_date = prompt_flight_date_menu2()
    get_data = (from_place + ";" + to_place + ";" + full_depart_date + ";" + full_return_date)
    total_row = 0
    total_list = []
    results = []
    long_line2()
    print("Search Results")
    long_line2()
    print("No.\t  Flight ID  \t From\t\t\t\t\t\t  To\t\t\t\t\t\t  Depart Date & Time\t\t\t  Return Date & Time\t\t     "
          " Price\n")
    long_line2()
    for line in file:
        if get_data in line:
            total_row += 1
            temp = line.replace("\n", "").strip("")
            temp2 = list(temp.split(";"))
            price_convert = int(temp2[9].strip("MYR"))
            print("\n", "{:<5}".format(total_row), end="")
            print("{:<15}".format(temp2[0]), end="")
            print(f"{temp2[1]}", end=", ")
            print("{:<15}".format(temp2[2]), end="")
            print(f"{temp2[3]}", end=", ")
            print("{:<20}".format(temp2[4]), end="")
            print(f"{temp2[5]}", end="|")
            print("{:<15}".format(temp2[7]), end="")
            print(f"{temp2[6]}", end="|")
            print("{:<15}".format(temp2[8]), end="")
            print("MYR" + str(price_convert * 2), end="\n")
            results.append(temp2)
            total_list.append(total_row)

    total_list_convert = str(total_list)

    long_line2()
    print("Press ENTER if you wish to return!")
    option = str(input("Select an option: "))

    if option in total_list_convert:
        if option == "":
            add_new_flight(get_username)
        else:
            while True:
                try:
                    option_convert = int(option)
                    break
                except ValueError:
                    print("Not a valid input! please try again!")
            get_results = results[option_convert - 1]
            from_place2 = get_results[1] + ";" + get_results[2]
            to_place2 = get_results[3] + ";" + get_results[4]
            full_depart_date2 = get_results[5] + "|" + get_results[7]
            full_return_date2 = get_results[6] + "|" + get_results[8]
            price2 = get_results[9].replace("MYR", "")
            convert_price2 = int(price2) * 2
            print("\n*---------------------\n"
                  "     How Many Passenger\n"
                  "-----------------------*")
            while True:
                try:
                    adult_count = int(input("Adult (12 years and above): "))
                    break
                except ValueError:
                    print("Not a valid input! please try again!")

            while True:
                try:
                    child_count = int(input("Child (2 to 11 years): "))
                    break
                except ValueError:
                    print("Not a valid input! please try again!")

            while True:
                try:
                    infant_count = int(input("Infant (below 2 years): "))
                    break
                except ValueError:
                    print("Not a valid input! please try again!")

            total_passenger_count = adult_count + child_count
            adult_price = float(adult_count * convert_price2)
            child_price = float((convert_price2 / 2) * child_count)
            infant_price = 0
            total_price_in_ticket = adult_price + child_price + infant_price
            long_line()
            print("\n*----------------------------\n"
                  "     Summary of Flight Booking:\n"
                  "------------------------------*")
            print(f'Adult: {adult_count}      Child: {child_count}      Infant: {infant_count}\n'
                  f'From: {from_place}              To: {to_place}\n'
                  f'Depart Date: {full_depart_date2}        Return Date: {full_return_date2}\n'
                  f'Price per ticket: MYR {convert_price2}\n'
                  f'Price in adult: MYR {convert_price2 } * {adult_count} = MYR {adult_price}\n'
                  f'Price in child (50% off): (MYR {convert_price2} * {child_count}) / 2) = MYR {child_price}\n'   
                  f'Price in infant (FREE): MYR {infant_price}.0\n'
                  f'Total price in ticket: MYR {total_price_in_ticket}\n'
                  f'Cabin Baggage Size: 7 KG\n'
                  f'Checked Baggage Size: 15 KG\n')
            long_line()
            seat_class_list = []
            total_seat_class_price = 0
            add_baggage_list = []
            total_add_baggage_price = 0
            seating_list = []
            total_seating_price = 0
            total_insurance = 0
            total_add_insurance = 0
            for i in range(total_passenger_count):
                print("\n*----------------\n"
                      f"Passenger {i + 1}\n"
                      "------------------*")
                seat_class, seat_class_price = choosing_class()
                more_size, add_baggage_price = add_more_checked_baggage_size()
                seating, add_seating_price = choosing_seat()
                insurance, add_insurance_price = add_insurance()
                long_line()
                print(f'Class: {seat_class}  Price: MYR {seat_class_price * 2}')
                print(f'Seat: {seating}  Price: MYR {add_seating_price * 2}')
                print(f'Add More Checked Baggage Size: {more_size}  Price: MYR {add_baggage_price * 2}')
                print(f'Insurance: {insurance}  Price: MYR {add_insurance_price * 2}')
                long_line()
                if insurance == "Included":
                    total_insurance += 1
                seat_class_list.append(seat_class)
                total_seat_class_price += seat_class_price * 2
                add_baggage_list.append(more_size)
                total_add_baggage_price += add_baggage_price * 2
                seating_list.append(seating)
                total_seating_price += add_seating_price * 2
                total_add_insurance += add_insurance_price * 2
            total_add_ons = float(total_seat_class_price + total_add_insurance + total_add_baggage_price + total_seating_price)
            final_price = float(total_price_in_ticket + total_add_ons)
            rewards_points = final_price * 10
            flight_id = get_results[0]
            print("\n" * 3)
            long_line()
            print("*----------------------------------\n"
                  "     Summary of Flight Booking:\n"
                  "----------------------------------*")
            print(f'Adult: {adult_count}      Child: {child_count}      Infant: {infant_count}\n'
                  f'From: {from_place}              To: {to_place}\n'
                  f'Depart Date: {full_depart_date2}        Return Date: {full_return_date2}\n'
                  f'Price per ticket: MYR {convert_price2}\n'
                  f'Price in adult: MYR {convert_price2} * {adult_count} = MYR {adult_price}\n'
                  f'Price in child (50% off): (MYR {convert_price2} * {child_count}) / 2) = MYR {child_price}\n'   
                  f'Price in infant (FREE): MYR {infant_price}.0\n'
                  f'Total price in ticket: MYR {total_price_in_ticket}\n'
                  f'Cabin Baggage Size: 7 KG\n'
                  f'Checked Baggage Size: 15 KG\n'
                  f'---------------------------------------------------------------------------------------------------'
                  f'----------------------------------\n'
                  f'Choosing Class List: {seat_class_list}\n'
                  f'Price: {total_seat_class_price}\n'
                  f'Add More Checked Baggage Size: {add_baggage_list}\n'
                  f'Price: MYR {total_add_baggage_price}\n'
                  f'Seat: {seating_list}\n'
                  f'Price: MYR {total_seating_price}\n'
                  f'Insurance: {total_insurance} Passenger included Travel Insurance\n'
                  f'Price: MYR {total_add_insurance}\n'
                  f'---------------------------------------------------------------------------------------------------'
                  f'----------------------------------\n'
                  f'Total Price in Ticket: MYR {total_price_in_ticket}\n'
                  f'Total Price in add_ons: MYR {total_add_ons}\n\n'
                  f'Final Price: MYR {final_price}\n'
                  f'Rewards Points: {rewards_points} Points\n\n'
                  f'---------------------------------------------------------------------------------------------------'
                  f'----------------------------------\n')
            while True:
                try:
                    option = int(input("*--------------------------------------\n"
                                       "            Payment Page\n"
                                       "---------------------------------------*\n"
                                       f"Total To Be Paid: MYR {final_price}\n"
                                       "Payment method will be online payment!\n"
                                       "*--------------------------------------\n"
                                       "1.Proceed\n"
                                       "2.Cancel Booking and back to main menu\n"
                                       "---------------------------------------*\n"
                                       "Select an option: "))
                    if option == 1:
                        full_name, card_number, cvv, exp_month, exp_year = payment_details()
                        print(f"Username: {get_username}\n\n"
                              f"Full Name: {full_name}\n"
                              f"Card Number: {card_number} CVV: {cvv}  Expiry Date: {exp_month}/ {exp_year}\n"
                              f"Total To Be Paid: RM{final_price}")
                        db = open("booking_data.txt", "a")
                        db.write(
                            get_username + ";" + flight_id + ";" + full_name + ";" + from_place2 + ";" +
                            to_place2 + ";" + full_depart_date2 + ";" + full_return_date2 + ";" + str(adult_count) + ";" +
                            str(child_count) + ";" + str(infant_count) + ";" + str(total_passenger_count) + ";" +
                            str(seat_class_list) + ";" + str(total_seat_class_price) + ";" + str(add_baggage_list) + ";" +
                            str(total_add_baggage_price) + ";" + str(seating_list) + ";" + str(total_seating_price) + ";" +
                            str(total_insurance) + ";" + str(total_add_insurance) + ";" + str(total_price_in_ticket) + ";" +
                            str(total_add_ons) + ";" + str(final_price) + ";" + str(rewards_points) + ";" + str(card_number) + ";" +
                            str(cvv) + ";" + str(exp_month) + ";" + str(exp_year) + "\n")
                        db.close()
                        db2 = open("booking_data2.txt", "a")
                        db2.write(
                            get_username + ";" + flight_id + ";" + full_name + ";" + from_place2 + ";" +
                            to_place2 + ";" + full_depart_date2 + ";" + full_return_date2 + ";" +
                            "Check-IN OPEN" + "\n")
                        db2.close()
                        print("The booking has been received! Thank you for your purchase!")
                        print("Redirecting to Main menu!")
                        regis_cus_menu(get_username)
                    elif option == 2:
                        regis_cus_menu(get_username)
                    else:
                        print("Please select option 1-2!")
                        print("Try again!")
                except ValueError:
                    print("Not a valid input! please try again!")
        file.close()

    else:
        print("Invalid option!")
        input("Press enter to retry!")
        add_new_flight(get_username)


def print_points(get_username):
    file = open("booking_data.txt", "r")
    total_row = 0
    long_line2()
    print(f"Username: {get_username}\t\t\t\t\t\t\t\t\t\t\t\t\tMy Points")
    long_line2()
    print("No.\t  Flight ID  \t From\t\t\t\t\t\t  To\t\t\t\t\t   Depart Date&Time\t\t\t\t "
          "Return Date&Time\t      Rewards Points")
    long_line2()
    for line in file:
        if get_username in line:
            total_row += 1
            temp = line.replace("\n", "").strip("")
            temp2 = list(temp.split(";"))
            print("\n", "{:<5}".format(total_row), end="")
            print("{:<15}".format(temp2[1]), end="")
            print(f"{temp2[3]}", end=", ")
            print("{:<15}".format(temp2[4]), end="")
            print(f"{temp2[5]}", end=", ")
            print("{:<17}".format(temp2[6]), end="")
            print("{:<30}".format(temp2[7]), end="")
            print("{:<25}".format(temp2[8]), end="")
            print((temp2[24]), end="\n")
    long_line2()
    file.close()

    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                regis_cus_menu(get_username)
            else:
                print("Please select option 1!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")
