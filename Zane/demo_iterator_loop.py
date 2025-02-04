#! /usr/bin/env/ python3
# Author: Zane Salam
# Description: This script will demo how to ITERATE through a SEQUENCE
# ONE item at a time using an ITERATOR for loop.
"""
    Docstring:
"""

films=['White Chicks', 'Star Wars', 'Idiocracy', 'The Ringer', 'Step Brothers', 'Rush Hour',
       'LOTR', 'Pulp Fiction', 'Top Gun' ]

# ITERATE through my list sequence one film at a film
# Using an ITERATOR for loop.
for film in films:
    print(film, end=", ")


# ITERATE through AND MODIFY my list sequence one film at a film
# Using an ITERATOR for loop.
idx = 0
for film in films:
    print(film.upper(), end="!, ")
    films[idx] = film.upper()
    idx += 1
print(films)

# ITERATE through AND MODIFY my list sequence one film at a film
# Using an ITERATOR for loop and built-in ENUMERATE function.
# enumerate(seq, start=0) returns TUPLE(idx, object)
for (idx, film) in enumerate(films, start=0):
    print(film.title(), end="\n")
    films[idx] = film.title()
print(films)