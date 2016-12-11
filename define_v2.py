# Author: Nimish

"""
    A Python script that extracts definitions by getting results from www.dictionary.com
    It also keeps the words in a dictionary formatted text file, which can be used for revision
    The word is first looked up in the local cache, if not found, only then it goes online and googles it up
    Good for building up vocabulary
    Also, shows statistics about number of words you have in past x days
    Also, every time you use the script, after fetching the answer, you're given a definition, for which you you have to give the word you searched earlier
    Uses Json for storing key-value pairs
"""

# To be added: JSON, local lookup, give_word_for_definition

########################################################################################################################

import urllib2
import sys
import random


# Gets counter from header and increments it by 1
def update_counter(f):
    counter = f.readline()
    # print counter
    for line in f:
        # print line
        line.replace(counter, str(int(counter) + 1))
        break
    return int(counter)


# Builds dictionary.com URL for the desired word
def build_url(word):
    url = "http://www.dictionary.com/browse/" + word
    return url


# Adds the word and the definition to the local dictionary
def add_to_dictionary(f, word, definition):
    f.write('@' + word.upper() + ' - ' + definition + '\n\n')
    f.close()
    return


# Gets the word from command line argument and returns it
def get_word():
    args = sys.argv
    word = args[1]
    # word = word[0].capitalize() + word[1:]
    return word


# Displays a random word and its definition for revision
def display_random_word(counter):
    fRead = open("dictionary.txt", 'r')
    random_number = 2 * random.randint(1, (counter - 1) / 2) + 1
    i = 0
    it = ""
    # print random_number
    for each_line in fRead:
        i += 1
        if i == random_number:
            it = each_line[1:]
            break
    # print it
    fRead.close()
    return it


# Main
def __main__():
    try:
        f = open("dictionary.txt", 'a+')

        word = get_word()
        url = build_url(word)

        counter = update_counter(f)
        revision_word = display_random_word(counter)
        # print revision_word

        response = urllib2.urlopen(url)
        # print type(response)
        source = response.read()
        source = source.lower()
        # print source
        def_in_source = "content=\"" + word
        # print def_in_source

        i = source.find(def_in_source)
        if i == -1:
            print "Cannot find that word!\n"
            print "Quitting!\n"
            exit()
        j = source.find(def_in_source, i + 10)
        i = j
        # print 'i is ' + str(i)

        definition_start = i + 9 + len(word) + 13
        definition_end = definition_start + (source[i + 9 + len(word) + 13:]).find('.')
        # print definition_start
        # print definition_end
        definition = source[definition_start:definition_end]
        print
        print word.upper() + ' - ' + definition

        add_to_dictionary(f, word, definition)

        print "\nHere is a word you searched for earlier:\n"
        print revision_word
        print 'Happy learning!'

    except IOError as e:
        print str(e)
        print "\nSome error occurred.\nTeminating."
        exit()


if __name__ == '__main__':
    __main__()
