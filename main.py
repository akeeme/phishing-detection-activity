import json
from textblob import TextBlob

'''
    this function should return a count of the number 
    of words in the string that are in the phishing_words list
'''
def check_for_word(string):
    phishing_words = ['click', 'clicking', 'link', 'account', 'confirm', 'confirming', 'update', 'updating', 'security', 'bank', 'password', 'login', 'verify', 'secure', 'transaction', 'alert',
                      'online', 'bill', 'payment', 'service', 'information', 'personal', 'card', 'activity', 'statement', 'transfer', 'fraud', 'transaction', 'alert', 'fraud']
    pass

'''
    this function checks if the string contains a link
    then returns true if it contains, false if it doesn't
'''
def check_for_link(string):
    pass

'''
    this function uses a function in the textblob package to check for misspellings in a string
    textblob documentation is listed here -> https://textblob.readthedocs.io/en/dev/
'''
def check_for_misspellings(string):
    pass

'''
    this function will use all the helper functions we've implemented 
    inside conditionals (if else statements) to determine if a given email is phishing
'''
def determine_if_phishing(email):
    pass


def main():
    emails = json.load(open('emails.json'))

    for email in emails:
        determine_if_phishing(email)


if __name__ == '__main__':
    main()
