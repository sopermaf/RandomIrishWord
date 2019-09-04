from bs4 import BeautifulSoup
import requests
import random
import string

def get_random_word():
    """
    Get a random word from http://www.teanglann.ie
    in Irish.

    Args:
        None

    Returns:
        A string of a random Irish word
    """
    letter = random.choice(string.ascii_letters).lower()
    website = 'https://www.teanglann.ie/en/fgb/_' + letter
    result = requests.get(website)
    soup = BeautifulSoup(result.content, 'html.parser')
    samples = soup.find_all('span', class_="abcItem")
    word = random.choice(samples)
    return word.a.text

def get_translation(word):
    """
    Get the translation of a given `word`
    from http://www.teanglann.ie

    Args:
        word - str of Irish word

    Returns:
        Str of dictionary entry
    """
    link = "https://www.teanglann.ie/en/fgb/" + word
    word_result = requests.get(link)
    word_page = BeautifulSoup(word_result.content, 'html.parser')
    #trans = word_page.find_all('span', class_='trans')
    trans = word_page.find_all('div', class_='entry')
    all_trans = []
    for tran in trans:
        all_trans.append(tran.text)
    return ' '.join(all_trans)

if __name__ == "__main__":
    word = get_random_word()
    print(get_translation(word))