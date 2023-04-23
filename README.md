# A PROPOS

**OpenClassrooms - Développeur d'application Python - Projet #7: Résolvez des problèmes en utilisant des algorithmes en Python**

_Testé sous Windows 10 et Python 3.10.2_

# Objectifs
Créer différents algorithmes qui vont afficher les actions les plus rentables (parmi un liste) à acheter pour maximiser le profit d'un client au bout de deux ans.
- Algorithme "brute force"
- Algorithme optimisé (knapsack version programmation dynamique)
- Non demandé mais quand même parce que éh oh : algo perso type gloûton ultra rapide


# Comankonfè (Windows)
### Récupération d'une copie du "dépôt"

- `git clone https://github.com/munchou/OpenClassrooms-Project-7.git`

### Création et activation de l'environnement virtuel
(Python doit avoir été installé)

- `python -m venv DOSSIER` où DOSSIER est le nom du dossier où sera créé l'environnement.
- Activation : `env\Scripts\activate`
    
### Installation des modules nécessaires

- `pip install -r requirements.txt`

### Pour lancer le programme

- `python xxx.py` ou `python3 xxx.py`
(où xxx est le nom du fichier de l'algorithme que vous souhaitez utiliser, donc ce sera "bruteforce", "optimized" ou "optimized_perso")

### Utilisation du programme
Pas grand chose à faire, en fait.
- Pour l'algo "bruteforce", il y a juste à le lancer et patienter, les résultats s'afficheront une fois le rendu terminé. Ne traite QUE le fichier des 20 actions.
- Pour les deux algo optimisés, un menu vous sera proposé via lequel vous pourrez choisir quel fichier traiter (celui de 20 actions, dataset1, dataset2 et même dataset3 qui est une fusion des 2 précédents).
