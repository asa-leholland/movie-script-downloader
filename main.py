# import requests
# from bs4 import BeautifulSoup
# import os

def get_movie_script_url(movie_title):
    title_words = movie_title.split(' ')
    print(title_words)
    if 'The' in title_words:
        non_the = [word for word in title_words if word != 'The']

        non_the[-1] = f'{non_the[-1]},'

        title_words = non_the + ['The']

    url_title = "-".join(title_words)
    url_title = url_title.replace(".", "")
    url_title = url_title.replace(":", "")

    # Build URL from title
    base_url = "https://imsdb.com/scripts/"
    url_suffix = ".html"
    return f"{base_url}{url_title}{url_suffix}"


def get_movie_script_text(script_url):
    # Returns the movie script text in dialogue form from the script URL
    pass

def save_movie_script_text(movie_title, script_text):
    # Saves the movie script text to a txt file with the movie title as filename
    pass

if __name__ == '__main__':
    # List of 641 movie titles
    movie_titles = ["American Beauty", "The Godfather II", "The Lord of the Rings: The Fellowship of the Ring"]

    for movie_title in movie_titles:
        script_url = get_movie_script_url(movie_title)
        script_text = get_movie_script_text(script_url)
        save_movie_script_text(movie_title, script_text)