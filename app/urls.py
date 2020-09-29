# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/statistik/1/', views.d_statistik_1, name='d_statistik_1'),
    path('dashboard/statistik/2/', views.d_statistik_2, name='d_statistik_2'),
    path('dashboard/statistik/3/', views.d_statistik_3, name='d_statistik_3'),
    path('dashboard/statistik/4/', views.d_statistik_4, name='d_statistik_4'),
    path('dashboard/statistik/5/', views.d_statistik_5, name='d_statistik_5'),
    path('dashboard/statistik/6/', views.d_statistik_6, name='d_statistik_6'),
    path('dashboard/statistik/7/', views.d_statistik_7, name='d_statistik_7'),
    path('dashboard/statistik/8/', views.d_statistik_8, name='d_statistik_8'),
    path('dashboard/statistik/9/', views.d_statistik_9, name='d_statistik_9'),
    path('dashboard/senarai-staf/', views.senarai_staf, name='senarai_staf'),
    path('dashboard/senarai-orang-awam/', views.senarai_orang_awam, name='senarai_orang_awam'),
    path('dashboard/rekod-kaji-selidik/', views.rekod_kaji_selidik, name='rekod_kaji_selidik'),
    path('dashboard/rekod-aduan/', views.rekod_aduan, name='rekod_aduan'),

    path('benar-nikah-online/', views.benar_nikah_online, name='benar_nikah_online'),
    path('benar-nikah-online/carian/', views.bno_carian, name='bno_carian'),
    path('benar-nikah-online/permohonan-baru-1/', views.bno_baru_1, name='bno_baru_1'),
    path('benar-nikah-online/permohonan-baru-2/', views.bno_baru_2, name='bno_baru_2'),
    path('benar-nikah-online/permohonan-baru-3/', views.bno_baru_3, name='bno_baru_3'),
    path('benar-nikah-online/permohonan-baru-4/', views.bno_baru_4, name='bno_baru_4'),
    path('benar-nikah-online/permohonan-baru-5/', views.bno_baru_5, name='bno_baru_5'),

    path('pra-perkahwinan-online/', views.pra_perkahwinan_online, name='pra_perkahwinan_online'),
    path('pra-perkahwinan-online/carian/', views.ppo_carian, name='ppo_carian'),
    path('pra-perkahwinan-online/permohonan-baru-1/', views.ppo_baru_1, name='ppo_baru_1'),

    path('ncr-luar-negara/', views.ncr_luar_negara, name='ncr_luar_negara'),
    path('rundingcara-online/', views.rundingcara_online, name='rundingcara_online'),
    path('rujuk-online/', views.rujuk_online, name='rujuk_online'),
    path('cerai-online/', views.cerai_online, name='cerai_online'),
    path('senarai-paid/', views.senarai_paid, name='senarai_paid'),
    path('panduan-perkahwinan/', views.panduan_perkahwinan, name='panduan_perkahwinan'),
    path('aduan-sppim/', views.aduan_sppim, name='aduan_sppim'),

    path('lupa-no-rujukan/', views.lupa_no_rujukan, name='lupa_no_rujukan'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
