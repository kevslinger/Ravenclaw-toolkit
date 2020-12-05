import argparse
import webbrowser
import os


###################################################
######################### USAGE ###################
########## python HP_display_page.py 4 100 ########
########## This would open the 100th page of ######
############## HP and the Goblet of Fire ##########
###################################################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('book', type=int, help='Number book (i.e. Goblet of Fire is 4)')
    parser.add_argument('page', type=int, help='Page number')

    args = parser.parse_args()

    webbrowser.open(rf"file://{os.path.join(os.getcwd(), 'Books', f'HP{args.book}', f'hp{args.book}_{args.page}.pdf')}")
    

if __name__ == '__main__':
    main()
