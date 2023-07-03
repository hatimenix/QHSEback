from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
import os
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#send email 
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
#permissions
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
#*Zakaria
#*Backend document unique 

#*Table commun :
class Utilisateur(models.Model):
    compte = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    courrier = models.EmailField()
    numero_tel = models.CharField(max_length=255, null=True, blank=True)
    presente_vous = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
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
   # documents = models.ManyToManyField(Document)

    def __str__(self):
        return str(self.site_nom)



class Services(models.Model):
    service_nom = models.CharField(max_length=255)
    
#*Table relation entre Service et Utilisateur 
class ChefServices(Utilisateur):
    services = models.ForeignKey(Services, on_delete=models.CASCADE)

class Secteurs(models.Model):
    secteur_nom = models.CharField(max_length=255)
    #documents = models.ManyToManyField(Document)


    

class Secteurs(models.Model):
    secteur_nom = models.CharField(max_length=255)
    #documents = models.ManyToManyField(Document)


    

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
    mesure_prevention = models.TextField(null=True, blank=True)
    ipr = models.FloatField()
    indice_risque = models.IntegerField()
    danger = models.ForeignKey(Danger, on_delete=models.CASCADE)
    
    def clean(self):
        if self.indice_risque not in [1, 2, 3]:
            raise ValidationError("L'indice de risque doit être 1, 2 ou 3.")
        
    
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

    



    def __str__(self):
        return self.intitule
    

    
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
    etat = models.CharField(max_length=150, default='Non commencé')
    annee = models.DateField(auto_now=True)
    danger = models.ManyToManyField(Danger, null=True, blank=True, db_constraint=False)
    evenement = models.ManyToManyField(Evenements, null=True, blank=True, db_constraint=False)
    piece_jointe = models.FileField(upload_to='uploads/docs',
                            null=True,
                            blank=True,
                            default=None,                            
                            validators=[FileExtensionValidator(allowed_extensions=['pdf','ppt','pptx'])])
    qualite = models.ManyToManyField('Qualite', null=True, blank=True, db_constraint=False)
    nc= models.ManyToManyField('NC', null=True, blank=True, db_constraint=False)
    analyserisque= models.ManyToManyField('AnalyseRisque', null=True, blank=True, db_constraint=False)
    ca = models.ManyToManyField('ConstatAudit', null=True, blank=True, db_constraint=False)

    
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

class Source(models.Model):
    nom=models.CharField(max_length=255,blank=True, null=True,)
    def __str__(self):
        return str(self.nom)
    
class Taches(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE,null=True, default=None)
    nom_tache = models.CharField(max_length=100)
    date_debut = models.DateField()
    echeance = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priorite = models.CharField(max_length=100, null=True, blank=True)
    assigne_a = models.ForeignKey(Utilisateur, on_delete=models.CASCADE,null=True, default=None)
    date_realisation = models.DateField(null=True, blank=True)
    etat = models.CharField(max_length=100, null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True)
    realisation_associee = models.ForeignKey(Realisation, on_delete=models.CASCADE,null=True, default=None)
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


 #modèle de la classe commande BOCHRA 

class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date_commande = models.CharField(max_length=50)
    type_commande = models.CharField(max_length=50)
    etat_commande = models.CharField(max_length=50)
    quantite = models.IntegerField()
    specificite_regime = models.CharField(max_length=50)
    specificite_texture = models.CharField(max_length=50)

  

#modèle de la classe Fiche Technique BOCHRA

class FicheTechnique(models.Model):
    id_fiche = models.AutoField(primary_key=True)
    fichier = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(['pdf', 'docx','odt'])],blank=True)
    nom_fiche = models.CharField(max_length=255)
    type_plat = models.CharField(max_length=50)


# Achraf
# 
# module RGPD  

# sous module Registre du  traitemant 

