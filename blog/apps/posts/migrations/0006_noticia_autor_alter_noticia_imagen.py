# Generated by Django 4.2.3 on 2023-08-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_noticia_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
    ]