# Generated by Django 5.1 on 2024-08-31 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0002_alter_medicalimageresult_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalimageresult',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
