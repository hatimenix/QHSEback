from rest_framework import serializers
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
    class Meta:
        model = Danger
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
    class Meta:
        model = Evenements
        fields = '__all__'

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
        
#Serializers Documentation 

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
