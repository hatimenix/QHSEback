from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import (
    Commande,
    Danger,
    EvaluationDanger,
    FicheTechnique,
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
    EvaluationDangerSerializer,
    FicheTechniqueSerializer,
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

@csrf_exempt
def commandeApi(request, id=0):
    if request.method== 'GET':
        commandes= Commande.objects.all()
        commandeSerializer = CommandeSerializer(commandes,many=True)
        return JsonResponse(commandeSerializer.data, safe=False)
    elif request.method=='POST':
        commande_data= JSONParser().parse(request)
        commandeSerializer= CommandeSerializer(data=commande_data)
        if commandeSerializer.is_valid():
            commandeSerializer.save()
            return JsonResponse('Added successfully ', safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        commande_data = JSONParser().parse(request)
        commande = Commande.objects.get(id_commande=commande_data['id_commande'])
        commandeSerializer = CommandeSerializer(commande, data=commande_data)
        if commandeSerializer.is_valid():
            commandeSerializer.save()
            return JsonResponse('Update successfully ', safe=False)
        return JsonResponse('Failed to update', status=400)
    
    elif request.method=='DELETE':
        commande= Commande.objects.get(id_commande=id)
        commande.delete()
        return JsonResponse('Deleted successfully', safe=False)


# CRUD pour les fiches techniques BOCHRA
@csrf_exempt
def FicheApi(request, id=0):
    if request.method == 'GET':
        fiches = FicheTechnique.objects.all()
        
        ficheSerializer = FicheTechniqueSerializer(fiches, many=True)
        return JsonResponse(ficheSerializer.data, safe=False)
    
    elif request.method == 'POST':
        fiche_data = JSONParser().parse(request)
        ficheSerializer = FicheTechniqueSerializer(data=fiche_data)
        if ficheSerializer.is_valid():
            ficheSerializer.save()
            return JsonResponse('Added successfully ', safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method == 'PUT':
        fiche_data = JSONParser().parse(request)
        fiche = FicheTechnique.objects.get(id_fiche=fiche_data['id_fiche'])
        ficheSerializer = FicheTechniqueSerializer(fiche, data=fiche_data)
        if ficheSerializer.is_valid():
            ficheSerializer.save()
            return JsonResponse('Update successfully ', safe=False)
        return JsonResponse('Failed to update', status=400)
    
    elif request.method == 'DELETE':
        fiche = FicheTechnique.objects.get(id_fiche=id)
        fiche.delete()
        return JsonResponse('Deleted successfully', safe=False)
    
