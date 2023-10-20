import tkinter as tk
from define import *
from tkinter import ttk
from PIL import Image, ImageTk 
from movies_func import *
import webbrowser

movie_data_list=read_movie_data()
data_list=[]

genre_vars = {}  # Variable control for each category
country_vars = {}  # Variable control for each country

genre_selected = False  # Flag to monitor the status of the "Select Movie Genre" button
country_selected = False  # Flag to monitor the status of the "Select Country" button

genre_window = None
country_window = None

search_result_labels=[]  # Initialize the search results list

window = tk.Tk()

def cmd_yes():
    #window operations
    global data_list
    chose_genres = genres_cbx.get()
    
    chose_country = country_cbx.get()

    movie_list=suggest_movies(data_list,None,chose_genres,chose_country)
    for result_label in search_result_labels:
        result_label.destroy()    
    
    show_movies_card(movie_list[:20])

def go_home():
    # Delete previous search data
    search_text.delete(0, tk.END)
    frame_filter.pack_forget()
    frame_timkiem.pack(expand=False, fill=tk.X,pady=50,padx=10)
    # Delete current search results
    for result_label in search_result_labels:
        result_label.destroy()
    
    #Set label to notify search status
    label_tk.config(text='')

def open_new_window(event,movie):
    new_window = tk.Toplevel(window,bg=den)
    new_window.title("More information")
    new_window.geometry("850x475")

    frame_tren = tk.Frame(new_window,bg=den, width=835, height=265)
    frame_tren.grid(row=0, column=0, sticky="nsew")
    
    #Frame chưa ảnh
    img_frame = tk.Frame(frame_tren,bg='#393939', width=165, height=215)
    img_frame.grid(row=0, column=0, sticky="nsew",pady=10,padx=10)
    webpage_url = "https://www.imdb.com/title/"+movie['imdb_id']
    def open_webpage(url):
        webbrowser.open(url)

    def frame_clicked(event):
        open_webpage(webpage_url)

    img_frame.bind("<Button-1>", frame_clicked)

    frame_infor = tk.Frame(frame_tren,bg=den ,width=650, height=215)

    frame_name = tk.Frame(frame_infor,bg=den ,width=650)
    frame_name.grid(row=0, column=0, sticky="nsew")
    movie_name = tk.Label(frame_name,bg=den, text=movie['title'],fg='white',font=("Times New Roman", 20,"bold"))
    movie_name.pack(side='left',pady=15)

    frame_time = tk.Frame(frame_infor,bg=den, width=650,height=60)
    frame_time.grid(row=1, column=0, sticky="nsew")
    tk.Label(frame_time,bg=den, text='Time: '+movie['time'],fg='white').grid(row=0, column=0, sticky="nsew",pady=10,padx=10)

    tk.Label(frame_time,bg=den, text=movie['country'],fg='white').grid(row=0, column=1, sticky="nsew",pady=10,padx=10)

    tk.Label(frame_time,bg=den, text=movie['release_date'],fg='white').grid(row=0, column=2, sticky="nsew",pady=10,padx=10)


    frame_vote = tk.Frame(frame_infor, bg=den,width=650)
    
    tk.Label(frame_vote,bg=den, text=movie['vote'],fg='white',font=("Times New Roman", 20,"bold")).grid(row=0, column=0, sticky="nsew",pady=10,padx=10)
    frame_star = tk.Frame(frame_vote)
    frame_star.grid(row=0, column=1, sticky="nsew",pady=10,padx=10)
    float_number = float(movie['vote'])
    rounded_down_number = int(float_number)

    for _ in range(rounded_down_number) :
        star_label=tk.Label(frame_star,bd=0,bg=den, text='★',fg='white',font=("Times New Roman", 20,"bold")).grid(row=0, column=_)
        
    frame_vote.grid(row=2, column=0, sticky="nsew")

    frame_grene = tk.Frame(frame_infor,bg=den, width=650)
    for indexs,_ in enumerate(movie['genre']):
               ma = tk.Label(frame_grene, bg=den, text=_ ,fg='white',font=("Times New Roman", 14))
               ma.grid(row=0, column=indexs, sticky="nsew",)
    frame_grene.grid(row=3, column=0, sticky="nsew")

    frame_infor.grid(row=0, column=1, sticky="nsew")

    frame_duoi = tk.Frame(new_window, width=835, height=265)
    review = tk.Label(frame_duoi, bg=den,text=movie['overview'],fg='white',wraplength=700,font=("Times New Roman", 12))
    review.pack(anchor="w")
    frame_duoi.grid(row=1, column=0, sticky="nsew")

    new_window.resizable(False, False)

def on_frame_configure(event):
    # Update the Canvas's scrollregion when the child frame's size changes
    canvas.configure(scrollregion=canvas.bbox("all"))

