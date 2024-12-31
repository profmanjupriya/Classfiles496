# crew_roster.py

# Initialize the crew roster as a list of dictionaries
crew_roster = []


def add_crew_member():
    name = input("Enter crew member's name: ")
    role = input("Enter crew member's role: ")
    crew_roster.append({"name": name, "role": role})
    print(f"Crew member {name} added successfully!\n")


def view_crew():
    if not crew_roster:
        print("The crew roster is empty.\n")
    else:
        print("\nCrew Roster:")
      #Write Code to Print all crew members Here
        print()


def search_crew_member():
    name = input("Enter the name of the crew member to search for: ")
   #Write Code to Search and print the list of crew members with the name here


def remove_crew_member():
    name = input("Enter the name of the crew member to remove: ")
   #Write code to Remove the crew member here


def main():
    while True:
        print("Crew Roster Management")
        print("1. Add Crew Member")
        print("2. View Crew")
        print("3. Search Crew Member")
        print("4. Remove Crew Member")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_crew_member()
        elif choice == "2":
            view_crew()
        elif choice == "3":
            search_crew_member()
        elif choice == "4":
            remove_crew_member()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
       #Write Code to handle invalid Inputs


if __name__ == "__main__":
    main()
