from rest_framework import serializers
from .models import Site, Services, Danger, Famille, EvaluationDanger, Utilisateur, ChefServices, Evenements, AnalyseEvenement, ArretTravail, Actions, Realisation, MesureEfficacite, Processus, Taches

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class DangerSerializer(serializers.ModelSerializer):
    famille_name = serializers.CharField(source='famille.famille_nom', default=None)
    Site_name = serializers.CharField(source='site.site_nom', default=None)
    service_name = serializers.CharField(source='service.service_nom', default=None)
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
    class Meta:
        model = Processus
        fields = '__all__'

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taches
        fields = '__all__'

class FamilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famille
        fields = '__all__'