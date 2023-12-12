# Function to count the frequency of words in a given list of words
def count_word_frequency(words):
    myDict = {}
    for i in range(len(words)):
        myDict[words[i]] = words.count(words[i])

    return myDict

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
myDict = count_word_frequency(words)
print(myDict)

# Time Complexity: O(n)
# Space Complexity: O(n)