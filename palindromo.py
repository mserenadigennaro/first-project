#chiedi all'utente di inserire una parola
parola=input("Inserisci una parola: ")
             
#rendi la parola minuscola
parola=parola.lower()

#verifica se la parola è uguale alla sua versione invertita
if parola == parola[::-1]:
    print("la parola è un palindromo!")
else:
    print("La parola non è un palindromo.")