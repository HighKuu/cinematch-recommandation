import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from sklearn.neighbors import NearestNeighbors
from st_on_hover_tabs import on_hover_tabs
from pathlib import Path
import base64


st.set_page_config(layout="wide")

st.markdown("""
<h1 style='text-align: center; color: black;'>
    <em>Wild Code School 2025</em><br>run
    <strong>Projet 2 - IMDb</strong><br>
</h1>
""", unsafe_allow_html=True)

# Utiliser des colonnes pour centrer l'image
col1, col2, col3 = st.columns([1.5, 1, 1])

with col2:  # Placer l'image dans la colonne centrale
    st.image("logo projet2.PNG", width=200)

# Convertir l'image locale en base64
image_path = Path("logo arriere plan 3.png")
if image_path.is_file():
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
else:
    st.error(f"L'image '{image_path.name}' est introuvable dans le dossier : {image_path.parent}")

# CSS avec image de fond en base64
css = f'''
<style>

    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        
    }}

    section[data-testid='stSidebar'] {{
        background-color: #111;
        min-width: unset !important;
        width: unset !important;
        flex-shrink: unset !important;
    }}

    button[kind="header"] {{
        background-color: transparent;
        color: rgb(180, 167, 141);
    }}

    @media(hover) {{
        header[data-testid="stHeader"] {{
            display: none;
        }}

        section[data-testid='ststreaSidebar'] > div {{
            height: 100%;
            width: 95px;
            position: relative;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            transition: 0.5s ease;
            padding-top: 60px;
            white-space: nowrap;
        }}

        section[data-testid='stSidebar'] > div:hover {{
            width: 388px;
          
        }}

        button[kind="header"] {{
            display: none;
        }}
    }}

    @media(max-width: 272px) {{
        section[data-testid='stSidebar'] > div {{
            width: 15rem;
        }}

    }}

    /* Ajouter une image de fond */
</style>
'''
st.markdown(css, unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Présentation', 'Analyse de marché', 'KPI', "Système de recommandation", "Machine Learning","Axes d'amélioration"], 
                         iconName=['co_present', 'signpost', 'data_thresholding', 'search', 'select_all','tips_and_updates'], default_choice=0)
	
