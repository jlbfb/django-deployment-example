# Generated by Django 3.0.3 on 2020-04-03 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Headings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=264)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.Documents')),
            ],
            options={
                'unique_together': {('document', 'heading')},
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageURL', models.URLField(unique=True)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubHeadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheading', models.CharField(max_length=264)),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.Headings')),
            ],
            options={
                'unique_together': {('subheading', 'heading')},
            },
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('metadata', models.CharField(blank=True, max_length=500)),
                ('subheading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.SubHeadings')),
            ],
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.Documents')),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.Headings')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.States')),
                ('subheading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.SubHeadings')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_two.Texts')),
            ],
            options={
                'unique_together': {('state', 'document', 'heading', 'subheading', 'text')},
            },
        ),
    ]
