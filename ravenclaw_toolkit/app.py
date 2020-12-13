from flask import Flask, render_template, request
#from flask import Flask, render_template, request, redirect, send_file, send_from_directory
import os
# import other modules from this project
import utils, constants, handlers

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
        return handlers.handle_display_page(request)
    # If we don't get a post request, just return the home page I guess
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    # Comment out the line above and uncomment the one below if you want to work in dev mode.
    #app.run(debug=True)

    
