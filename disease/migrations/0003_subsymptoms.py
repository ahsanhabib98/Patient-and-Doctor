# Generated by Django 2.0 on 2018-07-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0002_delete_subsymptoms'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSymptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]