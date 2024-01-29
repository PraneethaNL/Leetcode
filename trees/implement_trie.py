#QUESTION:

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
#ALGO:

# I have used a list here to implement the trie

class Trie:

    def __init__(self):
        self.trie=[]
        

    def insert(self, word: str) -> None:
        self.trie.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:

        length=len(prefix)

        for w in self.trie:
            if len(w)>=length and prefix in w[:length]:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)