from django import forms
from django.forms.utils import ErrorList
from django.forms import Field
from django.utils.translation import gettext as _, ugettext_lazy


Field.default_error_messages = {
    'required': ugettext_lazy("Veuillez renseigner ce champ!!")
}
#iterables
YEARS= [x for x in range(1996,2021)]
DEPARTMENTS =(
    ("Tronc commun", ugettext_lazy("tronc commun")),
    ("Génie informatique", ugettext_lazy("Génie informatique")),
    ("Génie électromécanique", ugettext_lazy("Génie électromécanique")),
    ("Génie civil", ugettext_lazy("Génie civil")),
    ("Génie aéronautique", ugettext_lazy("Génie aéronautique")),
)
CLASSES =(
    ("TC1", "TC1"),
    ("TC2", "TC2"),
    ("DIC1", "DIC1"),
    ("DIC2", "DIC2"),
    ("DIC3", "DIC3"),
)


  

class SignInForm(forms.Form):
    #champ nom
    nom = forms.CharField(
        label=_('Prénom et Nom'),
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': ugettext_lazy('Nom')}),
        required=True
        )
    #champ prenom
    prenom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('Prénom')}),
        required=True
        )

    #champ email
    email = forms.EmailField(
        label=_('Adresse Mail'),
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('etudiant@ept.sn')}), #ajout de la classs bootstrap : form-control
        required=True)

    #champ departement (select list)
    departement = forms.ChoiceField(
        label=_('Département'),
        choices = DEPARTMENTS,
        widget=forms.Select(attrs={'class':'form-select form-control'}),
        required=True)


    #champ classe (select list)
    classe = forms.ChoiceField(
            label=_('Classe-Niveau'),
            choices = CLASSES,
            widget=forms.Select(attrs={'class':'form-select form-control'}),
            required=True)

    #policy
    policy = forms.BooleanField(
        label="",
        required=False
    )

    #champ date de naissance (select list)
    dateNaissance = forms.DateField(
        label=_('Date et lieu de naissance'),
        widget=forms.SelectDateWidget(
        attrs={'class': 'form-select form-control inline-select'},
        years=YEARS),
        required=True)

    #champ Lieu de naissance
    lieuNaissance = forms.CharField(
        label=_('lieuNaissance'),
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('Lieu de Naissance')}),
        required=True
        )

    #captcha généré
    captcha = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
        required=True
        )

    #champ code captcha
    captchaCode = forms.CharField(
        label='Captcha',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('Entrer le code')}),
        required=True
        )
    #mot de passe
    signInPassword = forms.CharField(
        label='password',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('Saisir un mot de passe'),'type':'password'}),
        required=True
        )

    #mot de passe confirmation
    passwordConfirm = forms.CharField(
        label='confirmer le mot de passe',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('ressaisir le mot de passe'),'type':'password'}),
        required=True
        )


class LogInForm(forms.Form):


    #champ email
    login = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('adresse email')}), 
        required=True)

     #champ mdp
    password = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ugettext_lazy('Mot de passe'), 'type':'password'}),
        required=True
        )

    #remind
    remindMe = forms.BooleanField(
        required=False
    )



class MappingForm(forms.Form):
    

    #champ adresse
    adresse = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': ugettext_lazy('Ville / Région')}), 
        required=True)

     #champ bp
    bp = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': ugettext_lazy('Boite Postale')}),
        required=True
        )


