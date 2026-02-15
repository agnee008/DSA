def groupAnagrams(s):
    reverse_sorted = ["".join(sorted(i)) for i in s]
    hash = {}
    for i in range(len(reverse_sorted)):
        if reverse_sorted[i] in hash:
            hash[reverse_sorted[i]].append(s[i])
        else:
            hash[reverse_sorted[i]] = s[i]
    return list(hash.values())