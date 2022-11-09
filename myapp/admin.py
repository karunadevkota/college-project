from django.contrib import admin
from myapp.models import Contact, Profile,Report,News,Case_Study,Record,ChartData
admin.site.site_header = "CRIME REPORT MANAGEMENT| Admin"
# Register your models here.

class NewsAdmin(admin.ModelAdmin): 
      list_display=('title','content')    
 
class ReportAdmin(admin.ModelAdmin):     
     list_display=('victimname','description','affected')
     radio_fields={"affected":admin.HORIZONTAL}      
      
admin.site.register(Report,ReportAdmin) 
   
admin.site.register(News,NewsAdmin)      
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Case_Study)
admin.site.register(ChartData)
admin.site.register(Record)