if tabs =='Présentation':
    # Titre principal
    st.title("Relance de l'activité d'un cinéma indépendant")

    # Introduction
    st.markdown("""
    Un directeur de cinéma basé dans la Creuse nous a sollicités face aux difficultés qu'il rencontrait pour attirer un public suffisant et relancer son activité. 
    Après une analyse approfondie des tendances de consommation cinématographique, nous lui avons recommandé de s'implanter dans le département du Nord (59), 
    un territoire offrant un public plus large et une culture cinématographique plus développée. 

    Pour accompagner cette transition, nous avons conçu une solution innovante basée sur l'analyse de données et le machine learning, permettant de générer 
    une liste de recommandations de films adaptées aux attentes du nouveau public tout en tenant compte des préférences exprimées par le client.
    """)

    # Titre principal
    st.title("Plan d'action pour la relance d'un cinéma indépendant")
    # Section 1 : Récupération et traitement des données
    st.header("1. Récupération et traitement des données")
    st.write("""
    - **Extraction des données** : Base de données IMDB (origine, genres, thématiques, années de sortie).
    - **Nettoyage et tri** : Utilisation des bibliothèques Python comme **pandas** et **DuckDB** pour isoler les données pertinentes.
    - **Analyse exploratoire** : Visualisation des tendances grâce à **matplotlib** et **seaborn**.
    """)
    # Section 2 : Création d’un algorithme de recommandation
    st.header("2. Création d’un algorithme de recommandation")
    st.write("""
    - **Modèle** : Méthode des **proches voisins (Nearest Neighbors)**.
    - **Critères principaux** :
    - Thématiques saisonnières : Halloween, Noël, vacances scolaires.
    - Genres préférés : Comédie/Action, Animation, Horreur, et Familiale.
    - Films récents : À partir de 2020.
    """)
    # Section 3 : Visualisation et interface utilisateur
    st.header("3. Visualisation et interface utilisateur")
    st.write("""
    - **Application interactive** : Développée avec **Streamlit** pour permettre au client de personnaliser ses critères.
    - **Visualisations dynamiques** : Créées avec **Plotly Express** pour explorer les tendances du marché cinématographique et les recommandations de films.
    """)
    # Footer
    st.markdown("---")

    # Méthodologie et choix techniques
    st.header("Méthodologie et choix techniques")
    st.markdown("""
    - Nettoyage rigoureux des données pour garantir leur qualité et leur pertinence.
    - Simulations et validations régulières pour s'assurer de l'exactitude et de la fiabilité des recommandations.
    - Conception d'une interface intuitive et accessible, adaptée aux utilisateurs novices en technologie.
    """)

    # Résultat attendu
    st.header("Résultat attendu")
    st.markdown("""
    Cette solution permettra au directeur de cinéma de proposer une programmation sur mesure, optimisant l'attractivité de ses projections et garantissant une 
    relance durable de son activité dans un marché plus favorable.
    """)

    st.header("Technos utilisées pour l'organisation et la réalisation du projet :")
    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    with col1 :	
        st.image("logo slack.PNG")
    with col2 :	
        st.image("logo imdb.PNG")
    with col3 :	
        st.image("logo tmdb.PNG")
    with col4 :	
        st.image("logo python.PNG")
    with col5 :	
        st.image("logo pandas.PNG")
    with col6 :	
        st.image("logo vscode.PNG")
    with col7 :	
        st.image("logo scikit-learn.PNG")
    with col8 :	
        st.image("logo streamlit.PNG")

