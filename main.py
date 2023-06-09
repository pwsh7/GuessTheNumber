import random
import time

print("""
********************************************************************

	      Guess the hidden number between 1 and 100


********************************************************************""")

rasgele_sayı=random.randint(1,100)
tahmin_hakkı=5
kullanıcı=input("Enter your name:")
while True:
	tahmin=int(input("Type a number:"))	
	if tahmin<rasgele_sayı:
		print("Thinking...")
		time.sleep(1)

		print("Make a bigger guess...")

		tahmin_hakkı-=1

	elif tahmin>rasgele_sayı:
		print("Thinking...")
		time.sleep(1)

		print("Make a smaller guess...")

		tahmin_hakkı-=1
	else:
		print("Thinking...")
		time.sleep(1)

		print("Congrats!",kullanıcı," the number was",rasgele_sayı)
		break
	if tahmin_hakkı==0:
		print("Your guess rights is over")
		print(" the number was",rasgele_sayı)
		break
