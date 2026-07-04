
# exanple : systeme de verification de mot de passe
password = input("entrer votre mot de passe")
password_length = len (password)
print(password_length)


# verifier si le mot de passe est inferieur à 8 caracteres
if password_length <=  8:
	print("mot de psse trop court! ")
elif	  8 < password_length <= 12:
		print("mot de passe moyen")
else :
	print("mot de passe parfait")














