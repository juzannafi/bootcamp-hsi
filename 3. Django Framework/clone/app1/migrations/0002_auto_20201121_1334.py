# Generated by Django 2.2.1 on 2020-11-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90, null=True)),
                ('level', models.CharField(max_length=90, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='peserta',
            name='id',
            field=models.CharField(max_length=80, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='DaftarPeserta',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('materi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Materi')),
                ('peserta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Peserta')),
            ],
        ),
    ]
