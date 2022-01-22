from admin import *


def main_menu():
    while True:
        try:
            option = int(input("\n*------------------------------------------\n"
                               "   AIRLINE RESERVATIONS SYSTEM Main Menu  \n"
                               "------------------------------------------*\n"
                               "1.Show airline schedules\n"
                               "2.Search airline schedules\n"
                               "3.Signup Membership\n"
                               "4.Login\n"
                               "5.Exit program\n"
                               "*------------------------------------------\n"
                               "Please select one option: "))
            if option == 1:
                show_airline()
            elif option == 2:
                search_airline()
            elif option == 3:
                register()
            elif option == 4:
                login_page()
            elif option == 5:
                print("Successfully Exit AIRLINE RESERVATIONS SYSTEM")
                exit()
            else:
                print("Please select option 1-5!")
                print("Try again!")
                main_menu()

            break

        except ValueError:
            print("Not a valid input! please try again!")


def register():
    db = open("checkusername.txt", "r")
    username = input("Username: ")
    pwd = input("Password:")
    pwd2 = input("Confirm Password: ")

    if pwd != pwd2:
        print("Password doesn't match")
        print("Try again!")
        while True:
            try:
                option = int(input("*---------------------\n"
                                   "1.Retry\n"
                                   "2.Back\n"
                                   "---------------------*\n"
                                   "Select an option: "))

                if option == 1:
                    register()
                elif option == 2:
                    main_menu()
                else:
                    print("Input does not exist! Try Again!")

            except ValueError:
                print("Input does not exist! Try Again!")

    else:
        if len(pwd) <= 6:
            print("Password is too short")
            print("try again!")
            while True:
                try:
                    option = int(input("*---------------------\n"
                                       "1.Retry\n"
                                       "2.Back\n"
                                       "---------------------*\n"
                                       "Select an option: "))
                    if option == 1:
                        register()
                    elif option == 2:
                        main_menu()
                    else:
                        print("Input does not exist! Try Again!")

                except ValueError:
                    print("Input does not exist! Try Again!")

        elif "\t" + username + "\n" in db:
            print("Username already exists")
            print("try again!")
            while True:
                try:
                    option = int(input("*---------------------\n"
                                       "1.Retry\n"
                                       "2.Back\n"
                                       "---------------------*\n"
                                       "Select an option: "))
                    if option == 1:
                        register()
                    elif option == 2:
                        main_menu()
                    else:
                        print("Input does not exist! Try Again!")

                except ValueError:
                    print("Input does not exist! Try Again!")

        else:
            db = open("customerdata.txt", "a")
            db.write(username + "\t\t" + pwd + "\n")
            db.close()
            db2 = open("checkusername.txt", "a")
            db2.write(("\t" + username + "\n"))
            db2.close()
            print("Redirecting to update details.....")
            print("Successfully register!")
            email = str(input("Email Address: "))
            name = str(input("Full Name: "))
            mobile_number = str(input("Mobile Number: "))
            dob = str(input("Date of Birth(DD - MM - YYYY): "))
            citizenship = str(input("Citizenship: "))
            print("*" * 40)
            print("Travel Document Details")
            passport_id = str(input("Passport ID: "))
            print("*" * 40)
            print("Emergency Contact")
            mobile_number2 = str(input("Emergency Contact Number: "))
            relationship = str(input("Relationship: "))
            print("*" * 40)
            print("Payment Details")
            card_id = str(input("Credit / Debit Card No: "))
            ex_date = str(input("Expiry Date: "))
            db = open("customerdata2.txt", "a")
            db.write(
                username + ", " + pwd + ", " + email + ", " + name + ", " +
                mobile_number + ", " + dob + ", " + citizenship + ", " +
                passport_id + ", " + mobile_number2 + ", " + relationship + ", " +
                card_id + ", " + ex_date + "\n")
            db.close()
            print("Your Profile is successfully updated into the system.!")
            print("Redirecting back to Menu...")
            main_menu()


def login_page():
    while True:
        try:
            option1 = int(input("\n*-------------------------\n"
                                "       Login Page\n"
                                "-------------------------*\n"
                                "1.Login as customer\n"
                                "2.Login as Administrator\n"
                                "3.Back to Main Menu...\n"
                                "*-------------------------\n"
                                "Please select one option: "))

            if option1 == 1:
                login_customer()
            elif option1 == 2:
                login_admin()
            elif option1 == 3:
                main_menu()
            else:
                print("\nInput does not exist! Again!")
                login_page()
            break

        except ValueError:
            print("Not a valid input! please try again!")


