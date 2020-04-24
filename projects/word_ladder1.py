# Given two words (begin_word and end_word), and a dictionary's word list, 
# return the shortest transformation sequence from begin_word to end_word, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
print(words)


# create a set of words, for easy lookup
words_set = set()
for word in words:
    words_set.add(word)


def neighbors(vertex):
    neighbors = []
    # for each letter in the word
    # list_of_chars = list(words):


def find_path(begin_word, end_word):
    visited = set()
    words_to_visited = Queue()
    words_to_visited.enqueue([begin_word])
    while words_to_visited.size() > 0:
        # remove the current vertex and path from queue
        path = words_to_visited.dequeue()
        current_word = path[-1]
        # make sure we havent visited this word
        if current_word not in visited:
            # add to visited
            visited.add(current_word)
            # check if this current word is our target
            if current_word == end_word:

