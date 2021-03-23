# Generated by Django 3.1.7 on 2021-03-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hookah',
            name='hoookah_tobacco',
        ),
        migrations.AddField(
            model_name='hookah',
            name='hookah_tobacco',
            field=models.ManyToManyField(blank=True, to='places.HookahTobacco'),
        ),
        migrations.AlterField(
            model_name='hookah',
            name='hookah_type',
            field=models.ManyToManyField(blank=True, to='places.HookahType'),
        ),
    ]