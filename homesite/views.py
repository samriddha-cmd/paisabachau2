from typing import Text
from django.core import paginator
from django.db.models import base
from django.http.request import HttpHeaders
from django.shortcuts import render
import requests
from requests.api import delete
from bs4 import BeautifulSoup
from operator import itemgetter
import json
from django.core import serializers
from django.http import JsonResponse
import scrapy 
from .models import gaminglaptop, lenovo, xiaomi
from .models import homepagemobile
from .models import alllaptops
from .models import acer
from .models import hp
from .models import dell
from .models import asus
from .models import msi
from .models import razerblade
from .models import apple
from .models import applemobile,poco,samsungmobile,realme,oppo,vivo,allmobiles,oneplus,bestmidranger,nokia,latestflagship
from django.core.paginator import Paginator
from django.db.models import Q

def searchresult(request):
    results_list=[]
    if request.method=='GET':

        query=request.GET.get('q')
        
        results=alllaptops.objects.filter(Q(laptopname__icontains=query)).order_by('price')
        results2=allmobiles.objects.filter(Q(mobilename__icontains=query)).order_by('price')
       
        
        count1=len(results)
        count2=len(results2)
        count=count1+count2
   
        for i in results:
            results_list.append(i)
        for j in results2:
            results_list.append(j)
        
       

    return render(request,'searchresult.html',{'ittinepal':results_list,'count':count})




def home(request):
    ittitotalinfolist=[]
    base_url="https://www.itti.com.np/"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' 
    }
    r=requests.get('https://itti.com.np/',headers=headers)
  
    soups=BeautifulSoup(r.content,'html.parser')
    productlist=soups.find('div',class_='product-container')
    productlist=productlist.find_all('div',class_='deals-items')
    infos=homepagemobile.objects.all()

    count=0
    for info in productlist:
      
        name = info.find('h2', class_='product-name').text.strip()
    
        price = getattr(info.find('span', class_='price'), 'text', None)
        image=info.find('img',class_='product-image-photo')
   
        forwardpage=info.find('a',class_='product-item-link')

     
        sort=price.split('NPR')[1].replace(',','').replace('.00','')
     
        count=count+1
        if count>=6:
            break
        ittitotalinfo = {
            'name': name,
            'price': price,
            'image':image['data-src'],
            'forwardpage0':forwardpage['href'],
            'arranger':sort,
            'logo':1
        }
        ittitotalinfolist.append(ittitotalinfo)
   
    return render(request,'home.html',{'infos':infos,'ittitotalinfo':ittitotalinfolist})

def laptop(request):
    
    

    #ripple laptops ---------------------------------------------------------------
    base_url='https://rippledevice.com/shop/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.5',
    }
    r=requests.get(base_url, headers = headers)
    price=[]
    ripplelaptopfinalpage=[]
    soup=BeautifulSoup(r.content,'html.parser')
  
    productlist=soup.find_all('div',class_='product-card')
    for link in productlist:
        for links in link.find_all('a'):
            price.append(links)
    for info in price:
         ripplelaptopfinalpage.append(info['href'])     
    nameinfo=soup.find_all('h6')
 
    priceinfo=soup.find_all('span',class_='woocommerce-Price-amount')
    ripplelaptopspriceinfo=[]
    ripplelaptopsprice=[]
    for price in priceinfo:
        price=price.text
        price=price.split("\n")
        ripplelaptopspriceinfo.append(price)
    for price in ripplelaptopspriceinfo:
        price.pop(0)

    for price in ripplelaptopspriceinfo:
        for prices in price:
            ripplelaptopsprice.append(prices)
    ripplelaptopname=[]
    ripplelaptopspecs=[]
    ripplelaptopspecsinfo=[]
    names=[]
    count=0
    for name in nameinfo:
        name=name.text
        ripplelaptopname.append(name)


    ripplespecs=soup.find_all('h3')
    for name in ripplespecs:
        ripplelaptopspecsinfo.append(name.text)
    
    for name in range(len(ripplelaptopname)):
        ripplelaptopspecs.append(ripplelaptopspecsinfo[name])

    ripplelaptopimage=[]
    priceinfo=[]
   
    totalinfo={}

    for info in productlist:
        for link in info.find_all('img'):
           priceinfo.append(link)
    for info in priceinfo:
        ripplelaptopimage.append(info['src'])
  
    for a in range(0,len(ripplelaptopspriceinfo)):
        totalinfo[ripplelaptopsprice[a]]=ripplelaptopname[a],ripplelaptopspecs[a],ripplelaptopimage[a],ripplelaptopfinalpage[a]


    # Gaming Laptops Data--------------------------------------------------------------------

    infos=gaminglaptop.objects.all().order_by('-price')[50:55]
    entrylevellaptops=alllaptops.objects.all().order_by('price')[0:5]
  



    return render(request,'laptop.html',{'productslist':totalinfo ,'productlists':soup,'infos':infos,'entrylaptops':entrylevellaptops})



