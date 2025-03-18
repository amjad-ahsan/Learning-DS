from prettytable import PrettyTable
from datetime import datetime, timedelta
import random  # randomizer

# Randomizer

def randomizer_date():  # random date
    today = datetime.now()
    start_date = today - timedelta(days=365)  # One year ago
    random_days = random.randint(0, 365)  # Random number of days within the last year
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")


def randomizer_id():  # random id
    random_id = random.randint(1000, 9999) # from 1000 - 9999 generata random number
    return random_id

# Table for ALL

library = [
    {
        'ID': randomizer_id(),
        'Title': 'Netzwerk B1 Ubungztbuch',
        'Genre': 'Horror, Educational',
        'Last Update': randomizer_date(),
        'Total Copies': 3,
        'Available Copies': 0
    },
    {
        'ID': randomizer_id(),
        'Title': 'Netzwerk B1 Kursbuch',
        'Genre': 'Horror, Educational',
        'Last Update': randomizer_date(),
        'Total Copies': 5,
        'Available Copies': 2
    },
    {
        'ID': randomizer_id(),
        'Title': 'Python for Dummies',
        'Genre': 'Educational',
        'Last Update': randomizer_date(),
        'Total Copies': 5,
        'Available Copies': 0
    },
    {
        'ID': randomizer_id(),
        'Title': 'Bean Bear',
        'Genre': 'Comedy',
        'Last Update': randomizer_date(),
        'Total Copies': 10,
        'Available Copies': 0
    },
    {
        'ID': randomizer_id(),
        'Title': 'Overlord',
        'Genre': 'Fantasy, Scifi',
        'Last Update': randomizer_date(),
        'Total Copies': 8,
        'Available Copies': 2
    },
    # 5
    {
        'ID': randomizer_id(),
        'Title': 'Family 3',
        'Genre': 'Family, Adventure',
        'Last Update': randomizer_date(),
        'Total Copies': 5,
        'Available Copies': 1
    },
    {
        'ID': randomizer_id(),
        'Title': 'Donkey Kong',
        'Genre': 'Comedy, Animation',
        'Last Update': randomizer_date(),
        'Total Copies': 8,
        'Available Copies': 2
    },
    {
        'ID': randomizer_id(),
        'Title': 'Blitz',
        'Genre': 'War, Gore, Adventure',
        'Last Update': randomizer_date(),
        'Total Copies': 6,
        'Available Copies': 2
    },
    {
        'ID': randomizer_id(),
        'Title': 'Space',
        'Genre': 'Horror, Scifi',
        'Last Update': randomizer_date(),
        'Total Copies': 3,
        'Available Copies': 2
    },
    {
        'ID': randomizer_id(),
        'Title': 'Mein Geld!',
        'Genre': 'Comedy, Adventure',
        'Last Update': randomizer_date(),
        'Total Copies': 2,
        'Available Copies': 0
    },
]

def book_status(book_copies):  # check status 
    try:
        book_copies = int(book_copies)
        if book_copies > 0:
            return 'Available'
        else:
            return "Not Available"
    except ValueError:
        return '-+-+- Invalid input for available copies -+-+-'

def table_list(library):
    data_table = PrettyTable()
    data_table.field_names = ["Number", 'ID', "Title", "Genre", "Last Update", "Status", "Available/Total"]

    for index_num, title in enumerate(library, start=1):  # dont use range(len()), error after multiple instances. said stackoverflow
        status = book_status(title['Available Copies'])
        col_copies = f'{title["Available Copies"]}/{title["Total Copies"]}'

        data_table.add_row([
            index_num,  # Start from 1 change to  +1 if using range(len())
            title['ID'],
            title['Title'],
            title['Genre'],
            title['Last Update'],
            status,
            col_copies
        ])
    print(data_table)  # Print the table

####################################
## YorN function


def yorn():
    while True:
        y_or_n = input("\n-+-+- Would you like to do it again? (yes/no): ").lower()
        if y_or_n == "yes":
            return True
        elif y_or_n == "no":
            print("-+-+- Returning to  menu -+-+-")
            return False
        else:
            print("-+-+- Invalid input! Please enter 'yes' or 'no'. -+-+-")



