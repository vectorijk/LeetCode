# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. 
# A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#

#my version
class TrieNode(object):
    def __init__(self, cha):
        self.cha = cha
        self.children = [None] * 26
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rootNode = TrieNode('')

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        def dfs(word, idx, cur):
            if idx == len(word):
                return cur.isWord
            if word[idx] == '.':
                flag = False
                for nxt in cur.children:
                    if nxt is not None:
                        res = dfs(word, idx + 1, nxt)
                        flag = flag or res
                return flag
            else:
                nxt = cur.children[ord(word[idx]) - ord('a')]
                if nxt is None:
                    return False
                else:
                    return dfs(word, idx + 1, nxt)
        
        cur = self.rootNode
        return dfs(word, 0, cur)

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            if not c in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)
        
    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.leaves:
            return self.searchHelper(word, start+1, curr.leaves[word[start]])
        elif word[start] == '.':
            for c in curr.leaves:
                if self.searchHelper(word, start+1, curr.leaves[c]):
                    return True
       
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
