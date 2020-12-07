# File to be used for storing any and all constants


STATIC = 'static'

TITLES = ('Harry Potter and the Sorcerer\'s Stone',
         'Harry Potter and the Chamber of Secrets',
         'Harry Potter and the Prisoner of Azkaban',
         'Harry Potter and the Goblet of Fire',
         'Harry Potter and the Order of the Phoenix',
         'Harry Potter and the Half-Blood Prince',
         'Harry Potter and the Deathly Hallows')
SHORT_TITLES = ('Sorcerer\'s Stone',
         'Chamber of Secrets',
         'Prisoner of Azkaban',
         'Goblet of Fire',
         'Order of the Phoenix',
         'Half-Blood Prince',
         'Deathly Hallows')

TOTAL_PAGES = (309, 341, 435, 734, 870, 652, 759)


# Total number of pages for each book, in order
PAGE_NUMBERS = (309, 341, 435, 734, 870, 652, 759)

# Page where each chapter starts. CHAPTER_PAGE[1][0] is Book 1 Chapter 1.
CHAPTER_PAGE = {
    1: (1, 18, 31, 46, 61, 88, 113, 131, 143, 163, 180, 194, 215, 228, 242, 262, 288),
    2: (1, 12, 24, 42, 65, 86, 104, 122, 140, 161, 182, 205, 227, 249, 265, 283, 306, 327),
    3: (1, 16, 31, 49, 69, 96, 123, 141, 162, 183, 211, 233, 252, 269, 291, 314, 332,
        349, 358, 378, 386, 416),
    4: (1, 16, 26, 39, 51, 65, 75, 95, 117, 145, 158, 171, 193, 209, 228, 248, 272, 288, 313,
        337, 363, 385, 403, 433, 458, 479, 509, 535, 564, 581, 605, 636, 644, 659, 670, 692, 716),
    5: (1, 20, 42, 59, 79, 98, 121, 137, 152, 179, 200, 221, 250, 279, 306, 330, 350, 374,
        397, 420, 441, 466, 492, 516, 543, 570, 599, 624, 651, 676, 703, 729, 751, 764, 781,
        807, 820, 845),
    6: (1, 19, 38, 57, 81, 105, 129, 155, 171, 194, 217, 237, 258, 279, 303, 325, 349, 373, 399,
        423, 447, 469, 492, 513, 535, 555, 579, 597, 611, 633),
    7: (1, 13, 30, 43, 63, 86, 111, 137, 160, 176, 201, 223, 246, 268, 284, 311, 330, 350, 363,
        388, 405, 446, 477, 502, 519, 544, 554, 571, 589, 608, 638, 659, 691, 705, 724, 753),
}

