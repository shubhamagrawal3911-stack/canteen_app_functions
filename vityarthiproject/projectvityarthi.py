    choice_text = input("Enter the number of the dish you tried: ").strip()
    if not choice_text.isdigit():
        print("Please enter a menu number.")
        return

    choice = int(choice_text)
    if choice < 1 or choice > len(menu):
        print("That dish number is not on the menu.")
        return

    rating_text = input("Give it a rating from 1 to 5: ").strip()
    if not rating_text.isdigit():
        print("Please enter a number from 1 to 5.")
        return

    rating = int(rating_text)
    if rating < 1 or rating > 5:
        print("The rating must be from 1 to 5.")
        return

    comment = input("Add a short comment (or press Enter to skip): ").strip()
    entry = {"dish": menu[choice - 1]["name"], "rating": rating, "comment": comment}
    feedback_list.append(entry)
    print("Thanks! Your feedback has been recorded.")


def show_feedback(feedback_list):
    print("\n--- FEEDBACK SUMMARY ---")
    if len(feedback_list) == 0:
        print("No feedback has been submitted yet.")
        return

    dish_names = []
    for entry in feedback_list:
        if entry["dish"] not in dish_names:
            dish_names.append(entry["dish"])

    for dish_name in dish_names:
        total_rating = 0
        count = 0
        for entry in feedback_list:
            if entry["dish"] == dish_name:
                total_rating = total_rating + entry["rating"]
                count = count + 1
        average = total_rating / count
        print(dish_name + ": " + str(round(average, 1)) + "/5 from " + str(count) + " rating(s)")

    print("\nComments:")
    found_comment = False
    for entry in feedback_list:
        if entry["comment"] != "":
            print("- " + entry["dish"] + ": " + entry["comment"])
            found_comment = True
    if not found_comment:
        print("No written comments yet.")


def show_options():
    print("\nWhat would you like to do?")
    print("1. View the menu")
    print("2. Add a dish (canteen staff)")
    print("3. Give feedback")
    print("4. View feedback summary")
    print("5. Exit")


def main():
    menu = [
        {"name": "Vegetable Sandwich", "price": 40},
        {"name": "Masala Dosa", "price": 55},
        {"name": "Veg Thali", "price": 90},
        {"name": "Lemon Juice", "price": 25},
    ]
    feedback_list = []

    print("Welcome to the College Canteen App!")
    running = True
    while running:
        show_options()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_menu_item(menu)
        elif choice == "3":
            give_feedback(menu, feedback_list)
        elif choice == "4":
            show_feedback(feedback_list)
        elif choice == "5":
            print("Thanks for visiting. See you next time!")
            running = False
        else:
            print("Please choose a number from 1 to 5.")


main()
