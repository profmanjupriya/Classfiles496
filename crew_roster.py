import os

# Initialize the crew roster as a list of dictionaries
crew_roster = []

# Prepare the log file
log_file = "testing_log.txt"
if os.path.exists(log_file):
    os.remove(log_file)

# Function to write to the log file
def write_to_log(action, message):
    with open(log_file, "a") as f:
        f.write(f"{action}: {message}\n")

def add_crew_member():
    name = input("Enter crew member's name: ")
    role = input("Enter crew member's role: ")
    crew_roster.append({"name": name, "role": role})
    print(f"Crew member {name} added successfully!\n")
    write_to_log("Add Crew Member", f"Added {name} as {role}")

def view_crew():
    if not crew_roster:
        print("The crew roster is empty.\n")
        write_to_log("View Crew", "The roster is empty.")
    else:
        print("\nCrew Roster:")
        for i, member in enumerate(crew_roster, start=1):
            print(f"{i}. {member['name']} - {member['role']}")
        print()
        write_to_log("View Crew", "Displayed the crew roster.")

def search_crew_member():
    name = input("Enter the name of the crew member to search for: ")
    # Write Code to Search and print the list of crew members with the name here
    write_to_log("Search Crew Member", f"Searched for {name}.")

def remove_crew_member():
    name = input("Enter the name of the crew member to remove: ")
    # Write code to Remove the crew member here
    write_to_log("Remove Crew Member", f"Tried to remove {name}.")

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
            write_to_log("Exit", "Program exited.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            write_to_log("Invalid Input", f"User entered {choice}.")

if __name__ == "__main__":
    main()
