import random
caratteri_pw = " a b c d e f g h i j k l m n o p q r s t u v w x y z "\
                " A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "\
                " ? ! £ $ % & / ^ + * § ° € = - _ < > # @ [ ] { } ( ) "\
                " 0 1 2 3 4 5 6 7 8 9 ' | \ "
while True:
    try:
        input_utente = int(input("Determina la lunghezza della tua password (solo numeri interi): "))
        break
    except ValueError: pass
password = ""
for i in range(0, input_utente):
    password += random.choice(caratteri_pw.split())
print(password)