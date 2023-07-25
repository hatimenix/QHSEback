from django.contrib import admin
from .models import NC, Commande, Documents, FicheTechnique, Menus, Site, Utilisateur,Services,Famille,Danger,EvaluationDanger,Evenements,AnalyseEvenement,ArretTravail,Processus,Actions,Realisation,Taches,MesureEfficacite
# Register your models here.

admin.site.register(NC)
admin.site.register(Utilisateur)
admin.site.register(Site)
admin.site.register(Services)
admin.site.register(Famille)
admin.site.register(Danger)
admin.site.register(EvaluationDanger)
admin.site.register(Evenements)
admin.site.register(AnalyseEvenement)
admin.site.register(ArretTravail)
admin.site.register(Processus)
admin.site.register(Actions)
admin.site.register(Realisation)
admin.site.register(Taches)
admin.site.register(MesureEfficacite)
admin.site.register(FicheTechnique)
admin.site.register(Commande)
admin.site.register(Documents)
admin.site.register(Menus)

