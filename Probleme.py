Transformer = ['Legend Class', 'Core Class', 'Deluxe Class', 'Voyager Class', 'Leader Class', 'Titan Class'] # cite les differentes tailles de transformer disponibles
price = [11, 17, 23, 31, 47, 60] # cite les prix de chaque catégorie

somme = int(input("Entrer une somme: ")) # demande a l'utilisateur de dire quelle somme d'argent la personne posséde
print("\nVous pouvez vous prendre les Transformers suivants: ")

for i in range(len(Transformer)): #compte les elements dans la liste
    if somme >= price[i]:# si la somme est égale ou supérieur
        print(Transformer[i])# donnez le nom de chaque categorie dans la liste correspondant