#####################################
### FOR CHECK / SEARCHES FUNCTION ##

# View table list for search_function()
def view_available_only():
    available_books = []
    for title in library:
        if title['Available Copies'] > 0:
            available_books.append(title)
    table_list(available_books)

def view_not_available_only():
    not_available_books = []
    for title in library:
        if title['Available Copies'] == 0:
            not_available_books.append(title)
    table_list(not_available_books)



# Search function for search_function()
def name_search_func(library):
    while True:
        search_name = input('-+-+- Insert Name here: ').lower()

        searches = []
        for title in library:
            if search_name in title['Title'].lower():
                searches.append(title)

        if searches:
            print('\n-+-+- Search Results:')
            table_list(searches)
        else:
            print(f'\n-+-+- Error: "{search_name}" not found -+-+-')

        if not yorn(): 
            break

def genre_search_func(library):
    while True:
        search_genre = input('-+-+- Insert Genre here: ').lower()

        searches = []
        for title in library:
            if search_genre in title['Genre'].lower():
                searches.append(title)
        if searches:
            print('\n-+-+- Search Results:')
            table_list(searches)
        else:
            print(f'\n-+-+- Error: "{search_genre}" not found -+-+-')

        if not yorn(): 
            break

# search Function
def search_function():
    while True:
        search_menu()
        print('\n-+-+- Select your answer from 1/2/3/4/5/6 -+-+-')
        check_input = input("-+-+- Please insert your choice here: ")

        if check_input == "1":
            print('\n-+-+- Showing All Books -+-+-')
            table_list(library)

        elif check_input == "2":
            print('\n-+-+- Showing Only Available Books -+-+-')
            view_available_only()

        elif check_input == "3":
            print('\n-+-+- Showing Only Not Available Books -+-+-')
            view_not_available_only()

        elif check_input == "4":
            print('\n-+-+- Searching by Name, Please insert the title of the book -+-+-')
            name_search_func(library)#add library 

        elif check_input == "5":
            print('\n-+-+- Searching by genre, Please insert the genre of the book -+-+-')
            genre_search_func(library)

        elif check_input == "6":
            print('\n-+-+- Returning to main menu -+-+-')
            break
        else:
            print("\n-+-+- Invalid option! Please try again. -+-+-")

###########################################
### FOR RENTING AND RETURNING BOOK #####

# Rent function, deduct book
def rent_func(library):
    while True:
        rent_input = input('\n-+-+- Input ID or the name of the book: ').strip().lower()  

        book_found = False  

        for title in library:
            if title['Title'].lower() == rent_input or str(title['ID']).lower() == rent_input:
                book_found = True  
                if title['Available Copies'] > 0:
                    title['Available Copies'] -= 1
                    title['Last Update'] = datetime.now().strftime("%Y-%m-%d")  # Update date
                    print(f"-+-+- Book '{title['Title']}' rented successfully. -+-+-")
                else:
                    print(f"-+-+- Sorry, '{title['Title']}' is not available for rent. -+-+-")
                break  

        if not book_found:  
            print(f"-+-+- Book '{rent_input}' is not available in the library. -+-+-")
        print('\n-+-+- Showing the Updated Books Available in the Library -+-+-')
        table_list(library)      
        if not yorn(): 
            break

# Return function, add book
def return_func(library):
    while True:
        return_input = input('\n-+-+- Input ID or the name of the book: ').strip().lower() 

        book_found = False 

        for title in library:
            if title['Title'].lower() == return_input or str(title['ID']).lower() == return_input:
                book_found = True 
                if title['Available Copies'] < title['Total Copies']:
                    title['Available Copies'] += 1
                    title['Last Update'] = datetime.now().strftime("%Y-%m-%d")  # Update date
                    print(f"-+-+- Book '{title['Title']}' returned successfully. -+-+-")
                else:
                    print(f"-+-+- Error: All copies of '{title['Title']}' are already available. -+-+-")
                break  

        if not book_found:  
            print(f"-+-+- Book '{return_input}' is not available in the library. -+-+-")
        print('\n-+-+- Showing the Updated Books Available in the Library -+-+-')
        table_list(library)      
        if not yorn(): 
            break

