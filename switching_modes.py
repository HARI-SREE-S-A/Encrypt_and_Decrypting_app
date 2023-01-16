def moode():
    m = vari.get()
    if m == 'Encode':
        result.set(encode(p_key.get(), Text.get()))
    else:
        result.set(Decode(p_key.get(), Text.get()))
        
