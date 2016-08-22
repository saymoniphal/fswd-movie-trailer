#!/bin/bash/env python

import webbrowser

class Video(object):
    ''' A template for Video '''  
    def __init__(self, title, runtime, trailer):
        self.title = title
        self.runtime = runtime 
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrower.open(self.trailer_youtube_url)

class Movie(Video):
    ''' A template for Movie, which inherites from Video class
    and take a dictionary as input to constructor
    @Input to constructor: a dictionary with keys:
        title, runtime, trailer_youtube_url, poster_image_url 
    ''' 
    def __init__(self, movie_dict):
        super(Movie, self).__init__(movie_dict["title"],
                                    movie_dict["runtime"],
                                    movie_dict["trailer_youtube_url"])
        self.storyline = movie_dict["storyline"]
        self.poster_image_url = movie_dict["poster_image_url"]

    def show_storyline(self):
        print self.storyline 
