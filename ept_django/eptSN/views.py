from django.shortcuts import render, redirect
from .forms import SignInForm, MappingForm, LogInForm
from .models import Departement, Etudiant, Inscription, User
from django.db import transaction, IntegrityError
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
from .models import Etudiant, Departement,Classe, Inscription








# Create your views here.

#page d'accueil
@transaction.atomic
def index(request):
    depts = Departement.objects.all()
    if 'lang' in request.session:
        translation.activate(request.session["lang"])
    else:
        translation.activate("fr")

    #connexion
    if request.method=='POST' and 'login' in request.POST:
        logInform = LogInForm(request.POST)
        email = request.POST.get('login')
        password= request.POST.get('password')
        if not request.POST.get('remindMe', None):
            request.session.set_expiry(0)
        else:
            request.session["rememberMe"]=True
            request.session["username"]=email
            request.session["password"]=password

        #on cherche dans la base si c'est le bon email et le bon mot de passe
        etudiant = Etudiant.objects.filter(email=email,password=password)
        if etudiant.exists():
            user_obj=Etudiant.objects.get(email=email,password=password)
            messages.success(request, f'bienvenue {user_obj.prenom}')
            request.session['username'] = email
            username=email

            return render(request, 'eptSN/index.html',{"user":user_obj,"departements":depts})
        else:
            messages.info(request, _("adresse email ou mot de passe incorrect"))


    #inscription
    #si le formulaire est soumis (appuie sur valider)
    if request.method=='POST':
        #instanciation de notre formulaire avec les données saisies
        signInform = SignInForm(request.POST)
        if signInform.is_valid(): #is_valid vérifie si les données sont correctent, si oui il les stock dans un dictionnaire appelé cleaned_data
            #récupération des données     
            nom = signInform.cleaned_data['nom']
            prenom = signInform.cleaned_data['prenom']
            email = signInform.cleaned_data['email']
            departement= signInform.cleaned_data['departement']
            classe= signInform.cleaned_data['classe']
            dateNaissance= signInform.cleaned_data['dateNaissance']
            lieuNaissance= signInform.cleaned_data['lieuNaissance']
            password= signInform.cleaned_data['signInPassword']
            view= request.POST.get("page")


            try: #on met toutes les requêtes en transaction
                with transaction.atomic(): 
                    etudiant = Etudiant.objects.filter(email=email) #recupération de l'etudiant dans la BD (renvoie un object queryset)

                    if not etudiant.exists():
                        # si l'etudiant n'existait pas on le crée.
                        etudiant = Etudiant.objects.create(
                            nom=nom,
                            prenom=prenom,
                            email=email,
                            password=password,
                            date_naissance=dateNaissance,
                            lieu_naissance=lieuNaissance
                        )
                        #le message à afficher dans un toast
                        messages.success(request, f'salut {prenom}, votre compte a été créé avec succès!')
                        #on crée aussi une inscription pour lui
                        #on récupère l'object classe en faisant un filtre sur la classe et le département

                        classe_obj=Classe.objects.get(Q(nom_classe__istartswith=classe),Q(departement__nom_dept__icontains=departement) | Q(departement__nom_dept_en__icontains=departement))


                        inscription = Inscription.objects.create(
                            annee_scolaire= int(datetime.now().year),
                            etudiant=etudiant,
                            classe = classe_obj
                        ) 

                        #
                        return redirect('eptSN:'+view)

                        
                    else:
                        etudiant = etudiant.first()   #s'il existe on récupère la première occurence 
                        messages.warning(request, f'désolé {etudiant.prenom}, ce compte existe déja!')
                        #
                        return redirect('eptSN:'+view)



            except IntegrityError: #au cas de l'echec d'une transaction
                signInform.errors['internal'] = _("Une erreur interne est apparue. Merci de recommencer votre requête.")


        

    context = {
            'page': _("accueil"),
            'view':"index"
            }

    signInform = SignInForm() 
    logInform = LogInForm()
    context['signInform'] = signInform
    context['logInform'] = logInform
    context['departements'] = depts

    return render(request, 'eptSN/index.html', context)


#page Contacts
def contacts(request):
    mappingform = MappingForm() 
    signInform = SignInForm()
    logInform = LogInForm()
    page=request.resolver_match.url_name


    depts = Departement.objects.all()

    context = {
        'form':mappingform,
        'page' :_('contacts'),
        'view' : "contacts",
        'departements':depts,
        'signInform':signInform,
        'logInform':logInform,
        'view':'contacts'
    }
    return render(request, 'eptSN/contacts.html', context)


#traitement de l'itinéraire maps
def ajax(request):
    form = MappingForm(request.POST)
    if form.is_valid(): 
        adresse = request.POST.get("adresse")
        bp = request.POST.get("bp")
        data=_("implementation en cours !!! revenez plus tard")
    else:
        context={
            'form':MappingForm()
        }
        return render(request, 'eptSN/contacts.html', context)


    return JsonResponse({"result": data})


#langage translation
def switch_lang(request, lang_code="fr", page="index"):
    #gérer la rediction
    if page:
        view=page
    if request.method == "GET":
        if lang_code=="fr":
            request.session["lang"] = "fr"
            translation.activate("fr")
        elif lang_code=="en":
            request.session["lang"] = "en"
            translation.activate("en")

        return redirect('eptSN:'+view)






#deconnexion
def logOut(request):
    if request.method=='GET':
        if request.session.has_key('username'):
            del request.session['username']
            request.session.flush()
            return redirect('eptSN:index')
    else:
        return render(request, 'eptSN/index.html')



#page GIT
def goToDept(request, department="default"):
    depts = Departement.objects.all()

    if "username" in request.session:
        #récupérons d'abord les objects inscription
        insc_objects=Inscription.objects.filter(Q(classe__nom_classe__iendswith="GIT"))
        #maintenant récupérons les étudiants pour chaque object
        etudiants=list()
        for i_obj in insc_objects:
            etudiants.append((i_obj.etudiant, i_obj.classe))
        return render(request, 'eptSN/gitDept.html',{"etudiants":etudiants,"departements":depts})
    else:
        messages.warning(request, _('désolé Vous devez être connecté pour accéder à cette page'))
        return redirect('eptSN:index')
