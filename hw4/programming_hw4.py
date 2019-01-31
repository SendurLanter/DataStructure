###########################################
#   107-1 Data Structure and Programming
#   Programming Assignment #4
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************
'''
You need to complete this class MinBinaryHeap()
Feel free to add more functions in this class.
'''
class MinBinaryHeap():
    def __init__(self):
        self.heap = [0] # with a dummy node

    def balancing(self):

        size = self.size()

        def check(index):
            left = 2*index
            right = 2*index+1
            if left <= size and self.heap[index] > self.heap[left] :
                s=left
            else:
                s=index

            if right <= size and self.heap[s] > self.heap[right] :
                s=right

            if s!=index:
                temp = self.heap[index]
                self.heap[index] = self.heap[s]
                self.heap[s] = temp
                check(s)
            else:
                return

        check(1)

    def insert(self, item):
        # TODO #
        self.heap.append(item)
        
        index = self.size()

        while index!=1:
            if(self.heap[int(index/2)] > item):
                self.heap[index] = self.heap[int(index/2)]
                self.heap[int(index/2)] = item
                index = int(index/2)
            else:
                break
        self.balancing()
        return

    def deleteMin(self):
        # TODO #
        if(self.size()==0):
            return

        self.heap.pop(1)
        self.heap.insert(1,self.heap[-1])
        self.heap.pop(-1)

        '''while 1:          
            if 2*index <= self.size():               
                if self.heap[2*index] < self.heap[index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[2*index]
                    self.heap[2*index] = temp
                    index*=2
                    continue

                elif 2*index+1 <= self.size():

                    if self.heap[2*index+1] < self.heap[index]:
                        temp = self.heap[index]
                        self.heap[index] = self.heap[2*index+1]
                        self.heap[2*index+1] = temp
                        index = index*2 +1
                        continue
                    else:
                        break
                else:
                    break
            else:
                break'''
        self.balancing()
        return

    def findMin(self):
        # TODO #
        if self.size()!=0:
            return self.heap[1]

    def size(self):
        # TODO #
        return len(self.heap)-1
    
    def string(self):
        # Convert self.heap into a string
        return list2String(self.heap[1:])

def list2String(l):
    formatted_list = ['{}' for item in l ] 
    s = ','.join(formatted_list)
    return s.format(*l)

if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw4.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_line_list = list(inFile.read().splitlines())
    input_cmd_list = [ line.split(' ') for line in input_line_list ]
    inFile.close()

    # 3. Solve
    minPQ = MinBinaryHeap()
    findMin_list = []
    for cmd in input_cmd_list:
        if cmd[0] == 'insert':
            # print('insert {}'.format(cmd[1]))
            minPQ.insert(int(cmd[1]))
        elif cmd[0] == 'deleteMin':
            # print('deleteMin')
            if minPQ.size() > 0:
                minPQ.deleteMin()
        elif cmd[0] == 'findMin':
            # print('findMin')
            if minPQ.size() > 0:
                findMin_list.append(minPQ.findMin())
            else:
                findMin_list.append('-')
        else: # Unknown command
            assert False
        # print(minPQ.string())
    
    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    # 4.1 Output FindMin string
    outFile.write('{}\n'.format(list2String(findMin_list)))
    # 4.2 Output minPQ string
    outFile.write('{}'.format(minPQ.string()))
    outFile.close()