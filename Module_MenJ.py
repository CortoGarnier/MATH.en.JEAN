def theorem_DF_HL(B=int(input("choisissez le nombre B:")), n=int(input("choisissez le nombre n:"))):
    '''
This function allows to answer the first question with the theorem of Diffie-Hellman.
    :param B: first public number
    :param n: second public number
    :return: the key
    '''
    tour =0
    while tour < 1:
        # definition of secret number of Alice
        nbr_secretAL = input("Alice choisit un nombre: ")
        # first calculation with secret number of Alice
        first_resultAL = B ** int(nbr_secretAL) % n
        # result of Alice
        print("Le resultat du calcule d'Alice est {0}.".format(first_resultAL))
        # definition of secret number of Bob
        nbr_secretBOB = input("Bob choisit un nombre: ")
        # first calculation with secret number of Bob
        first_resultBOB = B ** int(nbr_secretBOB) % n
        # result of Bob
        print("Le resultat du calcule de Bob est {0}.".format(first_resultBOB))
        # if one of the results is equal to 1, the key is equal to 1 and Charlie know the key
        if first_resultAL == 0 or 1:
            tour = 0
            print("\n")
            print("Erreur, le résultat d'Alice est égale a la clé.")
        elif first_resultBOB == 0 or 1:
            tour = 0
            print("\n")
            print("Erreur, le résultat de Bob est égale a la clé.")
        else:
            tour += 1

    tours = 0

    while tours < 2:
        if tours == 0:
            # recovery of the result of Bob
            nbr_secret_partner= input("Alice entre le premier résultat de Bob: ")
            # finale calculation with the result of the partner
            final_resultAL = int(nbr_secret_partner) ** int(nbr_secretAL)%n
            # finale result : The Key
            print("La clé trouver par Alice est {0}.".format(final_resultAL))
        elif tours == 1:
            # recovery of the result of the partner Alice
            nbr_secret_partner = input("Bob entre le premier résultat de Alice: ")
            # finale calculation with the result of the partner
            final_resultBOB = int(nbr_secret_partner) ** int(nbr_secretBOB) % n
            # finale result : The Key
            print("La clé trouver par Bob est {0}.".format(final_resultBOB))
        tours += 1
    return final_resultBOB


def comb_aleatoire():
    '''
This function distribute the cards randomly.
    :return: a dictionary which contain the cards of Alice, Bob and Charlie
    '''
    from random import randint as rand
    # the list of the cards
    liste = [0, 1, 2, 3, 4, 5, 6]
    tours = 0
    while tours < 3:
        if tours == 0:
            # combination of Alice
            comb_1 = [liste.pop(rand(0, 6)), liste.pop(rand(0, 5)), liste.pop(rand(0, 4))]
            print("les cartes d'Alice sont:{0}".format(comb_1))
        elif tours == 1:
            # combination of Bob
            comb_2 = [liste.pop(rand(0, 3)), liste.pop(rand(0, 2)), liste.pop(rand(0, 1))]
            print("les cartes de Bob sont:{0}".format(comb_2))
        elif tours == 2:
            # card of Charlie
            comb_3 = liste
            print("la carte de Charlie est:{0}".format(comb_3))
        tours += 1
    return {"Alice": comb_1, "Bob": comb_2, "Charlie": comb_3}


def BobCalcul(Result=8, BobL = [4, 1, 3]):
    '''
    This function find the cards of Alice the cards of Bob and the adding cards of Alice.
    :param Result:Adding card of Alice
    :param BobL:Cards of Bob
    :return:Cards of Alice
    '''
    # We remove the cards of Bob of possibilities
    liste = [0, 1, 2, 3, 4, 5, 6]
    R1 = BobL[0]; R2 = BobL[1]; R3 = BobL[2]
    liste.remove(R1)
    liste.remove(R2)
    liste.remove(R3)
    LIST_INV = list(liste)
    listDeReslt = []
    nbrtour = range(0, 2)
    nbrtour2 = range(0, 2)
    nbrtour3 = range(0, 2)
    # We find the cards of Alice ...
    tours = 0
    for i in nbrtour:
        for j in nbrtour2:
            for k in nbrtour3:
                # ... with a loop for which create combination with the what Bob doesn't have
                liste = list(LIST_INV)
                a = liste.pop(int(i))
                b = liste.pop(int(j))
                c = liste.pop(int(k)-1)
                R = int(a)+int(b)+int(c)
                if tours == 0 and R == Result:
                    tours += 1
                    listDeReslt.extend([[a, b, c]])
                if tours < 0 and R == Result:
                    F1 = listDeReslt[0]
                    if tours >= 2 and F1[0] == a or b or c:
                        if F1[1] == a or b or c:
                            if F1[2] == a or b or c:
                                listDeReslt.extend([[a, b, c]])
    return listDeReslt[0]