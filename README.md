# Ravenclaw Toolbox!

Hello, and welcome to our repository! We hope to write some cool tools to help people with Arithmancy. If you are planning to work on this as a developer, please see the [Developer](#developer) section.

### PDF Splitter

To split your Harry Potter PDFs into pages, first you'll need to move your PDFs into the `ravenclaw_toolkit/static` folder. Make sure they are named the following:
* Harry Potter and the Sorcerer's Stone.pdf
* Harry Potter and the Chamber of Secrets.pdf
* Harry Potter and the Prisoner of Azkaban.pdf
* Harry Potter and the Goblet of Fire.pdf
* Harry Potter and the Order of the Phoenix.pdf
* Harry Potter and the Half-Blood Prince.pdf
* Harry Potter and the Deathly Hallows.pdf

Once you do that, you're ready to run our program! (For now, assume python experience). Open up your terminal and run `python3 ravenclaw_toolkit/book_splitter.py`. Your results will be waiting in the `ravenclaw_toolkit/static` folder! (`ravenclaw_toolkit/static/HP1` will contain all the pages of Sorcerer's Stone.)


### Display Page

To view a single page of one of the books, You'll need to have populated your `ravenclaw_toolkit/static` folder with the PDF Splitter (See [PDF Splitter](#pdf-splitter)). Once you've done that, you can go back into your terminal and run `python3 ravenclaw_toolkit/display_page.py <book_num> <page_num>` and you'll see the page open! For example, `python3 display_page.py 4 100` opens the 100th page of Goblet of Fire.


## Developer

### Getting Started 

Everything you need to do will be done from insdie the `ravenclaw_toolkit` directory, so get in there (`cd ravenclaw_toolkit`). First, you need to create an `instance` folder, which we'll use to make a `config.py` file for storing your secret key. 

```
mkdir instance 
touch config.py
```

Then, fill in your secret key (one way to do this is to run `python3 -c 'import os; print(os.urandom(12))'`) and copy/paste the output. Specifically, your `config.py` should be 1-line and look something like `SECRET_KEY = b'm\xef\xc8\xef\x97v\x1c\xe3\xf0t=\xf6'`. After you do that, you'll need to populate the `ravenclaw_toolkit/static` folder with the texts. You can use the method outlined in the [PDF Splitter](#pdf-splitter) section, or provide your own. The directory structure is 

```
.
+-- static
|  +-- HP1
|  +-- HP2
|     +-- hp2_1.png
|     +-- hp2_2.png
|  +-- HP3
```

(note: structure subject to change.) Once you have an `instance/config.py` and a populated `ravenclaw_toolkit/static`, then you need to make sure you have all the python dependencies installed. We recommend using a virtual environment (like [virtualenv](https://pypi.org/project/virtualenv/)) for managing the dependencies. Once you have virtualenv installed, create a virtual environment with `virtualenv venv --python=python3`, then `source venv/bin/activate`. Then, install the dependencies with `pip install -r requirements.txt`. 

If you've gotten this far, you should be all set to run the web app locally!! Try running `python app.py`. The output should give you the URL to go to (for me, it is `http://127.0.0.1:5000/`)

### Help

If you need help, feel free to raise a GitHub issue! IF you're on the ravenclaw discord, you can ask.... someone... in, uh... one of the channels (maybe study-hall would be good for this)
