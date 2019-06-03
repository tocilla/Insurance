# Generated by Django 2.2.1 on 2019-05-22 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('boolean', 'Boolean'), ('option', 'Option'), ('date', 'Date')], max_length=20)),
                ('required', models.BooleanField(default=True)),
                ('risk_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_fields', to='risk_types.RiskType')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('risk_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_options', to='risk_types.RiskField')),
            ],
        ),
    ]
