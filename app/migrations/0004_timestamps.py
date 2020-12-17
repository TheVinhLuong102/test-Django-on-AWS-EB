# Generated by Django 3.1.4 on 2020-12-17 23:50


from django.db import migrations
import django.utils.timezone

import model_utils.fields


class Migration(migrations.Migration):
    dependencies = ('app', '0003_timestamps'),

    operations = [
        migrations.AddField(
            model_name='m',
            name='created',
            field=model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')
        ),

        migrations.AddField(
            model_name='m',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified')
        )
    ]
