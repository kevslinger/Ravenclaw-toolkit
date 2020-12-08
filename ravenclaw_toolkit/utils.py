# File for all utility functions
import constants
import os

# Return the path to Book <booknum> and Page <pagenum>
# Our directory structure (for some reason) is
# HP<booknum>/hp<booknum>_<pagenum>.png
# lines is a flag for whether we should display the annotated page
def build_path(booknum, pagenum, lines):
    if lines:
        return os.path.join('HP' + str(booknum), 'hp' + str(booknum) + '_' + str(pagenum) + '_lines.png')
    else:
        return os.path.join('HP' + str(booknum), 'hp' + str(booknum) + '_' + str(pagenum) + '.png')


# If user enters < 1 or > 7, then it's not a canonical HP book!
def valid_book_number(book_number):
    return 1 <= book_number <= 7


# Obviously we cannot display a page before 1 or after the last page.
def valid_page_number(book_number, page_number):
    return 1 <= page_number <= constants.TOTAL_PAGES[book_number-1] # books are 1-indexed but the list is 0-indexed


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
        assert b > 0
        assert p > 0
        if valid_book_number(b) and valid_page_number(b, p):
            return b, p, 1
        else:
            return b, p, 0
    except (ValueError, AssertionError):
        return book_number, page_number, -1

def validate_book_number(book_number):
    try:
        b = int(book_number)
        assert b > 0
        if valid_book_number(b):
            return b, 1
        else:
            return b, 0
    except (ValueError, AssertionError):
        return book_number, -1

def validate_page_number(page_number, booknum, chapternum=None):
    try:
        p = int(page_number)
        assert p > 0
        if chapternum:
            # 0-indexed, first chapter
            if chapternum == 1:
                chapter_length = constants.CHAPTER_PAGE[booknum][chapternum] - 1
            # Last chapter
            elif chapternum == len(constants.CHAPTER_PAGE[booknum]):
                chapter_length = constants.TOTAL_PAGES[booknum-1] - constants.CHAPTER_PAGE[booknum][chapternum-1]
            # All other chapters
            else:
                chapter_length = constants.CHAPTER_PAGE[booknum][chapternum] - constants.CHAPTER_PAGE[booknum][chapternum-1]
            if p <= chapter_length:
                return p, 1
            else:
                return p, 0
        else:
            if valid_page_number(p, booknum):
                return p, 1
            else:
                return p, 0
    except (ValueError, AssertionError):
        return page_number, -1

def validate_chapter_number(chapter_number, booknum):
    try:
        c = int(chapter_number)
        assert c > 0
        if c <= len(constants.CHAPTER_PAGE[booknum]):
            return c, 1
        else:
            return c, 0
    except (ValueError, AssertionError):
        return chapter_number, -1

def get_page(booknum, chapternum, chapterpagenum):
    return constants.CHAPTER_PAGE[booknum][chapternum-1] + chapterpagenum - 1
    
    
# util for binary search
def calculate_mid(lower_bound, upper_bound):
    return lower_bound + (upper_bound - lower_bound) // 2


# Determine what page number we're at relative to the beginning of the chapter (which is page 1 of that chapter)
# Function returns:
# Chapter: integer, the chapter we're in
# Chapter Page Num: integer, the page number we are at in the chapter
def get_chapter_page(booknum, pagenum):
    chapter_list = constants.CHAPTER_PAGE[booknum]

    # Last chapter
    if pagenum >= chapter_list[-1]:
        return len(chapter_list), pagenum - chapter_list[-1] + 1
    
    # We can use binary search to find the chapter, or use weird python list iteration...
    upper_bound = len(chapter_list) - 1
    lower_bound = 0
    mid = calculate_mid(lower_bound, upper_bound)

    # Maybe we're lucky? PauseChamp
    if chapter_list[mid] == pagenum:
        return mid + 1, 1 # We're 0-indexed

    # This loop will end once upper bound and lower bound are neighbors. Then, lower bound will be the chapter
    while upper_bound > lower_bound + 1:
        # Maybe we got lucky again?
        if chapter_list[mid] == pagenum:
            return mid + 1, 1
        # If we're below the middle, we need to move our upper bound down.
        elif pagenum < chapter_list[mid]:
            upper_bound = mid
            mid = calculate_mid(lower_bound, upper_bound)
        # If we're above the middle, we need to move our lower bound up.
        else:
            lower_bound = mid
            mid = calculate_mid(lower_bound, upper_bound)

    # If we're at this point, then lower_bound is the chapter number.
    return lower_bound + 1, pagenum - chapter_list[lower_bound] + 1
