from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import action
from rest_framework import viewsets
import requests
from .models import (
    Danger,
    EvaluationDanger,
    Site,
    Services,
    Utilisateur,
    ChefServices,
    Evenements,
    AnalyseEvenement,
    ArretTravail,
    Actions,
    Realisation,
    Taches,
    MesureEfficacite,
    Processus,
    NC,
    Secteurs,
    Equipement
)
from .serializers import (
    DangerSerializer,
    EvaluationDangerSerializer,
    SiteSerializer,
    ServiceSerializer,
    UtilisateurSerializer,
    ChefServiceSerializer,
    EvenementSerializer,
    AnalyseEvenementSerializer,
    ArretTravailSerializer,
    ActionSerializer,
    RealisationSerializer,
    TacheSerializer,
    MesureEfficaciteSerializer,
    ProcessusSerializer,
    NCSerializer,
    SecteursSerializer,
    EquipementSerializer
)


class DangerViewSet(viewsets.ModelViewSet):
    queryset = Danger.objects.all()
    serializer_class = DangerSerializer


class EvaluationDangerViewSet(viewsets.ModelViewSet):
    queryset = EvaluationDanger.objects.all()
    serializer_class = EvaluationDangerSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class ChefServiceViewSet(viewsets.ModelViewSet):
    queryset = ChefServices.objects.all()
    serializer_class = ChefServiceSerializer


class EvenementViewSet(viewsets.ModelViewSet):
    queryset = Evenements.objects.all()
    serializer_class = EvenementSerializer


class AnalyseEvenementViewSet(viewsets.ModelViewSet):
    queryset = AnalyseEvenement.objects.all()
    serializer_class = AnalyseEvenementSerializer


class ArretTravailViewSet(viewsets.ModelViewSet):
    queryset = ArretTravail.objects.all()
    serializer_class = ArretTravailSerializer


class ActionsViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionSerializer


class RealisationViewSet(viewsets.ModelViewSet):
    queryset = Realisation.objects.all()
    serializer_class = RealisationSerializer


class TachesViewSet(viewsets.ModelViewSet):
    queryset = Taches.objects.all()
    serializer_class = TacheSerializer


class MesureEfficaciteViewSet(viewsets.ModelViewSet):
    queryset = MesureEfficacite.objects.all()
    serializer_class = MesureEfficaciteSerializer


class ProcessusViewSet(viewsets.ModelViewSet):
    queryset = Processus.objects.all()
    serializer_class = ProcessusSerializer

#Create,update,retrieve and delete table non-conformité :
class NCViewSet(viewsets.ModelViewSet):
    queryset = NC.objects.all()
    serializer_class = NCSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        view = NC.as_view()
        response = view(request=request, pk=pk)
        piece_jointe = response.data['piece jointe']
        file_url = response.data['file_url']
        filename = response.data['filename']

        # Créer une réponse pour le téléchargement du fichier avec le nom de fichier correct
        response = (requests.get(file_url, stream=True).raw)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
    
class SecteursViewSet(viewsets.ModelViewSet):
    queryset = Secteurs.objects.all()
    serializer_class = SecteursSerializer

class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        view = NC.as_view()
        response = view(request=request, pk=pk)
        certificat = response.data['certificat']
        file_url = response.data['file_url']
        filename = response.data['filename']

        # Créer une réponse pour le téléchargement du fichier avec le nom de fichier correct
        response = (requests.get(file_url, stream=True).raw)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response