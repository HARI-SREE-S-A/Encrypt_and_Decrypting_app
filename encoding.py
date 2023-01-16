def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        print(enc)
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
