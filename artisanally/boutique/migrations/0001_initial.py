# Generated by Django 4.2.16 on 2024-11-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('prix', models.FloatField(default=0.0)),
                ('quantite', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits')),
            ],
        ),
    ]