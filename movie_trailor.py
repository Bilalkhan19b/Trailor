#!/usr/bin/env python
# coding: utf-8

# ### Name: Muhammad Bilal Khan
# ### Email: mbikhan@students.uit.edu
# ### Whatsapp: 03363791297
# # Project for Python & Deep Learning Bootcamp

# In[4]:

#importing web browser
import webbrowser

class Movie:
    def __init__(self, title, storyline, release_date, rating, youtube_url, director, box_office):
        self.title = title
        self.storyline = storyline
        self.release_date = release_date
        self.rating = rating
        self.youtube_url = youtube_url
        self.director = director
        self.box_office = box_office

    def show_trailer(self):
        webbrowser.open(self.youtube_url)

    def show_info(self):
        print("Title: " + self.title)
        print("Storyline: " + self.storyline)
        print("Release Date: " + self.release_date)
        print("Rating: " + self.rating)
        print("Trailer URL: " + self.youtube_url)
        print("Director: " + self.director)
        print("Box Office: " + self.box_office)

# Creating an instance of the Movie class
movie = Movie("John Wick", "John Wick, a retired hitman, is forced to return to his old ways after a group of Russian gangsters steal his car and kill a puppy gifted to him by his late wife.", "07-11-2014", "7.4/10 IMDb", "https://www.youtube.com/watch?v=C0BMx-qxsP4", "Chad Stahelski", "$86 million")

# Calling the methods to show trailer and movie information
movie.show_trailer()
movie.show_info()
