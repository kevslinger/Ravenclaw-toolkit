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
@app.route("/display_page", methods=['POST'])
def handle_display_page():
    if request.method == 'POST':
        booknum, pagenum, valid = utils.validate_book_page_number(request.form.get('booknum'), request.form.get('pagenum'))
        if valid:
            chapter, chapter_pagenum = utils.get_chapter_page(booknum, pagenum)
            return render_template('display_page.html', filename=utils.build_path(booknum, pagenum), booknum=booknum, chapternum=chapter, chapter_pagenum=chapter_pagenum)
        elif valid == 0:
            return render_template('invalid_number.html', booknum=booknum, pagenum=pagenum, maxpagenum=constants.PAGE_NUMBERS[booknum-1] if 1<=booknum<=7 else 0)
        elif valid == -1:
            return render_template('invalid_format.html', booknum=booknum, pagenum=pagenum)



if __name__ == "__main__":
    app.run()


    
