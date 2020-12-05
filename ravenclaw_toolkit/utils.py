# File for all utility functions
import constants

# If user enters < 1 or > 7, then it's not a canonical HP book!
def valid_book_number(book_number):
    return 1 <= book_number <= 7



def valid_page_number(book_number, page_number):
    return 1<= page_number <= constants.PAGE_NUMBERS[book_number-1]


# Make sure the page number the user enters is actually a valid page!
# Returns book number and page number cast into integer
# and an error number:
#### 1 means valid
#### -1 means invalid type (non-number)
#### 0 means page or book number not in range (e.g. book 10)
def validate_book_page_number(book_number, page_number):
    try:
        b = int(book_number)
        p = int(page_number)
        if valid_book_number(b) and valid_page_number(b, p):
            return b, p, 1
        else:
            return b, p, 0
    except ValueError:
        return b, p, -1
