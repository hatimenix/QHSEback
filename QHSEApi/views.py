from base64 import urlsafe_b64encode
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from rest_framework.decorators import action
from rest_framework import viewsets
import requests
import re
import requests
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from argparse import _ActionsContainer
from django.http import FileResponse, HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.http import require_GET
from django.db.models import Count
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.core.mail import send_mail

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.tokens import default_token_generator




from rest_framework import viewsets
from rest_framework import viewsets
import requests
#logi imports 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings

#login imports 
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.views.decorators.http import require_POST


from .models import (
    NC,
    AnalyseRisque,
    CertificatCalibration,
    Commande,
    Cotation,
    Control,
    Danger,
    DocumentUtilities,
    Documents,
    Evaluation,
    EvaluationDanger,
    Exigences,
    Famille,
    FavorisDocument,
    FelicitationRP,
    FicheTechnique,
    Fournisseur,
    GroupeUser,
    HistoriqueDocument,
    Menus,
    PartiesInteresses,
    Pj,
    RapportDaudit,
    Secteurs,
    Site,
    Services,
    Source,
    Traitement,
    TypePartie,
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
    Sante,
    Qualite,
    ConstatAudit

)
from .serializers import (
    
    AnalyseRisqueSerializer,
    CertificatCalibrationSerializer,
    CommandeSerializer,
    ConstatAuditSerializer,
    ControlSerializer,
    CotationSerializer,
    DangerSerializer,
    DocumentUtilitiesSerializer,
    DocumentsSerializer,
    EvaluationDangerSerializer,
    EvaluationSerializer,
    ExigencesSerializer,
    FamilleSerializer,
    FavorisDocumentSerializer,
    FelicitationRPSerializer,
    
    FicheTechniqueSerializer,
    FournisseurSerializer,

    GroupeUserSerializer,
    HistoriqueDocumentSerializer,
    MenusSerializer,
    NCSerializer,
    PJSerializer,
    PartiesInteressesSerializer,
    RapportDauditSerializer,
    SecteursSerializer,
    SiteSerializer,
    ServiceSerializer,
    SourceSerializer,
    TraitementSerializer,
    TypePartieSerializer,
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
    SanteSerializer,
    QualiteSerializer,
    ConstatAuditSerializer
)
#login 
# Authentication
@require_POST
def check_email_exists(request):
    email = request.POST.get('email')

    if email:
        email_exists = UserApp.objects.filter(email=email).exists()
        return JsonResponse({'exists': email_exists})

    return JsonResponse({'error': 'Invalid email'})


class UserTokenObtainPairView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        
        try:
            user = UserApp.objects.get(email=email)
            
            if not user.check_password(password):
                return Response(
                    {"message": "Incorrect password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            refresh = RefreshToken.for_user(user)
            
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                }
            )
       
        except UserApp.DoesNotExist:
            return Response(
                {"message": "Incorrect email"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except:
            return Response(
                {"message": "Both email and password are incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
#Details Users 
class UserDetailsAPIView(APIView):

    def get(self, request):
        user = request.user
        # Add any additional logic or data processing you need here
        serialized_user = UserAppSerializer(user).data  # Replace UserSerializer with your user serializer
        return Response(serialized_user)

#Details Group 

class GroupDetailsAPIView(APIView):
    def get(self, request, group_id):
        try:
            group = GroupeUser.objects.get(id=group_id)
        except GroupeUser.DoesNotExist:
            return Response(
                {"message": "Group not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = GroupeUserSerializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)



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

    @action(detail=False, methods=['GET'])
    def stats_by_type_action(self, request):
        stats = Actions.objects.values('type_action').annotate(count=Count('id'))
        return Response(stats)


class RealisationViewSet(viewsets.ModelViewSet):
    queryset = Realisation.objects.all()
    serializer_class = RealisationSerializer


class TachesViewSet(viewsets.ModelViewSet):
    queryset = Taches.objects.all()
    serializer_class = TacheSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

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
    
    @action(detail=False, methods=['GET'])
    def stats_by_nature(self, request):
        stats = NC.objects.values('nature').annotate(count=Count('id'))
        return Response(stats)

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

class QualiteViewSet(viewsets.ModelViewSet):
    queryset = Qualite.objects.all()
    serializer_class = QualiteSerializer

class TypePartieViewSet(viewsets.ModelViewSet):
    queryset = TypePartie.objects.all()
    serializer_class = TypePartieSerializer

class PartiesInteressesViewSet(viewsets.ModelViewSet):
    queryset = PartiesInteresses.objects.all()
    serializer_class = PartiesInteressesSerializer

class ExigencesViewSet(viewsets.ModelViewSet):
    queryset = Exigences.objects.all()
    serializer_class = ExigencesSerializer

class AnalyseRisqueViewSet(viewsets.ModelViewSet):
    queryset = AnalyseRisque.objects.all()
    serializer_class = AnalyseRisqueSerializer

class CotationViewSet(viewsets.ModelViewSet):
    queryset = Cotation.objects.all()
    serializer_class = CotationSerializer
 
@require_GET
def get_existing_file_url(request, nc_id):
    try:
        nc = NC.objects.get(id=nc_id)
        file_url = nc.piece_jointe.url if nc.piece_jointe else None
        return JsonResponse({'file_url': file_url})
    except NC.DoesNotExist:
        return JsonResponse({'error': 'NC not found'}, status=404)
    

  
class ConstatAuditViewSet(viewsets.ModelViewSet):
    queryset = ConstatAudit.objects.all()
    serializer_class = ConstatAuditSerializer
#suivie des contrôles réglementaires

class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer



# class PreviousControlViewSet(viewsets.ModelViewSet):
#     queryset = PreviousControl.objects.all()
#     serializer_class = PreviousControlSerializer

class PJViewSet(viewsets.ModelViewSet):
    queryset = Pj.objects.all()
    serializer_class = PJSerializer

class RapportDauditViewSet(viewsets.ModelViewSet):
    queryset = RapportDaudit.objects.all()
    serializer_class = RapportDauditSerializer

class CertificatCalibrationViewSet(viewsets.ModelViewSet):
    queryset = CertificatCalibration.objects.all()
    serializer_class = CertificatCalibrationSerializer

class FelicitationRPViewSet(viewsets.ModelViewSet):
    queryset = FelicitationRP.objects.all()
    serializer_class = FelicitationRPSerializer

#RESET PASSWORD 
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
UserApp = get_user_model()
@csrf_exempt
@require_POST
def send_password_reset_email(request):
    email = request.POST.get('email')
    
    if email:
        user = get_object_or_404(UserApp, email=email)
        token = default_token_generator.make_token(user)
        reset_link = f"http://localhost:4200/reset-password/{user.pk}/{token}"
        
        send_mail(
            'Password Reset',
            f'Please click the following link to reset your password: {reset_link}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        
        return JsonResponse({'message': 'Password reset email sent.'})
    
    return JsonResponse({'error': 'Invalid email'})


@csrf_exempt
@require_POST
def reset_password(request, user_id, token):
    password = request.POST.get('password')
    
    if password:
        user = get_object_or_404(UserApp, pk=user_id)
        
        if default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            
            return JsonResponse({'message': 'Password reset successful.'})
        
        return JsonResponse({'error': 'Invalid token'})
    
    return JsonResponse({'error': 'Invalid password'})