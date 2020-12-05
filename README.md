# Ravenclaw Toolbox!

Hello, and welcome to our repository! We hope to write some cool tools to help people with Arithmancy. 

### PDF Splitter

To split your Harry Potter PDFs into pages, first you'll need to move your PDFs into the `books` folder. Make sure they are named the following:
* Harry Potter and the Sorcerer's Stone.pdf
* Harry Potter and the Chamber of Secrets.pdf
* Harry Potter and the Prisoner of Azkaban.pdf
* Harry Potter and the Goblet of Fire.pdf
* Harry Potter and the Order of the Phoenix.pdf
* Harry Potter and the Half-Blood Prince.pdf
* Harry Potter and the Deathly Hallows.pdf

Once you do that, you're ready to run our program! (For now, assume python experience). Open up your terminal and run `python3 ravenclaw_toolkit/book_splitter.py`. Your results will be waiting in the `Books` folder!


### Display Page

To view a single page of one of the books, You'll need to have populated your `Books` folder with the PDF Splitter (See [PDF Splitter](#pdf-splitter)). Once you've done that, you can go back into your terminal and run `python3 ravenclaw_toolkit/display_page.py <book_num> <page_num>` and you'll see the page open! For example, `python3 display_page.py 4 100` opens the 100th page of Goblet of Fire.
