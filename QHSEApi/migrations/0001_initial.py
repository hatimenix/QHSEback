# Generated by Django 4.2 on 2023-04-28 14:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=100)),
                ('type_action', models.CharField(max_length=100)),
                ('origine_action', models.CharField(max_length=50)),
                ('reference', models.CharField(blank=True, max_length=100)),
                ('domaine', models.CharField(max_length=100)),
                ('analyse_cause', models.CharField(max_length=255)),
                ('plan_action', models.TextField()),
                ('delai_mise_en_oeuvre', models.DateField()),
                ('assigne_a', models.CharField(max_length=100)),
                ('priorite', models.IntegerField()),
                ('delai_mesure_eff', models.DateField()),
                ('type_critere_eff', models.CharField(max_length=100)),
                ('detail_critere_eff', models.TextField()),
                ('etat', models.CharField(default='Non commencé', max_length=150)),
                ('annee', models.DateField(auto_now=True)),
                ('piece_jointe', models.FileField(blank=True, default=None, null=True, upload_to='uploads/docs', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'pptx'])])),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id_commande', models.AutoField(primary_key=True, serialize=False)),
                ('date_commande', models.CharField(max_length=50)),
                ('type_commande', models.CharField(max_length=50)),
                ('etat_commande', models.CharField(max_length=50)),
                ('quantite', models.IntegerField()),
                ('specificite_regime', models.CharField(max_length=50)),
                ('specificite_texture', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Danger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste_de_travail', models.CharField(max_length=255)),
                ('taches', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('consequences', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('codification', models.CharField(max_length=255)),
                ('version', models.IntegerField()),
                ('date_approbation', models.DateField()),
                ('date_previsionnelle', models.DateField()),
                ('nv_version', models.CharField(max_length=255)),
                ('type_docs', models.CharField(max_length=255)),
                ('url_document', models.FileField(blank=True, upload_to='documents/')),
                ('icon', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentUtilities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=255)),
                ('modified_by', models.CharField(blank=True, max_length=255)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('typologie', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('famille_nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FicheTechnique',
            fields=[
                ('id_fiche', models.AutoField(primary_key=True, serialize=False)),
                ('fichier', models.FileField(default=None, null=True, upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'odt'])])),
                ('nom_fiche', models.CharField(max_length=255)),
                ('type_plat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('numerodesiret', models.CharField(blank=True, max_length=255, null=True)),
                ('type_de_prestation', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_de_recepisse_de_declaration_prefectorale', models.CharField(blank=True, max_length=255, null=True)),
                ('pageweb', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('numerodetelecopie', models.CharField(blank=True, max_length=255, null=True)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('codepostal', models.CharField(blank=True, max_length=255, null=True)),
                ('ville', models.CharField(blank=True, max_length=255, null=True)),
                ('pays', models.CharField(blank=True, max_length=255, null=True)),
                ('nometprenom', models.CharField(blank=True, max_length=255, null=True)),
                ('adressedecourier', models.CharField(blank=True, max_length=255, null=True)),
                ('fonction', models.CharField(blank=True, max_length=255, null=True)),
                ('numerodetelephone', models.CharField(blank=True, max_length=255, null=True)),
                ('telephonepersonnel', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Realisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_realise', models.CharField(max_length=255)),
                ('date_realisation', models.DateField()),
                ('etat', models.CharField(max_length=50)),
                ('action_associe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.actions')),
            ],
        ),
        migrations.CreateModel(
            name='Secteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secteur_nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compte', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('courrier', models.EmailField(max_length=254)),
                ('numero_tel', models.CharField(blank=True, max_length=255, null=True)),
                ('presente_vous', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('fonction', models.CharField(blank=True, max_length=255, null=True)),
                ('adresse_sip', models.CharField(blank=True, max_length=255, null=True)),
                ('othermail', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REFtraitement', models.CharField(blank=True, max_length=255, null=True)),
                ('nomtraitement', models.CharField(blank=True, max_length=255, null=True)),
                ('datedecreation', models.DateTimeField(auto_now_add=True)),
                ('datedemiseajour', models.DateTimeField(auto_now=True)),
                ('donneesensible', models.BooleanField()),
                ('personneconcernee', models.CharField(blank=True, max_length=255, null=True)),
                ('precision', models.CharField(blank=True, max_length=255, null=True)),
                ('typeregistre', models.CharField(blank=True, max_length=255, null=True)),
                ('finaliteprincipale', models.TextField(blank=True, null=True)),
                ('sous_finalite1', models.TextField(blank=True, null=True)),
                ('sous_finalite2', models.TextField(blank=True, null=True)),
                ('sous_finalite3', models.TextField(blank=True, null=True)),
                ('sous_finalite4', models.TextField(blank=True, null=True)),
                ('categorie', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('dureedeconcesrvation', models.CharField(blank=True, max_length=255, null=True)),
                ('mtypedemesuredesecurite', models.CharField(blank=True, max_length=255, null=True)),
                ('precisiondumesuredesecurite', models.CharField(blank=True, max_length=255, null=True)),
                ('typedestinataire', models.CharField(blank=True, max_length=255, null=True)),
                ('precisions', models.CharField(blank=True, max_length=255, null=True)),
                ('donneeconcernee', models.CharField(blank=True, max_length=255, null=True)),
                ('destinataire', models.CharField(blank=True, max_length=255, null=True)),
                ('pays', models.CharField(blank=True, max_length=255, null=True)),
                ('typedegarantie', models.CharField(blank=True, max_length=255, null=True)),
                ('lienversladocumentation', models.CharField(blank=True, max_length=255, null=True)),
                ('lesdonneesconcernee', models.CharField(blank=True, max_length=255, null=True)),
                ('prenomnomresptraitement', models.CharField(blank=True, max_length=255, null=True)),
                ('emailresptraitement', models.CharField(blank=True, max_length=255, null=True)),
                ('telephonereesptraitement', models.CharField(blank=True, max_length=255, null=True)),
                ('prenommomDPO', models.CharField(blank=True, max_length=255, null=True)),
                ('EmailDPO', models.CharField(blank=True, max_length=255, null=True)),
                ('telephoneDPO', models.CharField(blank=True, max_length=255, null=True)),
                ('prenomnomrepresentant', models.CharField(blank=True, max_length=255, null=True)),
                ('emailrepresentant', models.CharField(blank=True, max_length=255, null=True)),
                ('telephonerepresentant', models.CharField(blank=True, max_length=255, null=True)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Taches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('nom_tache', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('echeance', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('priorite', models.CharField(blank=True, max_length=100, null=True)),
                ('assigne_a', models.CharField(blank=True, max_length=100, null=True)),
                ('date_realisation', models.DateField(blank=True, null=True)),
                ('etat', models.CharField(blank=True, max_length=100, null=True)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('piece_jointe', models.FileField(blank=True, default=None, null=True, upload_to='uploads/docs', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'pptx'])])),
                ('realisation_associee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.realisation')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_nom', models.CharField(max_length=255)),
                ('sigle', models.CharField(max_length=255)),
                ('groupe_retso', models.CharField(max_length=255)),
                ('responsable_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Processus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=255)),
                ('typologie', models.CharField(max_length=255)),
                ('sigle', models.CharField(max_length=50)),
                ('finalite', models.TextField()),
                ('acteurs', models.TextField()),
                ('donnee_entree', models.TextField()),
                ('activites', models.TextField()),
                ('donnee_sortie', models.TextField()),
                ('ressources_tech_org', models.TextField()),
                ('objectifs_ind', models.TextField()),
                ('outils_surveil', models.TextField()),
                ('pilote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='NC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=255)),
                ('nature', models.CharField(max_length=255)),
                ('domaine', models.CharField(blank=True, max_length=255, null=True)),
                ('date_nc', models.DateField()),
                ('date_prise_en_compte', models.DateField(blank=True, default=None, null=True)),
                ('description_detailee', models.TextField(blank=True, default=None, null=True)),
                ('annee', models.CharField(blank=True, max_length=255, null=True)),
                ('mois', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_cause', models.CharField(blank=True, max_length=255, null=True)),
                ('delai_prevu', models.DateField(blank=True, null=True)),
                ('type_cause', models.CharField(blank=True, max_length=255, null=True)),
                ('cout', models.CharField(blank=True, max_length=255, null=True)),
                ('progress', models.CharField(blank=True, max_length=255, null=True)),
                ('info_complementaires', models.TextField(blank=True, null=True)),
                ('piece_jointe', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('frequence', models.BooleanField(blank=True, null=True)),
                ('gravite', models.BooleanField(blank=True, null=True)),
                ('action_immediate', models.BooleanField(blank=True, null=True)),
                ('nc_cloture', models.BooleanField(blank=True, null=True)),
                ('processus', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.processus')),
                ('responsable_traitement', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.utilisateur')),
                ('site', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site')),
            ],
        ),
        migrations.CreateModel(
            name='MesureEfficacite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cloture', models.DateField()),
                ('resultat_mesure_eff', models.CharField(max_length=100)),
                ('mesure_eff', models.TextField()),
                ('cout', models.FloatField()),
                ('action_associee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.actions')),
            ],
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois_concerne', models.CharField(max_length=255)),
                ('menus_generaux', models.FileField(blank=True, upload_to='documents/')),
                ('menus_dessert', models.FileField(blank=True, upload_to='documents/')),
                ('menu_s1', models.FileField(blank=True, upload_to='documents/')),
                ('menu_s2', models.FileField(blank=True, upload_to='documents/')),
                ('menu_s3', models.FileField(blank=True, upload_to='documents/')),
                ('menu_s4', models.FileField(blank=True, upload_to='documents/')),
                ('menu_s5', models.FileField(blank=True, upload_to='documents/')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriqueDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('description_modif', models.CharField(max_length=255)),
                ('date_modif', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.documents')),
                ('modifie_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Evenements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contract', models.CharField(max_length=255)),
                ('nom_personne', models.CharField(max_length=255)),
                ('type_evenement', models.CharField(max_length=255)),
                ('intitule', models.CharField(max_length=255)),
                ('resume', models.TextField()),
                ('temoins', models.CharField(max_length=255)),
                ('premiere_pers_info', models.CharField(max_length=255)),
                ('action_immediate', models.TextField()),
                ('date_accident', models.DateField()),
                ('periode_travail', models.CharField(max_length=255)),
                ('lieu_accident', models.CharField(max_length=255)),
                ('tache_effectue', models.CharField(max_length=255)),
                ('utiliser_chien', models.BooleanField()),
                ('siege_de_lesions_1', models.CharField(blank=True, max_length=255)),
                ('siege_de_lesions_2', models.CharField(blank=True, max_length=255)),
                ('nature_lesions', models.CharField(max_length=255)),
                ('arret_travail', models.BooleanField()),
                ('dangers', models.ManyToManyField(blank=True, null=True, to='QHSEApi.danger')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.services')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationDanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('probabilite', models.IntegerField()),
                ('severite', models.IntegerField()),
                ('frequences_exposition', models.IntegerField()),
                ('mesure_prevention', models.TextField(blank=True, null=True)),
                ('ipr', models.FloatField()),
                ('indice_risque', models.IntegerField()),
                ('danger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.danger')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delai', models.IntegerField(blank=True, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('qualite', models.IntegerField(blank=True, null=True)),
                ('reactive', models.IntegerField(blank=True, null=True)),
                ('realationnel', models.IntegerField(blank=True, null=True)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.fournisseur')),
                ('traitement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.traitement')),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_equipement', models.CharField(blank=True, max_length=255, null=True)),
                ('codification', models.CharField(max_length=255)),
                ('date_mise_en_service', models.DateField(blank=True, null=True)),
                ('date_modification', models.DateField(blank=True, null=True)),
                ('verification', models.CharField(blank=True, max_length=255, null=True)),
                ('prochaine_verification', models.DateField(blank=True, null=True)),
                ('commentaires', models.CharField(blank=True, max_length=255, null=True)),
                ('Equipement_declasse', models.BooleanField(blank=True, null=True)),
                ('N_serie', models.CharField(blank=True, max_length=255, null=True)),
                ('Certificat', models.FileField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('secteur', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.secteurs')),
                ('site', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site')),
            ],
        ),
        migrations.AddField(
            model_name='documents',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.utilisateur'),
        ),
        migrations.AddField(
            model_name='documents',
            name='processus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.processus'),
        ),
        migrations.AddField(
            model_name='documents',
            name='secteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.secteurs'),
        ),
        migrations.AddField(
            model_name='documents',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site'),
        ),
        migrations.AddField(
            model_name='danger',
            name='famille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.famille'),
        ),
        migrations.AddField(
            model_name='danger',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.services'),
        ),
        migrations.AddField(
            model_name='danger',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site'),
        ),
        migrations.CreateModel(
            name='ArretTravail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CMI_volet_recup', models.CharField(max_length=50)),
                ('date_debut_arret', models.DateField()),
                ('date_fin_arret', models.DateField()),
                ('duree_arret', models.IntegerField()),
                ('prolongation', models.BooleanField()),
                ('duree_total_pro', models.IntegerField()),
                ('rechute', models.BooleanField()),
                ('duree_total_rechute', models.IntegerField()),
                ('duree_total_arret', models.IntegerField()),
                ('evenement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.evenements')),
            ],
        ),
        migrations.CreateModel(
            name='AnalyseEvenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.TextField()),
                ('probabilite', models.IntegerField()),
                ('frequences', models.IntegerField()),
                ('severite', models.IntegerField()),
                ('niveau_risque', models.IntegerField()),
                ('arbe_cause', models.FileField(blank=True, default=None, null=True, upload_to='uploads/docs', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'pptx'])])),
                ('danger_lie', models.ManyToManyField(blank=True, null=True, to='QHSEApi.danger')),
                ('evenement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.evenements')),
            ],
        ),
        migrations.AddField(
            model_name='actions',
            name='danger',
            field=models.ManyToManyField(blank=True, db_constraint=False, null=True, to='QHSEApi.danger'),
        ),
        migrations.AddField(
            model_name='actions',
            name='evenement',
            field=models.ManyToManyField(blank=True, db_constraint=False, null=True, to='QHSEApi.evenements'),
        ),
        migrations.AddField(
            model_name='actions',
            name='processus',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.processus'),
        ),
        migrations.AddField(
            model_name='actions',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.site'),
        ),
        migrations.CreateModel(
            name='FavorisDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.documents')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.utilisateur')),
            ],
            options={
                'unique_together': {('document', 'utilisateur')},
            },
        ),
        migrations.CreateModel(
            name='ChefServices',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='QHSEApi.utilisateur')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QHSEApi.services')),
            ],
            bases=('QHSEApi.utilisateur',),
        ),
    ]
