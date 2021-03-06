# Generated by Django 3.1.2 on 2020-10-11 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authh', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authh.user')),
                ('full_name', models.CharField(max_length=70, verbose_name='Nome Completo')),
                ('companies', models.ManyToManyField(related_name='Funcionarios', to='company.Company', verbose_name='Empresas')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionarios',
            },
            bases=('authh.user',),
        ),
    ]
