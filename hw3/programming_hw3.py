############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #3
#   Instructor: Pei-Yuan Wu
############################################

# Do not import any other library
import sys

# **********************************
# *  TODO                          *
# **********************************

# You may need this node class for implementation of tree.
class Node:
    def __init__(self, data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data

# This function is for checking if a sequence can be a preorder of BST or not.
# if yes, return the postorder traversal of the BST.
# if not, return '-'.
def preorder_check(input_string):               #preorder的case
    
    global result
    parse = input_string.split(',')
    result=[]
    root = Node(parse[0])                       #root基準

    for e in parse[1:]:                         #填入各個node ,建立tree 

        node = Node(e)                          #創建新node
        current = root
            
        while 1:                                #開始彈珠檯,找位置依規則填入
            if int(e)>int(current.data):        #如果大於
                if current.right!=None:
                    current = current.right
                else:
                    current.right=node
                    break

            elif int(e)<int(current.data):      #如果小於
                if current.left!=None:
                    current=current.left
                else:
                    current.left=node
                    break

    preorder(root)                              #認證preorder出來是不是跟原本一樣

    if result == parse:
        result=[]                               #重新算題目要求
        postorder(root)

        return ''.join(e+',' for e in result)[0:-1]
    else:
        return '-'

# This function is for checking if a sequence can be a postorder of BST or not.
# if yes, return the preorder traversal of the BST.
# if not, return '-'.
def postorder_check(input_string):         #postorder的case

        global result
        result=[]
        parse = input_string.split(',')

        def determintpost(parse):               #內函數
          
            subroot=Node(parse[-1])             #小次root case divid and conquer
            sublefttree=[]                      #子樹
            subrighttree=[]

            for e in parse:                     #左子樹
                if int(e)<int(parse[-1]):
                    sublefttree.append(e)
                else:                           #不符左子樹規則
                    start = parse.index(e)
                    break
                                                #看看能不能合法拆成左右兩子樹(小<root<大)
            for e in parse[start:-1]:           #右子數
                if int(e)>int(parse[-1]):
                    subrighttree.append(e)
                else:                           #不合
                    return False

            
            if(len(sublefttree)>0):             #直到base case
                r = determintpost(sublefttree)  #遞迴+
                
                if not r:                       #判斷是否合
                    subroot=False                    
                else:
                    subroot.left=r              #接上左子樹

            if(len(subrighttree)>0):
                r = determintpost(subrighttree)
                
                if not r:
                    subroot=False
                    
                else:
                    subroot.right=r

            return subroot                      #返回節點

        root = determintpost(parse)             #root的node
        
        if not root:
            return '-'

        else:
            preorder(root)
        
            return ''.join(e+',' for e in result)[0:-1]

result=[]

def preorder(current):                      #pre traversal

    result.append(current.data)
    if current.left != None:
        preorder(current.left)
    if current.right != None:
        preorder(current.right)

def postorder(current):                     #post traversal
    
    if current.left != None:
        postorder(current.left)
    if current.right != None:
        postorder(current.right)
    result.append(current.data)

# **********************************
# *  Do NOT modify the code below  *
# **********************************

if __name__ == '__main__':
    # 1. Check the command line arguments
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 programming_hw3.py <-pre | -post> <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[2], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)
    
    # 3. Solve
    if sys.argv[1] == '-pre':
        answer_list = [ preorder_check(s) for s in input_list ]
    elif sys.argv[1] == '-post':
        answer_list = [ postorder_check(s) for s in input_list ]
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[3], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()