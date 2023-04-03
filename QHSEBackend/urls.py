from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from QHSEApi import views
from QHSEBackend import settings

router = DefaultRouter()
router.register(r'site', views.SiteViewSet, basename="site")
router.register(r'service', views.ServiceViewSet, basename="service")
router.register(r'evaluation', views.EvaluationDangerViewSet, basename="evaluation")
router.register(r'danger', views.DangerViewSet, basename="danger")
router.register(r'evenement', views.EvenementViewSet, basename="evenement")
router.register(r'analyse_evenement', views.AnalyseEvenementViewSet, basename="analyse_evenement")
router.register(r'arret_travail', views.ArretTravailViewSet, basename="arret_travail")
router.register(r'action', views.ActionsViewSet, basename="action")
router.register(r'realisation', views.RealisationViewSet, basename="realisation")
router.register(r'tache', views.TachesViewSet, basename="tache")
router.register(r'mesure_efficacite', views.MesureEfficaciteViewSet, basename="mesure_efficacite")
router.register(r'processus', views.ProcessusViewSet, basename="processus")
#les routes pour commande et fiche 
router.register(r'commande', views.CommandeViewSet, basename="commande")
router.register(r'fiche', views.FicheViewSet, basename="fiche")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
