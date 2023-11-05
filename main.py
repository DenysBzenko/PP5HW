from ctypes import cdll, c_char_p, c_int, create_string_buffer


cipher_lib = cdll.LoadLibrary("D:\\KSE\\paradigm\\HW3PP\\Dll1\\x64\\Debug\\Dll1.dll")


cipher_lib.encrypt.argtypes = [c_char_p, c_int, c_char_p]
cipher_lib.decrypt.argtypes = [c_char_p, c_int, c_char_p]
cipher_lib.encrypt.restype = None
cipher_lib.decrypt.restype = None

def encrypt(data, key):
    buffer = create_string_buffer(len(data) + 1)
    cipher_lib.encrypt(data.encode('utf-8'), c_int(key), buffer)
    return buffer.value.decode('utf-8')

def decrypt(data, key):
    buffer = create_string_buffer(len(data) + 1)
    cipher_lib.decrypt(data.encode('utf-8'), c_int(key), buffer)
    return buffer.value.decode('utf-8')


