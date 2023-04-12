from rest_framework import serializers

from .models import Site, Services, Danger, EvaluationDanger, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches,NC,Secteurs,Equipement
from .models import NC, Commande, DocumentUtilities, Evaluation, Famille, FicheTechnique, Fournisseur, Site, Services, Danger, EvaluationDanger, Traitement, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches
from .models import Site, Services, Danger, Famille, EvaluationDanger, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches
from .models import Commande, FicheTechnique, Site, Services, Danger, EvaluationDanger, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches
from .models import Commande, Document, FicheTechnique, Secteurs, Site, Services, Danger, EvaluationDanger, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches



class SiteSerializer(serializers.ModelSerializer):
    responsable_name = serializers.CharField(source='responsable_site.nom', default=None)
    class Meta:
        model = Site
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class SecteursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secteurs
        fields = '__all__'

class DangerSerializer(serializers.ModelSerializer):
    famille_name = serializers.CharField(source='famille.famille_nom', default=None)
    Site_name = serializers.CharField(source='site.site_nom', default=None)
    service_name = serializers.CharField(source='service.service_nom', default=None)
    class Meta:
        model = Danger
        fields = '__all__'

#FamilleSerializer
class FamilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famille
        fields = '__all__'

class EvaluationDangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationDanger
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class ChefServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefServices
        fields = '__all__'

class EvenementSerializer(serializers.ModelSerializer):
    danger_name = serializers.SerializerMethodField()
    Site_name = serializers.CharField(source='site.site_nom', read_only=True, default=None)
    service_name = serializers.CharField(source='service.service_nom', read_only=True, default=None)
    class Meta:
        model = Evenements
        fields = '__all__'
    def get_danger_name(self, obj):
        dangers = obj.dangers.all()
        if dangers:
            return ', '.join(d.description for d in dangers)
        else:
            return None

class AnalyseEvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyseEvenement
        fields = '__all__'

class ArretTravailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArretTravail
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

class RealisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisation
        fields = '__all__'

class MesureEfficaciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureEfficacite
        fields = '__all__'

class ProcessusSerializer(serializers.ModelSerializer):
    pilote_name = serializers.CharField(source='pilote.nom', default=None)
                                        
    class Meta:
        model = Processus
        fields = '__all__'

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taches
        fields = '__all__'

class CustomBooleanField(serializers.BooleanField):
    def to_representation(self, value):
        if value:
            return 'Oui'
        return 'non'

class NCSerializer(serializers.ModelSerializer):
    
    frequence = CustomBooleanField()
    gravite = CustomBooleanField()
    action_immediate = CustomBooleanField()
    nc_cloture = CustomBooleanField()
    
    processus_name = serializers.ReadOnlyField(source='processus.processus_nom',default=None)
    site_name = serializers.ReadOnlyField(source='site.site_nom',default=None)
    responsable_name = serializers.ReadOnlyField(source='responsable_traitement.nom',default=None)


    class Meta:
        model = NC
        fields = '__all__'

class SecteursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secteurs
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):

    secteur_name = serializers.ReadOnlyField(source='secteur.secteur_nom',default=None)
    site_name = serializers.ReadOnlyField(source='site.site_nom',default=None)


    class Meta:
        model = Equipement
        fields = '__all__'


class FamilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famille

#Serializer pour la fiche technique BOCHRA 
class FicheTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheTechnique
        fields = '__all__'

#Serializer pour la commande BOCHRA
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

#Achraf's serialisers 

#RGPD MODULE
  # SOUS MODULE REGISTRE DE TRAITEMENT

#Fournisseur serializers
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'

#Traitement serializers
class TraitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        fields = '__all__'

#Evaluation serializers
class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

#Document utiles  serializers
class DocumentUtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentUtilities
        fields = '__all__'

#ilyas
#NC
class NCSerializer(serializers.ModelSerializer):
    class Meta:

        processus_name = serializers.ReadOnlyField(source='processus.processus_nom',default=None)
        site_name = serializers.ReadOnlyField(source='site.site_nom',default=None)
        responsable_name = serializers.ReadOnlyField(source='responsable_traitement.nom',default=None)

    model = NC
    fields = '__all__'
        
#Serializers Documentation 

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

