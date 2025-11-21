def main():
    print("Main Menu:" \
    "What would you like to do?" \
    "0) Exit"
    "1) New file")
    while True:
        try:
            choice = int(input("Choice: "))
            break
        except Exception as e:
            "Invalid choice"
    
    choice_selector(choice)


def choice_selector(choice):
    if choice == 0:
        quit()
    elif choice == 1:
        print("Need to make new file")

    else:
        main()

    main()
main()