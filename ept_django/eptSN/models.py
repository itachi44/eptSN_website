from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator



class User(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    class Meta:
            verbose_name = "Utilisateur"

    def __str__(self):
        return self.nom +" "+ self.prenom

class Departement(models.Model):
    nom_dept = models.CharField(max_length=200, unique=True)
    nom_dept_en = models.CharField(help_text='dept name in English', max_length=200, null=True)
    email_dept = models.EmailField(max_length=200, unique=True) 
    numero_dept = models.CharField(max_length=200, unique=True)
    desc_dept = models.TextField()


    class Meta:
            verbose_name = "Departement"


    def __str__(self):
        return self.nom_dept


class Classe(models.Model):
    nom_classe= models.CharField(max_length=100, unique=True)
    desc_classe= models.TextField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, blank=True)

    
    class Meta:
            verbose_name = "Classe"

    def __str__(self):
        return self.nom_classe



class Etudiant(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    date_naissance=models.DateField() 
    lieu_naissance=models.CharField(max_length=200)



    class Meta:
            verbose_name = "Etudiant"


    def __str__(self):
        return self.nom +" "+ self.prenom




class Professeur(models.Model):
    phone_regex=RegexValidator(regex=r'^(\+221)?[- ]?(77|70|76|78)[- ]?([0-9]{3})[- ]?([0-9]{2}[- ]?){2}$', message="le numero de telephone est invalide!") #phone number validator
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    contact_prof = models.CharField(validators=[phone_regex], max_length=20, unique=True) 
    date_adhesion=models.DateField() 
    chef_departement = models.BooleanField(default=False)
    #relation many to many avec departement
    departments = models.ManyToManyField(Departement, related_name='professeurs')



    class Meta:
            verbose_name = "Professeur"



    def __str__(self):
        return self.nom +" "+ self.prenom





class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=200, unique=True)
    code_matiere = models.CharField(max_length=200, unique=True) 
    coef_matiere = models.IntegerField()
    credit_matiere = models.IntegerField()
    quota_horaire= models.IntegerField()
    desc_matiere= models.TextField()
    #many to many field with professeur
    professeurs = models.ManyToManyField(Professeur, related_name='matieres')



    class Meta:
            verbose_name = "Matiere"

    def __str__(self):
        return self.nom_matiere+"/"+ self.code_matiere



class UE_matiere(models.Model):
    nom_UE = models.CharField(max_length=100, unique=True)
    code_UE =  models.CharField(max_length=100, unique=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE) 
    matiere = models.ForeignKey(Matiere,related_name='UE_matieres', on_delete=models.CASCADE) 

    def coef_UE(id_UE):
        s=0
        #on recupère toutes les matières d'une UE
        ue = UE_matiere.objects.get(id=id_UE)
        mats =ue.matiere.all()
        #ensuite on fait la somme des coef des différentes matières
        for m in mats:
            s+=m.coef_matiere
        return s
    
    def credit_UE():
        s=0
        #on recupère toutes les matières d'une UE
        ue = UE_matiere.objects.get(id=id_UE)
        mats =ue.matiere.all()
        #ensuite on fait la somme des credits des différentes matières
        for m in mats:
            s+=m.credit_matiere
        return s

    def __str__(self):
        return self.nom_UE

    class Meta:
        verbose_name = "UE_matiere"






class Inscription(models.Model):
    annee_scolaire = models.PositiveIntegerField(validators=[MinValueValidator(2019), MaxValueValidator(datetime.now().year)])
    etudiant = models.ForeignKey(Etudiant,related_name="inscriptions", on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Inscription"



