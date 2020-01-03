''' Get a random word and then send to feed'''
import words
import requests
import os


def post_word(feed_url):
    ''' Sends a word to the feed_url '''
    word = words.get_random_definition()
    response = requests.post(feed_url, data=word.encode('utf-8'))
    print("Request response: \n%s" % response)


if "__main__" == __name__:
    base_url = r"https://notify.run"
    feed_url = r"%s/%s" % (base_url, os.environ['IRISH_WORD_FEED'])

    print("Attempting to post word to feed @ '%s'" % feed_url)
    post_word(feed_url)
    