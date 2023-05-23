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
#logi imports 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
#login imports 
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.hashers import check_password

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
    GroupeUser,
    HistoriqueDocument,
    Menus,
    Secteurs,
    Site,
    Services,
    Traitement,
    UserApp,
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
    Equipement,
    Sante

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
    GroupeUserSerializer,
    HistoriqueDocumentSerializer,
    MenusSerializer,
    NCSerializer,
    SecteursSerializer,
    SiteSerializer,
    ServiceSerializer,
    TraitementSerializer,
    UserAppSerializer,
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
    EquipementSerializer,
    SanteSerializer
)
#login 
# Authentication
class UserTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        email = request.data.get("adresse_email")
        password = request.data.get("password")
        try:
            user = UserApp.objects.get(adresse_email=email)
            
            
            if not user.check_password(password):
                    return Response(
                        {"message": "Email ou mot de passe invalide"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            refresh = RefreshToken.for_user(user)
            
            return Response(
                    {
                        "access": str(refresh.access_token),
                        "user": {user.nom_complet, user.adresse_email},
                        "refresh": str(refresh),
                    }
                )
       
        except UserApp.DoesNotExist:
            return Response(
                {"message": "Email ou mot de passe invalide2"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    #Details Users 
class UserDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Add any additional logic or data processing you need here
        serialized_user = UserAppSerializer(user).data  # Replace UserSerializer with your user serializer
        return Response(serialized_user)

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
    @api_view(['GET'])
    def download_file(request, pk):
        document = get_object_or_404(DocumentUtilities, pk=pk)
        response = FileResponse(document.file)
        response['Content-Disposition'] = 'attachment; filename={}'.format(document.filename)
        return response


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

#User and groupes 
class UserAppViewSet(viewsets.ModelViewSet):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer

class GroupeUserViewSet(viewsets.ModelViewSet):
    queryset = GroupeUser.objects.all()
    serializer_class = GroupeUserSerializer

#Authentication 

class SanteViewSet(viewsets.ModelViewSet):
    queryset = Sante.objects.all()
    serializer_class = SanteSerializer
 

  


    

  