#Fournisseur model
class Fournisseur(models.Model):
    # Existing fields
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255,blank=True, null=True)
    numerodesiret = models.CharField(max_length=255,blank=True, null=True)
    type_de_prestation = models.CharField(max_length=255,blank=True, null=True)
    numero_de_recepisse_de_declaration_prefectorale = models.CharField(max_length=255,blank=True, null=True)
    pageweb = models.CharField(max_length=255,blank=True, null=True)
    telephone = models.CharField(max_length=255,blank=True, null=True)
    numerodetelecopie = models.CharField(max_length=255,blank=True, null=True)
    adresse = models.CharField(max_length=255,blank=True, null=True)
    codepostal = models.CharField(max_length=255,blank=True, null=True)
    ville = models.CharField(max_length=255,blank=True, null=True)
    pays = models.CharField(max_length=255,blank=True, null=True)
    nometprenom = models.CharField(max_length=255,blank=True, null=True)
    adressedecourier = models.CharField(max_length=255,blank=True, null=True)
    fonction = models.CharField(max_length=255,blank=True, null=True)
    numerodetelephone = models.CharField(max_length=255,blank=True, null=True)
    telephonepersonnel = models.CharField(max_length=255,blank=True, null=True)
    
    def __str__(self):
        return f'Fournisseur {self.id} ({self.nom})'
    
#Traitement model 
class Traitement(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    typeregistre = models.CharField(max_length=255,blank=True, null=True)
    nomtraitement = models.CharField(max_length=255,blank=True, null=True)
    description_generale=models.TextField(blank=True, null=True)
    datedecreation = models.DateTimeField(auto_now_add=True)
    datedemiseajour = models.DateTimeField(auto_now=True)
    responsable_traitement=models.CharField(max_length=255,blank=True, null=True)
    finaliteprincipale = models.TextField(blank=True, null=True)
    sous_finalite1 = models.TextField(blank=True, null=True)
    sous_finalite2 = models.TextField(blank=True, null=True)
    sous_finalite3 = models.TextField(blank=True, null=True)
    sous_finalite4 = models.TextField(blank=True, null=True)
    donneesensible = models.BooleanField(blank=True, null=True)
    type_donnee=models.CharField(max_length=255,blank=True, null=True)
    categorie = models.CharField(max_length=255,blank=True, null=True)
    description = models.CharField(max_length=255,blank=True, null=True)
    dureedeconcesrvation = models.CharField(max_length=255,blank=True, null=True)
    personneconcernees = models.CharField(max_length=255,blank=True, null=True)
    precisions = models.CharField(max_length=255,blank=True, null=True)
    typedestinataire = models.CharField(max_length=255,blank=True, null=True)
    precision = models.CharField(max_length=255,blank=True, null=True)
    donneeconcernees = models.CharField(max_length=255,blank=True, null=True)
    mtypedemesuredesecurite = models.CharField(max_length=255,blank=True, null=True)
    destinataire = models.CharField(max_length=255,blank=True, null=True)
    pays = models.CharField(max_length=255,blank=True, null=True)
    typedegarantie = models.CharField(max_length=255,blank=True, null=True)
    lienversladocumentation = models.CharField(max_length=255,blank=True, null=True)
    lesdonneesconcernee = models.CharField(max_length=255,blank=True, null=True)
    fournisseur_dpo = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name='traitements_dpo')
    fournisseur_representant = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name='traitements_representant')
    
    def save(self, *args, **kwargs):
        if not self.id:  # only set REFtraitement if it's a new object
            year = timezone.now().year
            self.REFtraitement = f'{year}-{self.id}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Traitement {self.id} ({self.nomtraitement})'
    

#Evaluation model
class Evaluation(models.Model):
    # New fields
    delai = models.IntegerField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    qualite = models.IntegerField(blank=True, null=True)
    reactive = models.IntegerField(blank=True, null=True)
    realationnel = models.IntegerField(blank=True, null=True)
    
    # ForeignKey to Fournisseur
    traitement = models.ForeignKey(Traitement, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)


    def __str__(self):
        return f'Evaluation {self.id}'    
    

#sous module document utiles
    
#Document utiles Model
class DocumentUtilities(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, blank=True)
    modified_by = models.CharField(max_length=255, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    typologie = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)


#ilyas

#Table des non-conformités :

