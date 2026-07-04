

# code
wallet = 5000
smart_phone = 1000

# le prix du telephone est inferieur à 1000€
if  smart_phone <= wallet or smart_phone > 1000  :
	print("l’achat est possible ")
	wallet = wallet - smart_phone
else:
	print("l’achat est impossible, vous navez que ()€  " . format(wallet) )
	
text = ("l’achat est possible ", "l’achat est imposible")[smart_phone <= 1000 ]
print(text)
print(wallet)		
	


























