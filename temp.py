def boj1316():
    ans = 0
    for _ in range(int(input())):
        words = input()
        words_set = set(list(words))
        words_dict = dict(zip(words_set, [0] * len(words_set)))
 
        # if len(words) == len(words_set):
        #     ans += 1
        
        for i in range(len(words) - 1):
            words_dict[words[i]] += 1
            if words[i] == words[i + 1]:
                words_dict[words[i]] -= 1
            else:
                pass
            if words_dict[words[i]] > 1:
                
                break
            else:
                pass
            ans += 1    
    print(ans)


if __name__ == "__main__":
    boj1316()