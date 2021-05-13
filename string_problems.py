# idea is, we will sort each string in list of strings and store in mapping as a key, it's value will
# be list having it's anagrams

def groupAnagrams(strings):
    mapping = {}

    for string in strings:
        stringSorted = "".join(sorted(string))

        if stringSorted in mapping:
            mapping[stringSorted].append(string)
        else:
            mapping[stringSorted] = [string]

    for key in mapping:
        print(key, "\t", mapping[key])

