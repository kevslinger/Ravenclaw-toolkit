import sys
sys.path.append('../')
import utils


SUCCESS = 'success'
FAILED = 'failed'

class TestClass:
    def __init__(self):
        self.valid_booknum = 5
        self.valid_chapternum = 7
        self.valid_pagenum = 15

        self.invalid_booknum = 20
        self.invalid_chapternum = 55
        self.invalid_pagenum = 975

    def run_all_tests(self):
        successes = 0
        total = 0

        #wtf how is there no better way to do this
        successes += self.test_build_path_no_lines()
        total += 1
        successes += self.test_build_path_with_lines()
        total += 1
        successes += self.test_valid_book_number_true()
        total += 1
        successes += self.test_valid_book_number_false()
        total += 1
        successes += self.test_valid_page_number_true()
        total += 1
        successes += self.test_valid_page_number_false()
        total += 1
        print(f'{successes} tests passed and {total - successes} failed.')
        

    def test_build_path_no_lines(self):
        fun_name = 'test_build_path_no_lines'
        lines = False
        correct = 'HP' + str(self.valid_booknum) + '/hp' + str(self.valid_booknum) + '_' + str(self.valid_pagenum) + '.png'
        try:
            assert correct == utils.build_path(self.valid_booknum, self.valid_pagenum, lines)
            print(fun_name + ' ' + SUCCESS)
            return 1
        except AssertionError:
            print(fun_name + ' ' + FAILED)
            return 0
    
    def test_build_path_with_lines(self):
        fun_name = 'test_build_path_with_lines'
        lines = True
        correct = 'HP' + str(self.valid_booknum) + '/hp' + str(self.valid_booknum) + '_' + str(self.valid_pagenum) + '_lines.png'
        try:
            assert correct == utils.build_path(self.valid_booknum, self.valid_pagenum, lines)
            print(fun_name + ' ' + SUCCESS)
            return 1
        except AssertionError:
            print(fun_name + ' ' + FAILED)
            return 0
    

    def test_valid_book_number_true(self):
        fun_name = 'test_valid_book_number_true'
        correct = True
        try:
            assert correct == utils.valid_book_number(self.valid_booknum)
            print(fun_name + ' ' + SUCCESS)
            return 1
        except AssertionError:
            print(fun_name + ' ' + FAILED)
            return 0


    def test_valid_book_number_false(self):
        fun_name = 'test_valid_book_number_false'
        correct = False
        try:
            assert correct == utils.valid_book_number(self.invalid_booknum)
            print(fun_name + ' ' + SUCCESS)
            return 1
        except AssertionError:
            print(fun_name + ' ' + FAILED)
            return 0


    def test_valid_page_number_true(self):
        fun_name = 'test_valid_page_number_true'
        correct = True
        try:
            assert correct == utils.valid_page_number(self.valid_booknum, self.valid_pagenum)
            print(fun_name + ' ' + SUCCESS)
            return 1
        except AssertionError:
            print(fun_name + ' ' + FAILED)
            return 0

    def test_valid_page_number_false(self):
        fun_name = 'test_valid_page_number_false'
        correct = False
        try:
            assert correct == utils.valid_page_number(self.valid_booknum, self.invalid_pagenum)
            print(fun_name + ' ' + SUCCESS)
            return 1
        except AssertionError:
            print(fun_name + ' ' + FAILED)
            return 0


if __name__ == '__main__':
    test = TestClass()
    test.run_all_tests()
    
