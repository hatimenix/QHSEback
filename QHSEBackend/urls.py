from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from QHSEApi import views
from django.contrib.auth import views as auth_views


#jwt login imports


#end imports

router = DefaultRouter()
router.register(r'site', views.SiteViewSet, basename="site")
router.register(r'service', views.ServiceViewSet, basename="service")
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
router.register(r'fiche_technique', views.FicheTechniqueViewSet, basename="fiche_technique")
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
router.register(r'qualite', views.QualiteViewSet, basename="qualite")
router.register(r'typePartie', views.TypePartieViewSet, basename="typePartie")
router.register(r'partiesInteresses', views.PartiesInteressesViewSet, basename="partiesInteresses")
router.register(r'exigences', views.ExigencesViewSet, basename="exigences")
router.register(r'analyseRisque', views.AnalyseRisqueViewSet, basename="analyseRisque")
router.register(r'cotation', views.CotationViewSet, basename="cotation")
router.register(r'source', views.SourceViewSet, basename="source")
router.register(r'constataudit', views.ConstatAuditViewSet, basename="constataudit")
router.register(r'planalimentaire', views.PlanAlimentaireViewSet, basename="planalimentaire")

router.register(r'exercicesecurite', views.ExerciceSecuriteViewSet, basename="exercicesecurite")
router.register(r'reunion', views.ReunionViewSet, basename="reunion")


#suivie des contrôles réglementaires 
router.register(r'control', views.ControlViewSet, basename="control")
# Récents
router.register(r'pj', views.PJViewSet, basename="pj")
router.register(r'rapportAudit', views.RapportDauditViewSet, basename="rapportAudit")
router.register(r'CertificatCalibration', views.CertificatCalibrationViewSet, basename="CertificatCalibration")
router.register(r'AxesStrategiques', views.AxesStrategiquesViewSet, basename="AxesStrategiques")


###########################
router.register(r'felicitationRP', views.FelicitationRPViewSet, basename="felicitationRP")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #login imports 
    path('userapp/check_email_exists/', views.check_email_exists, name='check_email_exists'),

    path('api/login/', views.UserTokenObtainPairView.as_view(), name='login'),
    path('user/', views.UserDetailsAPIView.as_view(), name='get_authenticated_user'),
    path('groups/<int:group_id>/', views.GroupDetailsAPIView.as_view(), name='group_details'),
    path('nc/<int:nc_id>/file-url/', views.get_existing_file_url, name='get_existing_file_url'),
    path('api/reset-password/', views.send_password_reset_email, name='send_password_reset_email'),

    path('api/change_password/', views.ChangePasswordView.as_view(), name='change_password'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
