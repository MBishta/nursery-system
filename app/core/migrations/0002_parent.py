# Generated by Django 5.1.7 on 2025-03-28 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('relation_to_child', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('guardian', 'Guardian')], max_length=50)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.child')),
            ],
        ),
    ]
