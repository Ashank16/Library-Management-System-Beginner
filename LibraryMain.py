Library = {'DBMS': 10, 'Networking':10, 'Python': 10, 'Java': 5, 'JavaScript':5}


def add_book(book_name,num_of_copies):
    Library[book_name] = num_of_copies


def delete_book(book_name):
    Library.pop(book_name)


def print_all_books():
    print("\n===========================================")
    for book in Library.keys():
        print(book," ->", Library[book]," copies")
    print("===========================================")


def check_availability(book_name):
    if Library[book_name] > 0:
        return True
    else:
        return False


def issue_book(book_name):
    available = check_availability(book_name)
    if available == True:
        Library[book_name] = Library[book_name] - 1
        print(book_name, " Book is issued")
    else:
        print(book_name, " Book is unavailable currently")


def return_book(book_name):
    Library[book_name] = Library[book_name] + 1
    print(book_name, " Book returned")


def calc_charges(days_past_due):
    per_day_penalty = 10
    fine = days_past_due * per_day_penalty
    print("Charges are: ", fine)

def search_book(book_name):
    if book_name in Library.keys() and Library[book_name]>0:
        num_of_available_copies = Library[book_name]
        print(num_of_available_copies, " copies of ",book_name, " are available.")
    else:
        print("Book Unavailable")


if __name__ == '__main__':
    book = input()
    num_of_copies = int(input())
    add_book(book, num_of_copies)
    issue_book('Java')
    issue_book('Java')
    issue_book('Java')
    issue_book('Java')
    issue_book('Java')
    issue_book('Java')
    return_book('Java')
    issue_book('Java')
    search_book('DBMS')
    print_all_books()
    calc_charges(10)
