# Generated by Django 2.1.3 on 2018-11-09 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("cast", "0003_audio_duration")]

    operations = [
        migrations.RenameField(model_name="audio", old_name="original", new_name="mp3")
    ]