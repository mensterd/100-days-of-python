from bs4 import BeautifulSoup
import requests

# Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/


response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, features="html.parser")

article_texts = []


articles = soup.find_all("span", class_="titleline")
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)


# As List comprehension
scores = [score.getText() for score in soup.find_all(name="span", class_="score")]
# Create List of Integers
int_scores = [int(score.split()[0]) for score in scores]


# print(int_scores)

# Find largest amount upvotes and get the index of it
largest_number = max(int_scores)
index = int_scores.index(largest_number)
print(largest_number, index)

# print article with largest amount upvotes
print(article_texts[index])

FILE_NAME = "movies.txt"

def write_to_file(movie_list:list)->bool:
    try:
        with open(FILE_NAME, "w") as f:
            for line in movie_list:
                f.write(line + "\n")
        return True
    except Exception as e:
        print(f"Something went wrong: {e}")
        f.close()
        return False




def hundred_movies():
    response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
    movies = response.text
    soup = BeautifulSoup(movies, features="html.parser")

    movie_list = []
    # movies = soup.find_all("h3", class_="title")
    movies = soup.find_all("img", class_="landscape")
    for movie in movies:
        title = movie.get("title")
        movie_list.append(title)

    # Reverse the list so that 1 is on top and 100 on bottom
    movie_list.reverse()
    # Edit the 58th element for testing purposes. This title had an invalid character in it's name
    movie_list[58] = "59) E.T. The Extra Terrestrial"
    print(movie_list)
    write_to_file(movie_list)


    












hundred_movies()

# tester = ["Dimitrie", "Mennings"]
# write_to_file(tester)