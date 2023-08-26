# Movie Script Downloader

The **Movie Script Downloader** is a Python tool designed to fetch movie scripts from the Internet Movie Script Database (IMSDb) website and save them as text files. It utilizes web scraping techniques to retrieve movie scripts and organize them for offline access and analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/movie-script-fetcher.git
    ```
   
## Navigate to the project directory:

```sh
cd movie-script-fetcher
```

Install the required dependencies using pip:

```sh
pip install requests beautifulsoup4
```

## Usage
Create a text file named movies.txt in the project directory. Each line of the file should contain the titles of the movies for which you want to fetch the scripts.

Run the script using the following command:

```shell
python fetch_scripts.py
```

The script will process the movies listed in the movies.txt file and fetch their scripts from IMSDb. The fetched scripts will be saved in a scripts directory within the project folder.

If you want to test the script without actually fetching the scripts, you can use the run=False parameter in the fetch_movie_script_text function.

After the script has finished processing, you will see either a success message indicating that all movies were processed successfully, or a message indicating the number of movies that failed to be processed. If there are any failures, a text file named failed_movies.txt will be generated, listing the titles of the movies that couldn't be processed.

## Examples
To fetch scripts for specific movies, simply add their titles to the movies.txt file. For example:

```
The Matrix
Inception
Pulp Fiction
```

Running the script will fetch the scripts for these movies and save them in the scripts directory.

Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
