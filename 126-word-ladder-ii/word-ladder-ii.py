class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        word_set=set(wordList)
        if endWord not in word_set:
            return []
        parents=defaultdict(list)
        current_layer=set([beginWord])
        if beginWord in word_set:
            word_set.remove(beginWord)
        found=False
        while current_layer and not found:
            next_layer=set()
            for word in current_layer:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch==word[i]:
                            continue
                        new_word=word[:i]+ch+word[i+1:]
                        if new_word in word_set:
                            next_layer.add(new_word)
                            parents[new_word].append(word)
                            if new_word==endWord:
                                found=True
            word_set-=next_layer
            current_layer=next_layer
        result=[]
        if found:
            def dfs(current_word,current_path):
                if current_word==beginWord:
                    result.append(current_path[::-1])
                    return
                for parent in parents[current_word]:
                    dfs(parent,current_path+[parent])
            dfs(endWord,[endWord])
        return result