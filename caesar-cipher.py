

key = 3

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

table = dict()

def setTable():
    for i in range(len(alphabets)):
        table[alphabets[i]] = i

setTable()
print(table)
def encrypt():
    plainText = input("Enter the plain text(only alphabet): ")
    plainText = plainText.lower()
    cipherText = ""
    for lt in plainText:
        if lt != ' ':
            index = (table[lt] + key) % 26
            cipherText += alphabets[index]
    return cipherText

    
def decrypt(cipherText):
    pass


cipherText = encrypt()
print(cipherText)