def show_movies_card(data_list):
    # Display results in new labels
    for index,result in enumerate(data_list):
        #create master frame
        search_results_label = tk.Frame(frame,bg="#25282c", height=120)
        #movie photo frame
        img_movie = tk.Frame(search_results_label,bg="#d4d6d5", width=120, height=120)
        img_movie.grid(row=0, column=0, sticky="nsew",pady=10,padx=10)

        #content frames
        frame_conten = tk.Frame(search_results_label,bg="#25282c", width=120, height=120)

        name_movie = tk.Label(frame_conten, bg="#25282c",text=result['title'],fg='white',font=custom_font)
        name_movie.pack(anchor="w")

        infor_movie = tk.Frame(frame_conten, bg="#25282c")
        year_movie = tk.Label(infor_movie, bg="#25282c", text=result['release_date'] ,fg='white',font=("Times New Roman", 14))
        year_movie.grid(row=0, column=0, sticky="nsew",)
        for indexs,_ in enumerate(result['country']):
            country_movie = tk.Label(infor_movie, bg="#25282c", text=_ ,fg='white',font=("Times New Roman", 14))
            country_movie.grid(row=0, column=indexs + 1, sticky="nsew",)
        infor_movie.pack(anchor="w")

        review = tk.Label(frame_conten, bg="#25282c",text=result['overview'],fg='white',wraplength=700,font=("Times New Roman", 12))
        review.pack(anchor="w")

        frame_conten.grid(row=0, column=1, sticky="nsew",pady=10,padx=10)
        search_results_label.grid(row=index+1, column=0, sticky="nsew",pady=10,padx=10)
        search_result_labels.append(search_results_label)
        img_movie.bind("<Button-1>", lambda event, arg=result: open_new_window(event,arg))

    canvas.update_idletasks()  # Update the actual size of the Canvas
    canvas.configure(scrollregion=canvas.bbox("all"))  # Update scrollregion

def search_movies(event):
    global data_list
    frame_timkiem.pack_forget()
    key_word = search_text.get()
    
    data_list = suggest_movies(movie_data_list,key_word,None,None)

    for result_label in search_result_labels:
        result_label.destroy() 

    if key_word=='':
        label_tk.config(text='')
        frame_filter.pack_forget()
        return   
    frame_filter.pack(side='right',expand=False, fill=tk.X,pady=10,padx=10)
    
    label_tk.config(text='search results for "' + key_word + '"')

    show_movies_card(data_list[:20])

def apply_choices(genre_vars, country_vars):
    #genre_vars and country_vars are dictionaries that contain information about
    #Movie genre and country have been selected by the user through checkboxes.
    selected_genres = [genre for genre, var in genre_vars.items() if var.get()]
    selected_countries = [country for country, var in country_vars.items() if var.get()]
    filtered_movies = filter_movies_by_country_and_genre(movie_data_list, selected_countries, selected_genres)


    for result_label in search_result_labels:
        result_label.destroy()
    label_tk.config(text='')
    frame_filter.pack_forget()
    show_movies_card(filtered_movies[:20]) 

def genre_button_clicked():
    global genre_selected
    genre_selected = True
    show_genre_checkboxes()

def country_button_clicked():
    global country_selected
    country_selected = True
    show_country_checkboxes()
    
#category checkbutton
def show_genre_checkboxes():
    global genre_window
    if genre_window and genre_window.winfo_exists():
        genre_window.deiconify()
    else:
        genre_window = tk.Toplevel(window)
        genre_window.title("Choose genres")
        create_checkboxes(genre_window, genres_list, genre_vars)
    genre_window.resizable(False, False)

#country checkbutton
def show_country_checkboxes():
    global country_window
    if country_window and country_window.winfo_exists():
        country_window.deiconify()
    else:
        country_window = tk.Toplevel(window)
        country_window.title("Choose country")
        create_checkboxes(country_window, country_arr, country_vars)
    country_window.resizable(False, False)


# Initialize window
window.geometry(size_window)
window.title("MovieSearcher")
window.iconbitmap("display\input_image_path\icon.ico")


# Initializes the 2 largest frames in the window
title_frame = tk.Frame(window,bg='#24262a')
title_frame.pack(fill=tk.X)

body_frame = tk.Frame(window,bg='red')
body_frame.pack(fill=tk.BOTH)


# Initialize the element in title_frame
title_label = tk.Label(title_frame, text='Search Movie', fg='white', bd=0,bg="#24262a")
title_label.config(font=('Transformers Movie',30))
title_label.pack(pady=10)


# Initialize the component in body_frame
left_frame = tk.Frame(body_frame, bg="#101114", width=255,height=800)
left_frame.pack(side="left",fill=tk.Y)

