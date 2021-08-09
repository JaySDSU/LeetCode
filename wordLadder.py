# add beginWord to queue,(bfs), traverse each char of beginWord and create all possible newWord from it, if newWord is present in wordList
# we add newWord and length+1 to queue as it differs only by one char and isPresent in wordList 

import collections

def wordLadder(beginWord, endWord, wordList):
    wordList = set(wordList)
    
    if not beginWord or not endWord or (endWord not in wordList):
        return 0
   
    que = collections.deque()
    que.append([beginWord,1])
    
    while que:
        word, length = que.popleft()
        if word == endWord:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordList:
                    wordList.remove(new_word)
                    que.append([new_word, length+1])
        
    return 0
        
s1 = 'hit'
s2 = 'cog'
l1 = ["hot","dot","dog","lot","log","cog"]

print(wordLadder(s1,s2,l1))