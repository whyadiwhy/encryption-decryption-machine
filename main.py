def adi_machine():
    keys = 'abcdefgjhijklmnopqrstuvwxyz !'
    values = keys[-1]+ keys[0:-1]
    
    encryptDict = dict(zip(keys,values))
    decryptDict = dict(zip(values,keys))
    message = input("Please enter your secret message: ")
    mode = input("Please input the mode: Encode(E) or Decode(D) ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else:
        print("Please Enter a correct Choice")

    return newMessage
print(adi_machine())