content_frame = tk.Frame(body_frame, bg="black", width=255,height=800) # Create a frame containing search content and results
content_frame.pack(fill=tk.BOTH)


# Initialize the component in left_frame
home_button = tk.Button(left_frame, bg='#58595b',font=("Times New Roman", 20),width=15 ,text="Home",command=go_home)
home_button.pack(expand=False, fill=tk.X,pady=10,padx=10)

frame_timkiem = tk.Frame(left_frame, bg='#58595b')
frame_timkiem.pack(expand=False, fill=tk.X,pady=50,padx=10)


# Initialize the component in content_frame
search_bar_frame = tk.Frame(content_frame, bg="#212121", width=200, height=50)  # Create a frame for the search bar
search_bar_frame.pack(fill=tk.X)

mucapxep= tk.Frame(content_frame, bg="#212121", width=200, height=50) #Create sorting and filtering frames
mucapxep.pack(fill=tk.X)

search_results_label = tk.Frame(content_frame,bg="#212121", width=200, height=50) # Label displays search results
search_results_label.pack(fill=tk.X)
label_tk = tk.Label(search_results_label, bg="#212121", text='', fg='white', font=("Times New Roman", 30))
label_tk.pack(side='left')

results_frame =  tk.Frame(content_frame, bg="#1c1d20", width=200, height=700) # Create frames for search results
results_frame.pack(fill=tk.BOTH)


# Initialize components in search frame
title_cc = tk.Label(frame_timkiem, bg='#58595b',font=("Times New Roman", 14), text="Genres and Countries only")
title_cc.pack(expand=False, fill=tk.X, side='top')

open_genre_selection_button = tk.Button(frame_timkiem, bg='#58595b',font=("Times New Roman", 14), text="Genres", command=genre_button_clicked) #Create a category selection button
open_genre_selection_button.pack(expand=False, fill=tk.X, side='left')

open_country_selection_button = tk.Button(frame_timkiem, bg='#58595b',font=("Times New Roman", 14), text="Countries", command=country_button_clicked) #create country selection button
open_country_selection_button.pack(expand=False, fill=tk.X, side='left')

apply_button = tk.Button(frame_timkiem, bg='#58595b',font=("Times New Roman", 14), text="Apply",command=lambda: apply_choices(genre_vars, country_vars)) #create an apply button
apply_button.pack(expand=False, fill=tk.X,pady=10,padx=10)


#initialize the component in search_bar_frame
search_bar_image=Image.open('display\input_image_path\search_bar2.png')
search_bar_render=ImageTk.PhotoImage(search_bar_image)
search_bar_label=tk.Label(search_bar_frame,bd=0, image=search_bar_render) # Create a search bar
search_bar_label.place(relx=0.5, rely=0.5, anchor="center")

search_text =tk.Entry(search_bar_frame,font=("Times New Roman", 10),bg="#24262a", bd=0, fg='white',width=75 ) # Create a search keyword input box
search_text.place(relx=0.5011, rely=0.5, anchor="center")


#Initialize components in mucapxep
frame_filter = tk.Frame(mucapxep)#create filter frames

cmbt1 = tk.Button(frame_filter, text="Search", font=("consolas", 15),
               bg="#58595b", command=cmd_yes)
cmbt1.pack(side='right',expand=False, fill=tk.X,pady=10,padx=10)

country_cbx = ttk.Combobox(frame_filter, values=country_arr1)           #country filter 
country_cbx.pack(side='right',expand=False, fill=tk.X,pady=10,padx=10)
lb_2 = tk.Label(frame_filter, text="Country", font=("cambria", 12))
lb_2.pack(side='right',expand=False, fill=tk.X,pady=10,padx=10)

genres_cbx = ttk.Combobox(frame_filter, values=genres_list)          #Category genre
genres_cbx.pack(side='right',expand=False, fill=tk.X,pady=10,padx=10)
lb_2 = tk.Label(frame_filter, text="Genre", font=("cambria", 12))
lb_2.pack(side='right',expand=False, fill=tk.X,pady=10,padx=10)


#Initialize components in results_frame
canvas = tk.Canvas(results_frame,bg="#1c1d20", width=200, height=700) # Create a Canvas to contain the result frame and Scrollbar
canvas.pack(side="left", fill="both", expand=True)

vscrollbar = tk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)   # Create a vertical Scrollbar
vscrollbar.pack(side="right", fill="y")

# Create a frame to place content
frame = tk.Frame(canvas,bg="#1c1d20")
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=vscrollbar.set)

canvas.bind("<Configure>", on_frame_configure)   # Set up the Canvas to scroll when resizing the window


for frame in search_result_labels:
    frame.bind("<Configure>", on_frame_configure)
    
search_text.bind("<Return>", search_movies) # Connect the "Enter" event to the search function

window.mainloop()
