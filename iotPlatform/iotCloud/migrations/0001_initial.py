# Generated by Django 3.0.8 on 2020-08-19 21:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_capteur', models.CharField(max_length=30, unique=True)),
                ('adresse_capteur', models.CharField(max_length=30)),
                ('description_capteur', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Reseau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_reseau', models.CharField(max_length=30)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('description_reseau', models.TextField(max_length=500)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Proprietaire')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('duree', models.IntegerField()),
                ('cout', models.FloatField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Souscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sous', models.DateTimeField(auto_now_add=True)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Proprietaire')),
                ('reseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Reseau')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Puits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=15)),
                ('cle', models.CharField(max_length=32)),
                ('reseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Reseau')),
            ],
        ),
        migrations.CreateModel(
            name='Etat_capteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energie', models.IntegerField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('heure', models.TimeField(auto_now_add=True)),
                ('capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Capteur')),
            ],
        ),
        migrations.CreateModel(
            name='Donnee_ctrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taux_livraison', models.FloatField()),
                ('qlte_signal', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('heure', models.TimeField(auto_now_add=True)),
                ('voisin', models.TextField()),
                ('capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Capteur')),
            ],
        ),
        migrations.CreateModel(
            name='Donnee_appli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur_brute', models.IntegerField()),
                ('valeur_traite', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('heure', models.TimeField(auto_now_add=True)),
                ('capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Capteur')),
            ],
        ),
        migrations.AddField(
            model_name='capteur',
            name='reseau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotCloud.Reseau'),
        ),
    ]
