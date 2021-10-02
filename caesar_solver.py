print('caesar cipher solver')

def bruteforce():
	print('enter the ciphertext:')
	s = input()
	s.upper()

	for i in range(1,26):
		print('--------------------------------------')
		print('key = {}'.format(i))
		c = ''
		for j in s:
			c+= chr((ord(j) + i-65) % 26 + 65)
		print(c)

def encrypt():
	s = input("enter text to encrypt")
	k = int(input("enter key"))
	c = ''
	for j in s:
		c+= chr((ord(j) + k-65) % 26 + 65)
	print(c)

def decrypt():
	s = input("enter text to decrypt")
	k = int(input("enter key"))
	c = ''
	for j in s:
		c+= chr((ord(j) + k-65) % 26 + 65)
	print(c)

n = int(input("Choose your option:\n[1]Encrypt\n[2]Decrypt\n[3]Bruteforce"))
if n == 1:
	encrypt()
elif n == 2:
	decrypt()
elif n == 3:
	bruteforce()
else:
	print("Enter proper value")