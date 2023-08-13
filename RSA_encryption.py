import random # Import the random module to generate random numbers for the public and private keys
import math # Import the math module to gcd function to check if a number is coprime with another number

def is_prime(num): # Check if a number is prime
    if num == 2: # 2 is the only even prime number
        return True # 2 is prime
    if num < 2 or num % 2 == 0: # If the number is less than 2 or even, it is not prime
        return False # The number is not prime
    for n in range(3, int(num ** 0.5) + 2, 2): # Check if the number is divisible by any odd number from 3 to the square root of the number
        if num % n == 0: # If the number is divisible by any odd number from 3 to the square root of the number, it is not prime
            return False # The number is not prime
    return True # The number is prime

def pick_random_prime(): # Pick a random prime number
    while True:
        num = random.randint(1000, 10000) # 4 digit prime number
        if is_prime(num): # Check if the number is prime
            return num # Return the prime number

def set_keys(): # Set the public and private keys
    prime1 = pick_random_prime() # Pick a random prime number
    prime2 = pick_random_prime() # Pick another random prime number

    print("Picking two random prime numbers.......") # Print the prime numbers
    print("Prime 1:", prime1) 
    print("Prime 2:", prime2)
    print("\n")

    n = prime1 * prime2 # Calculate n
    fi = (prime1 - 1) * (prime2 - 1) # Calculate torsion

    e = 2 # Pick a random number between 1 and fi
    while True:
        if math.gcd(e, fi) == 1: # Check if the number is coprime with fi
            break # If the number is coprime with fi, stop
        e += 1 # If the number is not coprime with fi, pick another number

    public_key = e # Set the public key

    d = 2 # Pick a random number between 1 and fi
    while True:
        if (d * e) % fi == 1: # Check if the number is the multiplicative inverse of e
            break #     If the number is the multiplicative inverse of e, stop
        d += 1 # If the number is not the multiplicative inverse of e, pick another number

    private_key = d # Set the private key

    print("Generating public and private keys.......") # Print the public and private keys
    print("Public key(e):", public_key )
    print("Private key(d):", private_key)
    print("N:", n)
    print("\n")

    return public_key, private_key, n # Return the public and private keys and n

def encrypt_func(message, e, n): # Encrypt function
    encrypted_text = pow(message, e, n) # Calculate the encrypted text
    return encrypted_text # Return the encrypted text

def decrypt(encrypted_text, d, n): # Decrypt function
    decrypted = pow(encrypted_text, d, n) # Calculate the decrypted text
    return decrypted # Return the decrypted text

def encrypt_and_encode(message, e, n): # Encrypt and encode the message
    encoded = []
    for letter in message: # For each letter in the message
        encoded_num = encrypt_func(ord(letter), e, n) # Encrypt the letter
        encoded_hex = hex(encoded_num).upper()  # Convert the encrypted number to hexadecimal
        encoded.append(encoded_hex) # Add the hexadecimal to the list
    return ' '.join(encoded) # Return the list as a string


def decode_and_decrypt(encoded, d, n): # Decode and decrypt the message
    hex_nums = encoded.split('0X')[1:] # Split the hexadecimal numbers
    hex_nums = [int('0x' + c.lower(), 0) for c in hex_nums]  # Convert the hexadecimal to decimal

    for i in range(len(hex_nums)): # For each number in the list
        hex_nums[i] = decrypt(hex_nums[i], d, n) # Decrypt the number
        hex_nums[i] = chr(hex_nums[i]) # Convert the number to a letter
    decrypted = ''.join(hex_nums)   # Return the list as a string
    return decrypted  # Return the decrypted text 


def main():
    public_key, private_key, n = set_keys() # Set the public and private keys

    print("RSA Encryption and Decryption using Python") # Print the menu
    print("\n")
    print("1. Encrypt plaintext")
    print("2. Decrypt ciphertext")
    print("3. Exit")
    print("\n")

    choice = input("Enter your choice: ") # Get the user's choice

    while choice != "3":
        if choice == "1":
            message = input("Enter the plaintext: ") # Get the plaintext
            encrypted_text = encrypt_and_encode(message, public_key, n) # Encrypt and encode the plaintext
            print("Encrypted text:",  encrypted_text.replace(" ", "")) # Print the encrypted text

            print("\n")
        
        elif choice == "2":
            encrypted_text = input("Enter the ciphertext: ") # Get the ciphertext
            decrypted_text = decode_and_decrypt(encrypted_text, private_key, n) #  Decrypt and decode the ciphertext
            print("Decrypted text:", decrypted_text) #  Print the decrypted text

            print("\n")

        else:
            print("Invalid input!") # Print an error message

        choice = input("Enter your choice: ") # Get the user's choice

    print("Exiting...\n---a program by Layan Moyura---") 

if __name__ == "__main__":
    main()
