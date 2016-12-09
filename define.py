<<<<<<< HEAD
# A Python script that extracts definitions and their usage by getting results from www.dictionary.com
# It also keeps the words in a dictionary formatted text file, which can be used for revision
# The word is first looked up in the local cache, if not found, only then it goes online and googles it up
# Good for building up vocabulary
# Also, shows statistics about number of words you have in past x days
# Also, every time you use the script, after fetching the answer, you're asked to define a word from your past searches
# Uses Json for storing key-value pairs

import urllib2
import sys
import io

def build_url(word):
    url = "http://www.dictionary.com/browse/" + word
    return url

def add_to_dictionary(f, word, definition):
    f.write('@' + word.upper()+' - '+definition + '\n\n')
    f.close()
    return

def get_word():
    args = sys.argv
    word = args[1]
    # word = word[0].capitalize() + word[1:]
    return word

try:
    f = open("dictionary.txt", 'a+')

    word = get_word()
    url = build_url(word)

    response = urllib2.urlopen(url)
    # print type(response)

    source = response.read()
    source = source.lower()
    # print source

    def_in_source = "content=\"" + word
    # print def_in_source

    i = source.find(def_in_source)
    j = source.find(def_in_source, i+10)
    i = j
    # print 'i is ' + str(i)

    definition_start = i+9+len(word)+13
    definition_end = definition_start + (source[i+9+len(word)+13:]).find('.')
    # print definition_start
    # print definition_end

    print
    definition = source[definition_start:definition_end]
    print word.upper() + ' - ' + definition
    add_to_dictionary(f, word, definition)

except Exception as e:
    # print str(e)
=======
# A Python script that extracts definitions and their usage by getting results from www.dictionary.com
# It also keeps the words in a dictionary formatted text file, which can be used for revision
# The word is first looked up in the local cache, if not found, only then it goes online and googles it up
# Good for building up vocabulary
# Also, shows statistics about number of words you have in past x days
# Also, every time you use the script, after fetching the answer, you're asked to define a word from your past searches
# Uses Json for storing key-value pairs

import urllib2
import sys

try:
    args = sys.argv
    word = args[1]

    # word = "absorb"
    word = word[0].capitalize() + word[1:]

    url = "http://www.dictionary.com/browse/" + word

    response = urllib2.urlopen(url)
    # print type(response)

    source = response.read()
    # print source

    def_in_source = "content=\"" + word
    # print def_in_source

    i = source.find(def_in_source)
    # print i

    definition_start = i+9+len(word)+13
    definition_end = definition_start + (source[i+9+len(word)+13:]).find('.')
    # print definition_start
    # print definition_end

    print
    print source[definition_start:definition_end]
except Exception as e:
    print
>>>>>>> 933c344c69b554c292ed8846a6b1622a944ef078
    print "Can't find that word!"