# Generated by Django 2.2.3 on 2019-07-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docxmerge', '0005_auto_20190719_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumemerged',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
