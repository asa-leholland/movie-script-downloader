from main import get_movie_script_url,save_movie_script_text, main
import os

def test_get_movie_script_url():
    movie_title = "American Beauty"
    expected_url = "https://imsdb.com/scripts/American-Beauty.html"

    assert get_movie_script_url(movie_title) == expected_url

def test_should_get_script_with_the():
    movie_title = "The Godfather"
    expected_url = "https://imsdb.com/scripts/Godfather,-The.html"

    assert get_movie_script_url(movie_title) == expected_url

def test_should_get_multiword_with_the():
    movie_title = "The Godfather Part II"
    expected_url = "https://imsdb.com/scripts/Godfather-Part-II,-The.html"

    assert get_movie_script_url(movie_title) == expected_url



def test_should_handle_longer_title():
    movie_title = "The Lord of the Rings: The Fellowship of the Ring"
    expected_url = "https://imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html"

    assert get_movie_script_url(movie_title) == expected_url



def test_sample_text_should_write_to_file():
    movie_title = "American Beauty"
    script_text = "This is a sample script text"
    expected_file_name = "American Beauty.txt"

    save_movie_script_text(movie_title, script_text)

    assert os.path.exists(expected_file_name)

    with open(expected_file_name, 'r') as f:
        assert f.read() == script_text

    os.remove(expected_file_name)

def test_should_main_run():
    main(is_requesting=False)
    # assert that a failed_movies.txt file was created
    # assert that it contains the movie title "American Beauty"
    assert os.path.exists('failed_movies.txt')
    with open('failed_movies.txt', 'r') as f:
        assert 'American Beauty' in f.read()

    os.remove('failed_movies.txt')
