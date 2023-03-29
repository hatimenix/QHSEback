from django.db import models

#*Zakaria
#*Backend document unique 

#*Table commun :
class Utilisateur(models.Model):
    compte = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    courrier = models.EmailField()
    numero_tel = models.CharField(max_length=255, null=True, blank=True)
    presente_vous = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    fonction = models.CharField(max_length=255, null=True, blank=True)
    adresse_sip = models.CharField(max_length=255, null=True, blank=True)
    othermail = models.EmailField(null=True, blank=True)
    def __str__(self):
        return str(self.nom)

class Site(models.Model):
    site_nom = models.CharField(max_length=255)
    sigle = models.CharField(max_length=255)
    responsable_site = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    groupe_retso = models.CharField(max_length=255)
    def __str__(self):
        return str(self.site_nom)

class Services(models.Model):
    service_nom = models.CharField(max_length=255)

#*Backend Danger :
class Famille(models.Model):
    famille_nom = models.CharField(max_length=255)

class Danger(models.Model):
    poste_de_travail = models.CharField(max_length=255)
    taches = models.CharField(max_length=255)
    description = models.TextField()
    consequences = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    service = models.ForeignKey(Services ,blank=True ,on_delete=models.CASCADE)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    
class EvaluationDanger(models.Model):
    date = models.DateField(auto_now=True)
    probabilite = models.IntegerField()
    severite = models.IntegerField()
    frequences_exposition = models.IntegerField()
    mesure_prevention = models.TextField()
    danger = models.ForeignKey(Danger, on_delete=models.CASCADE)
    
#*Table relation entre Service et Utilisateur 
class ChefServices(Utilisateur):
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    
#*Backend evenemnts :
class Evenements(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    type_contract = models.CharField(max_length=255)
    nom_personne = models.CharField(max_length=255)
    type_evenement = models.CharField(max_length=255)
    intitule = models.CharField(max_length=255)
    resume = models.TextField()
    temoins = models.CharField(max_length=255)
    premiere_pers_info = models.CharField(max_length=255)
    action_immediate = models.TextField()
    date_accident = models.DateField()
    periode_travail = models.CharField(max_length=255)
    lieu_accident = models.CharField(max_length=255)
    tache_effectue = models.CharField(max_length=255)
    utiliser_chien = models.BooleanField()
    siege_de_lesions_1 = models.CharField(max_length=255, blank=True)
    siege_de_lesions_2 = models.CharField(max_length=255, blank=True)
    nature_lesions = models.CharField(max_length=255)
    dangers = models.ManyToManyField(Danger)
    
class AnalyseEvenement(models.Model):
    cause = models.TextField()
    probabilite = models.IntegerField()
    frequences = models.IntegerField()
    severite = models.IntegerField()
    niveau_risque = models.IntegerField()
    arbe_cause = models.TextField()
    danger_lie = models.ForeignKey(Danger, on_delete=models.CASCADE)
    evenement = models.OneToOneField(Evenements, on_delete=models.CASCADE)

class ArretTravail(models.Model):
    arret = models.BooleanField()
    CMI_volet_recup = models.CharField(max_length=50)
    date_debut_arret = models.DateField()
    date_fin_arret = models.DateField()
    duree_arret = models.IntegerField()
    prolongation = models.BooleanField()
    duree_total_pro = models.IntegerField()
    rechute = models.BooleanField()
    duree_total_rechute = models.IntegerField()
    duree_total_arret = models.IntegerField()
    evenement = models.OneToOneField(Evenements, on_delete=models.CASCADE)
    
#*Table Processus :
class Processus(models.Model):
    processus_nom=models.CharField(max_length=255,null=True, default=None)
    intitule = models.CharField(max_length=255)
    typologie = models.CharField(max_length=255)
    sigle = models.CharField(max_length=50)
    finalite = models.TextField()
    pilote = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    acteurs = models.TextField()
    donnee_entree = models.TextField()
    activites = models.TextField()
    donnee_sortie = models.TextField()
    ressources_tech_org = models.TextField()
    objectifs_ind = models.TextField()
    outils_surveil = models.TextField()
    def __str__(self):
        return str(self.processus_nom)
    
#*Backend Actions :
class Actions(models.Model):
    intitule = models.CharField(max_length=100)
    type_action = models.CharField(max_length=50)
    origine_action = models.CharField(max_length=50)
    reference = models.CharField(max_length=50, blank=True)
    domaine = models.CharField(max_length=50)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    processus = models.ForeignKey(Processus, on_delete=models.CASCADE)
    analyse_cause = models.ForeignKey(AnalyseEvenement, on_delete=models.CASCADE)
    plan_action = models.TextField()
    delai_mise_en_oeuvre = models.DateField()
    assigne_a = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    priorite = models.IntegerField()
    delai_mesure_eff = models.DateField()
    type_critere_eff = models.CharField(max_length=50)
    detail_critere_eff = models.TextField()
    danger = models.ManyToManyField(Danger)
    evenement = models.ManyToManyField(Evenements)
    
class Realisation(models.Model):
    action_realisee = models.ForeignKey(Actions, on_delete=models.CASCADE)
    date_realisation = models.DateField()
    etat = models.CharField(max_length=50)
    
class Taches(models.Model):
    source = models.CharField(max_length=50)
    nom_tache = models.CharField(max_length=100)
    date_debut = models.DateField()
    echeance = models.DateField()
    description = models.TextField()
    priorite = models.CharField(max_length=50)
    assigne_a = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_realisation = models.DateField()
    état = models.CharField(max_length=50)
    commentaire = models.TextField()
    piece_jointe = models.CharField(max_length=500, null=True, blank=True)
    realisation_associee = models.ForeignKey(Realisation, on_delete=models.CASCADE)
    
class MesureEfficacite(models.Model):
    date_cloture = models.DateField()
    resultat_mesure_eff = models.TextField()
    mesure_eff = models.TextField()
    cout = models.FloatField()
    action_associee = models.OneToOneField(Actions, on_delete=models.CASCADE)

#Table des non-conformités :
class NC(models.Model):
    intitule = models.CharField(max_length=255)
    nature= models.CharField(max_length=255)
    site=models.ForeignKey(Site, on_delete=models.CASCADE)
    processus=models.ForeignKey(Processus, on_delete=models.CASCADE)
    domaine = models.CharField(max_length=255)
    date_nc=models.DateField()
    date_prise_en_compte = models.DateField()
    description_detailee= models.TextField()
    annee=models.PositiveIntegerField()
    mois=models.CharField(max_length=255)
    detail_cause=models.CharField(max_length=255)
    delai_prevu=models.DateField()
    type_cause=models.CharField(max_length=255)
    cout=models.FloatField(max_length=100)
    progress=models.FloatField(max_length=100)
    etat=models.BooleanField()
    info_complementaires=models.TextField()
    piece_jointe=models.FileField(upload_to='uploads/',null=True, default=None)
    frequence=models.BooleanField()
    gravite=models.BooleanField()
    action_immediate=models.BooleanField()
    nc_cloture=models.BooleanField()
    responsable_traitement = models.ForeignKey(Utilisateur, on_delete=models.CASCADE,null=True, default=None)



