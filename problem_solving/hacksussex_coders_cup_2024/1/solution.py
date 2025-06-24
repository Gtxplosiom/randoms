# You are given the arary paths, where paths[i] = [cityAi, cityBi] means
# there exists a direct path going from cityAi to cityBi. Return the
# distination city, that is, the city without any path outgoing to another city

# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city

# Example 1:
# Input: paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paolo"]]
# Output: "Sao Paulo"
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the
# destination city. Your trip consist of:
# "London" -> "New York" -> "Lima" -> "Sao Paulo".

# my solution
# an array has 0 = start and 1 = destination. so check for index 1s only. "blot out" index 0s
# so in short if a place with an index = 1 did not became a 0 = destination. it must be the destination

def solution(paths: list):
  compare = []
  destination = ""

  for i in range(len(paths)):
    compare.append(paths[i][0])

  for j in range(len(paths)):
    if paths[j][1] not in compare:
      destination = paths[j][1]
      break
  
  return destination

if __name__ == '__main__':
  paths_set = [
    [["A", "B"], ["B", "C"], ["C", "D"]],
    [["Berlin", "Munich"], ["Munich", "Vienna"], ["Vienna", "Prague"]],
    [["X", "Y"]],
    [["Red", "Blue"], ["Blue", "Green"], ["Green", "Yellow"], ["Yellow", "Purple"]],
    [["Tokyo", "Osaka"], ["Osaka", "Kyoto"], ["Kyoto", "Hiroshima"]],
    [["C", "D"], ["A", "B"], ["B", "C"]]
  ]

  for set in paths_set:
    print(solution(set))
