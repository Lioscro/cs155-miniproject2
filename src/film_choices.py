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
# []
def get_scifi():
    return []

# This returns the 10 randomly selected films, which are:
# []
def random_ten():
    return []
