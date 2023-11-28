from django.db import models

# Create your models here.


class Autor(models.Model):
    
    nome = models.CharField("Nome", max_length=200)
    data_nascimento = models.DateField("Data de Nascimento", default="1980-01-01")
    email = models.EmailField("Email")
    idade = models.PositiveSmallIntegerField("Idade")
    avatar = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Escritor"
        verbose_name_plural = "Escritores"


class Livro(models.Model):
    
    EDITORA = (
        ('Ática', 'Ática'),
        ('Objetiva', 'Objetiva'),
        ('Atlas', 'Atlas'),
        ('FTD', 'FTD'),

    )
    
    titulo = models.TextField(default='Título do Livro',max_length=90)
    sinopse = models.TextField(default='Sinopse do Livro',max_length=255)
    ilustrador =  models.CharField('Ilustrador', max_length=70)
    ano = models.SmallIntegerField('Ano de Publicação', default=2000)
    escritor = models.ForeignKey(Autor,default='1',verbose_name='Autor', on_delete=models.CASCADE)
    editora = models.CharField(
        max_length=20,
        choices=EDITORA,
    )

    def __str__(self):
        return self.titulo 