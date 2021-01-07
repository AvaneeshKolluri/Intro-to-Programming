'''

I pledge my honor that I have abided by the Stevens Honor system.
'''

class Board(object):
    
    def __init__(self,width = 7,height = 7):
        self.width = width
        self.height = height
        self.data = [[" " for x in range(width)] for x in range(height)]

    def __str__(self):
        ss = ''
        for z in self.data:
            for a in z:
                ss += '|' + a
            ss += '|\n'
        ss += '-' * (self.width*2 +1) + '\n'
        for sm in range(self.width):
            ss += " "+ str(sm)
        return ss

    def allowsMove(self,col):
        if not ((col < self.width) and col> -1):
            return False
        some_space = 0
        for item in range(self.height):
            if self.data[item][col] == " ":
                some_space += 1
            else:
                pass
        return some_space > 0

    def addMove(self,col,ox):
        if self.allowsMove(col):
            for item in range(self.height):
                if self.data[item][col] != ' ':
                    self.data[item-1][col] = ox
                    return
            self.data[self.height-1][col] = ox

    def setBoard(self,move_string):
        val = 'X'
        for item in move_string:
            val_Col = int(item)
            if 0 <= val_Col < self.width:
                self.addMove(val_Col,val)
            if val == 'X':
                val = 'O'
            else:
                val = 'X'

    def delMove(self,col):
        if (col< self.width) and (col>-1):
            for hcol in range(self.height):
                if self.data[hcol][col] != ' ':
                    self.data[hcol][col] = ' '
                    return

    def winsFor(self,ox):
        def reverse(d):
            ret = []
            for row in d:
                nrow = []
                for val in reversed(row):
                    r.append(val)
                ret.append(nrow)
            return ret

        def diagonal(d, width, height):
            for diagonal in range(height + width - 1):
                counter = 0
                for w in range(width):
                    h = diagonal - w
                    if h <= 0:
                        break
                    if diagonal > width - 1:
                        if not w <= diagonal - width:
                            if d[w][h] == ox:
                                counter += 1
                                if counter > 3:
                                    return True
                            else:
                                counter = 0
                    else:
                        if d[w][h] == ox:
                            counter += 1
                            if counter > 3:
                                return True
                        else:
                            counter = 0
            return False


            for col in range(self.width):
                counter = 0
                for row in range(self.height):
                    if self.data[row][col] == ox:
                        counter += 1
                        if counter > 3:
                            return True
                    else:
                        counter = 0
            for row in range(self.height):
                counter = 0
                for col in range(self.width):
                    if self.data[row][col] == ox:
                        counter += 1
                        if counter > 3:
                            return True
                    else:
                        counter = 0
        return diagonal(self.data,self.width,self.height) or diagonal(reverse(self.data),self.width,self.height)

    def hostGame(self):
        print("Welcome to Connect Four!")
        value = 'O'
        while True:
            if self.winsFor(value):
                print(value + "wins -- Congratulations!")
                print(self)
                break
            if value == "O":
                value = "X"
            else:
                value = "O"
            print(self)
            move = int(input(value + "'s choice: "))
            if not self.allowsMove(move):
                print("\n")
                continue
            print("\n")
            self.addMove(move, value)

                    
if __name__ == '__main__':
    b = Board( 7, 6 )
    b.hostGame()

        
