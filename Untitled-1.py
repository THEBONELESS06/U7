class Abonnement:
    def __init__(self, nom, duree, qualite, ecrans):
        self.nom = nom
        self.duree = duree
        self.qualite = qualite
        self.ecrans = ecrans

    def __str__(self):
        return f"{self.nom} - {self.duree} mois - {self.qualite} - {self.ecrans} écrans"


class ServiceStreaming:
    def __init__(self):
        self.abonnements = []

    def ajouter_abonnement(self, nom, duree, qualite, ecrans):
        abonnement = Abonnement(nom, duree, qualite, ecrans)
        self.abonnements.append(abonnement)
        print(f"Abonnement '{nom}' ajouté avec succès.")

    def modifier_abonnement(self, nom, nouvelle_duree=None, nouvelle_qualite=None, nouveaux_ecrans=None):
        for abonnement in self.abonnements:
            if abonnement.nom == nom:
                if nouvelle_duree:
                    abonnement.duree = nouvelle_duree
                if nouvelle_qualite:
                    abonnement.qualite = nouvelle_qualite
                if nouveaux_ecrans:
                    abonnement.ecrans = nouveaux_ecrans
                print(f"Abonnement '{nom}' modifié avec succès.")
                return
        print("Abonnement non trouvé.")

    def supprimer_abonnement(self, nom):
        self.abonnements = [ab for ab in self.abonnements if ab.nom != nom]
        print(f"Abonnement '{nom}' supprimé avec succès.")

    def rechercher_abonnement(self, nom):
        for abonnement in self.abonnements:
            if abonnement.nom == nom:
                print("Abonnement trouvé :", abonnement)
                return abonnement
        print("Abonnement non trouvé.")
        return None

    def lister_abonnements(self):
        if not self.abonnements:
            print("Aucun abonnement disponible.")
        else:
            print("Liste des abonnements :")
            for abonnement in self.abonnements:
                print(abonnement)


# Exemple d'utilisation
service = ServiceStreaming()
service.ajouter_abonnement("Premium", 12, "4K", 4)
service.ajouter_abonnement("Standard", 6, "HD", 2)
service.ajouter_abonnement("Basic", 1, "SD", 1)

service.lister_abonnements()

service.modifier_abonnement("Standard", nouvelle_duree=9, nouveaux_ecrans=3)
service.rechercher_abonnement("Standard")

service.supprimer_abonnement("Basic")
service.lister_abonnements()
