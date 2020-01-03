from bs4 import BeautifulSoup
import requests
import random
import string
import sys

letters = [char for char in string.ascii_lowercase]
probs = [
    0.059927035685846036,
    0.06883460804829719,
    0.13853960258523307,
    0.07685327506064928,
    0.023037463656734383,
    0.0773718031815404,
    0.06574195818441082,
    0.008148299042574863,
    0.035778440341487805,
    0.0002777829219059612,
    0.0,
    0.053315802144484156,
    0.06357525139354432,
    0.022741161873368027,
    0.0150373155058427,
    0.040797051797255506,
    5.555658438119224e-05,
    0.03274134706198263,
    0.13333580251486138,
    0.06720494823978222,
    0.013833589510916868,
    0.0021111502064853054,
    0.0,
    0.000537046982351525,
    5.555658438119224e-05,
    0.00014815089168317933
 ]

def write_random_word_file():
    ''' Get a random word and save to a txt file '''
    word = get_random_definition()
    with open('irish_word.txt', 'w+') as word_file:
        word_file.write(word)


def interactive_main():
    '''Random word or search for -t and word'''
    if '-t' in sys.argv:
        word_to_trans = sys.argv[2]
        translate_word(word_to_trans)
    else:
        word = get_random_definition()
        print(word)


def get_random_definition():
    '''Get a random irish word and its definition'''
    word = get_random_word()
    definition = get_translation(word)
    return definition


def get_random_word():
    """
    Get a random word from http://www.teanglann.ie
    in Irish. Uses a cumulative probability distribution
    based on the number of entries for each letter.

    Args:
        None

    Returns:
        A string of a random Irish word without translation
    """
    letter = random.choices(letters, probs)[0]

    # Cumulative Probability Based on Num of Dictionary entries

    website = 'https://www.teanglann.ie/en/fgb/_' + letter
    result = requests.get(website)
    soup = BeautifulSoup(result.content, 'html.parser')
    samples = soup.find_all('span', class_="abcItem")
    word = random.choice(samples)
    return word.a.text


def translate_word(word):
    translation = get_translation(word)
    
    if not translation:
        print('No translation found for %s' % word)
    else:
        print(translation)


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
    trans = word_page.find_all('div', class_='entry')
    all_trans = []
    for tran in trans:
        if '=' in tran.text:
            word = tran.text.split('=')[-1]
            word = ''.join(filter(str.isalpha, word))
        all_trans.append(tran.text)
        
    trans = ' '.join(all_trans)
    if '=' in trans:
        trans += "(AUTOSEARCH) " + get_translation(word)
    
    return trans


def get_num_entries(letter):
    """
    Get number of entries that start with `letter`
    in https://www.teanglann.ie.

    Args:
        str: first letter of entries to count

    Returns:
        int: number of entries

    """
    website = 'https://www.teanglann.ie/en/fgb/_' + letter
    result = requests.get(website)
    soup = BeautifulSoup(result.content, 'html.parser')
    samples = soup.find_all('span', class_="abcItem")
    return len(samples)


if __name__ == "__main__":
    interactive_main()
