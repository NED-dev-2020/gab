# Generated by Django 3.2.9 on 2021-12-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='categorie',
            field=models.CharField(choices=[('Shoot', 'Shooting photo'), ('Design', 'Design'), ('Web', 'Web'), ('Logiciel', 'Logiciel'), ('Application mobile', 'Application mobile'), ('Conception des badges', 'Conception des badges'), ('Conception CV professionnels', 'Conception CV professionnels'), ('Formations à domicile', 'Formations à domicile'), ('Autre ...', 'Autre ...')], max_length=100),
        ),
    ]
