from flask import render_template
import constants
import utils


# This function is very hard to read and quite messy.
# Any suggestions for refactoring welcome! While maintaining the modularity of the validation functions
def handle_display_page(request):
    # We validate our inputs piece by piece. First, we make sure the user-entered book number is valid.
    booknum, book_valid = utils.validate_book_number(request.form.get('booknum'))
        # Entered book number is positive int from 1 to 7
    if book_valid == 1:
        # Next we validate the chapter number. Note that this field is optional, so we may get None
        chapternum = request.form.get('chapternum')
        # If the user supplied a chapter num, then we need to validate it.
        if chapternum:
            chapternum, chapter_valid = utils.validate_chapter_number(chapternum, booknum)
            # If the chapter number the user supplied for the given book is valid, then we need to validate the page number
            if chapter_valid == constants.VALID:
                chapter_pagenum, page_valid = utils.validate_page_number(request.form.get('pagenum'), booknum, chapternum)
                # If the page number the user supplied for the book is valid, then we can go fetch the page!
                if page_valid == constants.VALID:
                    # Check to see if the user wants line numbers on the page (this is defaulted to true)
                    if request.form.get('overlay'):
                        lines = True
                    else:
                        lines = False
                        # Since our user-entered pagenumber is relative to the chapter, we need to fetch the absolute pagenumber from the book.
                    pagenum = utils.get_page(booknum, chapternum, chapter_pagenum)
                    # Display the page.
                    return render_template('display_page.html', filename=utils.build_path(booknum, pagenum, lines), booknum=booknum, bookname=constants.SHORT_TITLES[booknum-1], chapternum=chapternum, chaptertitle=constants.CHAPTER_NAME[booknum][chapternum-1], chapter_pagenum=chapter_pagenum, chapter_beginning_pagenum=constants.CHAPTER_PAGE[booknum][chapternum-1], pagenum=pagenum)
                    
                # Getting here means that the page number is too high for the specified chapter (note that it can never be too low because every chapter starts at page 1 and we throw invalid format on non-positive integers)
                elif page_valid == constants.INVALID_NUMBER:
                    return render_template('invalid_page.html', booknum=booknum, booktitle=constants.SHORT_TITLES[booknum-1], chapternum=chapternum, chaptertitle=constants.CHAPTER_NAME[booknum][chapternum-1], pagenum=chapter_pagenum, maxchapternum=constants.CHAPTER_PAGE[booknum][chapternum] - constants.CHAPTER_PAGE[booknum][chapternum-1], maxpagenum=constants.TOTAL_PAGES[booknum-1])
                    # Getting here means that the page number is not a number!
                elif page_valid == constants.INVALID_FORMAT:
                    return render_template('invalid_format.html', booknum=booknum, chapternum=chapternum, pagenum=chapter_pagenum)
            # Getting here means the chapter entered is too large for the number of chapters in the book.
            elif chapter_valid == constants.INVALID_NUMBER:
                return render_template('invalid_chapter.html', booknum=booknum, booktitle=constants.SHORT_TITLES[booknum-1], chapternum=chapternum, pagenum=request.form.get('pagenum'), maxpagenum=constants.TOTAL_PAGES[booknum-1])
                # Getting here means the chapter entered is invalid format
            elif chapter_valid == constants.INVALID_FORMAT:
                return render_template('invalid_format.html', booknum=booknum, chapternum=chapternum, pagenum=request.form.get('pagenum'))
        # If chapternum is not supplied, then we validate the old way.
        else:
            # Validate book and page number together (TODO: modularize?) based on absolute book length.
            booknum, pagenum, valid = utils.validate_book_page_number(request.form.get('booknum'), request.form.get('pagenum'))
            # If both book and page number are valid, then we can display our page! Just check if we need line numbers of no.
            if valid == constants.VALID:
                chapternum, chapter_pagenum = utils.get_chapter_page(booknum, pagenum)
                if request.form.get('overlay'):
                    lines = True
                else:
                    lines = False
                # TODO: move the calculations of chapternum, etc. outside of the function call? Makes this call look hella bloated.
                return render_template('display_page.html', filename=utils.build_path(booknum, pagenum, lines), bookname=constants.SHORT_TITLES[booknum-1], booknum=booknum, chapternum=chapternum, chaptertitle=constants.CHAPTER_NAME[booknum][chapternum-1], chapter_pagenum=chapter_pagenum, chapter_beginning_pagenum=constants.CHAPTER_PAGE[booknum][chapternum-1], pagenum=pagenum)
            # Here, the page and book number are positive ints, but not within (1-7) for book number, of (1-book length) for page number
            elif valid == constants.INVALID_NUMBER:
                return render_template('invalid_number.html', booknum=booknum, booktitle=constants.SHORT_TITLES[booknum-1], pagenum=pagenum, maxpagenum=constants.TOTAL_PAGES[booknum-1] if 1<=booknum<=7 else 0)
            # Either book or page number are not positive integers.
            elif valid == constants.INVALID_FORMAT:
                return render_template('invalid_format.html', booknum=booknum, chapternum=None, pagenum=pagenum)
    # Entered book number is positive int but not 1-7
    elif book_valid == constants.INVALID_NUMBER:
        return render_template('invalid_book.html', booknum=booknum, booktitle=None, chapternum=request.form.get('chapternum'), pagenum=request.form.get('pagenum'), maxpagenum=None)
    # Entered book number not a positive int
    elif book_valid == constants.INVALID_FORMAT:
        return render_template('invalid_book.html', booknum=booknum, chapternum=None, pagenum=None)
