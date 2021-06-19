def encrypt(Alphabets,shift,message):

    if shift > 25:
        shift = shift % 25

    enc_msg = ""

    for i in range( len(message)):

        to_find = message[i]
        j = 0

        while  j < 26:
            if Alphabets[j] == to_find:
                position = j
                break
            j+=1

        if j > 25:
            enc_msg += message[i]
            continue

        position += shift

        if position > 25:
            position -= 25

        enc_msg += Alphabets[position]

    return enc_msg



def decrypt(Alphabets,shift,message):

    if shift > 25:
        shift = shift % 25

    dec_msg = ""

    for i in range( len(message)):

        to_find = message[i]
        j = 0

        while  j < 26:
            if Alphabets[j] == to_find:
                position = j
                break
            j+=1

        if j > 25:
            dec_msg += message[i]
            continue

        position -= shift

        if position < 0 :
            position += 25

        dec_msg += Alphabets[position]

    return dec_msg


Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


message = input("Enter the message(in small Characters(a-z)): ")
choice = input("Type 'Encrypt' to encrypt or 'Decrypt' to decrypt The message: ")
shift = int(input("Enter the key: "))

choice = choice.lower()

if choice == "encrypt":
    encoded_msg = encrypt(Alphabets, 9, message.lower())
    print("Encrypted message is : " + encoded_msg)
elif choice == "decrypt" :
    decoded_msg = decrypt(Alphabets, 9, message)
    print(decoded_msg)
else:
    print("Give the required inputes properly")


