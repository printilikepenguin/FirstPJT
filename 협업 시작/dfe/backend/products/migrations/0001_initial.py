# Generated by Django 4.2.4 on 2023-11-17 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=50)),
                ('fin_co_no', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50, unique=True)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('dcls_strt_day', models.CharField(max_length=50)),
                ('dcls_end_day', models.CharField(blank=True, max_length=50, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('rate_6', models.FloatField(blank=True, null=True)),
                ('rate_12', models.FloatField(blank=True, null=True)),
                ('rate_24', models.FloatField(blank=True, null=True)),
                ('rate_36', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=50)),
                ('fin_co_no', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50, unique=True)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('dcls_strt_day', models.CharField(max_length=50)),
                ('dcls_end_day', models.CharField(blank=True, max_length=50, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('rate_6', models.FloatField(blank=True, null=True)),
                ('rate_12', models.FloatField(blank=True, null=True)),
                ('rate_24', models.FloatField(blank=True, null=True)),
                ('rate_36', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=50)),
                ('fin_co_no', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('intr_rate_type', models.CharField(max_length=50)),
                ('intr_rate_type_nm', models.CharField(max_length=50)),
                ('rsrv_type', models.CharField(max_length=50)),
                ('rsrv_type_nm', models.CharField(max_length=50)),
                ('save_trm', models.CharField(max_length=50)),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField(blank=True, null=True)),
                ('savingproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.savingproduct')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=50)),
                ('fin_co_no', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.CharField(max_length=50)),
                ('intr_rate_type', models.CharField(max_length=50)),
                ('intr_rate_type_nm', models.CharField(max_length=50)),
                ('save_trm', models.CharField(max_length=50)),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField(blank=True, null=True)),
                ('depositproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.depositproduct')),
            ],
        ),
    ]
