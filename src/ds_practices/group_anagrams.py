def group_anagrams(strs):
    res = {}

    for i in strs:
        x = "".join(sorted(i))
        
        if x in res:
            res[x].append(i)
        else:
            res[x] = [i]
    return list(res.values())

# [['apple'], ['rope', 'pore'], ['cat', 'tac', 'atc']]
print(group_anagrams(["apple", "rope", "cat", "tac", "atc", "pore"]))