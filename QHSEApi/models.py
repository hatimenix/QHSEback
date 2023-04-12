from django.db import models

from django.core.validators import FileExtensionValidator
import os


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

class Site(models.Model):
    site_nom = models.CharField(max_length=255)
    sigle = models.CharField(max_length=255)
    responsable_site = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    groupe_retso = models.CharField(max_length=255)

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
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    
class EvaluationDanger(models.Model):
    date = models.DateField(auto_now=True)
    probabilite = models.IntegerField()
    severite = models.IntegerField()
    frequences_exposition = models.IntegerField()
    mesure_prevention = models.TextField()
    ipr = models.FloatField()
    indice_risque = models.IntegerField()
    danger = models.ForeignKey(Danger, on_delete=models.CASCADE)
    
    def clean(self):
        if self.indice_risque not in [1, 2, 3]:
            raise ValidationError("L'indice de risque doit être 1, 2 ou 3.")
    
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
    arret_travail = models.BooleanField()
    dangers = models.ManyToManyField(Danger, null=True, blank=True)
    
class AnalyseEvenement(models.Model):
    cause = models.TextField()
    probabilite = models.IntegerField()
    frequences = models.IntegerField()
    severite = models.IntegerField()
    niveau_risque = models.IntegerField()
    arbe_cause = models.FileField(upload_to='uploads/docs',
                            null=True,
                            blank=True,
                            default=None,                            
                            validators=[FileExtensionValidator(allowed_extensions=['pdf','ppt','pptx'])])
    danger_lie = models.ManyToManyField(Danger, null=True, blank=True)
    evenement = models.OneToOneField(Evenements, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.id:
            old_instance = AnalyseEvenement.objects.get(id=self.id)
            if self.arbe_cause != old_instance.arbe_cause:
                if old_instance.arbe_cause:
                    os.remove(old_instance.arbe_cause.path)
        super().save(*args, **kwargs)

class ArretTravail(models.Model):
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
    
#*Backend Actions :
class Actions(models.Model):
    intitule = models.CharField(max_length=100)
    type_action = models.CharField(max_length=100)
    origine_action = models.CharField(max_length=50)
    reference = models.CharField(max_length=100, blank=True)
    domaine = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    processus = models.ForeignKey(Processus, on_delete=models.CASCADE, blank=True)
    analyse_cause = models.CharField(max_length=255)
    plan_action = models.TextField()
    delai_mise_en_oeuvre = models.DateField()
    assigne_a = models.CharField(max_length=100)
    priorite = models.IntegerField()
    delai_mesure_eff = models.DateField()
    type_critere_eff = models.CharField(max_length=100)
    detail_critere_eff = models.TextField()
    etat = models.CharField(max_length=150)
    annee = models.DateField(auto_now=True)
    danger = models.ManyToManyField(Danger, null=True, blank=True)
    evenement = models.ManyToManyField(Evenements, null=True, blank=True)
    piece_jointe = models.FileField(upload_to='uploads/docs',
                            null=True,
                            blank=True,
                            default=None,                            
                            validators=[FileExtensionValidator(allowed_extensions=['pdf','ppt','pptx'])])
    
    def save(self, *args, **kwargs):
        if self.id:
            old_instance = Actions.objects.get(id=self.id)
            if self.piece_jointe != old_instance.piece_jointe:
                if old_instance.piece_jointe:
                    os.remove(old_instance.piece_jointe.path)
        super().save(*args, **kwargs)
    
class Realisation(models.Model):
    action_associe = models.ForeignKey(Actions, on_delete=models.CASCADE)
    action_realise = models.CharField(max_length=255)
    date_realisation = models.DateField()
    etat = models.CharField(max_length=50)
    
class Taches(models.Model):
    nom_tache = models.CharField(max_length=100)
    date_debut = models.DateField()
    echeance = models.DateField()
    description = models.TextField()
    priorite = models.CharField(max_length=100)
    assigne_a = models.CharField(max_length=100)
    date_realisation = models.DateField()
    état = models.CharField(max_length=100)
    commentaire = models.TextField(blank=True)
    realisation_associee = models.ForeignKey(Realisation, on_delete=models.CASCADE)
    piece_jointe = models.FileField(upload_to='uploads/docs',
                            null=True,
                            blank=True,
                            default=None,                            
                            validators=[FileExtensionValidator(allowed_extensions=['pdf','ppt','pptx'])])
    
    def save(self, *args, **kwargs):
        if self.id:
            old_instance = Taches.objects.get(id=self.id)
            if self.piece_jointe != old_instance.piece_jointe:
                if old_instance.piece_jointe:
                    os.remove(old_instance.piece_jointe.path)
        super().save(*args, **kwargs)
    
class MesureEfficacite(models.Model):
    date_cloture = models.DateField()
    resultat_mesure_eff = models.CharField(max_length=100)
    mesure_eff = models.TextField()
    cout = models.FloatField()
    action_associee = models.OneToOneField(Actions, on_delete=models.CASCADE)
    