def companys(request,brandslug):
    brand=brandslug
    if brand=='acer':
        branddata=acer.objects.all().order_by('price')
      
    if brand=='asus':
        branddata=asus.objects.all().order_by('price')
    if brand=='apple':
        branddata=apple.objects.all().order_by('price')
    if brand=='msi':
        branddata=msi.objects.all().order_by('price')
    if brand=='hp':
        branddata=hp.objects.all().order_by('price')
    if brand=='lenovo':
        branddata=lenovo.objects.all().order_by('price')
    if brand=='razerblade':
        branddata=razerblade.objects.all().order_by('price')
    if brand=='dell':
        branddata=dell.objects.all().order_by('price')
    count=len(branddata)
    paginator=Paginator(branddata,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    try:
        filtered_data=[]
        if request.method=='GET':
            upperlimit=int(request.GET.get('upperlimits'))
            lowerlimit=int(request.GET.get('lowerlimits'))

        for infos in branddata:
          
            if infos.price >= lowerlimit and infos.price <= upperlimit:
                filtered_data.append(infos)
        count=len(filtered_data)
        return render(request, 'laptopbrand.html',{'ittinepal':filtered_data,'brand':brandslug.capitalize(),'count':count})
    except:   
        return render(request, 'laptopbrand.html',{'ittinepal':page_obj,'brand':brandslug.capitalize(),'count':count})

def pricerange(request,priceslug):
  
    price=priceslug

    price=price.split('-')

    lowerprice=price[1]
    upperprice=price[2]
    lowerprice=int(lowerprice)
    upperprice=int(upperprice)
    filtered_data=[]
    if price[0]=='laptop':
        flag=1
        alllaptopdata=alllaptops.objects.all().order_by('price')

        for infos in alllaptopdata:
            if infos.price>=lowerprice and infos.price <=upperprice:
                filtered_data.append(infos)
             
    
        count=len(filtered_data)
    else:
        flag=2
        allmobilesdata=allmobiles.objects.all().order_by('price')
        for infos in allmobilesdata:
            if infos.price>=lowerprice and infos.price<=upperprice:
                filtered_data.append(infos)
        count=len(filtered_data)
    if flag==1:
        brand='laptop'
    else:
        brand='mobile'
    try:
        filtered_data2=[]
        if request.method=='GET':
            upperlimit=int(request.GET.get('upperlimits'))
            lowerlimit=int(request.GET.get('lowerlimits'))

            for infos in filtered_data:
                if infos.price>=lowerlimit  and infos.price <=upperlimit:
                    filtered_data2.append(infos)
                 
               
            count=len(filtered_data)

        return render(request,'laptopbrand.html',{'ittinepal':filtered_data2,'count':count,'brand':brand,'flag':flag})
    except:
           
        return render(request,'laptopbrand.html',{'ittinepal':filtered_data,'count':count,'brand':brand,'flag':flag})
    

def mobile(request):
    base_url='https://www.daraz.com.np/smartphones/samsung-brand/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.5',
    }
    r=requests.get(base_url, headers = headers)
    soup=BeautifulSoup(r.content,'html.parser')
    product=soup.find('div',class_='c1_t2i')
    print(product)
    mobiles=allmobiles.objects.all().order_by('-price')
    mobiless=allmobiles.objects.all().order_by('price')
    midranger=bestmidranger.objects.all()
    expensivephones=latestflagship.objects.all()
    flagshipmobiledata=[]
    entrylevelsmartphone=[]
    count=0
    for infos in mobiles:
        count=count+1
        if count<6:
            flagshipmobiledata.append(infos)
    count=0
    for infos in mobiless:
        count=count+1
        if count<6:
            entrylevelsmartphone.append(infos)
    

    return render(request,'mobile.html',{'flagshipmobile':flagshipmobiledata,'entrylevelsmartphone':entrylevelsmartphone,'bestmidranger':midranger,'expensivephones':expensivephones})

def mobilecompany(request,brandslug):
    brand=brandslug
    if brand=='apple':
        branddata=applemobile.objects.all().order_by('price')
      
    if brand=='realme':
        branddata=realme.objects.all().order_by('price')
    if brand=='poco':
        branddata=poco.objects.all().order_by('price')
    if brand=='samsung':
        branddata=samsungmobile.objects.all().order_by('price')
    if brand=='vivo':
        branddata=vivo.objects.all().order_by('price')
    if brand=='oppo':
        branddata=oppo.objects.all().order_by('price')
    if brand=='oneplus':
        branddata=oneplus.objects.all().order_by('price')
    if brand=='xiaomi':
        branddata=xiaomi.objects.all().order_by('price')
    if brand=='nokia':
        branddata=nokia.objects.all().order_by('price')
    count=len(branddata)
    paginator=Paginator(branddata,10)

    page_number=request.GET.get('page')
 
    page_obj=paginator.get_page(page_number)
    
    
    try:
        filtered_data=[]
        if request.method=='GET':
            upperlimit=int(request.GET.get('upperlimits'))
            lowerlimit=int(request.GET.get('lowerlimits'))

        for infos in branddata:
          
            if infos.price >= lowerlimit and infos.price <= upperlimit:
                filtered_data.append(infos)
        count=len(filtered_data)
        return render(request, 'mobilebrand.html',{'iteminfo':filtered_data,'brand':brandslug.capitalize(),'count':count})
    except:   
        return render(request, 'mobilebrand.html',{'iteminfo':page_obj,'brand':brandslug.capitalize(),'count':count})
    
def gaminglaptops(request):
    
 

 

  

    ittinepal=gaminglaptop.objects.all().order_by('-price')
    count=0
    for gaminglaptops in ittinepal:
        
 
        if gaminglaptops.price==0:
            gaminglaptops.delete()
    count=len(ittinepal)
    brand="Gaming Laptops"

    paginator=Paginator(ittinepal,50)

    page_number=request.GET.get('page')
 
    page_obj=paginator.get_page(page_number)
    
    try:
        filtered_data=[]
        if request.method=='GET':
            upperlimit=int(request.GET.get('upperlimits'))
            lowerlimit=int(request.GET.get('lowerlimits'))

        for infos in ittinepal:
          
            if infos.price >= lowerlimit and infos.price <= upperlimit:
                filtered_data.append(infos)
        count=len(filtered_data)
        return render(request, 'laptopbrand.html',{'ittinepal':filtered_data,'count':count,'brand':brand})
    except:   
        return render(request, 'laptopbrand.html',{'ittinepal':page_obj,'count':count,'brand':brand})

def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
