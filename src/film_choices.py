import os

import numpy as np
import pandas as pd

# defines functions that allow for grabbing the list of indicies for the
# films that we need to provide visualizations for


# This returns the 10 most popular films, these specifically correspond to:
# [Star Wars (1977), Contact (1997), Fargo (1996), Return of the Jedi (1983),
# Liar Liar (1997), The English Patient (1996), Scream (1996),
# Toy Story (1995), Air Force One (1997), and Independence Day (ID4) (1996)]
def get_popular():
    return [49, 257, 99, 180, 293, 285, 287, 0, 299, 120]


# This returns the 10 highest rated films, these specifically correspond to:
# [A Great Day in Harlem (1994), Someone Else's America (1995),
# Marlene Dietrich: Shadow and Light (1996), They Made Me a Criminal (1939),
# Entertaining Angels: The Dorothy Day Story (1996), Star Kid (1997),
# Santa with Muscles (1996), Prefontaine (1997), Aiqing wansui (1994),
# The Saint of Fort Washington (1993)]
def get_highest():
    return [813, 1598, 1200, 1121, 1652, 1292, 1499, 1188, 1535, 1466]


# This returns the 10 selected documentary films, which are:
# ['Carmen Miranda: Bananas Is My Business (1994)',
# 'American Dream (1990)', 'Paris Was a Woman (1995)',
# 'Wonderful, Horrible Life of Leni Riefenstahl, The (1993)',
# 'Leopard Son, The (1996)', 'Grateful Dead (1995)',
# 'Tigrero: A Film That Was Never Made (1994)',
# 'Heidi Fleiss: Hollywood Madam (1995) ', 'Unzipped (1995)',
# 'Nico Icon (1995)']
def get_documentary():
    return [1307, 1585,  857,  701, 1363,  973, 1561, 1128,  954, 1629]


# This returns the 10 selected scifi films, which are:
# ['Twelve Monkeys (1995)', 'Strange Days (1995)',
# 'Terminator 2: Judgment Day (1991)', 'Alien (1979)',
# 'Escape from L.A. (1996)', 'Visitors, The (Visiteurs, Les) (1993)',
# 'Nemesis 2: Nebula (1995)', 'Kid in King Arthur's Court, A (1995)',
# 'Star Trek: First Contact (1996)', 'Mars Attacks! (1996)']
def get_scifi():
    return [6, 38, 95, 182, 830, 1471, 1595, 559, 221, 234]

# This returns the 10 selected comedy films, which are:
# ['Mars Attacks! (1996)', 'Strictly Ballroom (1992)',
# 'Naked in New York (1994)', 'Manhattan (1979)',
# 'Cable Guy, The (1996)', 'Lady of Burlesque (1943)',
# 'Sabrina (1954)', 'George of the Jungle (1997)',
# 'Richie Rich (1994)', 'Life with Mikey (1993)']
def get_comedy():
    return [234,  708, 1501,  516,  121, 1451,  485,  258,  794, 1269]


# This returns the 10 selected action films, which are:
# ['GoldenEye (1995)', 'Terminator 2: Judgment Day (1991)', 'Supercop (1992)',
# 'Die Hard (1988)', 'Raiders of the Lost Ark (1981)', 'Terminator, The (1984)',
# 'Indiana Jones and the Last Crusade (1989)', 'Air Force One (1997)',
# 'Mission: Impossible (1996)', 'Hackers (1995)'']
def get_action():
    return [1, 95, 127, 143, 173, 194, 209, 299, 404, 1138]

# This returns the 10 randomly selected films, which are:
# ['Muppet Treasure Island (1996)', 'Lion King, The (1994)', 'Home Alone (1990)',
# 'Weekend at Bernie's (1989)', 'Good, The Bad and The Ugly, The (1966)', 
# 'Dead Poets Society (1989)', 'Star Trek: Generations (1994)', 
# 'Batman (1989)', 'Miami Rhapsody (1995)', 'Jumanji (1995)']
def random_ten():
    return [20, 70, 93, 157, 176, 195, 379, 402, 699, 754]
