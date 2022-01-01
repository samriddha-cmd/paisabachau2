from django.contrib import admin


from .models import alllaptops,latestflagship, allmobiles, bestmidranger, dell, gaminglaptop, homesite , homepagemobile, msi, razerblade,dell,hp,asus,acer,apple,lenovo, samsungmobile,oppo,vivo,xiaomi,realme,oneplus,applemobile,poco,nokia


class alllaptopsAdmin(admin.ModelAdmin):
    list_display=('laptopname','price','site')
class acerAdmin(admin.ModelAdmin):
    list_display=['site','price']
class homepagemobileAdmin(admin.ModelAdmin):
    list_display=('mobilename','price')
class allmobilesAdmin(admin.ModelAdmin):
    list_display=('mobilename','price','site')


admin.site.register(homesite)
admin.site.register(gaminglaptop)
admin.site.register(homepagemobile)
admin.site.register(msi)
admin.site.register(dell)
admin.site.register(hp)
admin.site.register(razerblade)
admin.site.register(asus)
admin.site.register(acer)
admin.site.register(apple)
admin.site.register(lenovo)
admin.site.register(alllaptops,alllaptopsAdmin)

admin.site.register(samsungmobile)
admin.site.register(oppo)
admin.site.register(vivo)
admin.site.register(applemobile)
admin.site.register(xiaomi)
admin.site.register(realme)
admin.site.register(oneplus)
admin.site.register(poco)
admin.site.register(nokia)
admin.site.register(allmobiles,allmobilesAdmin)
admin.site.register(bestmidranger)
admin.site.register(latestflagship)