# File to be used for storing any and all constants


STATIC = "static"


VALID = 1
INVALID_NUMBER = 0
INVALID_FORMAT = -1

TITLES = ("Harry Potter and the Sorcerer's Stone",
         "Harry Potter and the Chamber of Secrets",
         "Harry Potter and the Prisoner of Azkaban",
         "Harry Potter and the Goblet of Fire",
         "Harry Potter and the Order of the Phoenix",
         "Harry Potter and the Half-Blood Prince",
         "Harry Potter and the Deathly Hallows")
SHORT_TITLES = ("Sorcerer's Stone",
         "Chamber of Secrets",
         "Prisoner of Azkaban",
         "Goblet of Fire",
         "Order of the Phoenix",
         "Half-Blood Prince",
         "Deathly Hallows")

# Total number of pages for each book, in order
TOTAL_PAGES = (309, 341, 435, 734, 870, 652, 759)



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
        388, 405, 424, 446, 477, 502, 519, 544, 554, 571, 589, 608, 638, 659, 691, 705, 724, 753),
}

CHAPTER_NAME = {
    1: ("The Boy Who Lived", "The Vanishing Glass", "The Letters from No One", "The Keeper of the Keys", "Diagon Alley", "The Journey from Platform Nine and Three-quarters", "The Sorting Hat", "The Potions Master", "The Midnight Duel", "Halloween", "Quidditch", "The Mirror of Erised", "Nicholas Flamel", "Norbert the Norwegian Ridgeback", "The Forbidden Forest", "Through the Trapdoor", "The Man with Two Faces"),
    2: ("The Worst Birthday", "Dobby's Warning", "The Burrow", "At Flourish and Blotts", "The Whomping Willow", "Gilderoy Lockhart", "Mudbloods and Murmurs", "The Deathday Party", "The Writing on the Wall", "The Rogue Bludger", "The Dueling Club", "The Polyjuice Potion", "The Very Secret Diary", "Cornelius Fudge", "Aragog", "The Chamber of Secrets", "The Heir of Slytherin", "Dobby's Reward"),
    3: ("Owl Post", "Aunt Marge's Big Mistake", "The Knight Bus", "The Leaky Cauldron", "The Dementor", "Talons and Tea Leaves", "The Boggart in the Wardrobe", "Flight of the Fat Lady", "Grim Defeat", "The Marauder's Map", "The Firebolt", "The Patronus", "Gryffindor Versus Ravenclaw", "Snape's Grudge", "The Quidditch Final", "Professor Trelawney's Prediction", "Cat, Rat, and Dog", "Moony, Wormtail, Padfoot, and Prongs", "The Servant of Lord Voldemort", "The Dementor's Kiss", "Hermione's Secret", "Owl Post Again"),
    4: ("The Riddle House", "The Scar", "The Invitation", "Back to the Burrow", "Weasleys' Wizard Wheezes", "The Portkey", "Bagman and Crouch", "The Quidditch World Cup", "The Dark Mark", "Mayhem at the Ministry", "Aboard the Hogwarts Express", "The Triwizard Tournament", "Mad-Eye Moody", "The Unforgivable Curses", "Beauxbatons and Durmstrang", "The Goblet of Fire", "The Four Champions", "The Weighing of the Wands", "The Hungarian Horntail", "The First Task", "The House-Elf Liberation Front", "The Unexpected Task", "The Yule Ball", "Rita Skeeter's Scoop", "The Egg and the Eye", "The Second Task", "Padfoot Returns", "The Madness of Mr. Crouch", "The Dream", "The Pensieve", "The Third Task", "Flesh, Blood, and Bone", "The Death Eaters", "Priori Incantatem", "Veritaserum", "The Parting of Ways", "The Beginning"),
    5: ("Dudley Demented", "A Peck of Owls", "The Advance Guard", "Number Twelve, Grimmauld Place", "The Order of the Phoenix", "The Noble and Most Ancient House of Black", "The Ministry of Magic", "The Hearing", "The Woes of Mrs. Weasley", "Luna Lovegood", "The Sorting Hat's New Song", "Professor Umbridge", "Detention with Dolores", "Percy and Padfoot", "The Hogwarts High Inquisitor", "In the Hog's Head", "Educational Deree Number Twenty-Four", "Dumbledore's Army", "The Lion and the Serpent", "Hagrid's Tale", "The Eye of the Snake", "St. Mungo's Hospital for Magical Maladies and Injuries", "Christmas on the Closed Ward", "Occlumency", "The Beetle at Bay", "Seen and Unforeseen", "The Centaur and the Sneak", "Snape's Worst Memory", "Career Advice", "Grawp", "O.W.L.s", "Out of the Fire", "Fight and Flight", "The Department of Mysteries", "Beyond the Veil", "The Only One He Ever Feared", "The Lost Prophecy", "The Second War Begins"),
    6: ("The Other Minister", "Spinner's End", "Will and Won't", "Horace Slughorn", "An Excesss of Phlegm", "Draco's Detour", "The Slug Club", "Snape Victorious", "The Half-Blood Prince", "The House of Gaunt", "Hermione's Helping Hand", "Silver and Opals", "The Secret Riddle", "Felix Felicis", "The Unbreakable Vow", "A Very Frosty Christmas", "A Sluggish Memory", "Birthday Surprises", "Elf Tails", "Lord Voldemort's Request", "The Unknowable Room", "After the Burial", "Horcruxes", "Sectumsempra", "The Seer Overheard", "The Cave", "The Lightning Struck Tower", "Flight of the Prince", "The Phoenix Lament", "The White Tomb"),
    7: ("The Dark Lord Ascending", "In Memoriam", "The Dursleys Departing", "The Seven Potters", "Fallen Warrior", "The Ghoul in Pajamas", "The Will of Albus Dumbledore", "The Wedding", "A Place to Hide", "Kreacher's Tale", "The Bribe", "Magic is Might", "The Muggle-born Registration Commission", "The Thief", "The Goblin's Revenge", "Godric's Hollow", "Bathilda's Secret", "The Life and Lies of Albus Dumbledore", "The Silver Doe", "Xenophilius Lovegood", "The Tale of the Three Brothers", "The Deathly Hallows", "Malfoy Manor", "The Wandmaker", "Shell Cottage", "Gringotts", "The Final Hiding Place", "The Missing Mirror", "The Lost Diadem", "The Sacking of Severus Snape", "The Battle of Hogwarts", "The Elder Wand", "The Prince's Tale", "The Forest Again", "King's Cross", "The Flaw in the Plan", "Epilogue"),
}