elif tabs == 'Analyse de marché':
    st.title("Analyse de marché du département du Nord")

        # Section "Analyse démographique"
    st.subheader("Analyse démographique")
    st.image("analyse demographique.png", caption="Analyse des données démographiques liées aux films en 2024.", use_container_width=True)

    # Données
    data = {
        "Mois": [
            "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
            "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
        ],
        "2023": [14.82, 18.03, 15.76, 18.61, 13.76, 10.22, 18.30, 15.42, 8.95, 14.01, 15.17, 17.34],
        "2024": [13.71, 15.08, 15.19, 11.90, 15.72, 14.15, 17.87, 14.15, 10.05, 15.30, 17.69, 20.46],
        "Évolution (%)": [-7.4, -16.4, -3.6, -36.1, 14.3, 38.4, -2.4, -8.3, 12.2, 9.2, 16.6, 18.0]
    }

    df = pd.DataFrame(data)

    # Calcul du cumul annuel pour 2023 et 2024
    cumul_2023 = df["2023"].sum()
    cumul_2024 = df["2024"].sum()

    # Création du graphique
    fig = go.Figure()

    # Ligne pour 2023
    fig.add_trace(go.Scatter(
        x=df["Mois"],
        y=df["2023"],
        mode="lines+markers",
        name="2023",
        line=dict(color="blue", width=3),
        marker=dict(size=8)
    ))

    # Ligne pour 2024
    fig.add_trace(go.Scatter(
        x=df["Mois"],
        y=df["2024"],
        mode="lines+markers",
        name="2024",
        line=dict(color="red", width=3),
        marker=dict(size=8)
    ))

    # Annotations pour les évolutions
    for i, row in df.iterrows():
        fig.add_annotation(
            x=row["Mois"],
            y=row["2024"],
            text=f"{row['Évolution (%)']}%",
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-30 if row["Évolution (%)"] >= 0 else 30,
            font=dict(color="green" if row["Évolution (%)"] >= 0 else "red", size=10),
        )

    # Personnalisation
    fig.update_layout(
        title=f"Évolution mensuelle de la fréquentation totale (2023 vs 2024)<br><sup>Cumul annuel : 2023 = {cumul_2023:.2f} millions, 2024 = {cumul_2024:.2f} millions</sup>",
        title_x=0.5,  # Centrer le titre
        xaxis_title="Mois",
        yaxis_title="Fréquentation (millions d'entrées)",
        legend=dict(title="Année"),
        template="plotly_white",
        hovermode="x unified",
    )

    # Interface Streamlit
    st.title("Évolution mensuelle de la fréquentation totale")
    st.markdown(f"""
    - **Cumul annuel 2023** : {cumul_2023:.2f} millions d'entrées
    - **Cumul annuel 2024** : {cumul_2024:.2f} millions d'entrées
    """)
    st.plotly_chart(fig)

    # graph2
    # Création des données
    data = {
        "Origine Film": ["Films français", "Films américains", "Autres films"],
        "2023": [40.1, 41.2, 18.7],
        "2024": [44.4, 36.7, 18.9],
    }

    # Création d'un DataFrame
    df = pd.DataFrame(data)

    # Titre de l'application
    st.title("Évolution des parts de marché des films (2023-2024)")

    # Affichage du tableau dans Streamlit
    st.subheader("Tableau des parts de marché (%)")
    st.dataframe(df.style.format({"2023": "{:.1f}%", "2024": "{:.1f}%"}))

    # Transformation pour le graphique
    df_melted = df.melt(id_vars="Origine Film", var_name="Année", value_name="Part de marché (%)")

    # Création du graphique interactif
    fig = px.bar(
        df_melted,
        x="Origine Film",
        y="Part de marché (%)",
        color="Année",
        barmode="group",
        title="Évolution des parts de marché des films",
        text="Part de marché (%)",
        color_discrete_map={"2023": "skyblue", "2024": "orange"},  # Couleurs spécifiques pour les années
    )

    # Ajout de texte et mise en forme
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(
        yaxis=dict(title="Part de marché (%)", ticksuffix="%"),
        legend_title_text="Année",  # Titre de la légende
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)

    #graph3

    # Données
    data = {
        "Titre": [
            "Un p’tit truc en plus", "Le Comte de Monte-Cristo", "Vice-Versa 2",
            "Vaiana 2", "L’Amour ouf", "Moi, moche et méchant 4", "Dune : Deuxième partie",
            "Deadpool & Wolverine", "Gladiator II", "La Planète des singes : le nouveau royaume"
        ],
        "Nationalité": ["France", "France", "États-Unis", "États-Unis", "France",
                        "États-Unis", "États-Unis", "États-Unis", "États-Unis", "États-Unis"],
        "Sortie": [
            "2024-05-01", "2024-06-28", "2024-06-19", "2024-11-27", "2024-10-16",
            "2024-07-10", "2024-02-28", "2024-07-24", "2024-11-13", "2024-05-08"
        ],
        "Entrées (millions)": [10.31, 9.13, 8.26, 6.43, 4.73, 4.32, 4.13, 3.69, 2.87, 2.50],
    }

    df = pd.DataFrame(data)

    # Palette de couleurs personnalisée
    color_map = {"France": "blue", "États-Unis": "red"}

    # Diagramme circulaire : Répartition des entrées par nationalité
    pie_chart = px.pie(
        df,
        names="Nationalité",
        values="Entrées (millions)",
        title="Répartition des entrées par nationalité",
        color="Nationalité",
        color_discrete_map=color_map
    )

    # Graphique en barres : Entrées triées par ordre décroissant
    bar_chart = px.bar(
        df.sort_values(by="Entrées (millions)", ascending=False),
        x="Titre",
        y="Entrées (millions)",
        color="Nationalité",
        orientation="v",  # Graphique vertical
        title="Comparaison des entrées des films (triées par ordre décroissant)",
        labels={"Titre": "Films", "Entrées (millions)": "Entrées (millions)"},
        color_discrete_map=color_map
    )

    # Interface Streamlit
    st.title("Analyse des Entrées des Films en 2024")

    # Sous-titre et diagramme circulaire
    st.subheader("Répartition des entrées par nationalité")
    st.plotly_chart(pie_chart)

    # Sous-titre et graphique en barres
    st.subheader("Comparaison des entrées des films")
    st.plotly_chart(bar_chart)

