MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit'"
movies = []


def main():
    # this is a menu function
    select = input(MENU_PROMPT)
    while select != 'q':
        # until q is not pressed
        if select == 'a':
            # a to add movie to the database
            data()
        # calling the function data()
        elif select == 'l':
            # show movies inside the movie list
            print(movies)
        elif select == 'f':
            ask = input("Please enter a movie title that you want to find: ")
            #input keeps the desired movie
            result = find(ask)
            print(result)
        else:
            print("Unknown command. Please try again.")

        select = input(MENU_PROMPT)


def data():
    # This function adds the entered credential for the movie
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


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






main()
