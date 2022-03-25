print ("Hello, let's play!")
def characters_count():
    phrase = input("write something here: ") #j'ai changé le texte
    characters_nb = str(len(phrase))
    message = "your phrase has " + characters_nb + " characters"
    print(message)

characters_count()
characters_count()
characters_count()

print("c'est chouette quand ça marche")