elif tabs == 'KPI':
    st.title("KPI à suivre")
    
    # Section "Analyse démographique"
    st.subheader("KPI")
    # Utiliser des colonnes pour centrer l'image
    col1, col2, col3 = st.columns([1.5, 1, 1])

    with col2:  # Placer l'image dans la colonne centrale
        st.image("kpi.png", width=400)

    # Téléchargement du CSV
    df_français_comedy_action = pd.read_csv("df_français_comedy_action03.csv")

    # Comptage du nombre de films par genre
    df_count_genres = df_français_comedy_action["genres"].value_counts().reset_index()
    df_count_genres.columns = ["genres", "count"]

    # Création du graphique à barres avec Plotly Express
    fig = px.bar(
        df_count_genres,
        x="genres",
        y="count",
        color="genres",
        title="Répartition des genres de films",
        labels={"genres": "Genres", "count": "Nombre de films"},
        text="count",
        color_discrete_sequence=px.colors.sequential.Viridis
    )

    # Mise à jour de la présentation
    fig.update_traces(textposition="outside")
    fig.update_layout(
        xaxis_title="Genres",
        yaxis_title="Nombre de films",
        showlegend=False,  # Masquer la légende car chaque barre représente un genre unique
    )

    # Interface Streamlit
    st.title("Analyse des Genres de Films")
    st.subheader("Répartition des genres de films")
    st.plotly_chart(fig)

    # répartition année
    # Comptage du nombre de films par année
    df_films_annee = df_français_comedy_action["annee_sortie"].value_counts().reset_index()
    df_films_annee.columns = ["annee_sortie", "count"]

    # Création du diagramme circulaire avec Plotly Express
    fig = px.pie(
        df_films_annee,
        names="annee_sortie",
        values="count",
        title="Répartition des films par année",
        labels={"annee_sortie": "Année de sortie", "count": "Nombre de films"},
        color_discrete_sequence=px.colors.sequential.Viridis,
        hole=0.3  # Pour créer un diagramme circulaire en anneau
    )

    # Mise à jour des annotations pour afficher les pourcentages
    fig.update_traces(textinfo="percent+label")

    # Interface Streamlit
    st.title("Analyse des Films sur les 5 Dernières Années")
    st.subheader("Répartition des films par année")
    st.plotly_chart(fig)

