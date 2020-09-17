import database
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit'"


def main():
    # this is a menu function
    select = input(MENU_PROMPT)
    while select != 'q':
        # until q is not pressed
        if select == 'a':
            # a to add movie to the database
            prompt_add_book()
        # calling the function data()
        elif select == 'l':
            # show movies inside the movie list
            prompt_show_book()
        elif select == 'f':
            prompt_select_book()
        else:
            print("Unknown command. Please try again.")

        select = input(MENU_PROMPT)


def prompt_add_book():
    # This function adds the entered credential for the movie
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year")
    database.add_book(title, director, year)




def show():
    # This function returns each movie from the list of movies
    for movie in movies:
        return movie

def find(ask):
    for movie in movies:
    #searching in the list of movies
        for key, value in movie.items():
        #separating one movie to key and values
            if key == "title" and value == ask:
            #searching for specific ask in atribute
                return movie


def delete_book(name):
    books = [book for book in books if book['name'] != name]


main()