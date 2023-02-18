import random
print("Welcome to the Pypassword Generator !")
#Easy Level

#letters = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','q','s','t','w','x','v','y','z','A','B','C']
#numbers = ['0','1','2','3','4','5','6','7','8','9']
#symbols = ['!','#','$','%','&','(',')','*','+']
#nr_letters = int(input("How many letters would you like in your password?\n"))
#nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
#nr_symbols = int(input(f"How many symbols would you like in your password?\n")) 

#password = ""
#for char in range (1,nr_letters+1):
#  password +=random.choice(letters)
  
#for char in range (1,nr_numbers+1):
#  password += random.choice(numbers)  
#for char in range (1,nr_symbols+1):
#  password += random.choice(symbols)
#print(password)

#Hard Level 

password_list = []
for char in range(1,nr_numbers +1):
  password_list.append(random.choice(numbers))
for char in range(1, nr_letters +1):
  password_list.append(random.choice(letters))
for char in range(1,nr_symbols +1):
  password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
  password += char
print(f"Your password is : {password}")

