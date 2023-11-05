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

class CaesarCipherCLI:
    def __init__(self):
        self.data = ""
        self.key = 0
        self.operation = ""
        self.result = ""

    def read_data(self, method):
        if method == "1":
            file_name = input("Enter file name: ")
            self.data = self.read_from_file(file_name)
        elif method == "2":
            self.data = input("Enter encryption/decryption: ")
        else:
            raise ValueError("Invalid input .")

    def read_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return None

    def write_to_file(self, file_name, data):
        try:
            with open(file_name, 'w') as file:
                file.write(data)
            print(f"Result saved to '{file_name}'.")
        except Exception as e:
            print(f"Error: {e}")

    def set_key(self):
        self.key = int(input("Enter key (shift amount): "))

    def set_operation(self):
        self.operation = input("Select the operation encrypt or decrypt: ")
        if self.operation not in ['encrypt', 'decrypt']:
            raise ValueError("Invalid operation.")

    def process_data(self):
        if self.operation == 'encrypt':
            self.result = encrypt(self.data, self.key)
        elif self.operation == 'decrypt':
            self.result = decrypt(self.data, self.key)

    def output_result(self):
        output_file_name = input("Enter a file name to save the result or result in console (enter): ")
        if output_file_name:
            self.write_to_file(output_file_name, self.result)
        else:
            print("Result:", self.result)

