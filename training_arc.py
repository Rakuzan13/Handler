def reverse_a_list(yes):
    for ye in yes[::-1]:
        return(ye)
liste=[41789]
"""print(reverse_a_list(liste))""" #this programm return the last index only except of showing the reverse list 

import string
import random as rd

def generer_mdp(longueur=12):
    lettres=string.ascii_letters
    chiffres=string.digits
    symboles=string.punctuation

    alls=lettres+chiffres+symboles

    mdp=[
    rd.choices(lettres),
    rd.choices(chiffres),
    rd.choices(symboles)
    ]

    mdp+=rd.choices(all,k=longueur)
    rd.shuffle(mdp)
        return"".join(mdp)