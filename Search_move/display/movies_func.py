import csv
import json
from datetime import datetime

#The function gets a list of the genre of that movie
def extract_genres_name(genres_str):
    genres_data = json.loads(genres_str.replace("'", "\""))
    genres_names = [genre['name'] for genre in genres_data]
    return genres_names

#The function gets a list of the production country of that movie
def extract_country_names(countries_str):
    try: 
        # Checks if countries_str_str is null or numeric
        if not countries_str or isinstance(countries_str, (int, float)):
            return ["Unknown"]

        #Check if countries_str_str has a valid JSON string value
        countries_data = json.loads(countries_str.replace("'", "\""))
        if not isinstance(countries_data, list):
            return ["Unknown"]

        #Get list of category names from JSON objects
        countries_names = [country['name'] for country in countries_data]
        return countries_names
    
    except (json.JSONDecodeError, ValueError) as e:
        return ["Unknown"]

#get year
def get_year_from_release_date(release_date):
    if release_date:
        try:
            #Trying to convert to 'y-m-d' format
            date_obj = datetime.strptime(release_date, '%Y-%m-%d')
            return date_obj.year
        except ValueError:
            try:
                #If unsuccessful, try converting to 'd/m/y' format
                date_obj = datetime.strptime(release_date, '%d/%m/%y')
                return date_obj.year
            except ValueError:
                return 0  #Returns 0 if both formats are invalid
    return 0

#The list of movie titles includes information about that movie
def read_movie_data(): 
    movie_data_list = []
    with open('movies_metadata.csv', mode='r', encoding='utf-8') as file: 
        csv_reader = csv.DictReader(file) 
        for row in csv_reader:
            title = row['title']
            genres = extract_genres_name(row['genres'])
            country = extract_country_names(row['production_countries'])
            popularity = row['popularity']
            vote = row['vote_average']
            review = row['overview']
            time = row['runtime']
            imdb_id = row['imdb_id']
            year = get_year_from_release_date(row['release_date'])
            movie_data_list.append({'imdb_id':imdb_id,'title': title, 'genre': genres, 'release_date': year,
                                     'popularity': popularity,'time':time, 'vote': vote, 'country': country,'overview':review})
    return movie_data_list

#List of entire movie genres
def create_genre_arr(movie_data_list):
    genres_arr = []
    for movie_data in movie_data_list:
        genres = movie_data['genre']
        for genre in genres:
            if genre not in genres_arr:
                genres_arr.append(genre)
    return genres_arr

#List of all producing countries
def create_country_arr(movie_data_list):
    countries_arr = []
    for movie_data in movie_data_list:
        countrys = movie_data['country']
        for country in countrys:
            if country not in countries_arr:
                countries_arr.append(country)
    return countries_arr

#The function retrieves a movie based on input including movie name, genre, and country
def suggest_movies(movie_data_list, search_title=None, search_genre=None, search_country=None):

    filtered_movies = []

    for movie_data in movie_data_list:
        title = movie_data['title']
        genres = movie_data['genre']
        country = movie_data['country']

        #Checks whether title has the value None or not
        if title is not None:
            title_lower = title.lower()
        else:
            title_lower = ""

        #Check if it belongs or not
        if (not search_title or (search_title.lower() in title_lower)) and \
           (not search_genre or search_genre in genres) and \
           (not search_country or search_country in country):
            filtered_movies.append(movie_data)
    
    filtered_movies.sort(key=lambda x: float(x['vote']) if x['vote'] is not None else 0, reverse=True)

    return filtered_movies

#The function retrieves a movie based on input including just genre, and country
def filter_movies_by_country_and_genre(movie_data_list, countries=None, genres=None):
    filtered_movies = []
    priority_movies = []
    
    for movie_data in movie_data_list:
        production_countries = movie_data['country']
        movie_genres = movie_data['genre']

        if (not countries) or all(country in production_countries for country in countries):
            if (not genres) or all(genre in movie_genres for genre in genres):
                priority_movies.append(movie_data)
                
            elif any(genre in movie_genres for genre in genres):
                filtered_movies.append(movie_data)
        
        elif any(country in production_countries for country in countries) and\
                any(genre in movie_genres for genre in genres):
            priority_movies.append(movie_data)
        else:
            filtered_movies.append(movie_data)

    # Sort priority list and filter list based on vote score
    priority_movies.sort(key=lambda x: float(x['vote']) if x['vote'] is not None else 0, reverse=True)
    filtered_movies.sort(key=lambda x: float(x['vote']) if x['vote'] is not None else 0, reverse=True)

    return priority_movies + filtered_movies
