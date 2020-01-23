'''
Pomocnicze funkcje do szyfrowania i deszyforowania napisów
'''
__ch_a,__ch_A,__ch_z,__ch_Z = ord('a'),ord('A'),ord('z'),ord('Z')
__alp_len = __ch_z - __ch_a + 1
from itertools import cycle

def password_to_key(password):
    key = []
    for ch in [ord(c) for c in password.lower()]:
        if ch >= __ch_a and ch <= __ch_z:
            key.append(ch - __ch_a)
    return cycle(key)

def simple_encoder(raw_string,password):
    encoded_string = ''
    key = password_to_key(password)
    for ch in [ord(c) for c in raw_string]:
        if ch >= __ch_a and ch <= __ch_z: # Małe litery
            ch += next(key)
            if ch > __ch_z:
                ch -= __alp_len
        elif ch >= __ch_A and ch <= __ch_Z: # Wielkie litery
            ch += next(key)
            if ch > __ch_Z:
                ch -= __alp_len
        encoded_string += chr(ch)
    return encoded_string

def simple_decoder(encoded_string,password):
    raw_string = ''
    key = password_to_key(password)
    for ch in [ord(c) for c in encoded_string]:
        if ch >= __ch_a and ch <= __ch_z: # Małe litery
            ch -= next(key)
            if ch < __ch_a: ch += __alp_len
        elif ch >= __ch_A and ch <= __ch_Z: # Wielkie litery
            ch -= next(key)
            if ch < __ch_A: ch += __alp_len
        raw_string += chr(ch)
    return raw_string
