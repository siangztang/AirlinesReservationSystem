def long_line():
    print("-------------------------------------------------------------------------------------------------------"
          "------------------------------")


def long_line2():
    print("-------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")


def years():
    print("1. 2021")
    print("2. 2022")
    print("3. 2023")
    print("*********************************************")
    print("*********************************************")
    print("*********************************************")


def months():
    print("1. January")
    print("2. February")
    print("3. March")
    print("4. April")
    print("5. May")
    print("6. June")
    print("7. July")
    print("8. August")
    print("9. September")
    print("10. October")
    print("11. November")
    print("12. December")
    print("*********************************************")
    print("*********************************************")
    print("*********************************************")


def dates():
    print("1. 1")
    print("2. 2")
    print("3. 3")
    print("4. 4")
    print("5. 5")
    print("6. 6")
    print("7. 7")
    print("8. 8")
    print("9. 9")
    print("10. 10")
    print("11. 11")
    print("12. 12")
    print("13. 13")
    print("14. 14")
    print("15. 15")
    print("16. 16")
    print("17. 17")
    print("18. 18")
    print("19. 19")
    print("20. 20")
    print("21. 21")
    print("22. 22")
    print("23. 23")
    print("24. 24")
    print("25. 25")
    print("26. 26")
    print("27. 27")
    print("28. 28")
    print("29. 29")
    print("30. 30")
    print("31. 31")
    print("*********************************************")
    print("*********************************************")
    print("*********************************************")


def prompt_flight_date_menu1():
    while True:
        try:
            year = [2021, 2022, 2023]
            print("*********************************************")
            print("               Departure Year                ")
            print("*********************************************")
            print("*********************************************")
            years()
            print("\n")
            year_input = int(input("Enter Your Departure Year:"))

            if 1 <= year_input <= 3:
                departure_year = year[year_input - 1]
                while True:
                    try:
                        month = ["January", "February", "March", "April", "May", "June",
                                 "July", "August", "September", "October", "November", "December"]
                        print("*********************************************")
                        print("               Departure Month               ")
                        print("*********************************************")
                        print("*********************************************")
                        months()
                        print("\n")
                        month_input = int(input("Enter Your Departure Month:"))

                        if 1 <= month_input <= 12:
                            departure_month = month[month_input - 1]
                            while True:
                                try:
                                    date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                            13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                            23, 24, 25, 26, 27, 28, 29, 30, 31]
                                    print("*********************************************")
                                    print("               Departure Date                ")
                                    print("*********************************************")
                                    print("*********************************************")
                                    dates()
                                    print("\n")
                                    date_input = int(input("Enter Your Departure Date:"))

                                    if 1 <= date_input <= 31:
                                        departure_date = date[date_input - 1]
                                        full_depart_date = str(departure_date) + "-" + str(departure_month) + "-" + str(
                                            departure_year)
                                        print(
                                            f"The Date You Wish to Depart: {str(departure_date)} {departure_month} {str(departure_year)}")
                                        return full_depart_date
                                    else:
                                        print("Please select option 1-31!")
                                        print("Try again!")

                                except ValueError:
                                    print("Not a valid input! please try again!")
                                print("\n")
                        else:
                            print("Please select option 1-12!")
                            print("Try again!")

                    except ValueError:
                        print("Not a valid input! please try again!")
                    print("\n")
            else:
                print("Please select option 1-3!")
                print("Try again!")

        except ValueError:
            print("Not a valid input! please try again!")
        print("\n")


def prompt_flight_date_menu2():
    full_depart_date = prompt_flight_date_menu1()

    while True:
        try:
            year = [2021, 2022, 2023]
            print("*********************************************")
            print("               Return Year                   ")
            print("*********************************************")
            print("*********************************************")
            years()
            print("\n")
            year_input = int(input("Enter Your Return Year:"))

            if 1 <= year_input <= 3:
                return_year = year[year_input - 1]
                while True:
                    try:
                        month = ["January", "February", "March", "April", "May", "June",
                                 "July", "August", "September", "October", "November", "December"]
                        print("*********************************************")
                        print("                 Return Month                ")
                        print("*********************************************")
                        print("*********************************************")
                        months()
                        print("\n")
                        month_input = int(input("Enter Your Return Month:"))

                        if 1 <= month_input <= 12:
                            return_month = month[month_input - 1]
                            while True:
                                try:
                                    date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                            13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                            23, 24, 25, 26, 27, 28, 29, 30, 31]
                                    print("*********************************************")
                                    print("                 Return Date                 ")
                                    print("*********************************************")
                                    print("*********************************************")
                                    dates()
                                    print("\n")
                                    date_input = int(input("Enter Your Return Date:"))

                                    if 1 <= date_input <= 31:
                                        return_date = date[date_input - 1]
                                        full_return_date = str(return_date) + "-" + str(return_month) + "-" + str(
                                            return_year)
                                        print(
                                            f"The Date You Wish to Return: {str(return_date)} {return_month} {str(return_year)}")
                                        return full_depart_date, full_return_date
                                    else:
                                        print("Please select option 1-31!")
                                        print("Try again!")

                                except ValueError:
                                    print("Not a valid input! please try again!")
                                print("\n")
                        else:
                            print("Please select option 1-12!")
                            print("Try again!")

                    except ValueError:
                        print("Not a valid input! please try again!")
                    print("\n")
            else:
                print("Please select option 1-3!")
                print("Try again!")

        except ValueError:
            print("Not a valid input! please try again!")
        print("\n")
