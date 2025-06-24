# Check if one string swap can make strings equal
# You are given two strings s1 and s2 of equal length. A string swap is an operation 
# where you choose two indices in a string (not necessarily different)
# and swap the characters at these indices

# Return true if is possible to make both strings equal by performing at most
# one string swap on exactly one of the strings. Otherwise, return false.

# Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap
# the first character with the last
# character of s2 to make "bank"

def solution(word_1: str, word_2: str):
  word1_list = []
  word2_list = []

  for c in word_1:
    word1_list.append(c)

  for c in word_2:
    word2_list.append(c)

  for i in range(len(word2_list)):
    for j in range(len(word2_list)):
      if word2_list[i] == word2_list[j]:
        pass
      else:
        word2_list[i], word2_list[j] = word2_list[j], word2_list[i]
      if word2_list == word1_list:
        return True
      else:
        word2_list[i], word2_list[j] = word2_list[j], word2_list[i]
  return False

if __name__ == '__main__':
  compare = [
      ["bank", "kanb"],
      ["ab", "ba"],    
      ["abcd", "abdc"],
      ["aabb", "bbaa"],
      ["abc", "abc"],  
      ["ab", "cd"],    
      ["abcd", "dcba"],
      ["abc", "cab"],
      ["aa", "bb"],
      ["abc", "def"],
      ["aaaa", "aaab"],
      ["aa", "aa"],
      ["abab", "abab"],
      ["abcde", "edcba"],
      ["aabc", "aacb"]
  ]

  for i, j in compare:
    print(solution(i, j))