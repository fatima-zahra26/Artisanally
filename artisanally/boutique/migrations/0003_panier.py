# Generated by Django 4.2.16 on 2024-11-18 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boutique', '0002_commande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commandé', models.BooleanField(default=False)),
                ('date_commande', models.DateTimeField(blank=True, null=True)),
                ('commandes', models.ManyToManyField(to='boutique.commande')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
