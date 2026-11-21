from contact import Contact 

class Carnet:
    def __init__(self):
        self.contacts = []

    def ajouter(self, contact: Contact):
        self.contacts.append(contact)

    def chercher(self, nom_partiel: str) -> list:
        """Retourne la liste des contacts dont le nom contient la chaîne donnée."""
        nom_partiel_lower = nom_partiel.lower()
        return [c for c in self.contacts if nom_partiel_lower in c.nom.lower()]

    def __len__(self):
        return len(self.contacts)
if __name__ == "__main__":
    carnet = Carnet()
    c1 = Contact("Alami Salma ", "0612345678", "salma@example.com")
    c2 = Contact("Assim Adil", "0698765432", "adil@example.com")
    carnet.ajouter(c1)
    carnet.ajouter(c2)

    print(c1.initiale) 
    resultats = carnet.chercher("Adil")
    print(resultats) 
    print(len(carnet)) 