# Generated by Django 3.2.4 on 2023-01-18 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Brend')),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kategoriya')),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Tovar rangi')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Brend')),
                ('slug', models.SlugField(max_length=150)),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Necha foiz chegirma ?')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('top', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('views', models.PositiveIntegerField(default=1)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_products', to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Tovarning alohida rasmlari')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Tovarning rasmlari',
                'verbose_name_plural': 'Tovarning rasmlari',
            },
        ),
    ]
