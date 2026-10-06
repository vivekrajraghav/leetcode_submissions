class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        my_set=set(wordList)
        queue=deque()
        level=1
        queue.append((beginWord,level))
        while len(queue)!=0:
            curr_word,level=queue.popleft()
            if curr_word==endWord:
                return level
            for i in range(len(curr_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c==curr_word[i]:
                        continue
                    new_word=curr_word[:i]+c+curr_word[i+1:]
                    if new_word in my_set:
                        queue.append((new_word,level+1))
                        my_set.remove(new_word)
        return 0