import random
while True:
    try:
        input_utente = int(input("Determina la lunghezza della tua password (solo numeri interi): "))
        break
    except ValueError: pass
password_list = []
password = ""
for i in range (0, input_utente):
    password_list = password_list + random.sample(("a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 ? ! £ $ % & / ( ) ^ + # @".split()), k=1)
for lettera in password_list:
    password = password + lettera
print(password)