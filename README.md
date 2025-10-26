# CinéMatch - Système de Recommandation de Films

Application web de recommandation de films basée sur l'apprentissage automatique. Ce projet a été réalisé dans le cadre de ma formation Data Analyst chez Simplon.

## Le projet

CinéMatch est un système intelligent qui recommande des films similaires à partir d'une sélection de l'utilisateur. L'application utilise l'algorithme K-Nearest Neighbors pour analyser les caractéristiques des films et proposer des recommandations pertinentes.

**Lien de l'application déployée** : [À compléter après déploiement]

## Fonctionnalités

- **Recommandations personnalisées** : Sélectionnez un film et obtenez jusqu'à 10 recommandations similaires
- **Visualisation des bandes-annonces** : Regardez les trailers directement dans l'application
- **Interface moderne** : Design dark avec une navigation intuitive
- **Analyse détaillée** : Informations complètes sur chaque film (année, note, réalisateur, genre)

## Données

Le système analyse une base de 206 films français des genres :
- Comédie
- Action
- Films d'animation

Les données proviennent de TMDB (The Movie Database) et incluent :
- Titres originaux et français
- Années de sortie
- Notes moyennes
- Réalisateurs et acteurs
- Descriptions
- Liens vers les bandes-annonces

## Technologies utilisées

**Backend & Machine Learning**
- Python 3.11
- Pandas pour la manipulation de données
- Scikit-learn pour l'algorithme KNN
- NumPy pour les calculs numériques

**Frontend**
- Streamlit pour l'interface web
- Plotly pour les visualisations
- CSS personnalisé pour le design

**Déploiement**
- Streamlit Cloud
- GitHub pour le versioning

## Architecture du modèle

### Prétraitement des données

1. **Exploration** : Analyse des corrélations et distributions
2. **Nettoyage** : Gestion des valeurs manquantes
3. **Pondération** : Distinction des variables numériques et catégoriques
4. **Normalisation** : Mise à l'échelle des variables numériques
5. **Encodage** : Transformation des variables catégoriques
6. **Concaténation** : Création de la matrice finale

### Algorithme K-Nearest Neighbors

Le modèle utilise la distance cosinus pour mesurer la similarité entre films en se basant sur leurs caractéristiques (genre, réalisateur, acteurs, popularité, notes, etc.).

```python
model = NearestNeighbors(n_neighbors=5, metric='cosine')
model.fit(X_films)
distances, indices = model.kneighbors(film_recherché)
```

## Installation locale

### Prérequis
- Python 3.11 ou supérieur
- pip

### Installation

```bash
# Cloner le repository
git clone https://github.com/HighKuu/cinematch-recommandation.git
cd cinematch-recommandation

# Créer un environnement virtuel (optionnel mais recommandé)
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app_pro.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

## Structure du projet

```
cinematch-recommandation/
├── app_pro.py                          # Application principale
├── df_français_comedy_action03.csv    # Base de données des films
├── df_X.csv                           # Données prétraitées pour le ML
├── requirements.txt                   # Dépendances Python
├── logo projet2.PNG                   # Logo de l'application
└── README.md                          # Documentation
```

## Utilisation

1. **Sélectionnez un film** dans la liste déroulante
2. **Choisissez le nombre de recommandations** souhaitées (1-10)
3. **Cliquez sur "Obtenir des recommandations"**
4. **Explorez les résultats** avec les bandes-annonces associées

## Axes d'amélioration futurs

### Extensions possibles du catalogue

**Films d'animation**
- Élargir le catalogue aux films d'animation internationaux
- Cibler les familles avec des événements thématiques
- Partenariats avec des écoles et centres de loisirs

**Films de Noël**
- Programmation festive pendant les fêtes
- Ambiance et décoration thématique
- Événements spéciaux et animations

**Films d'horreur**
- Séances nocturnes et marathons thématiques
- Événements Halloween
- Expériences immersives

### Améliorations techniques

- Intégration d'un système de filtrage collaboratif
- Ajout de plus de genres cinématographiques
- Système de notation personnalisé
- Historique des recommandations par utilisateur
- API pour intégration externe

## Compétences démontrées

- Prétraitement et nettoyage de données
- Modélisation avec algorithmes de Machine Learning
- Développement d'applications web interactives
- Visualisation de données
- Déploiement d'applications cloud
- Gestion de version avec Git/GitHub

## Auteur

**Halim MOULAY**  
Formation Data Analyst - Simplon.co  
halim.moulay@gmail.com  
[GitHub](https://github.com/HighKuu)

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Remerciements

- TMDB pour les données des films
- Simplon.co pour la formation
- La communauté Streamlit pour la documentation
