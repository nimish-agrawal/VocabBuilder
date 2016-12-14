# Author: Nimish

"""
    A Python script that extracts definitions by getting results from www.dictionary.com

    It also keeps the words in a dictionary formatted text file, which can be used for revision

    The word is first looked up in the local cache, if not found, only then it goes online and googles it up

    Good for building up vocabulary

    Also, shows statistics about number of words you have in past x days

    Also, every time you use the script, after fetching the answer, you're given a definition, for which you have to
    give the word you searched earlier

    Uses Json for storing key-value pairs
"""

# UPDATE     : Included local dictionary lookup
# To be added: JSON, give_word_for_definition

########################################################################################################################

import urllib2
import sys
import random


# Returns the serial number of the last word
def get_counter(f):

    # Count number of lines; A list was used, since a file cannot be iterated more than once
    lines = []
    for each_line in f:
        lines.append(each_line)

    counter = len(lines)/2
    # print 'Last is ' + str(counter)
    return counter


# Builds dictionary.com URL for the desired word
def build_url(word):
    url = "http://www.dictionary.com/browse/" + word
    return url


# Adds the word and the definition to the local dictionary
def add_to_dictionary(f, word, definition):
    f.write(word.upper() + ' - ' + definition + '\n\n')
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
    random_number = 2 * random.randint(1, (counter - 1)) - 1
    i = 0
    it = ""
    # print random_number
    for each_line in fRead:
        i += 1
        if i == random_number:
            it = each_line
            break
    # print it
    fRead.close()
    return it


# Checks for the word in the local dictionary
def check_local(f, word):
    i = 0
    for each_line in f:
        i += 1
        if word.upper() in each_line:
            print
            print each_line
            it = each_line
            return it
    return ""


# Main
def __main__():
    try:
        f = open("dictionary.txt", 'a+')

        word = get_word()
        # First check locally

        # Used for making sure that the revision word and the searched words are different
        it = ""
        # it = check_local(f, word, it)[1]
        local_existence = check_local(f, word)

        f.close()
        f = open("dictionary.txt", 'a+')
        if local_existence:
            counter = get_counter(f)
            revision_word = display_random_word(counter)

            # Keep producing new revision words, until a new word is found
            while revision_word == it:
                f.close()
                f = open("dictionary.txt", "a+")
                counter = get_counter(f)
                revision_word = display_random_word(counter)

            print "Here is a word you searched for earlier:\n"
            print revision_word
            print "Happy learning!"
            exit()

        # If not in local, search online
        url = build_url(word)

        counter = get_counter(f)
        # print counter
        revision_word = display_random_word(counter)
        # print revision_word

        source = ""

        try:
            response = urllib2.urlopen(url)
            source = response.read()

        except urllib2.HTTPError:
            print "\nHey. That's no word!\n"
            print "Quitting"
            exit()


        source = source.lower()
        # print source
        def_in_source = "content=\"" + word
        # print def_in_source

        i = source.find(def_in_source)

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
        print "\nSome error occurred.\nTerminating."
        exit()

    finally:
        f.close()

if __name__ == '__main__':
    __main__()
