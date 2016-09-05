Better view of this README.md file in:
- Chrome or
- Get Markdown reader add-ons for firefox [here](https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer/)

# Project Overview:
This project is a movie trailer web-site which displays a list of movies (poster) and its youtube trailer will be launched upon mouse-click on each movie poster.

# Project structure:
The file movie-trailer.zip is a zip of folder movie-trailer with files as described below:
* **media.py**: module contains class Video and its derived class Movie with instance attributes: *title, poster_image_url, trailer_youtube_url, storyline, and runtime*.
* **fresh_tomatoes.py**: a module provided by Udacity which has function open_movies_page() taking list of Movie objects as input and create fresh_tomatoes.html file which has the content of movie and its trailer when clicked. 
* **entertainment_center.py**: a python program that read from json file (movie_entries.json) described in next point, and generates an html file named fresh_tomatoes.html that display movies posters.
* **movie_entries.json**: a file written in JSON format containing information related to movie as key,value pairs, the keys must be:
  * title: title of the movie to be displayed
  * poster_image_url: the link/url of the movie poster
  * trailer_youtube_url: the link/url of the movie trailer 
  * storyline: a short description about the movie 
  * runtime: runtime of the movie

content of file looks similar:  
```
{
    "<movie_var_name>" : {
        "title" : "<title of the movie> (str)",
        "poster_image_url": "<url of movie poster" (str)", 
        "trailer_youtube_url": "<url of movie trailer (str)",
        "storyline" : "<movie story line> (str)",
        "runtime" : <runtime> (int)
        }
}
```
example:
```
{
    "mulan" : {
    	"title" : "Mulan",
        "poster_image_url" : "http://ia.media-imdb.com/images/M/MV5BMTIwNjY4NDU2NF5BMl5BanBnXkFtZTcwMzM0OTUyMQ@@._V1_UY268_CR2,0,182,268_AL_.jpg",
        "trailer_youtube_url" : "https://www.youtube.com/watch?v=MsAniqGowKE",
        "storyline" : "A young woman secretly join army to save her father from going to fight in old age",
        "runtime" : 120
        } 

}
```
New entries can be added to *movie_entries.json* file in JSON format as described above.  
**Note**: please do not rename movie_entries.json file, in case you want to do so, you will need to change the value passed to function ```read_json(<json_filename>)``` in ```main()``` in **entertainment_center.py**. 

# How to run the project:
Follow below steps to launch the website:
 
1. Extract folder movie_trailer.zip, go to directory *movie_trailer*
2. Launch python program *entertainment_center.py*, the new page of *fresh_tomatoes.html* will be created and it will launched with your default browser. In case it's not lauched, you may try to directly open the *fresh_tomatoes.html* file with your browser (chrome, firefox, etc) 
3. To see the movie trailer, simply click on its poster.

