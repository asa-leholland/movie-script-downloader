from main import get_movie_script_url


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