elif tabs == 'Système de recommandation':
    st.title("Système de recommandation")

    st.cache_resource.clear()
    st.cache_data.clear()

    # Téléchargement du CSV
    df_français_comedy_action = pd.read_csv("df_français_comedy_action03.csv")
    liste_films = df_français_comedy_action['titre_original'].tolist()

    # Sélection du film
    film_rechercher = st.selectbox(
        "Sélectionnez un film pour découvrir des recommandations similaires :",
        options=liste_films,
        placeholder="Sélectionne ici..."
    )
    

        # Utilisation de st.slider
    nombre_voisin = st.slider(
        "Entrez un nombre de recommandations :",
        min_value=1,  # Nombre minimal
        max_value=20,  # Nombre maximal
        value=5  # Valeur par défaut
    )

    st.write(f"Nombre sélectionné : {nombre_voisin}")

    if nombre_voisin :
        # Chargement des données pour l'entraînement
        X = pd.read_csv("df_X.csv")

        # Séparation des données
        df_film_recherché = X.loc[X['titre_original'] == film_rechercher]
        df_reste_films = X.loc[X['titre_original'] != film_rechercher]

        # Vérification que le film recherché existe
        if df_film_recherché.empty:
            st.error("Film non trouvé dans la base de données.")
        else:
            # Modèle NN
            modelnn = NearestNeighbors(n_neighbors=nombre_voisin, metric='cosine')
            modelnn.fit(df_reste_films.drop(["titre_original", "index_original"], axis=1))

            # Trouver les voisins
            distances, indices = modelnn.kneighbors(
                df_film_recherché.drop(["titre_original", "index_original"], axis=1).values
            )

            # Récupérer les voisins
            voisins = [
                df_reste_films.iloc[index]['titre_original'] for index in indices[0]
            ]

            # Recommandations
            df_films_recommande = df_français_comedy_action.loc[
                df_français_comedy_action['titre_original'].isin(voisins)
            ]


            # stoké chemin affiche, titre et description
            chemin_daffiche_list = df_films_recommande['chemin_affiche'].values.tolist()
            titre_list = df_films_recommande['titre_original'].values.tolist()
            description_list = df_films_recommande['description_fr'].values.tolist()
            genre_list = df_films_recommande['genres'].values.tolist()
            annee_list = df_films_recommande['annee_sortie'].values.tolist()
            note_list = df_films_recommande['moyenne_notes'].values.tolist()
            video_list = df_films_recommande['video_id'].values.tolist()
                
            # Base URL pour les affiches (TMDB dans cet exemple)
            base_url = "https://image.tmdb.org/t/p/w500"

            # Parcourir chaque ligne du dataframe pour afficher les films
            for affiche, titre, description, genre, annee, note, video in zip(chemin_daffiche_list, titre_list, description_list, genre_list, annee_list, note_list, video_list):
                col1, col2 = st.columns([1, 2])

                # Colonne gauche : Affiche
                with col1:
                    st.image(f"{base_url}{affiche}", use_container_width=True)

                # Colonne droite : Titre, description et détails
                with col2:
                    st.markdown(
                        f"""
                        <div style="text-align: left; padding: 10px; border: 1px solid #ccc; border-radius: 8px; background-color: #f9f9f9;">
                            <h1 style='margin-top: 0px; color: #333; font-size: 22px;'>{titre}</h1>
                            <p style='font-size: 16px; color: #555; margin-top: 5px;'><strong>Genre :</strong> {genre}</p>
                            <p style='font-size: 16px; color: #555;'><strong>Année de sortie :</strong> {annee}</p>
                            <p style='font-size: 16px; color: #555;'><strong>Note moyenne :</strong> ⭐ {note}/10</p>
                            <p style='font-size: 14px; color: #777; margin-top: 15px; text-align: justify;'>{description}</p>
                            <div style="margin-top: 20px; text-align: center;">
                                <iframe width="100%" height="315" 
                                    src="https://www.youtube.com/embed/{video}" 
                                    title="YouTube video player" 
                                    frameborder="0" 
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                    allowfullscreen>
                                </iframe>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                # Séparateur entre les films
                st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)


elif tabs == 'Machine Learning':
    st.title("Machine Learning")

        # Titre principal
    st.header("🔄 Prétraitement et Traitement des Données pour Machine Learning")

    # Introduction
    st.markdown(
        """
        Avant de construire un modèle de machine learning, un travail conséquent de prétraitement et de traitement des données a été réalisé. 
        Cette étape est essentielle pour garantir des performances optimales du modèle et des résultats fiables.
        """
    )

    # Sections
    st.subheader("✏️ Étapes clés du prétraitement")

    # Visualisation
    st.subheader("1. Visualisations exploratoires")
    st.write("Exploration des données pour identifier les corrélations et vérifier les distributions (par exemple, lois normales).")

    # Gestion des valeurs manquantes
    st.subheader("2. Gestion des valeurs manquantes")
    st.write("Traitement des données manquantes pour éviter les biais ou erreurs lors de l'entraînement du modèle.")

    # Pondérations
    st.subheader("3. Établissement des pondérations")
    st.write(
        """Deux listes de pondérations ont été établies pour distinguer les variables numériques et catégoriques, 
        permettant une meilleure prise en compte des spécificités de chaque type de variable."""
    )

    # Séparation des variables
    st.subheader("4. Séparation des variables")
    st.write("Les variables indépendantes ont été séparées en deux catégories : numériques et catégoriques.")

    # Application des pondérations
    st.subheader("5. Application des pondérations")
    st.write("Les pondérations ont été appliquées afin d'ajuster l'importance relative des variables dans le modèle.")

    # Normalisation
    st.subheader("6. Normalisation des variables numériques")
    st.write(
        """Toutes les variables numériques indépendantes ont été normalisées pour garantir une cohérence des échelles, 
        ce qui est essentiel pour les algorithmes sensibles aux amplitudes des données."""
    )

    # Encodage des variables catégoriques
    st.subheader("7. Encodage des variables catégoriques")
    st.write("Les variables catégoriques ont été encodées en formats numériques exploitables par le modèle.")

    # Concaténation des variables
    st.subheader("8. Concaténation des variables traitées")
    st.write(
        "Après traitement, les variables numériques et catégoriques ont été regroupées pour former la matrice finale, prête à être utilisée comme entrée pour le modèle."
    )

    # Conclusion de l'introduction
    st.subheader("🔝 Importance du prétraitement")
    st.markdown(
        """
        Ce travail en amont est indispensable pour garantir que les résultats obtenus avec le modèle seront à la fois fiables et précis.
        Le soin apporté à ces étapes assure une base solide pour la construction de modèles performants.
        """
    )

    # début du model
    st.header("Début du modèle nn de Machine learning")

    code = '''

    # Téléchargement du CSV
    df_français_comedy_action = pd.read_csv("df_français_comedy_action03.csv")
    liste_films = df_français_comedy_action['titre_original'].tolist()

    # Sélection du film
    film_rechercher = st.selectbox(
        "Sélectionnez un film pour découvrir des recommandations similaires :",
        options=liste_films,
        placeholder="Sélectionne ici..."
    )
    

        # Utilisation de st.slider
    nombre_voisin = st.slider(
        "Entrez un nombre de recommandations :",
        min_value=1,  # Nombre minimal
        max_value=20,  # Nombre maximal
        value=5  # Valeur par défaut
    )

    st.write(f"Nombre sélectionné : {nombre_voisin}")

    if nombre_voisin :
        # Chargement des données pour l'entraînement
        X = pd.read_csv("df_X.csv")

        # Séparation des données
        df_film_recherché = X.loc[X['titre_original'] == film_rechercher]
        df_reste_films = X.loc[X['titre_original'] != film_rechercher]

        # Vérification que le film recherché existe
        if df_film_recherché.empty:
            st.error("Film non trouvé dans la base de données.")
        else:
            # Modèle NN
            modelnn = NearestNeighbors(n_neighbors=nombre_voisin, metric='cosine')
            modelnn.fit(df_reste_films.drop(["titre_original", "index_original"], axis=1))

            # Trouver les voisins
            distances, indices = modelnn.kneighbors(
                df_film_recherché.drop(["titre_original", "index_original"], axis=1).values
            )

            # Récupérer les voisins
            voisins = [
                df_reste_films.iloc[index]['titre_original'] for index in indices[0]
            ]

            # Recommandations
            df_films_recommande = df_français_comedy_action.loc[
                df_français_comedy_action['titre_original'].isin(voisins)
            ]

    '''
    st.code(code, language="python")


elif tabs == "Axes d'amélioration":
    st.title("Axes d'amélioration de notre livrable")

    st.title("Axes d'Améliorations pour Intégrer les Films d'Animation, de Noël et d'Horreur en Période de Vacances")
    st.header("Objectif Principal")
    st.write("""
    Profiter des thématiques saisonnières pour attirer une nouvelle clientèle, leur faire découvrir ou redécouvrir l'expérience cinématographique, et ainsi stimuler la fréquentation tout au long de l'année. L'objectif est de créer un lien émotionnel avec le public en proposant des expériences mémorables et immersives adaptées aux différents genres.
    """)
    st.header("1. Films d'Animation")
    st.subheader("Analyse des besoins")
    st.write("""
    - Attirer les familles et les enfants, tout en captant l'attention des amateurs d'animation adulte.
    - Proposer des films qui allient divertissement et valeur éducative.
    """)
    st.subheader("Stratégies d'amélioration")
    st.write("""
    - **Acquisition de contenu :** Sélectionner des films classiques, récents et indépendants pour offrir un large éventail d'options.
    - **Activités interactives :** Organiser des ateliers créatifs, des séances de coloriage, et des animations en lien avec les personnages des films projetés.
    - **Expériences immersives :** Proposer des marathons de films d'animation et des avant-premières exclusives.
    - **Marketing ciblé :** Campagnes sur les réseaux sociaux, partenariats avec des écoles, et publicités sur des plateformes fréquentées par les familles.
    - **Personnalisation de l'expérience :** Ajouter des options de doublage, sous-titrage et playlists thématiques pour satisfaire divers publics.
    - **Fidélisation :** Introduire des cartes de fidélité et des réductions spéciales pour les familles.
    """)
    st.header("2. Films de Noël")
    st.subheader("Analyse des besoins")
    st.write("""
    - Exploiter la forte demande pendant la saison des fêtes pour créer une ambiance chaleureuse et festive.
    - Cibler les familles, les couples et les groupes d'amis cherchant des expériences conviviales.
    """)
    st.subheader("Stratégies d'amélioration")
    st.write("""
    - **Programmation festive :** Proposer des marathons, des avant-premières et des projections spéciales accompagnées de décorations thématiques et d'effets lumineux.
    - **Animations spéciales :** Séances photos avec des personnages emblématiques de Noël, ateliers de fabrication de décorations et événements festifs interactifs.
    - **Marketing festif :** Lancer des concours et jeux avec des cadeaux personnalisés et des réductions pour les groupes.
    - **Partenariats :** Collaborations avec des marques et des entreprises locales pour des promotions croisées, comme des calendriers de l’Avent contenant des billets de cinéma.
    - **Expériences gourmandes :** Offrir des menus thématiques (popcorn saveur cannelle, chocolats chauds) pour renforcer l’atmosphère festive.
    """)
    st.header("3. Films d'Horreur")
    st.subheader("Analyse des besoins")
    st.write("""
    - Attirer un public plus jeune et amateur de sensations fortes en jouant sur la saisonnalité (Halloween, nuits spéciales).
    - Proposer des expériences uniques et immersives pour renforcer l’attractivité.
    """)
    st.subheader("Stratégies d'amélioration")
    st.write("""
    - **Expérience immersive :** Projections nocturnes, marathons thématiques, et créations d'ambiances effrayantes dans la salle (jeux de lumières, fumée, effets sonores).
    - **Activités thématiques :** Escape games, maisons hantées et soirées costumées en lien avec les films projetés.
    - **Marketing effrayant :** Campagnes promotionnelles pour Halloween, concours de costumes, et défis interactifs sur les réseaux sociaux.
    - **Contenu varié :** Mélanger films cultes, nouveautés et courts-métrages indépendants pour attirer un public diversifié.
    - **Animations spéciales :** Discussions après projection avec des réalisateurs ou experts en cinéma d’horreur, ajoutant une dimension éducative et participative.
    - **Offres exclusives :** Pass soirée horreur ou réductions pour les groupes d’amis.
    """)
    st.header("Conclusion")
    st.write("""
    Ce plan d'améliorations vise à exploiter pleinement les thématiques saisonnières pour attirer et fidéliser un public diversifié. En créant des expériences uniques et immersives, il s'agit de transformer les visiteurs occasionnels en spectateurs réguliers. Ces stratégies s'appuient sur des contenus variés, des événements interactifs et des campagnes marketing ciblées afin d'insuffler une dynamique durable dans la fréquentation des salles de cinéma.
    """)