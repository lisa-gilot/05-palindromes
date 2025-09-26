"""
Code permettant de déterminer si une chaine de caractères est un palindrome
"""

def ispalindrome(p):
    """
    Détermine si p(la chaine de caractères à tester) est un palindrome
    Renvoie un booléen indiquant True si p est un palindrome
    """
    p = p.replace(" ","").lower()  #pour enlever les espaces et majuscule
    for t in ",;:/.?!*-_([])='":
        p = p.replace(t, "")
    for t in "éèêë":
        p = p.replace(t, "e")
    p = p.replace("à","a").replace("ç","c").replace("ô","o").replace("ù","u")
    pi = p[::-1]
    return pi == p

def main():
    '''
    Réalise le test de la fonction ispalindrome pour certaines chaines
    de caractères
    '''
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
