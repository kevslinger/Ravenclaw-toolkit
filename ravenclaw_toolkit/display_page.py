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


def display_page(book, page, lines):
    if lines:
        webbrowser.open(rf"file://{os.path.join(os.getcwd(), 'static', f'HP{book}', f'hp{book}_{page}_lines.png')}")
    else:
        webbrowser.open(rf"file://{os.path.join(os.getcwd(), 'static', f'HP{book}', f'hp{book}_{page}.png')}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('book', type=int, help='Number book (i.e. Goblet of Fire is 4)')
    parser.add_argument('page', type=int, help='Page number')
    parser.add_argument('--lines', action='store_true')
    
    args = parser.parse_args()

    display_page(args.book, args.page, args.lines)
    

if __name__ == '__main__':
    main()
