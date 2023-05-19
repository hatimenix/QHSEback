from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from QHSEApi import views



router = DefaultRouter()
router.register(r'site', views.SiteViewSet, basename="site")
router.register(r'service', views.ServiceViewSet, basename="service")
router.register(r'chefservice', views.ChefServiceViewSet, basename="chefservice")
router.register(r'utilisateur', views.UtilisateurViewSet, basename="utilisateur")
router.register(r'evaluation_danger', views.EvaluationDangerViewSet, basename="evaluation")
router.register(r'danger', views.DangerViewSet, basename="danger")
router.register(r'evenement', views.EvenementViewSet, basename="evenement")
router.register(r'analyse_evenement', views.AnalyseEvenementViewSet, basename="analyse_evenement")
router.register(r'arret_travail', views.ArretTravailViewSet, basename="arret_travail")
router.register(r'action', views.ActionsViewSet, basename="action")
router.register(r'realisation', views.RealisationViewSet, basename="realisation")
router.register(r'tache', views.TachesViewSet, basename="tache")
router.register(r'mesure_efficacite', views.MesureEfficaciteViewSet, basename="mesure_efficacite")
router.register(r'processus', views.ProcessusViewSet, basename="processus")
router.register(r'secteurs', views.SecteursViewSet, basename="secteurs")
router.register(r'equipement', views.EquipementViewSet, basename="equipement")
router.register(r'famille', views.FamilleViewSet, basename="famille")
#les routes pour commande et fiche 
router.register(r'commande', views.CommandeViewSet, basename="commande")
router.register(r'fournisseurs',views.FournisseurViewSet)
router.register(r'traitements', views.TraitementViewSet)
#router.register(r'evaluations',views.EvaluationViewSet)
router.register(r'Documentsutile',views.DocumentutilesViewSet)
router.register(r'nc', views.NCViewSet, basename="nc")
router.register(r'famille', views.FamilleViewSet, basename="famille")
router.register(r'documentation', views.DocumentsViewSet, basename="documentation")
router.register(r'historiqueDocument', views.HistoriqueDocumentViewSet, basename="historiqueDocument")
router.register(r'favorisDocument', views.FavorisDocumentViewSet, basename="favorisDocument")
router.register(r'menus', views.MenusViewSet, basename="menus")
#users and groupes 
router.register(r'userapp', views.UserAppViewSet, basename="userapp")
router.register(r'groupeUser', views.GroupeUserViewSet, basename="groupeUser")
router.register(r'sante', views.SanteViewSet, basename="sante")


###########################


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