def login_customer():
    permission = True       # Set Boolean variable
    while permission:
        print("\n*---------------"
              "\n Customer Login Page"
              "\n---------------*")
        username = str(input("Username: "))
        pwd = str(input("Password: "))
        print("*---------------")
        with open("customerdata.txt", "r") as customerdb:
            for line in customerdb:
                list = line.split()
                if username == list[0] and pwd == list[1]:
                    permission = False
                    break
            if not permission:
                print("Logged in successful! Hi", username)
                get_username = username
                regis_cus_menu(get_username)
                break
            else:
                while True:
                    try:
                        opt = int(input('\nFailed to log in!\n'
                                        '*------------------\n'
                                        '1.Try again\n'
                                        '2.Back to menu\n'
                                        '------------------*\n'
                                        'Enter option: '))

                        if opt == 1:
                            login_customer()
                        elif opt == 2:
                            login_page()
                        else:
                            print("\nInput does not exist! Again!")

                    except ValueError:
                        print("Input not valid! Try again!")


def login_admin():
    username_admin = "admin"
    password_admin = "admin"
    print("\n*---------------"
          "\n  Admin Login"
          "\n---------------*")
    print("Please refer to README.txt for admin credentials!\nPress ENTER twice if you wish to return!")
    user_name = str(input("Enter admin username: "))
    pass_word = str(input("Enter admin password: "))

    if not user_name == "":
        if not pass_word == "":
            if user_name == username_admin and pass_word == password_admin:
                print(f"\nSuccessfully logged in! Good day {user_name}")
                admin_menu()
            else:
                print("Username or password was incorrect. Try again!")
                login_admin()
        else:
            print("Redirecting to login page...")
            login_page()
    else:
        print("Redirecting to login page...")
        login_page()


def show_airline():     # All airlines schedules
    totalrow = sum(1 for _ in open('Available_Flight_Schedules.txt'))  # To get how many lines in the text file
    # Interface Header
    print("*", "-" * 217, "*")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAir Malaysia Group (AMG) All Airlines\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("-" * 221)
    print("|No.|\tFlight Number:\t\t|\tFrom:\t\t\t\t\t\t\t\t|\tTo:\t\t\t\t\t\t\t\t\t\t|\tDepart Date:\t|\tTime:\t|\tReturn Date:\t|\tTime:\t|\tPrice\t|\tFlight Duration (in hours)\t|")
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
    while True:
        try:
            opt = int(input('*------------------\n'
                            '1.Back to menu\n'
                            '------------------*\n'
                            'Enter option: '))
            if opt == 1:
                main_menu()
            else:
                print("Please select option 1!")
                print("Try again!")

        except ValueError:
            print("Input not valid! Try again!")