class NC(models.Model):
    intitule = models.CharField(max_length=255)
    nature= models.CharField(max_length=255)

    site=models.ForeignKey(Site, on_delete=models.CASCADE,null=True, default=None)
    processus=models.ForeignKey(Processus, on_delete=models.CASCADE,null=True, default=None)
    domaine = models.CharField(blank=True, null=True,max_length=255)
    date_nc=models.DateField()
    date_prise_en_compte = models.DateField(blank=True, null=True, default=None)
    description_detailee= models.TextField(blank=True, null=True, default=None)
    annee=models.CharField(blank=True, null=True,max_length=255)

    mois=models.CharField(blank=True, null=True,max_length=255)
    detail_cause=models.CharField(blank=True, null=True,max_length=255)
    delai_prevu=models.DateField(blank=True, null=True)
    type_cause=models.CharField(blank=True, null=True,max_length=255)
    cout=models.CharField(blank=True, null=True,max_length=255)
    progress=models.CharField(blank=True, null=True,max_length=255)
    info_complementaires=models.TextField(blank=True, null=True)
    piece_jointe=models.FileField(upload_to='uploads/',blank=True, null=True, default=None)
    frequence=models.BooleanField(blank=True, null=True)
    gravite=models.BooleanField(blank=True, null=True)
    action_immediate=models.BooleanField(blank=True, null=True)
    nc_cloture=models.BooleanField(blank=True, null=True)
    responsable_traitement = models.ForeignKey(Utilisateur, on_delete=models.CASCADE,null=True, default=None)



class Equipement(models.Model):
    site=models.ForeignKey(Site, on_delete=models.CASCADE,null=True, default=None)
    secteur=models.ForeignKey(Secteurs, on_delete=models.CASCADE,null=True, default=None)
    type_equipement=models.CharField(max_length=255,blank=True, null=True,)
    codification=models.CharField(max_length=255)
    date_mise_en_service=models.DateField(blank=True, null=True,)
    date_modification=models.DateField(blank=True, null=True,)
    verification = models.CharField(max_length=255,blank=True, null=True,)
    prochaine_verification= models.DateField(blank=True, null=True,)
    commentaires=models.CharField(max_length=255,blank=True, null=True,)
    Equipement_declasse=models.BooleanField(blank=True, null=True,)
    N_serie=models.CharField(max_length=255,blank=True, null=True,)
    Certificat=models.FileField(upload_to='uploads/',blank=True,null=True, default=None)


#modèles de gestion des documentation  Bochra 

class Documents(models.Model):
    nom = models.CharField(max_length=255)
    codification = models.CharField(max_length=255)
    version = models.IntegerField()
    date_approbation = models.DateField()
    date_previsionnelle = models.DateField()
    #change the type 
    nv_version = models.CharField(max_length=255)
    type_docs = models.CharField(max_length=255)
    url_document = models.FileField(upload_to='documents/',blank=True)
    #add blank true
    icon = models.CharField(max_length=255, blank=True)
    processus = models.ForeignKey(Processus, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteurs, on_delete=models.CASCADE)
    personnel = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class HistoriqueDocument(models.Model):
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    version = models.IntegerField()
    modifie_par = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    description_modif = models.CharField(max_length=255)
    date_modif = models.DateTimeField(auto_now_add=True)

class FavorisDocument(models.Model):
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('document', 'utilisateur'),)

#modele de gestion des menus Bochra 



class Menus(models.Model):
    mois_concerne = models.CharField(max_length=255)
    menus_generaux = models.FileField(upload_to='documents/',blank=True)
    menus_dessert = models.FileField(upload_to='documents/',blank=True)
    menu_s1 = models.FileField(upload_to='documents/',blank=True)
    menu_s2 = models.FileField(upload_to='documents/',blank=True)
    menu_s3 = models.FileField(upload_to='documents/',blank=True)
    menu_s4 = models.FileField(upload_to='documents/',blank=True)
    menu_s5 = models.FileField(upload_to='documents/',blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)




