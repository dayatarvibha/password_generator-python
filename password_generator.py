import random
import string

def pass_generator():
	pass_length = 10
	pass_contain = string.ascii_letters + string.digits
	password = ''.join(random.choice(pass_contain) for i in range(pass_length))
	return password
generate = pass_generator()
print("generated password is: ", generate)

