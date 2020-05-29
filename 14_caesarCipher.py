# Time: O(n) and space = O(n)
def caesarCipher(string, key):
    newKey = key % 26
    answer = []
    for char in string:
        newOrd = ord(char) + newKey
        if  newOrd <= 122:
            answer.append(chr(newOrd))
        else:
            answer.append(chr(96 + newOrd % 122))

    return "".join(answer)

print(caesarCipher("xyz", 2))
            
