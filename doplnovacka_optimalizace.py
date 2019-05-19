""" s využitím vlastní funkce (vstupními parametry bude vložený text či název souboru, který se má načíst, 
a celé číslo představující, kolikáté slovo textu se má zaměnit za hvězdičky). 

TZN. puvodni slovo pridat do seznamu a seznam spojit do retezce a retezec ulozit
"""

def optimalizace (soubor, kolikate_nahradit):

		f = open(soubor) 
		text = f.read()
		f.closed

		#print(text)
		text = text.replace("\n", "* ")

		seznam = []
		seznam = text.split(" ")
		#print(seznam)
		vysledek = []
		interpunkce = ".,?!-:\";"

		for i in range(0,len(seznam)):
			slovo = seznam[i]
			slovoUpraveno = ""
			
			if ((i + 1) % kolikate_nahradit == 0):
				for pismeno in slovo:
					if pismeno not in interpunkce:
						slovoUpraveno += "*"
					else: slovoUpraveno += pismeno
				vysledek.append(slovoUpraveno)
			else:
				vysledek.append(slovo)

		s = " ".join(vysledek)
		s = s.replace("#", "\n")
		print(s)  

soubor = input ("Zadej název souboru, ve kterém chceš nahrazovat slova: ")
kolikate_nahradit = int(input("Zadej kolikáté slovo v textu chceš nahradit: "))

optimalizace(soubor,kolikate_nahradit)




