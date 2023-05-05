from rest_framework import serializers
from .models import  Documents, HistoriqueDocument, Menus, Site, Services, Danger, EvaluationDanger, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches,NC,Secteurs,Equipement,Traitement,Commande, DocumentUtilities, Evaluation, Famille, FicheTechnique, Fournisseur
from QHSEApi import models





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
    danger_name = serializers.SerializerMethodField()
    class Meta:
        model = AnalyseEvenement
        fields = '__all__'
    def get_danger_name(self, obj):
        danger_lie = obj.danger_lie.all()
        if danger_lie:
            return ', '.join(d.description for d in danger_lie)
        else:
            return None

class ArretTravailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArretTravail
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    danger_name = serializers.SerializerMethodField()
    evenement_name = serializers.SerializerMethodField()
    Proccesus_name = serializers.CharField(source='processus.intitule',default=None)
    Site_name = serializers.CharField(source='site.site_nom', read_only=True, default=None)
    class Meta:
        model = Actions
        fields = '__all__'
    def get_danger_name(self, obj):
        danger = obj.danger.all()
        if danger:
            return ', '.join(d.description for d in danger)
        else:
            return None
            
    def get_evenement_name(self, obj):
        evenement = obj.evenement.all()
        if evenement:
            return ', '.join(e.intitule for e in evenement)
        else:
            return None

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
    image = serializers.SerializerMethodField()
    class Meta:
        model = DocumentUtilities
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None


#ilyas

class NCSerializer(serializers.ModelSerializer):


    processus_name = serializers.ReadOnlyField(source='processus.intitule')
    site_name = serializers.ReadOnlyField(source='site.site_nom')
    responsable_name = serializers.ReadOnlyField(source='responsable_traitement.nom')

    class Meta:
        model = NC
        fields = '__all__'


#Documentation  serializers
class DocumentsSerializer(serializers.ModelSerializer):
    processus_name = serializers.ReadOnlyField(source='processus.intitule')
    site_name = serializers.ReadOnlyField(source='site.site_nom')
    secteur_name = serializers.ReadOnlyField(source='secteur.secteur_nom')
    personnel_name = serializers.ReadOnlyField(source='utilisateur.nom')
    url_document = serializers.SerializerMethodField()

    class Meta:
        model = Documents 
        fields = '__all__'

    def get_url_document(self, obj):
        if obj.url_document:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.url_document.url)
        return None



class HistoriqueDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueDocument
        fields = '__all__'

class FavorisDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueDocument
        fields = '__all__'

#menu serializer 

class MenusSerializer(serializers.ModelSerializer):
    site_name = serializers.ReadOnlyField(source='site.site_nom',default=None)
    class Meta: 
        model = Menus
        fields = '__all__'
    



