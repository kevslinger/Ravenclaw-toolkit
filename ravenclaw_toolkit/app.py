from flask import Flask, render_template, flash, request, url_for
#from flask import Flask, render_template, request, redirect, send_file, send_from_directory
import os
# import other modules from this project
import display_page, utils, constants

# Use instance relative config to hide our secret key away in the config file.
app = Flask(__name__.split('.')[0], instance_relative_config=True)
app.config['IMAGE_FOLDER'] = 'static'
# Load secret key
app.config.from_pyfile('config.py')

####################
### Landing Page ###
####################

# Home page
@app.route("/")
def landing():
    return render_template("home.html")



###########################
### Display Image Page ####
###########################
# TODO: Make the conditional structure flow better. It's so awkward and we're getting to the same endpoint multiple times making the code overly verbose
@app.route("/display_page", methods=['POST'])
def handle_display_page():
    if request.method == 'POST':
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
    # If we don't get a post request, just return the home page I guess
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    # Comment out the line above and uncomment the one below if you want to work in dev mode.
    #app.run(debug=True)

    
