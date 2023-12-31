# Generated by Django 4.1.4 on 2023-07-25 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=75)),
                ('poste', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'Administrateur',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id_etudiant', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=75)),
                ('matricule', models.CharField(max_length=75)),
                ('niveau', models.IntegerField()),
                ('option', models.CharField(max_length=75)),
                ('photo', models.ImageField(blank=True, upload_to='photos')),
            ],
            options={
                'db_table': 'Etudiant',
            },
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id_logement', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=75)),
                ('numero', models.IntegerField()),
                ('localisation', models.CharField(max_length=75)),
                ('etat', models.CharField(max_length=75)),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qr_code')),
            ],
            options={
                'db_table': 'Logement',
            },
        ),
        migrations.CreateModel(
            name='Occuper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_etudiant', models.ForeignKey(db_column='id_etudiant', on_delete=django.db.models.deletion.CASCADE, to='systeme_U.etudiant')),
                ('id_logement', models.ForeignKey(db_column='id_logement', on_delete=django.db.models.deletion.CASCADE, to='systeme_U.logement')),
            ],
            options={
                'db_table': 'Occuper',
                'unique_together': {('id_etudiant', 'id_logement')},
            },
        ),
    ]
