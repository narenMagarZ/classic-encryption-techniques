from itertools import count
key = "monarchy"
# create 5*5 matrix 
table = [
    ['m','o','n','a','r'],
    ['c','h','y','b','d'],
    ['e','f','g','i','k'],
    ['l','p','q','s','t'],
    ['u','v','w','x','z']
    ]
plainText = input("Enter the plain text(only alphabet): ")
# create digram
def createDigram():
    digram = []
    i = 0
    c = 0
    for j in count(): # network # ballon #nnnnn
        if i+1 == len(plainText):
            digram.append(f'{plainText[i]}x')
            break
        if (i+1) > len(plainText):
            break
        if plainText[i] == plainText[i+1]:
            digram.append(f'{plainText[i]}x')
            i=i+1
            c = c + 1
            pass
        else:
            digram.append(plainText[i:i+2])
            i = i+2
            c = c + 2
    return digram



digram = createDigram()
print(digram)
def encrypt():
    cipher = ''
    for i in digram:
        l = i[0]
        r = i[1]
        lPos = [] #0=row,1=col
        rPos = []
        col = 0
        for row in range(len(table)):
            if len(lPos) == 2 and len(rPos) == 2:
                break
            for col in range(len(table[row])):
                if len(lPos) == 2 and len(rPos) == 2:
                    break
                val = table[row][col]
                if val == l:
                    lPos.append(row)
                    lPos.append(col)
                elif val == r:
                    rPos.append(row)
                    rPos.append(col)

        # check for same col
        if lPos[1] == rPos[1]:
            a = 0 if lPos[0] + 1 >= 5 else lPos[0] + 1
            b = 0 if rPos[0] + 1 >= 5 else rPos[0] + 1
            cipher += table[a][lPos[1]]
            cipher += table[b][rPos[1]]
        # check for same row
        elif lPos[0] == rPos[0]:
            a = 0 if lPos[1] + 1 >= 5 else lPos[1] + 1
            b = 0 if rPos[1] + 1 >= 5 else rPos[1] + 1
            cipher += table[lPos[0]][a]
            cipher += table[rPos[0]][b]
        else:
            cipher += table[lPos[0]][rPos[1]]
            cipher += table[rPos[0]][lPos[1]]
    return cipher

cipher = encrypt()
print(cipher)