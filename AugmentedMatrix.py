"""algorithm for solving system of linear equations using RREF assuming the following:
    A system (matrix) is represented as a list of rows:
    __    __
    |  R1  |
    |  R2  |
    |  R3  |
..
    |  RN  |
    |_    __

1 row is 1 equation in a system of linear equations
1 row represented as list of coefficients (left+right of equal sign)
example: 2x -3y = 5 will be turned into 
    r = [2, -3 ,5]
    len(r) - 1  = number of variables 
    len(r) = num columns
"""    
class AugmentedMatrix:
    # 2D list: list of rows (or list of ri where ri is list of coefficients)
    # [r1, r2, .., rn]
    # len(rows) = number of equations in system   
    # rows represents augmented matrix
    def __init__(self, rows):
        self.numEquations = len(rows)
        self.numVariables = len(rows[0])-1
        self.rows = rows
        if not self.isValid():
            raise Exception("not a valid matrix, must input a 2d grid represented as list of list of numbers")
        
    
    def isValid(self):
        #checks wheter or not self.rows is a rectangular 2d array (each row must have the same number of columns)
        for i in range(1,len(self.rows)):
            if len(self.rows[i])!=len(self.rows[0]):
                return False
        return True
        
    def getConstantMatrix(self):
        #constant matrix is last column (rightmost column) of 2D grid
        return [row[len(row)-1] for row in self.rows]

    #ELEMENTARY ROW OPERATIONS ON AUGMENTED MATRIX: 
    def swapRows(self, i, j):
        #modifies self.rows
        print("swapping row "+str(i)+" and "+str(j))
        temp = [c for c in self.rows[i]]
        for x in range(len(self.rows[i])):
            self.rows[i][x] = self.rows[j][x]
            self.rows[j][x] = temp[x]
    
    def multiplyRow(self, r, s):
        if s==0:
            raise Exception("cannot multiply row by 0")
        #multiplies every entry of self.rows[r] by s
        print("multiplying row "+str(r)+" by "+str(s))
        for i in range(len(self.rows[r])):
            self.rows[r][i] *= s
    
    def addRows(self, r1, r2):
        # r1 += r2, self.rows[r1] is changed
        print("adding row "+str(r2)+" into row "+str(r1))
        for i in range(len(self.rows[r1])):
            self.rows[r1][i] += self.rows[r2][i]
    
    def printMatrix(self):
        print(self.rows)
    
    def solve(self):
        # perform RR (row reduction) algorithm on augmented matrix and return solution
        # solution is the constant matrix of the augmented matrix once the RR algorithm terminates 
        # sol is of the form: [s1, s2, .., sn]
        print("performing row reduction to augmented matrix...")
        while not self.rows.isRowReduced():
            printMatrix()
            #TODO iteratively modify self.rows until it is row reduced
        return getConstantMatrix()      
    
    def isRowReduced(self):
        #TODO
        return False

rows = [[2, -3, 5],[1, 2, -4]]
m1 = AugmentedMatrix(rows)


#m1.solve()
#print(m1.getConstantMatrix())

m1.printMatrix()
m1.swapRows(0, 1)
m1.printMatrix()
m1.addRows(0, 1)
m1.printMatrix()
m1.multiplyRow(0, 2)
m1.printMatrix()
