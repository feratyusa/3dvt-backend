# Generated by Django 4.1.2 on 2022-10-15 02:15

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0030_rename_section_title_landingpage_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagedata",
            name="groupname",
            field=models.CharField(
                help_text="User Group Name for this current Task",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="imagedata",
            name="images",
            field=models.FileField(
                help_text="Image File to be Processed",
                null=True,
                upload_to=api.models.ImageDataset,
                verbose_name="images",
            ),
        ),
        migrations.AlterField(
            model_name="imagedata",
            name="task",
            field=models.ForeignKey(
                help_text="Corresponding Task",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.taskhistory",
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="content",
            field=models.TextField(
                help_text="Content of Landing Page's Section",
                null=True,
                verbose_name="Content",
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="file",
            field=models.FileField(
                help_text="Optional File for Landing Page's Section",
                null=True,
                upload_to="",
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="image",
            field=models.ImageField(
                help_text="Optional Image for Landing Page's Section",
                null=True,
                upload_to="",
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="link",
            field=models.JSONField(
                default=dict,
                help_text="Optional External Link(s) for Landing Page's Section",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="taskhistory",
            name="groupname",
            field=models.CharField(
                help_text="User Group Name for this current Task",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="taskhistory",
            name="results",
            field=models.JSONField(
                default=list,
                help_text="Result Image's Url(s)",
                null=True,
                verbose_name="Result",
            ),
        ),
        migrations.AlterField(
            model_name="taskhistory",
            name="sources",
            field=models.JSONField(
                default=list,
                help_text="Source Image's Url(s)",
                null=True,
                verbose_name="Source",
            ),
        ),
        migrations.AlterField(
            model_name="taskhistory",
            name="status",
            field=models.CharField(
                help_text="Task Status, ex: 'STARTED', 'FINISHED",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="taskhistory",
            name="type",
            field=models.CharField(
                help_text="Type of the task, ex: 'segmentation'",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="apikey",
            field=models.CharField(
                help_text="User API Key (Token), generated by django AuthToken",
                max_length=50,
                null=True,
            ),
        ),
    ]