def flight_header():    # Used on Search Menu as a header, so it doesn't be too messy on the function.
    print("*", "-" * 213, "*")
    print("|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAir Malaysia Group (AMG)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("-" * 217)
    print("|\tFlight Number:\t\t|\tFrom:\t\t\t\t\t\t\t\t|\tTo:\t\t\t\t\t\t\t\t\t\t|\tDepart Date:\t|\tTime:\t|\tReturn Date:\t|\tTime:\t|\tPrice\t|\tFlight Duration (in hours)\t|")
    print("-" * 217)


def available_destinations():
    print("*", "-" * 130, "*")
    print("| \t\t\t\t\t\t\t\t\t\t Air Malaysia Group (AMG) Available Destinations: \t\t\t\t\t\t\t\t\t\t\t |")
    print("*", "-" * 130, "*"+"\n")
    print("\tKuala Lumpur (Malaysia), \t\tPenang (Malaysia), \t\t\t\t\tJohor Bahru (Malaysia), \t\tDhaka (Bangladesh),\n"
          "\tShanghai (China), \t\t\t\tBali (Indonesia), \t\t\t\t\tVientiane (Laos), \t\t\t\tChoibalsan (Mongolia),\n"
          "\tManila (Philippines), \t\t\tTaipei (Taiwan), \t\t\t\t\tBandar Seri Begawan (Brunei), \tBatumi (Georgia), \n"
          "\tTokyo (Japan), \t\t\t\t\tMandalay (Myanmar), \t\t\t\tSingapore (Singapore), \t\t\tBangkok (Thailand), \n"
          "\tPhnom Penh (Cambodia), \t\t\tChennai (India), \t\t\t\t\tSeoul (South Korea), \t\t\tDharavandhoo (Maldives), \n"
          "\tBhadrapur (Nepal), \t\t\t\tColombo (Sri Lanka), \t\t\t\tHo Chi Minh City (Vietnam), \tMelbourne (Australia), \n"
          "\tWellington (New Zealand), \t\tNew York City (United States), \t\tLondon (United Kingdom)")
    print("\n"+"*", "-" * 130, "*")
    print("*", "-" * 130, "*")
    print("\n")


def search_airline():
    with open("Available_Flight_Schedules.txt", "r") as file:
        line = file.readlines()
    available_destinations()
    flight = []
    for e in line:
        flight.append(e.split(";"))     # Add separator line by line

    while True:
        try:
            search_option = int(input("\n*-------------------------\n"
                                      "       Search by:\n"
                                      "-------------------------*\n"
                                      "1. Flight Number\n"
                                      "2. Departure & Arrival\n"
                                      "3. Date\n"
                                      "4. Back to Main Menu\n"
                                      "*-------------------------\n"
                                      "Please select one option: "))
            print("\n\n")

            if search_option == 1:
                with open("Available_Flight_Schedules.txt", "r") as file:
                    line = file.readlines()

                # Find "input" in text files
                line_temp = line        # To not affecting the lines in file, because i want to capitalize and delete spaces to match user input.
                for i in range(len(line_temp)):
                    line_temp[i] = line_temp[i].upper()
                    line_temp[i] = line_temp[i].replace(" ", "")
                    line_temp[i] = line_temp[i].strip()

                flight_temp = []        # To not affecting the actual "flight" list
                for e in line_temp:
                    flight_temp.append(e.split(";"))        # Add separator

                flag = 0            # Flag acts as a Boolean variable for condition usage.
                index = 0           # Index acts as a position.

                flight_number = input("\n\nSearch by Flight Number to View Flight Details:")
                flight_number = flight_number.upper()
                flight_number = flight_number.replace(" ","")
                flight_number = flight_number.strip()

                for line in flight_temp:
                    if flight_number in line:
                        flag = 1
                        break

                if flag == 0:  # Flag = 0, indicates that it is False.
                    print(f"Sorry, the flight number {flight_number} is unavailable in AMG.")
                else:
                    print(f"{flight_number} is available! \nSchedules are shown below.\n\n")
                    print(f"\n\nFlight Number: {flight_number}\n")
                    flight_header()

                for line in flight_temp:
                    index += 1
                    if flight_number in line:
                        search_flight_details = flight[index - 1]  # To get data, the reason use "flight" is because we do not want the data in capitalized version
                        print("\t", end="\t")
                        print("{:<20}".format(search_flight_details[0]), end="")  # Format is used to align all the data
                        print("{:<20}".format(search_flight_details[1]), end="")
                        print("({:<11})\t\t".format(search_flight_details[2]), end="")
                        print("{:<20}".format(search_flight_details[3]), end="")
                        print("({:<16})\t\t".format(search_flight_details[4]), end="")
                        print("{:<20}".format(search_flight_details[5]), end="")
                        print("{:<12}".format(search_flight_details[7]), end="")
                        print("{:<20}".format(search_flight_details[6]), end="")
                        print("{:<12}".format(search_flight_details[8]), end="")
                        print("{:<20}".format(search_flight_details[9]), end="")
                        print("{:<20}".format(search_flight_details[10]), end="")
                        print("\n" + "*", "-" * 213, "*")

            elif search_option == 2:
                with open("Available_Flight_Schedules.txt", "r") as file:
                    line = file.readlines()

                # Find "input" in text files
                line_temp = line        # To not affecting the lines in file, because i want to capitalize and delete spaces to match user input.
                for i in range(len(line_temp)):
                    line_temp[i] = line_temp[i].upper()
                    line_temp[i] = line_temp[i].replace(" ", "")
                    line_temp[i] = line_temp[i].strip()

                flight_temp = []        # To not affecting the actual "flight" list
                for e in line_temp:
                    flight_temp.append(e.split(";"))        # Add separator

                flag = 0        # Flag acts as a Boolean variable for condition usage.
                index = 0       # Index acts as a position.

                from_place = input("\n\nFrom: ")
                from_place = from_place.upper()
                from_place = from_place.strip()
                from_place = from_place.replace(" ", "")
                to_place = input("To: ")
                to_place = to_place.upper()
                to_place = to_place.strip()
                to_place = to_place.replace(" ","")

                for line in flight_temp:
                    if from_place in line and to_place in line:
                        flag = 1
                        break

                if flag == 0:       # Flag = 0, indicates that it is False.
                    print(f"Sorry, {from_place} to {to_place} is unavailable in AMG.")
                else:
                    print(f"{from_place} to {to_place} is available! \nSchedules are shown below.\n\n")
                    flight_header()

                for line in flight_temp:
                    index += 1
                    if from_place in line and to_place in line:
                        search_flight_details = flight[index-1]     # To get data, the reason use "flight" is because we do not want the data in capitalized version
                        print("\t", end="\t")
                        print("{:<20}".format(search_flight_details[0]), end="")            # Format is used to align all the data
                        print("{:<20}".format(search_flight_details[1]), end="")
                        print("({:<11})\t\t".format(search_flight_details[2]), end="")
                        print("{:<20}".format(search_flight_details[3]), end="")
                        print("({:<16})\t\t".format(search_flight_details[4]), end="")
                        print("{:<20}".format(search_flight_details[5]), end="")
                        print("{:<12}".format(search_flight_details[7]), end="")
                        print("{:<20}".format(search_flight_details[6]), end="")
                        print("{:<12}".format(search_flight_details[8]), end="")
                        print("{:<20}".format(search_flight_details[9]), end="")
                        print("{:<20}".format(search_flight_details[10]), end="")
                        print("\n" + "*", "-" * 213, "*")


            elif search_option == 3:

                with open("Available_Flight_Schedules.txt", "r") as file:
                    line = file.readlines()

                # Find "input" in text files
                line_temp = line  # To not affecting the lines in file, because i want to capitalize and delete spaces to match user input.

                for i in range(len(line_temp)):
                    line_temp[i] = line_temp[i].upper()
                    line_temp[i] = line_temp[i].replace(" ", "")
                    line_temp[i] = line_temp[i].strip()

                flight_temp = []  # To not affecting the actual "flight" list

                for e in line_temp:
                    flight_temp.append(e.split(";"))  # Add separator


                flag = 0        # Flag acts as a Boolean variable for condition usage.
                index = 0       # Index acts as a position.

                departure_date = int(input("Depart Date:"))
                departure_month = input("Depart Month:")
                departure_month = departure_month.upper()
                departure_month = departure_month.strip()
                departure_month = departure_month.replace(" ","")
                departure_year = int(input("Depart Year:"))
                departure_date_search = str(departure_date)+"-"+departure_month+"-"+str(departure_year)
                print("\n")

                return_date = int(input("Return Date:"))
                return_month = input("Return Month:")
                return_month = return_month.upper()
                return_month = return_month.strip()
                return_month = return_month.replace(" ","")
                return_year = int(input("Return Year:"))
                return_date_search = str(return_date)+"-"+return_month+"-"+str(return_year)
                print("\n")

                for line in flight_temp:
                    if departure_date_search in line and return_date_search in line:
                        flag = 1
                        break

                if flag == 0:       # Flag = 0, indicates that it is False.
                    print(f"Sorry, there are no flights on {departure_date_search} to {return_date_search}.")
                else:
                    print(f"Flights on {departure_date_search} to {return_date_search} is available! \nSchedules are shown below.\n\n")
                    flight_header()

                for line in flight_temp:
                    index += 1
                    if departure_date_search in line and return_date_search in line:
                        search_flight_details = flight[index-1]     # To get data, the reason use "flight" is because we do not want the data in capitalized version
                        print("\t", end="\t")
                        print("{:<20}".format(search_flight_details[0]), end="")            # Format is used to align all the data
                        print("{:<20}".format(search_flight_details[1]), end="")
                        print("({:<11})\t\t".format(search_flight_details[2]), end="")
                        print("{:<20}".format(search_flight_details[3]), end="")
                        print("({:<16})\t\t".format(search_flight_details[4]), end="")
                        print("{:<20}".format(search_flight_details[5]), end="")
                        print("{:<12}".format(search_flight_details[7]), end="")
                        print("{:<20}".format(search_flight_details[6]), end="")
                        print("{:<12}".format(search_flight_details[8]), end="")
                        print("{:<20}".format(search_flight_details[9]), end="")
                        print("{:<20}".format(search_flight_details[10]), end="")
                        print("\n" + "*", "-" * 213, "*")

            elif search_option == 4:
                main_menu()

            else:
                print("Please Insert 1-4 ONLY!\n")

        except ValueError:
            print("Input does not exist! Try Again!")