# Rent/Return Menu
def rent_return_function(library):
    while True:
        rent_return_display()
        print('\n-+-+- Select your answer from 1/2/3 -+-+-')
        rr_input = input("-+-+- Please insert your choice here: ")

        if rr_input == '1':  # Rent a Book
            print("\n-+-+- Showing Library Books List -+-+-")
            table_list(library)
            rent_func(library)

        elif rr_input == '2':  # Return a Book
            print("\n-+-+- Showing Library Books List -+-+-")
            table_list(library)
            return_func(library)

        elif rr_input == '3':  # Return to Main Menu
            print('\n-+-+-Returning to main menu -+-+-')
            break

        else:
            print('\n-+-+-Invalid choice! Please enter 1, 2, or 3.-+-+-')

############################################
# Editing existing data from the library
def library_edit_func(library):
    while True:
        edit_library_input = input('\n-+-+- Input ID or the name of the book: ').strip()

        for title in library:
            if title['Title'].lower() == edit_library_input.lower() or str(title['ID']).lower() == edit_library_input.lower():
                


                print("\n-+-+- Selected Book Details -+-+-")
                selected_table = PrettyTable()
                selected_table.field_names = ["ID", "Title", "Genre", "Last Update", "Status", "Available/Total"]
                status = book_status(title['Available Copies'])
                col_copies = f'{title["Available Copies"]}/{title["Total Copies"]}'
                selected_table.add_row([
                    title['ID'],
                    title['Title'],
                    title['Genre'],
                    title['Last Update'],
                    status,
                    col_copies
                ])


                print(selected_table)

                action = input("-+-+- Do you want to add or reduce copies? (add/reduce): ").lower()
                if action == "add":
                    copies_num = int(input("-+-+- Enter the number of copies to add: "))
                    title["Total Copies"] += copies_num
                    title["Available Copies"] += copies_num
                    title["Last Update"] = datetime.now().strftime("%Y-%m-%d")  # Update to current date
                    print(f"-+-+- Added {copies_num} copies of '{edit_library_input}'. -+-+-")
                elif action == "reduce":
                    copies_num = int(input("-+-+- Enter the number of copies to reduce: "))
                    if copies_num <= title["Total Copies"]:
                        title["Total Copies"] -= copies_num
                        title["Available Copies"] = max(title["Available Copies"] - copies_num, 0)
                        title["Last Update"] = datetime.now().strftime("%Y-%m-%d")  # Update to current date
                        print(f"-+-+- Reduced {copies_num} copies of '{edit_library_input}'. -+-+-")
                    else:
                        print("-+-+- Cannot reduce more copies than the total copies. -+-+-")
                else:
                    print("-+-+- Invalid action! Please choose 'add' or 'reduce'. -+-+-")
                break
        else:
            print(f"-+-+- Book '{edit_library_input}' not found in the library. -+-+-")
            
        if not yorn(): 
            break

#add new book
def add_new_book(library):
    while True:
        book_name = input("-+-+- Enter the name of the book: ").strip()
        genre = input("-+-+- Enter the genre of the book: ").strip()
        if not book_name or not genre:  
            print("-+-+- Warning! Book and Genre cannot be empty. Please try again. -+-+-")
            continue  
        break  


    while True:
        total_copies = input("-+-+- Enter the total number of copies: ").strip()
        available_copies = input("-+-+- Enter the number of available copies: ").strip()


        if not total_copies.isdigit() or not available_copies.isdigit():# numerical check
            print("-+-+- Warning! Invalid input! Please enter valid numbers. -+-+-")
            continue  

        total_copies = int(total_copies)# debugging, make sure the number is int always
        available_copies = int(available_copies)

        if total_copies < 0 or available_copies < 0:
            print("-+-+- Warning! Number of copies cannot be negative. Please try again. -+-+-")
            continue 
        if available_copies > total_copies:
            print("-+-+- Warning! Available copies cannot exceed total copies. Please try again. -+-+-")
            continue

        break

