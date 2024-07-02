# Generated by Django 4.2.13 on 2024-07-01 16:52

from django.db import migrations

FLAG_NAME = "developer-playground"

def create_developer_playground_feature_flag(apps, schema_editor):
    Flag = apps.get_model("waffle", "Flag")
    flag = Flag(
        name=FLAG_NAME,
        testing=True
    )
    flag.save()

def delete_developer_playground_feature_flag(apps, schema_editor):
    Flag = apps.get_model("waffle", "Flag")
    flags = Flag.objects.filter(name=FLAG_NAME)
    flags.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0043_alter_folder_options_historicallink_wacz_size_and_more'),
        ('waffle', '0004_update_everyone_nullbooleanfield'),
    ]

    operations = [
        migrations.RunPython(create_developer_playground_feature_flag, delete_developer_playground_feature_flag),
    ]
