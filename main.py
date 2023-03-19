import requests
from bs4 import BeautifulSoup
import os

def get_movie_script_url(movie_title):
    title_words = movie_title.split(' ')
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


def fetch_movie_script_text(url, run=False):
    if not run:
        return "test"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return pre_element.text if (pre_element := soup.find('pre')) else ""

def save_movie_script_text(movie_title, script_text) -> bool:
    if not script_text:
        return False
    # Saves the movie script text to a txt file with the movie title as filename
    clean_title = movie_title.replace(":", "")
    clean_title = clean_title.replace(".", "")
    with open(f"scripts/{movie_title}.txt", 'w') as f:
        f.write(script_text)
    return True

def main(infile, is_requesting=False):
    with open(infile, 'r') as f:
        movie_titles = f.read().splitlines()

    print(f'Processing {len(movie_titles)} movies...')

    # create a "scripts" directory if it doesn't exist
    if not os.path.exists('scripts'):
        os.mkdir('scripts')

    failures = []
    for movie_title in movie_titles:
        script_url = get_movie_script_url(movie_title)
        script_text = fetch_movie_script_text(url=script_url, run=is_requesting)
        if not save_movie_script_text(movie_title, script_text):
            failures.append(movie_title)
    if failures:
        print(f'Failed to process {len(failures)} movies')
        # write a new text file with the failed movies
        with open('failed_movies.txt', 'w') as f:
            f.write('\n'.join(failures))
    else:
        print('All movies processed successfully')


if __name__ == '__main__':
    main(infile='movies.txt', is_requesting=True)
