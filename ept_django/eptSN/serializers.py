from rest_framework import serializers 
from .models import Etudiant, Inscription


class EtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model=Etudiant
        fields=("nom","prenom","email","date_naissance","lieu_naissance")



class InscriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Inscription
        fields=("annee_scolaire","etudiant","classe")

