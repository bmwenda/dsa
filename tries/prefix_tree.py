"""Retrieval of a key in a dataset of string
It's a combination hashmaps and trees
use cases:
 - autocomplete
 - word search
 - spell checker
 - ip routing (longest prefix matching)
"""

# operation     average     worst
# search          O(n)        O(n)
# insert          O(n)        O(n)
# delete          O(n)        O(n)

# space: O(n)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