class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email))
        user.password = make_password(password)  # Use make_password to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class UserApp(AbstractBaseUser):
    nom_user = models.CharField(max_length=100)
    nom_complet = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=255)
    actif = models.BooleanField(blank=True, default=False)
    groupes_roles = models.ManyToManyField('GroupeUser', null=True, blank=True, db_constraint=False)
    send_email = models.BooleanField(default=False)  # New field for checkbox
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def has_module_perms(self, app_label):
        
        return self.is_staff
    
    def has_perm(self, perm, obj=None):

        return self.is_staff


class GroupeUser(models.Model):
    AUTORISATION_CHOICES = [
        ('Control_total', 'Control total'),
        ('Lecture', 'Lecture'),
        ('collaboration_avec_suppression', 'Collaboration avec suppression'),
        ('collaboration_sans_suppression', 'Collaboration sans suppression'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, default=None)
    proprietaire_groupe = models.ManyToManyField(UserApp, related_name='groupes_proprietaire', blank=True)
    autorisation = models.CharField(max_length=30, choices=AUTORISATION_CHOICES, blank=True)


class Sante(models.Model):
    site=models.ForeignKey(Site, on_delete=models.CASCADE,null=True, default=None)
    demande_de_conseils=models.CharField(max_length=255,blank=True, null=True,)
    demande_de_supervision=models.CharField(max_length=255,blank=True, null=True,)
    demande_de_reunion=models.CharField(max_length=255,blank=True, null=True,)
    demande_de_coaching=models.CharField(max_length=255,blank=True, null=True,)
    demande_de_groupe=models.CharField(max_length=255,blank=True, null=True,)
    comentaires=models.TextField(blank=True, null=True, default=None)
    demande_entretien=models.CharField(max_length=255,blank=True, null=True,)

class Qualite(models.Model):
    site=models.ForeignKey(Site, on_delete=models.CASCADE,null=True, default=None)
    titre=models.CharField(max_length=255,blank=True, null=True,)
    date_analyse = models.DateField(blank=True, null=True, default=None)
    reflexion=models.CharField(max_length=255,blank=True, null=True,)
    objectifs=models.CharField(max_length=255,blank=True, null=True,)
    commentaires_responsable=models.CharField(max_length=255,blank=True, null=True,)
    objectifs_annees=models.CharField(max_length=255,blank=True, null=True,)

class TypePartie(models.Model):
    nom=models.CharField(max_length=255,blank=True, null=True,)
    def __str__(self):
        return str(self.nom)

class PartiesInteresses(models.Model):
    typepartie=models.ForeignKey(TypePartie, on_delete=models.CASCADE,null=True, default=None)
    partieinteresse=models.CharField(max_length=255,blank=True, null=True,)
    importance=models.CharField(max_length=255,blank=True, null=True,)
    nature=models.CharField(max_length=255,blank=True, null=True,)
    enjeux=models.CharField(max_length=255,blank=True, null=True,)
    besoin=models.CharField(max_length=255,blank=True, null=True,)
    impactfinal=models.CharField(max_length=255,blank=True, null=True,)
    impactentreprise=models.CharField(max_length=255,blank=True, null=True,)
    cotation=models.CharField(max_length=255,blank=True, null=True,)
    impact=models.CharField(max_length=255,blank=True, null=True,)
    processus = models.ManyToManyField(Processus)
    def __str__(self):
        return self.partieinteresse


class Exigences(models.Model):
    type_exigence=models.CharField(max_length=255,blank=True, null=True,)
    intitule=models.CharField(max_length=255,blank=True, null=True,)
    evaluation_maitrise=models.CharField(max_length=255,blank=True, null=True,)
    description=models.CharField(max_length=255,blank=True, null=True,)
    commentaire=models.CharField(max_length=255,blank=True, null=True,)
    action=models.BooleanField(blank=True, null=True)
    partieinteresses= models.ManyToManyField(PartiesInteresses, null=True, blank=True, db_constraint=False)  
   

class AnalyseRisque(models.Model):
    site=models.ForeignKey(Site, on_delete=models.CASCADE,null=True, default=None)
    description=models.CharField(max_length=255,blank=True, null=True,)
    typologie=models.CharField(max_length=255,blank=True, null=True,)
    axe=models.CharField(max_length=255,blank=True, null=True,)
    famille=models.CharField(max_length=255,blank=True, null=True,)
    indice=models.CharField(max_length=255,blank=True, null=True,)
    niveau_risque=models.CharField(max_length=255,blank=True, null=True,)
    date_evaluation=models.DateField(blank=True, null=True)
    opportunite=models.CharField(max_length=255,blank=True, null=True,)
    origine=models.CharField(max_length=255,blank=True, null=True,)
    processus=models.ForeignKey(Processus, on_delete=models.CASCADE,null=True, default=None)
    contexte_int=models.CharField(max_length=255,blank=True, null=True,)
    contexte_ext=models.CharField(max_length=255,blank=True, null=True,)
    consequences=models.CharField(max_length=255,blank=True, null=True,)
    impact=models.CharField(max_length=255,blank=True, null=True,)
    probabilite=models.CharField(max_length=255,blank=True, null=True,)
    maitrise=models.CharField(max_length=255,blank=True, null=True,)
    mesure=models.CharField(max_length=255,blank=True, null=True,)
    type_action=models.CharField(max_length=255,blank=True, null=True,)
    partieinteresses= models.ManyToManyField(PartiesInteresses, null=True, blank=True, db_constraint=False) 


class Cotation(models.Model):
    maitrise=models.CharField(max_length=255,blank=True, null=True,)
    impact=models.CharField(max_length=255,blank=True, null=True,)
    probabilite=models.CharField(max_length=255,blank=True, null=True,)
    ipr=models.CharField(max_length=255,blank=True, null=True,)
    indice=models.CharField(max_length=255,blank=True, null=True,)
    date_evaluation=models.DateField(blank=True, null=True)
    analyserisque= models.ManyToManyField(AnalyseRisque, null=True, blank=True, db_constraint=False)


#suivie des contrôles réglementaires 

class Control(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    nature_control = models.CharField(max_length=255, blank=True)
    origine_reglementaire = models.CharField(max_length=255, blank=True)
    date_dernier_control = models.DateField(blank=True, null=True)
    date_control_suivant = models.DateField(blank=True, null=True)
    action_ouverte = models.CharField(max_length=255, blank=True, null=True)
    rapport = models.FileField(upload_to='documents/',blank=True)

class ConstatAudit(models.Model):
    intitule_constat = models.CharField(max_length=255,blank=True, null=True,)
    description_constat = models.CharField(max_length=255,blank=True, null=True,)
    type_constat = models.CharField(max_length=255,blank=True, null=True,)  
    audit_associe =  models.CharField(max_length=255,blank=True, null=True,)  
    site =models.ForeignKey(Site, on_delete=models.CASCADE,null=True, default=None)
    responsable_traitement = models.ManyToManyField(Utilisateur, null=True, blank=True, db_constraint=False)
    processus = models.ForeignKey(Processus, on_delete=models.CASCADE,null=True, default=None)
    date_reponse = models.DateField(blank=True, null=True)
    localisation =  models.CharField(max_length=255,blank=True, null=True,) 
    type_audit =  models.CharField(max_length=255,blank=True, null=True,) 
    rapport_audit =  models.FileField(upload_to='uploads/docs',
                            null=True,
                            blank=True,
                            default=None,                            
                            )   
   

class Pj(models.Model):
    nom = models.CharField(max_length=255, blank=True)
    url_document = models.FileField(upload_to='documents/', blank=True)
    date_modification = models.DateField(blank=True, null=True)
    modifie_par = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class RapportDaudit(models.Model): 
    nom = models.CharField(max_length=255, blank=True)
    url_document = models.FileField(upload_to='documents/', blank=True)
    date_modification = models.DateField(blank=True, null=True)
    modifie_par = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class CertificatCalibration(models.Model):
    nom = models.CharField(max_length=255, blank=True)
    url_document = models.FileField(upload_to='documents/', blank=True)
    date_modification = models.DateField(blank=True, null=True)
    modifie_par = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class AxesStrategiques(models.Model):
    axe=models.CharField(max_length=255,blank=True, null=True,)
    sigle=models.CharField(max_length=255,blank=True, null=True,)
    

















