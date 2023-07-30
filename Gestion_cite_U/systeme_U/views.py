from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def funct_logement(request):
    if request.method == 'POST':
        fm = Register_log(request.POST)
        if fm.is_valid():
            fm.save() 
    else:
        fm = Register_log()
    return render(request, 'systeme_U/logement.html',{'form':fm})

# ici on definir la fonction qui va recuperer les donnees dans la base de donnees et envoyer au frontend
#---------------------------------------------------------------------------------------------------------------

def page_chambre_collectif(request):
    niveau123=[]
    niveau45=[]
    etudiants = Occuper.objects.all()  
    niveaux = [obj.id_etudiant.niveau for obj in etudiants]
    
    for niv in niveaux:
        if niv in range(1,4): 
            niveau123.append(niv)
        else:
            niveau45.append(niv)
                
    context = {
        'etudiants': etudiants,
        'niv123':   niveau123
    }
    return render(request,'systeme_U/Etudiant_Logement_coll.html',context)

def page_chambre_individuel(request):
    niveau123=[]
    niveau45=[]
    etudiants = Occuper.objects.all()  
    niveaux = [obj.id_etudiant.niveau for obj in etudiants]

    for niv in niveaux:
        if niv in range(1,4): 
            niveau123.append(niv)
        else:
            niveau45.append(niv)
                
    context = {
        'etudiants': etudiants,
        'niv45':   niveau45
    }
    return render(request,'systeme_U/Etudiant_Logement_indi.html',context)