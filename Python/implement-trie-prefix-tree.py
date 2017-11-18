# Time:  O(n), per operation
# Space: O(1)
#
# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#


# my version
class TrieNode(object):
    def __init__(self, cha):
        self.cha = cha
        self.children = [None] * 26
        self.isWord = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rootNode = TrieNode('')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.rootNode
        for w in word:
            if cur.children[ord(w) - ord('a')] is None:
                tmp = TrieNode(w)
                cur.children[ord(w) - ord('a')] = tmp
                cur = tmp
            else:
                cur = cur.children[ord(w) - ord('a')]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.rootNode
        for w in word:
            if cur.children[ord(w) - ord('a')] is None:
                return False
            else:
                cur = cur.children[ord(w)-ord('a')]
                
        return cur.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.rootNode
        for w in prefix:
            if cur.children[ord(w) - ord('a')] is None:
                return False
            else:
                cur = cur.children[ord(w)-ord('a')]
        return cur != None



class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.childSearch(prefix) is not None

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
