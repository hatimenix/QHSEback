import re
import requests

from argparse import _ActionsContainer
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
import requests
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import (
    Commande,
    Danger,
    Document,
    
    EvaluationDanger,
    FicheTechnique,
    Secteurs,
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
)
from .serializers import (
    CommandeSerializer,
    DangerSerializer,
    DocumentSerializer,
    EvaluationDangerSerializer,
    FicheTechniqueSerializer,
    
    SecteursSerializer,
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

class SecteurViewSet(viewsets.ModelViewSet):
    queryset = Secteurs.objects.all()
    serializer_class = SecteursSerializer

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


# CRUD pour les commandes BOCHRA

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


# CRUD pour les fiches techniques BOCHRA


class FicheTechniqueView(APIView):
    def get(self, request, pk):
        fiche = get_object_or_404(FicheTechnique, pk=pk)
        filename = fiche.fichier.name.split('/')[-1]
        file_url = request.build_absolute_uri(fiche.fichier.url)
        return Response({'nom_fiche': fiche.nom_fiche, 'file_url': file_url, 'filename': filename})



class FicheViewSet(viewsets.ModelViewSet):
    queryset = FicheTechnique.objects.all()
    serializer_class = FicheTechniqueSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        view = FicheTechniqueView.as_view()
        response = view(request=request, pk=pk)
        nom_fiche = response.data['nom_fiche']
        file_url = response.data['file_url']
        filename = response.data['filename']

        # Créer une réponse pour le téléchargement du fichier avec le nom de fichier correct
        response = FileResponse(requests.get(file_url, stream=True).raw)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response

#Document Views Bochra
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    

    
  