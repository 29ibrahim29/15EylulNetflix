# Generated by Django 4.1.2 on 2022-11-20 17:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_kategori_movie_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
