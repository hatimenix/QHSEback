
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import action
from rest_framework import viewsets
import requests
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
from rest_framework import viewsets
import requests


from .models import (
    NC,
    Commande,
    Danger,
    DocumentUtilities,
    Evaluation,
    EvaluationDanger,
    Famille,
    FicheTechnique,
    Fournisseur,
    Secteurs,
    Site,
    Services,
    Traitement,
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
    CommandeSerializer,
    DangerSerializer,
    DocumentUtilitiesSerializer,
    EvaluationDangerSerializer,
    EvaluationSerializer,
    FamilleSerializer,
    FicheTechniqueSerializer,
    FournisseurSerializer,
    NCSerializer,
    SecteursSerializer,
    SiteSerializer,
    ServiceSerializer,
    TraitementSerializer,
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

#FamilleViewSet
class FamilleViewSet(viewsets.ModelViewSet):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer


class EvaluationDangerViewSet(viewsets.ModelViewSet):
    queryset = EvaluationDanger.objects.all()
    serializer_class = EvaluationDangerSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class SecteursViewSet(viewsets.ModelViewSet):
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


class FamilleViewSet(viewsets.ModelViewSet):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

# CRUD pour les commandes BOCHRA


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


# CRUD pour les fiches techniques BOCHRA


class FicheTechniqueViewSet (viewsets.ModelViewSet):
    queryset = FicheTechnique.objects.all()
    serializer_class = FicheTechniqueSerializer


    

class FicheViewSet(viewsets.ModelViewSet):
    queryset = FicheTechnique.objects.all()
    serializer_class = FicheTechniqueSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        view = FicheTechniqueViewSet.as_view()
        response = view(request=request, pk=pk)
        nom_fiche = response.data['nom_fiche']
        file_url = response.data['file_url']
        filename = response.data['filename']

        # Créer une réponse pour le téléchargement du fichier avec le nom de fichier correct
        response = FileResponse(requests.get(file_url, stream=True).raw)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response

#Achraf's views set 

#RGPD MODULE
  #REGISTRE DE TRAITEMENT
#Fournisseur view Set Crud
class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

#Traitement view set Crud
class TraitementViewSet(viewsets.ModelViewSet):
    queryset = Traitement.objects.all()
    serializer_class = TraitementSerializer
    
#Traitement view set Crud
class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

#Docuements utiles

class DocumentutilesViewSet(viewsets.ModelViewSet):
    queryset = DocumentUtilities.objects.all()
    serializer_class = DocumentUtilitiesSerializer


#Ilyas
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


    

    
  