#randomizer 
    book_id = randomizer_id()

#add book
    new_book = {
        "ID": book_id,
        "Title": book_name,
        "Genre": genre,
        "Total Copies": total_copies,
        "Available Copies": available_copies,
        "Last Update": datetime.now().strftime("%Y-%m-%d")  # Set to current date
    }
    library.append(new_book)
    #

    print(f"-+-+- Book '{book_name}' added successfully with ID '{book_id}'. -+-+-")
    print('\n-+-+- Showing the Updated Books Available in the Library -+-+-')
    table_list(library)

    
# Remove bok
def remove_book(library):
    while True:
        remove_id = input("-+-+- Enter the Book ID or Book Name to remove: ").strip()

        book_exist = False
        for title in library: # untuk nama didalam dict library
            if str(title["ID"]) == remove_id or (title["Title"].lower()) == remove_id.lower(): #debugging make sure title is string
                library.remove(title)  #dewbugging dont mix up library with title
                print(f"-+-+- Book '{title['Title']}' (ID: {title['ID']}) has been removed from the library. -+-+-")
                book_exist = True
                break

        if not book_exist:
            print(f"-+-+- Book with ID or Name '{remove_id}' not found in the library. -+-+-")

        print('\n-+-+- Showing the Updated Books Available in the Library -+-+-')
        table_list(library)
        if not yorn(): 
            break

## Managing Library Function ##
def library_manager():
    while True:
        library_manager_display()

        print('\n-+-+- Select your answer from 1/2/3/4 -+-+-')
        library_input = input("-+-+- Please insert your choice here: ")

        if library_input == '1':
            print('\n-+-+- Select the ID or title of the Book below: -+-+-')
            table_list(library)
            library_edit_func(library)


        elif library_input == '2':
            print('\n-+-+- Showing the Current Books Available in the Library -+-+-')
            table_list(library)
            add_new_book(library)


        elif library_input == '3':
            print('\n-+-+- Showing the Current Books Available in the Library -+-+-')
            table_list(library)
            remove_book(library)


        elif library_input == "4":  # Return to Main Menu
            print("\n-+-+-Returning to the main menu -+-+-")
            break
        else:
            print("\n-+-+- Invalid option! Please try again. -+-+-")

# Function for Menu

# 1st Menu
def menu_display():
    print('\n-+-+- Library -+-+-')
    print('\nWelcome to the Library!, Please select the option below to proceed :')
    print('1. Search Books within Library')
    print('2. Rent or Return a Book')
    print('3. Manage Library')
    print('4. Exit Program')
    

# 2nd Admin Menu
def library_manager_display():
    print('\n-+-+- Library Management -+-+-')
    print('Choose which options would you like to proceed: ')
    print('1. Edit Existing Book')
    print('2. Add New Book')
    print('3. Remove Existing Book')
    print('4. Return to Main Menu')

# Check Menu
def search_menu():
    print('\n-+-+- Searchs Option -+-+-')
    print('Choose which options would you like to proceed: ')
    print('1. Show All Books')
    print('2. Show Available Book Only')
    print('3. Show Not Available Book Only')
    print('4. Search Books by Name')
    print('5. Search Books by Genre')
    print('6. Return to Main Menu')

def rent_return_display():
    print("\n-+-+- Rent/Return Options -+-+-")
    print('Choose which options would you like to proceed: ')
    print("1. Rent a Book")
    print("2. Return a Book")
    print("3. Return to Main Menu")
# Main Function
def main_function():
    while True:
        menu_display()
        print('\n-+-+-Select the numbers 1/2/3/4 -+-+-')
        options_menu = input("-+-+- Please insert your choice here: ")

        if options_menu == "1":
            search_function()

        elif options_menu == "2":
            rent_return_function(library)

        elif options_menu == "3":
            library_manager()

        elif options_menu == '4':
            print('\n-+-+- Exiting program -+-+-')
            break

        else:
            print('\n-+-+- Invalid option! Please try again. -+-+-')

# Main
if __name__ == "__main__":
    main_function()