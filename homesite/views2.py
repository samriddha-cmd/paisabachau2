from typing import Text
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
from .models import alllaptops, allmobiles, gaminglaptop, realme, samsungmobile
from .models import homepagemobile
from .models import dell
from .models import msi
from .models import hp
from .models import asus
from .models import lenovo
from .models import apple
from .models import razerblade
from .models import acer

from .models import samsungmobile
from .models import oppo
from .models import vivo
from .models import realme
from .models import xiaomi
from .models import applemobile
from .models import allmobiles
from .models import oneplus
from .models import nokia
from .models import poco



def laptopscrape(request):
    password='Sam8359'

    if request.method=='POST':
        inputpassword=request.POST.get('password')
        if password==inputpassword:
            step1="password was correct"
            step2="site is being scraped please wait........................................."
            headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
            'Accept-Language': 'en-GB,en;q=0.5',}
            acer.objects.all().delete()
            asus.objects.all().delete()
            hp.objects.all().delete()
            dell.objects.all().delete()
            msi.objects.all().delete()
            lenovo.objects.all().delete()
            razerblade.objects.all().delete()
            apple.objects.all().delete()
            alllaptops.objects.all().delete()
            gaminglaptop.objects.all().delete()
          
      


         
           
            brands = ['apple','dell','hp','lenovo','msi','acer','razerblade','asus']
           
           #ittisitescrape


            for branditti in brands:
                if branditti=='acer' or branditti=='asus' :
                     baseurlitti = 'https://itti.com.np/laptops-by-brands/'+branditti+'-laptop-nepal?product_list_limit=36'
        
                elif branditti=='apple':
                    branditti='apple-macbook'
                    baseurlitti = 'https://itti.com.np/laptops-by-brands/'+branditti+'-laptops-nepal?product_list_limit=36'
                    branditti='apple'
                elif branditti=='dell':
                    baseurlitti = 'https://itti.com.np/laptops-by-brands/'+branditti+'?product_list_limit=36'
                else:
                    baseurlitti = 'https://itti.com.np/laptops-by-brands/'+branditti+'-laptops-nepal?product_list_limit=36'
                i = requests.get(baseurlitti, headers=headers)
                ittisite = BeautifulSoup(i.content, 'html.parser')
                productitti = ittisite.find('ol', class_='products list items product-items row')
                productitti = productitti.find_all('li', class_='item product product-item')
                for infos in productitti:
                    name = infos.find('h2', class_='product-name').text.strip()
                    price = getattr(infos.find('span', class_='price'), 'text', None)
                    image=infos.find('img',class_='product-image-photo')
            
                    forwardpage=infos.find('a',class_='product-item-link')

                
                    sort=price.split('NPR')[1].replace(',','').replace('.00','')
                    sort=int(sort)
                    site='ittinepal'
                    alllaptops.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)
                    if branditti=='acer':
                     
                        acer.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)
                    elif branditti=='asus':
                     
                        asus.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)   
                    elif branditti=='hp':
                        hp.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)           
                    elif branditti=='dell':
                        dell.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)           
                    elif branditti=='razerblade':
                        razerblade.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)           
                    elif branditti=='apple':
                       
                        apple.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)           
                    elif branditti=='lenovo':
                       lenovo.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)           
                    elif branditti=='msi':
                       msi.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=sort)           

                print('itti scrape suceesful')


            #zozohubscrape    
            brandszozo = ['apple','dell','hp','lenovo','msi','acer','asus']
  
            for brandzozo in brandszozo:
                if brandzozo=='acer':
                    brandzozo='17' 
                    position=1
                elif brandzozo=='asus':
                    brandzozo='18'
                    position=1
                elif brandzozo=='hp':
                    brandzozo='19' 
                    position=1
                elif brandzozo=='lenovo':
                    brandzozo='21'
                    position=1
                elif brandzozo=='msi':
                    brandzozo='22'
                    position=1
                elif brandzozo=='dell':
                    brandzozo='20'
                    position=1
                elif brandzozo=='apple':
                    brandzozo='16'
                    position=1
                if position==1:
                    baseurlzozohub='https://zozohub.com/category-products/'+brandzozo+'?limit=50'
                    zozohubsite=requests.get(baseurlzozohub,headers=headers).text
                
                    zozohubsite=json.loads(zozohubsite)

                    productszozo=zozohubsite['products']['data']
                

                    for infos in productszozo:
                        print("zozohubsite data")
                        selector = scrapy.Selector(text=infos['priceHTML'], type="html")
                        
                        selector=selector.xpath('//span/text()').extract()

                        price=selector[1]
                        price=price.split('Rs. ')[1].replace(',','')
                        price=int(price)
                        slug='https://zozohub.com/'+infos['slug']
                        site='zozohub'
                        alllaptops.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        if brandzozo=='17':
                            print('scraping acer')
                            acer.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        elif brandzozo=='18':
                            print('scraping asus')
                            asus.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        elif brandzozo=='19':
                            print('scraping hp')
                            hp.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        elif brandzozo=='20':
                            dell.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        
                        elif brandzozo=='16':
                            apple.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        elif brandzozo=='21':
                            lenovo.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)
                        elif brandzozo=='22':
                            msi.objects.create(forwardlink=slug,photolink=infos['image'],site=site,laptopname=infos['name'],price=price)



            #LDS scrape-----------------------------------------------------
            # brandsldss = ['apple','dell','hp','lenovo','msi','acer','asus']
            # print("lds scraping started.....................")
            # for brandlds in brandsldss:
            #     ldscount=0
            #     if brandlds=='acer' or brandlds=='hp' or brandzozo=='dell' or brandlds=='lenovo' or brandlds=='msi' or brandlds=='asus':
            #         ldscount=1
            #         baseurllds = 'https://lds.com.np/brand/'+brandlds+'?limit=36'
                    
            #     elif brandlds=='apple':
            #         brandlds='Apple'
            #         ldscount=1
            #         baseurllds='https://lds.com.np/brand/'+brandlds+'?limit=36'
            #         brandlds='apple'
                
            #     if ldscount== 1:
            #         l=requests.get(baseurllds,headers=headers)
            #         ldssite=BeautifulSoup(l.content,'html.parser')
            #         productlds=ldssite.find('div',class_='products-block')
            #         productlds=productlds.find_all('div',class_='product-block')
                    
            #         for infos in productlds:
            #             name=infos.find('h6',class_='name').text
            #             price=infos.find('span',class_='price-new').text
            #             image=infos.find('img',class_='img-responsive')
            #             forwardpage=infos.find('a',class_='img')
                    
            #             pricesort=price.split('NPR')[1].replace(',','').replace('.00','')
            #             pricesort=int(pricesort)
            #             site='ldsnepal'
            #             print('scraping lds data')
            #             alllaptops.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)
            #             if brandlds=='acer':
            #                 print('scraping lds acer ')
            #                 acer.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)
            #             elif brandlds=='asus':
            #                 asus.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)   
            #             elif brandlds=='hp':
            #                 hp.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)           
            #             elif brandlds=='dell':
            #                 dell.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)           
                           
            #             elif brandlds=='apple':
            #                 apple.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)           
            #             elif brandlds=='lenovo':
            #                 lenovo.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)           
            #             elif brandlds=='msi':
            #                 print('scraping lds msi ')
            #                 msi.objects.create(forwardlink=forwardpage['href'],photolink=image['src'],site=site,laptopname=name,price=pricesort)           
            # print('lds data scrape sucessful')  




    #ptech brand-------------------------------------
            print('starting ptech data scrape')
            brandptechs=['apple','dell','hp','lenovo','msi','acer','razerblade','asus']
            count=0
            for brandptech in brandptechs:
                if brandptech=='acer' or brandptech=='hp' or brandptech=='dell' or brandptech=='lenovo' or brandptech=='msi' or brandptech=='asus':
                    baseurlptech='https://ptechktm.com/laptops/'+brandptech+'?product_list_limit=36'
                    count=1
                if count==1:
                    print(baseurlptech)
                    p=requests.get(baseurlptech,headers=headers)
                    ptechsite=BeautifulSoup(p.content,'html.parser')
                    productptech=ptechsite.find('ol', class_='products list items product-items')
                    productptech=productptech.find_all('div',class_='images-container')

                    for infos in productptech:
                        name=infos.find('h2','product-name product-item-name').text
                        price=infos.find('span',class_='price').text
                        image=infos.find('img',class_='product-image-photo')
                        forwardpage=infos.find('a',class_='product-item-photo')
                        pricesort=price.split('Rs ')[1].replace(',','').replace('.00','')
                        site='ptech electronics'
                        alllaptops.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],laptopname=name,price=pricesort,site=site)
                        if brandptech=='acer':
                          
                            acer.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=pricesort)
                        elif brandptech=='asus':
                            asus.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=pricesort)   
                        elif brandptech=='hp':
                            hp.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=pricesort)           
                        elif brandptech=='dell':
                            dell.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=pricesort)           
                        
                        
                        elif brandptech=='lenovo':
                    
                            lenovo.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=pricesort)           
                        elif brandptech=='msi':
                       
                            msi.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],site=site,laptopname=name,price=pricesort)           

               
            print('ptech data sucessfully saved')
        #gaming laptop data scrape-------------------------------------------
            for i in range(1,5):
            
                baseurlgaminglaptop='https://itti.com.np/gaming-laptops-nepal?product_list_limit=36&p='+str(i)
                itti=requests.get(baseurlgaminglaptop, headers = headers)
                ittisite = BeautifulSoup(itti.content, 'html.parser')
                productitti = ittisite.find('ol', class_='products list items product-items row')
                productitti = productitti.find_all('li', class_='item product product-item')
                site='ittinepal'
                for infos in productitti:
                    name = infos.find('h2', class_='product-name').text.strip()
                    price = getattr(infos.find('span', class_='price'), 'text', None)
                    image=infos.find('img',class_='product-image-photo')

                    forwardpage=infos.find('a',class_='product-item-link')

                
                    sort=price.split('NPR')[1].replace(',','').replace('.00','')
                    sort=int(sort)
                    site='ittinepal'
                    gaminglaptop.objects.create(forwardlink=forwardpage['href'],photolink=image['data-src'],laptopname=name,price=sort,site=site)    
            for i in range(1,10):
                baseurlgaminglaptopbigbyte='https://bigbyte.com.np/gaming-laptops/?product-page='+str(i)
                bigbyte=requests.get(baseurlgaminglaptopbigbyte, headers = headers)
                bigbyteproduct = BeautifulSoup(bigbyte.content, 'html.parser')
                bigbyteproduct=bigbyteproduct.find('ul',class_='products columns-3')
                bigbyteproduct=bigbyteproduct.find_all('li')

                for i in  bigbyteproduct:
                    photo=i.find('span',class_='et_shop_image')
                    name=i.find('h2').text
                    forwardlink=i.find('a',class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')['href']
                    photo=photo.find('img')['data-src']
                    price=i.find('span',class_='price').text
                    site='bigbyte'
                
                    try:
                        pricesort=price.split('NPR')[1].replace(',','').replace('.00','').strip()
                
                        pricesort=int(pricesort)
            
                    except:
                        pricesort=0
                    gaminglaptop.objects.create(forwardlink=forwardlink,photolink=photo,laptopname=name,price=pricesort,site=site)        

            #daraz scrape------------------------------------------
            print('daraz started')
            darazbrands=['acer','asus','msi','dell','Lenovo','hp']
            for brandaraz in darazbrands:
                darazurl='https://www.daraz.com.np/traditional-laptops/'+brandaraz+'/'
                d=requests.get(darazurl,headers=headers).text
                site=BeautifulSoup(d,'html.parser')
                site=site.find_all('script')[3].string[16:]
                data=json.loads(site)
                alldata=data['mods']['listItems']
                print(brandaraz)
                print(darazurl)
                for datas in alldata:
                    price=datas['priceShow'].split('Rs. ')[1].replace(',','')
                    price=int(price)
            
                    site='daraz'
                    try:
                        name=datas['name']
                    except:
                        name=datas['name'].encode('utf-8')
                    alllaptops.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    if brandaraz=='acer':
                        acer.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='asus':
                        asus.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='msi':
                        msi.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])

                    elif brandaraz=='dell':
                        dell.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='razer':
                        razerblade.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='lenovo':
                        lenovo.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    else:
                        hp.objects.create(laptopname=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
            
                    

            return render(request,'laptopscrape.html',{'password':step1,'wait':step2})
            

            
        else:
            step1="password was incorrect"
            step2="Please type password again"
            return render(request,'laptopscrape.html',{'password':step1,'wait':step2})
    return render(request,'laptopscrape.html')


def mobilescrape(request):
    password='Sam8359'

    if request.method=='POST':
        inputpassword=request.POST.get('password')
        if password==inputpassword:
            step1="password was correct"
            step2="site is being scraped please wait........................................."
            headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
            'Accept-Language': 'en-GB,en;q=0.5',}
            oppo.objects.all().delete()
            samsungmobile.objects.all().delete()
            allmobiles.objects.all().delete()
            vivo.objects.all().delete()
            oneplus.objects.all().delete()
            applemobile.objects.all().delete()
            xiaomi.objects.all().delete()
            realme.objects.all().delete()
            poco.objects.all().delete()
            nokia.objects.all().delete()

            
            branddealayo=['xiaomi','oppo','vivo','realme','nokia','poco']
            for company in branddealayo:
                
                if company=='samsung':
                    upperlimit=4
                elif company=='xiaomi':
                    upperlimit=3
                else:
                    upperlimit=2
                for i in range(1,upperlimit):
                    i=str(i)
                    baseurl='https://www.dealayo.com/mobile/'+company+'.html?mode=grid&p='+i
                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
                        'Accept-Language': 'en-GB,en;q=0.5',
                    }
                    d=requests.get(baseurl, headers = headers)
                    soup=BeautifulSoup(d.content,'html.parser')
                    dealayoproduct=soup.find('div','products-grid amda-block-product01')
                    dealayoproduct=dealayoproduct.find_all('li','item product-item col-desktop-4 col-tablet-l-3 col-tablet-p-2 col-mobile-2')
                   
                    for infos in dealayoproduct:
                        count=0
                        name=infos.find('h2').text
                        try:
                            price=infos.find('p', class_='special-price')
                            price=price.find('span',class_='price').text.strip()
                            price1=price
                            count=count+1
                        except:
                            price=infos.find('span',class_='regular-price').text.strip()
                            price2=price
                        if count==1:
                            price=price1
                            price=price.split('Rs.')[1].replace(',','')
                            price=int(price)
                        else:
                            price=price2
                            price=price.split('Rs.')[1].replace(',','')
                            price=int(price)
                        imagelink=infos.find('div',class_='amda-product-top')
                        imagelink=imagelink.find('img',class_='img-responsive')['src']
                        forwardlink=infos.find('div',class_='amda-product-top')
                        forwardlink=forwardlink.find('a',class_='product-image no-alt-img')['href']
                        site='dealayo'
                        allmobiles.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
                        
                        if company=='realme':
                            realme.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
                        if company=='xiaomi':
                            xiaomi.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
                        if company=='oppo':
                            oppo.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
                        if company=='vivo':
                            vivo.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
                        if company=='poco':
                            poco.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
                        if company=='nokia':
                            nokia.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)
        

        #abcd mobile scrape data:
            print('scraping abcd mobile data')
            baseurl='https://www.acdcmobile.com/mobile-phone?pagesize=100'
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
                'Accept-Language': 'en-GB,en;q=0.5',
            }
           
            abcd=requests.get(baseurl, headers = headers)
            soup=BeautifulSoup(abcd.content,'html.parser')
            product=soup.find('div',class_='row shop_container')
            product=product.find_all('div',class_='col-md-3 col-6')
            for infos in product:
                name=infos.find('h6',class_='product_title').text.strip()
                price=infos.find('span',class_='price').text
                photolink=infos.find('img',class_='product_hover_img')['src']
                forwardlink=infos.find('h6',class_='product_title')
                forwardlink=forwardlink.find('a')['href']
                site='acdcmobile'
                forwardlink='https://www.acdcmobile.com'+forwardlink
                price=price.split('Rs. ')[1]
                price=int(price)

                allmobiles.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
    
                namechecker=name.split()[0]
               
           
                namechecker=namechecker.upper()
            
                if namechecker=='SAMSUNG':
       
                    samsungmobile.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='IPHONE':
                    applemobile.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='POCO':
                    poco.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='MI' or namechecker=='XIAOMI' or namechecker=='REDMI':
               
                    xiaomi.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='OPPO':
                    oppo.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='VIVO':
                    vivo.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='ONEPLUS':
              
                    oneplus.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                elif namechecker=='REALME':
                    realme.objects.create(forwardlink=forwardlink,photolink=photolink,mobilename=name,price=price,site=site)
                else:
                    pass

        #onlinesathi scrape portion::::::::::::::::::::::::::::::::=======================

            print("online sathi scraping")
            baseurlonlinesathi='https://onlinesaathi.com/category/'
            brandonlinesathi=['apple','samsung','xiaomi','oppo','vivo','oneplus','nokia']
            for brand in brandonlinesathi:
                if brand=='xiaomi':
                    brand='mi'
               
           
                onlinesathi=requests.get(baseurlonlinesathi+brand, headers = headers)
                soup=BeautifulSoup(onlinesathi.content,'html.parser')
                product=soup.find('div',class_='col-md-9 col-md-push-3')
                product=product.find_all('div',class_='col-md-3 col-sm-4 col-xs-6')
            
                for infos in product:
                    name=infos.find('h3',class_='product-name-small').text
        
                    price=infos.find('span',class_='product-price').text
                    
                    price=price.split('रु ')[1]
                  
            
                    photolink=infos.find('div',class_='shadow-div')
                    photolinks=photolink.find('img')['src']
            
                    forwardlink=infos.find('div',class_='single-item-contain')
                    forwardlink=forwardlink.find('a')['href']
                    site='onlinesathi'
                    allmobiles.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='samsung':
                            samsungmobile.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='realme':
                        realme.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='mi':
                        xiaomi.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='oppo':
                        oppo.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='vivo':
                        vivo.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='poco':
                        poco.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='nokia':
                        nokia.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if brand=='apple':
                        applemobile.objects.create(forwardlink=forwardlink,photolink=photolinks,mobilename=name,price=price,site=site)
                    if company=='nokia':
                        nokia.objects.create(forwardlink=forwardlink,photolink=imagelink,mobilename=name,price=price,site=site)

            #daraz site ==================================
            print('daraz started')
            darazbrands=['redmi','nokia','samsung-brand','oneplus_brand','vivo','oppo','apple','realme']
            for brandaraz in darazbrands:
                darazurl='https://www.daraz.com.np/smartphones/'+brandaraz+'/'
                d=requests.get(darazurl,headers=headers).text
                site=BeautifulSoup(d,'html.parser')
                site=site.find_all('script')[3].string[16:]
                data=json.loads(site)
                alldata=data['mods']['listItems']
                print(brandaraz)
                print(darazurl)
                for datas in alldata:
                    price=datas['priceShow'].split('Rs. ')[1].replace(',','')
                    price=int(price)
            
                    site='daraz'
                    try:
                        name=datas['name']
                    except:
                        name=datas['name'].encode('utf-8')
                    allmobiles.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    if brandaraz=='oneplus_brand':
                        oneplus.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='apple':
                       applemobile.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='redmi':
                        xiaomi.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])

                    elif brandaraz=='poco':
                        poco.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='oppo':
                        oppo.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='vivo':
                        vivo.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='samsung-brand':
                        samsungmobile.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    elif brandaraz=='nokia':
                        nokia.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
                    else:
                        realme.objects.create(mobilename=name,forwardlink=datas['productUrl'],price=price,site=site,photolink=datas['image'])
        else:
            step1="password was incorrect"
            step2="Please type password again"
            return render(request,'laptopscrape.html',{'password':step1,'wait':step2})

    return render(request,'laptopscrape.html')