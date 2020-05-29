from django.contrib import admin
from courses.models import Course #importando o model do curso
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    #vai mostrar os campos 
    list_display = ['name', 'slug', 'start_date', 'created_at']
    #buscar pelos campos (se contém o nome ou o atalho)
    search_fields = ['name', 'slug']
    prepopulated_fields = { 'slug': ('name', )}

admin.site.register(Course, CourseAdmin) #ficara disponivel na pagina admin