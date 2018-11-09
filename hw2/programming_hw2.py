############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #2
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************

def solution(input_string):
    '''
    Modify this function
    1. Return the number (integer) of all possible ways 
       to divide input_string into n1, n2, ... , nk (0 <= ni <= 100).
    2. For example, given input_string '21005', you should return 4.
       '21005'  =>  '2,1,0,0,5'  => return 4
                    '21,0,0,5'
                    '2,10,0,5'
                    '2,100,5' 
    3. Feel free to add more functions.
    '''
    table={}
    def solution2(input_string):

        if input_string in table:               #lookup table
            return table[input_string]

        count=0

        #base case
        if int(input_string)==100 or (input_string[0]!='0' and len(input_string)==2) or len(input_string)==1:
            count+=1
            
        #嘗試3格
        if int(input_string[0:3])==100:
            count += solution2(input_string[3:])      #丟三格後的
        #嘗試2格
        if input_string[0]!='0' and len(input_string)>2:
            
            count += solution2(input_string[2:])      #丟兩格後的
        #嘗試1格
        if len(input_string)>1:
                count += solution2(input_string[1:]) #丟一格後的

        table[input_string]=count                   #lookup table

        return count

    return solution2(input_string)

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw2.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    answer_list = [ solution(s) for s in input_list ]
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()