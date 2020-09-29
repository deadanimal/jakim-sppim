# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

# @login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "pages/dashboard.html")

@login_required(login_url="/login/")
def d_statistik_1(request):
    return render(request, "pages/dashboard/laporan/statistik-1.html")
@login_required(login_url="/login/")
def d_statistik_2(request):
    return render(request, "pages/dashboard/laporan/statistik-2.html")
@login_required(login_url="/login/")
def d_statistik_3(request):
    return render(request, "pages/dashboard/laporan/statistik-3.html")
@login_required(login_url="/login/")
def d_statistik_4(request):
    return render(request, "pages/dashboard/laporan/statistik-4.html")
@login_required(login_url="/login/")
def d_statistik_5(request):
    return render(request, "pages/dashboard/laporan/statistik-5.html")
@login_required(login_url="/login/")
def d_statistik_6(request):
    return render(request, "pages/dashboard/laporan/statistik-6.html")
@login_required(login_url="/login/")
def d_statistik_7(request):
    return render(request, "pages/dashboard/laporan/statistik-7.html")
@login_required(login_url="/login/")
def d_statistik_8(request):
    return render(request, "pages/dashboard/laporan/statistik-8.html")
@login_required(login_url="/login/")
def d_statistik_9(request):
    return render(request, "pages/dashboard/laporan/statistik-9.html")

@login_required(login_url="/login/")
def senarai_staf(request):
    return render(request, "pages/dashboard/senarai-staf.html")

@login_required(login_url="/login/")
def senarai_orang_awam(request):
    return render(request, "pages/dashboard/senarai-orang-awam.html")

@login_required(login_url="/login/")
def rekod_kaji_selidik(request):
    return render(request, "pages/dashboard/rekod-kaji-selidik.html")

@login_required(login_url="/login/")
def rekod_aduan(request):
    return render(request, "pages/dashboard/rekod-aduan.html")

### Benar Nikah Online Section
def benar_nikah_online(request):
    if request.method == 'POST':
        return redirect('bno_carian')

    return render(request, "pages/benar-nikah-online.html")

def bno_carian(request):
    return render(request, "pages/benar-nikah-online/carian.html")
def bno_baru_1(request):
    return render(request, "pages/benar-nikah-online/permohonan-baru-1.html")
def bno_baru_2(request):
    return render(request, "pages/benar-nikah-online/permohonan-baru-2.html")
def bno_baru_3(request):
    return render(request, "pages/benar-nikah-online/permohonan-baru-3.html")
def bno_baru_4(request):
    return render(request, "pages/benar-nikah-online/permohonan-baru-4.html")
def bno_baru_5(request):
    return render(request, "pages/benar-nikah-online/permohonan-baru-5.html")

### Pra Perkahwinan Online Section
def pra_perkahwinan_online(request):
    if request.method == 'POST':
        return redirect('ppo_carian')

    return render(request, "pages/pra-perkahwinan-online.html")

def ppo_carian(request):
    return render(request, "pages/pra-perkahwinan-online/carian.html")
def ppo_baru_1(request):
    return render(request, "pages/pra-perkahwinan-online/permohonan-baru-1.html")

def ncr_luar_negara(request):
    return render(request, "pages/ncr-luar-negara.html")

def rundingcara_online(request):
    return render(request, "pages/rundingcara-online.html")

def rujuk_online(request):
    return render(request, "pages/rujuk-online.html")

def cerai_online(request):
    return render(request, "pages/cerai-online.html")

def senarai_paid(request):
    return render(request, "pages/senarai-paid.html")

def panduan_perkahwinan(request):
    return render(request, "pages/panduan-perkahwinan.html")

def lupa_no_rujukan(request):
    return render(request, "pages/lupa-no-rujukan.html")

def aduan_sppim(request):
    return render(request, "pages/aduan-sppim.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
