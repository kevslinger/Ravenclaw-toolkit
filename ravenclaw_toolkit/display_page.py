import argparse
import webbrowser
import os
import constants


###################################################
######################### USAGE ###################
########## python HP_display_page.py 4 100 ########
########## This would open the 100th page of ######
############## HP and the Goblet of Fire ##########
###################################################


def display_page(book, page):
    webbrowser.open(rf"file://{os.path.join(os.getcwd(), 'static', f'HP{book}', f'hp{book}_{page}.pdf')}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('book', type=int, help='Number book (i.e. Goblet of Fire is 4)')
    parser.add_argument('page', type=int, help='Page number')

    args = parser.parse_args()

    display_page(args.book, args.page)
    

if __name__ == '__main__':
    main()
