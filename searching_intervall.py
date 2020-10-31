def searching_intervall(rang):
    born=rang
    while len(list_prime(0,born))<=rang:
        born=born+rang
    return born
