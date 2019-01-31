############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #5
#   Instructor: Pei-Yuan Wu
############################################

import sys
# **********************************
# *  TODO                          *
# **********************************

def SSort(lists):

  def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res = res + left + right
    return res

  if len(lists) <= 1:
    return lists
  mid = len(lists)//2
  left = SSort(lists[:mid])
  right = SSort(lists[mid:])
  return merge(left,right)

def solution(input_K, input_integer_set):
    '''
    Modify this function
    1. Return the minimum difference between maximum and minimum 
       of all possible K-element subsets.
    2. For example, given input_integer_set [13,24,1,44,15], you should return 9.
          input_set        possible_subset     difference        minimum difference 
       [13,24,1,44,15]  =>    [1,13,15]     =>      14       =>     return 11
                              [1,13,24]             23
                              [1,13,44]             43
                              [1,15,24]             23
                              [1,15,44]             43
                              [1,24,44]             43
                              [13,15,24]            11
                              [13,15,44]            31 
                              [13,24,44]            31
                              [15,24,44]            29         
    3. Feel free to add more functions.
    '''
    SORTED = SSort(input_integer_set)
    end = len(SORTED)
    minimum = 500
    index = input_K-1

    while index < end:
      temp = SORTED[index] - SORTED[index-(input_K-1)]
      if(temp) < minimum:
        minimum = temp
      index += 1
    return minimum

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw5.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()

    # 3. Solve
    input_k = int(input_list[0])
    input_set = input_list[1].split(',')
    input_set = [ int(s) for s in input_set ]
    answer = solution(input_k, input_set) 

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    outFile.write(str(answer))
    outFile.close()