from django.db import models

#manage

class CourseManager(models.Manager):
    def search (self, query): #quando a função for chamada, a string que for apssada como parametro vai ser usada na busca
        return self.get_queryset().filter( #e vai retornar um objeto q contenha a string passada na descrição ou no nome
            
            #models.q vai retornar um ou outro
            models.Q(name__icontains=query) | 
            models.Q(description__icontains = query)
            )#retorna o objeto  


# Create your models here. acesso ao banco de dados

class Course(models.Model):
    #campos da tabela    //nivel de usuário
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho")         #não é obrigatório
    description = models.TextField("Descrição", blank = True)
    about = models.TextField('Sobre o Curso', blank=True)

    start_date = models.DateField("Data de inicio", auto_now=False, auto_now_add=False, blank = True, null = True)
    image = models.ImageField("Image", upload_to= 'courses/images', height_field=None, width_field=None, 
        max_length=None,
        null = True, #vai aceitar valor nulos
        blank = True 
        )
                                             #caminho configurado em sttigns.py
    created_at = models.DateField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateField("Atualizado em", auto_now=True, auto_now_add=False)#toda vez que for atualizado

    objects = CourseManager()#manager customizado definido a cima

    def __str__(self):#representação de string
        return self.name #vai retornar o nome pra pagina admin


    