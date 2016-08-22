import media
import fresh_tomatoes
import json

def read_json(filename):
    ''' Read from file in json format and return dictionary object
    @Input: filename(str): file in json format
        file format should be:
        {
            "movie1" : {
                 "title" : "Mymovie1",
                 "Runtime" : 120,
                 "poster_image_url" : "urlhere",
                 "youtube_trailer_url" : "trailer url here"
            }
            "movie2" : {
                 "title" : "Mymovie2",
                 ...
            }
        }
    @Output: dictionary with (key, value) pair as given in filename 
    '''

    movie_dict = {}
    with open(filename, 'r') as f:
        movie_dict = json.load(f)    
    return movie_dict

def movies(movie_info_dict):
    ''' Return list of movie objects ''' 

    movies = []
    for movie_info in movie_info_dict.values():
        movies.append(media.Movie(movie_info)) 
    return movies

def main():
    movie_dict = read_json("movie_entries.conf")
    fresh_tomatoes.open_movies_page(movies(movie_dict)) 

if __name__ == "__main__":
    main()
