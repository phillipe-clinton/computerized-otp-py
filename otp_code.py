import secrets

def encrypt(message, key):
  """Encrypts a message using a one-time pad.

  Args:
    message: The message to encrypt.
    key: The key to use for encryption.

  Returns:
    The encrypted message.
  """

  # Convert the message and key to binary strings.
  message_bytes = message.encode("utf-8")
  key_bytes = key.encode("utf-8")

  # XOR the message and key bytes.
  encrypted_bytes = bytes([a ^ b for a, b in zip(message_bytes, key_bytes)])

  # Convert the encrypted bytes to a string.
  encrypted_message = encrypted_bytes.decode("utf-8")

  return encrypted_message

def decrypt(encrypted_message, key):
  """Decrypts an encrypted message using a one-time pad.

  Args:
    encrypted_message: The encrypted message to decrypt.
    key: The key to use for decryption.

  Returns:
    The decrypted message.
  """

  # Convert the encrypted message and key to binary strings.
  encrypted_message_bytes = encrypted_message.encode("utf-8")
  key_bytes = key.encode("utf-8")

  # XOR the encrypted message and key bytes.
  decrypted_bytes = bytes([a ^ b for a, b in zip(encrypted_message_bytes, key_bytes)])

  # Convert the decrypted bytes to a string.
  decrypted_message = decrypted_bytes.decode("utf-8")

  return decrypted_message



message = input("Enter your string: ")
key = secrets.token_hex(len(message))

encrypted_message = encrypt(message, key)
#print encrypted msg
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
#print original msg
print(decrypted_message)





