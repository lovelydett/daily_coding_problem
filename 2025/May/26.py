'''
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string "de" and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

from typing import List

class Trie:
    class Node:
        __slots__ = ["children", "is_end"]
        def __init__(self):
            self.children = {}
            self.is_end = False
    
    def __init__(self):
        self.root = Trie.Node()
    
    def insert(self, word: str):
        cur = self.root
        for ch in word:
            cur = cur.children.setdefault(ch, Trie.Node())
        
        cur.is_end = True
    
    def getStartsWith(self, prefix: str) -> List[str]:
        cur: Trie.Node = self.root
        for ch in prefix:
            cur = cur.children.get(ch)
            if not cur:
                break
        
        res: List[str] = []
        def dfs(word: str, node: Trie.Node):
            nonlocal res
            if node.is_end:
                res.append(word)
            for ch, child in node.children.items():
                dfs(word + ch, child)

        dfs(prefix, cur)
        return res

def solution(prefix: str, words: List[str]):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    return trie.getStartsWith(prefix)
    

if __name__ == "__main__":
    prefix = "de"
    words = ["dog", "deer", "deal"]

    print(solution(prefix, words))
