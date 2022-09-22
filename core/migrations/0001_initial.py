# Generated by Django 4.1.1 on 2022-09-22 10:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField()),
                ('designers', models.ManyToManyField(related_name='designers', to=settings.AUTH_USER_MODEL)),
                ('developers', models.ManyToManyField(related_name='developers', to=settings.AUTH_USER_MODEL)),
                ('maintainers', models.ManyToManyField(related_name='maintainers', to=settings.AUTH_USER_MODEL)),
                ('picture', models.ManyToManyField(to='core.picture')),
            ],
        ),
    ]
