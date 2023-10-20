import tkinter as tk
from movies_func import *

size_window = "1125x700"

movie_data_list = read_movie_data()

#Get from create_genre_arr(movie_data_list)
genres_list = ["Action", "Adventure", "Animation", "Comedy", "Crime",
            "Documentary", "Drama", "Family", "Fantasy", "Foreign",
            "History", "Horror", "Music", "Mystery", "Romance",
            "Science Fiction", "Thriller", "TV Movie","War", "Western"]

country_arr =['Vietnam','United States of America', 'United Kingdom', 'France', 'Germany',
            'Italy', 'Canada', 'Japan', 'Spain', 'Russia', 'India',
            'Hong Kong', 'Sweden', 'Australia', 'South Korea', 'Belgium', 'Denmark',
            'Finland', 'Netherlands', 'China', 'Mexico',
            'Poland', 'Brazil', 'Argentina', 'Switzerland', 'Ireland', 'Austria']

#Get from create_country_arr(movie_data_list)
country_arr1 = ['United States of America', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'China',
        'Australia', 'South Africa', 'Canada', 'Switzerland', 'Belgium', 'Japan', 'Iran', 'Netherlands', 'Hong Kong',
        'Tunisia', 'Ireland', 'Dominican Republic', 'Croatia', 'Russia', 'Macedonia', 'Austria', 'Taiwan', 'New Zealand', 
        'Mexico', 'Poland', 'Peru', 'Cuba', 'Liechtenstein', 'Denmark', 'Portugal', 'Finland', 'Sweden', 'Argentina', 'Iceland',
        'South Korea', 'Serbia', 'Hungary', 'Czech Republic', 'India', 'Brazil', 'Greece', 'Congo', 'Senegal', 'Burkina Faso',
        'Romania', 'Philippines', 'Vietnam', 'Trinidad and Tobago', 'Bulgaria', 'Chile', 'Norway', 'Kazakhstan', 'Algeria', 
        'Luxembourg', 'Georgia', 'Ukraine', 'Botswana', 'Aruba', 'Israel', 'Turkey', 'Ecuador', 'Lebanon', 'Morocco', 
        'Bosnia and Herzegovina', 'Bahamas', 'Malaysia', 'Bhutan', 'Jamaica', 'Pakistan', 'Nepal', 'Unknown', 'Thailand', 
        'Namibia', 'Cameroon', 'Colombia', 'Czechoslovakia', 'Uruguay', 'Slovenia', 'Libyan Arab Jamahiriya', 'Puerto Rico', 
        'Soviet Union', 'East Germany', 'Singapore', 'Afghanistan', 'Malta', 'Panama', 'Egypt', 'Zimbabwe', 'Tajikistan',
        'Uzbekistan', 'Costa Rica', 'Kuwait', 'Martinique', 'Ghana', 'Armenia', 'Indonesia', 'Mongolia', 'Bolivia', 'Monaco', 
        'Iraq', 'Slovakia', 'Serbia and Montenegro', 'Venezuela', 'Lithuania', 'Rwanda', 'Palestinian Territory', 'Chad', 
        'Paraguay', 'Qatar', 'Estonia', 'Macao', 'Mali', 'United States Minor Outlying Islands', 'Latvia', 'United Arab Emirates',
         'Azerbaijan', 'Cayman Islands', 'Nicaragua', 'Liberia', 'Yugoslavia', 'Montenegro', 'Angola', 'Belarus', 'Cambodia', 
         'Mauritania', 'Cyprus', 'Bangladesh', 'Syrian Arab Republic', 'Kyrgyz Republic', 'Albania', 'Tanzania', 'North Korea',
         'Kenya', 'Jordan', 'Uganda', 'Saudi Arabia', 'Somalia', 'Guatemala', 'Madagascar', 'Ethiopia', 'Sri Lanka', 'Papua New Guinea', 
         'Nigeria', 'French Polynesia', 'Netherlands Antilles', 'Myanmar', 'Bermuda', 'El Salvador', 'French Southern Territories', 'Samoa',
           'Moldova', 'Barbados', 'Antarctica', 'Gibraltar', 'Brunei Darussalam', 'Honduras', 'Guinea']

country_arr1 = sorted(country_arr1)

den ='#171717'

custom_font = ("Times New Roman", 14,"bold")

def create_checkboxes(master, items, var_dict):
    for i, item in enumerate(items):
        var = tk.BooleanVar()
        var_dict[item] = var
        checkbutton = tk.Checkbutton(master, text=item, variable=var)
        
        # Use grid to adjust the position of the checkbox in two columns
        if i % 2 == 0:  # Adjust rows and columns for the first column
            checkbutton.grid(row=i//2, column=0, sticky="w")
        else:  #Adjust rows and columns for the second column
            checkbutton.grid(row=i//2, column=1, sticky="w")
