#chiedi all'utente di inserire una frase
frase=input("Inserisci una frase")

#dividi la frase in parole
parole=frase.split()

#inverti l'ordine delle parole
parole_invertite=parole[::-1]

#ricomponi la frase invertita
frase_invertita=" ".join(parole_invertite)

# stampa la frese invertita
print("Frase con ordine delle parole invertito:")
print(frase_invertita)