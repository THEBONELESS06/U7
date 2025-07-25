class Offre:
    def __init__(self, nom, prix, volume_internet, minutes_appel, sms_inclus):
        self.nom = nom
        self.prix = prix
        self.volume_internet = volume_internet
        self.minutes_appel = minutes_appel
        self.sms_inclus = sms_inclus

    def __str__(self):
        return (f"Offre: {self.nom}, Prix: {self.prix}, Volume Internet: {self.volume_internet}, "
                f"Minutes Appel: {self.minutes_appel}, SMS Inclus: {self.sms_inclus}")

offres = []

def ajouter_offre(nom, prix, volume_internet, minutes_appel, sms_inclus):
    nouvelle_offre = Offre(nom, prix, volume_internet, minutes_appel, sms_inclus)
    offres.append(nouvelle_offre)
    print("Offre ajoutée avec succès")

def modifier_offre(nom_recherche, nouveau_prix, nouveau_volume_internet, nouvelles_minutes_appel, nouveaux_sms):
    for offre in offres:
        if offre.nom == nom_recherche:
            offre.prix = nouveau_prix
            offre.volume_internet = nouveau_volume_internet
            offre.minutes_appel = nouvelles_minutes_appel
            offre.sms_inclus = nouveaux_sms
            print("Offre modifiée avec succès")
            return
    print("Offre non trouvée")

def supprimer_offre(nom_recherche):
    for offre in offres:
        if offre.nom == nom_recherche:
            offres.remove(offre)
            print("Offre supprimée avec succès")
            return
    print("Offre non trouvée")

def rechercher_offre(nom_recherche):
    for offre in offres:
        if offre.nom == nom_recherche:
            print("Offre trouvée :", offre)
            return
    print("Offre non trouvée")

def afficher_offres():
    if not offres:
        print("Aucune offre disponible")
    else:
        for offre in offres:
            print(offre)

# Exemple d'utilisation
ajouter_offre("Offre1", 20, "5GB", 100, 50)
ajouter_offre("Offre2", 30, "10GB", 200, 100)
afficher_offres()

rechercher_offre("Offre1")
modifier_offre("Offre1", 25, "6GB", 150, 60)
afficher_offres()

supprimer_offre("Offre2")
afficher_offres()