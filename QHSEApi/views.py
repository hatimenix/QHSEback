
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import action
from rest_framework import viewsets
import requests
import re
import requests
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
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
    Documents,
    Evaluation,
    EvaluationDanger,
    Famille,
    FavorisDocument,
    FicheTechnique,
    Fournisseur,
    HistoriqueDocument,
    Menus,
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
    DocumentsSerializer,
    EvaluationDangerSerializer,
    EvaluationSerializer,
    FamilleSerializer,
    FavorisDocumentSerializer,
    FicheTechniqueSerializer,
    FournisseurSerializer,
    HistoriqueDocumentSerializer,
    MenusSerializer,
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



class FicheTechniqueViewSet(viewsets.ModelViewSet):
    queryset = FicheTechnique.objects.all()
    serializer_class = FicheTechniqueSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        fiche = self.get_object()
        file_path = fiche.fichier.path
        file_name = fiche.fichier.name.split('/')[-1]
        file = open(file_path, 'rb')
        response = FileResponse(file, as_attachment=True, filename=file_name)
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

    @api_view(['GET'])
    def download_file(request, pk):
        piece_jointe = get_object_or_404(NC, pk=pk)
        response = FileResponse(piece_jointe.file)
        response['Content-Disposition'] = 'attachment; filename={}'.format(piece_jointe.filename)
        return response


class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

    @api_view(['GET'])
    def download_file(request, pk):
        Certificat = get_object_or_404(Equipement, pk=pk)
        response = FileResponse(Certificat.file)
        response['Content-Disposition'] = 'attachment; filename={}'.format(Certificat.filename)
        return response
   
#Document


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
  
class HistoriqueDocumentViewSet(viewsets.ModelViewSet):
    queryset = HistoriqueDocument.objects.all()
    serializer_class = HistoriqueDocumentSerializer

class FavorisDocumentViewSet(viewsets.ModelViewSet):
    queryset = FavorisDocument.objects.all()
    serializer_class = FavorisDocumentSerializer

class MenusViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Loop through the menus and extract the filenames
        for menu in serializer.data:
            if menu['menus_generaux'] is not None:
                menu['menus_generaux'] = menu['menus_generaux'].split('/')[-1]
            if menu['menus_dessert'] is not None:
                menu['menus_dessert'] = menu['menus_dessert'].split('/')[-1]
            if menu['menu_s1'] is not None:
                menu['menu_s1'] = menu['menu_s1'].split('/')[-1]
            if menu['menu_s2'] is not None:
                menu['menu_s2'] = menu['menu_s2'].split('/')[-1]
            if menu['menu_s3'] is not None:
                menu['menu_s3'] = menu['menu_s3'].split('/')[-1]
            if menu['menu_s4'] is not None:
                menu['menu_s4'] = menu['menu_s4'].split('/')[-1]
            if menu['menu_s5'] is not None:
                menu['menu_s5'] = menu['menu_s5'].split('/')[-1]

        return Response(serializer.data)

    

  
