import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="CinéMatch - Recommandation de Films",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS moderne dark avec navigation horizontale
st.markdown("""
<style>
    /* Palette dark */
    :root {
        --dark-bg: #0a0e27;
        --dark-secondary: #1a1f3a;
        --dark-card: #16213e;
        --accent-blue: #00d4ff;
        --accent-purple: #8b5cf6;
        --text-primary: #e2e8f0;
        --text-secondary: #94a3b8;
    }

    /* Background principal dark */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
    }

    /* Cacher la sidebar par défaut */
    section[data-testid='stSidebar'] {
        display: none;
    }

    /* Container principal */
    .main .block-container {
        padding: 1rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }

    /* Navigation horizontale */
    .nav-horizontal {
        background: rgba(22, 33, 62, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem 2rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: center;
        gap: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    .nav-button {
        background: transparent;
        color: var(--text-secondary);
        border: 2px solid transparent;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 1rem;
    }

    .nav-button:hover {
        background: rgba(0, 212, 255, 0.1);
        border-color: var(--accent-blue);
        color: var(--accent-blue);
        transform: translateY(-2px);
    }

    .nav-button.active {
        background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
        color: white;
        border-color: transparent;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }

    /* En-tête */
    .header-container {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(139, 92, 246, 0.1));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        color: var(--text-secondary);
        font-size: 1.3rem;
        font-weight: 400;
    }

    /* Cards dark */
    .card {
        background: rgba(22, 33, 62, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 212, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 212, 255, 0.2);
        border-color: rgba(0, 212, 255, 0.3);
    }

    /* Film card */
    .film-card {
        background: linear-gradient(135deg, rgba(22, 33, 62, 0.9), rgba(26, 31, 58, 0.9));
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid var(--accent-blue);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }

    .film-card:hover {
        transform: translateX(5px);
        border-left-color: var(--accent-purple);
        box-shadow: 0 6px 25px rgba(139, 92, 246, 0.3);
    }

    .film-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--accent-blue);
        margin-bottom: 0.8rem;
    }

    .film-info {
        color: var(--text-secondary);
        font-size: 0.95rem;
        margin: 0.4rem 0;
    }

    /* Textes */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
    }

    p, div, span, label {
        color: var(--text-secondary) !important;
    }

    /* Boutons */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 212, 255, 0.5);
    }

    .stButton > button p {
        color: white !important;
    }

    /* Inputs dark */
    .stSelectbox > div > div {
        background: rgba(22, 33, 62, 0.8);
        color: var(--text-primary) !important;
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 10px;
    }

    .stSelectbox label {
        color: var(--text-primary) !important;
        font-weight: 600;
    }

    .stSelectbox input {
        color: white !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(22, 33, 62, 0.9) !important;
        color: white !important;
    }

    /* Slider label */
    .stSlider label {
        color: var(--text-primary) !important;
        font-weight: 600;
    }

    /* Metrics dark */
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--accent-blue);
    }

    div[data-testid="stMetricLabel"] {
        color: var(--text-secondary);
    }

    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--accent-blue);
    }

    /* Info box dark */
    .info-box {
        background: rgba(0, 212, 255, 0.1);
        border-left: 4px solid var(--accent-blue);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: var(--text-primary);
    }

    /* Success box dark */
    .success-box {
        background: rgba(16, 185, 129, 0.1);
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: var(--text-primary);
    }

    /* Tabs dark */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(22, 33, 62, 0.8);
        border-radius: 10px;
        padding: 0.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary);
        border-radius: 8px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
        color: white !important;
    }

    /* Expander dark */
    .streamlit-expanderHeader {
        background: rgba(22, 33, 62, 0.6);
        color: var(--text-primary);
        border-radius: 10px;
    }

    /* Slider dark */
    .stSlider > div > div > div {
        background: var(--accent-blue);
    }
</style>
""", unsafe_allow_html=True)

# En-tête principal
st.markdown("""
<div class="header-container">
    <h1 class="main-title">CinéMatch</h1>
    <p class="subtitle">Système intelligent de recommandation de films</p>
</div>
""", unsafe_allow_html=True)

# Navigation horizontale
st.markdown("""
<div class="nav-horizontal">
    CinéMatch - Navigation
</div>
""", unsafe_allow_html=True)

# Utiliser des boutons horizontaux pour la navigation
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Accueil", use_container_width=True, key="nav_home"):
        st.session_state.page = "home"
with col2:
    if st.button("Recommandations", use_container_width=True, key="nav_reco"):
        st.session_state.page = "reco"
with col3:
    if st.button("Machine Learning", use_container_width=True, key="nav_ml"):
        st.session_state.page = "ml"
with col4:
    if st.button("Améliorations", use_container_width=True, key="nav_improve"):
        st.session_state.page = "improve"

# Initialiser la page par défaut
if 'page' not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page

# Page Accueil
if page == "home":
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Bienvenue sur CinéMatch")
        st.write("""
        Découvrez des films similaires à vos préférences grâce à notre système 
        de recommandation intelligent basé sur le machine learning.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Comment ça marche ?")
        st.write("""
        1. **Sélectionnez** un film que vous aimez
        2. **Choisissez** le nombre de recommandations
        3. **Découvrez** des films similaires avec leurs bandes-annonces
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Statistiques")

        try:
            df = pd.read_csv("df_français_comedy_action03.csv")
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Films", len(df))
            with col_b:
                st.metric("Genres", "3")
        except FileNotFoundError:
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Films", "206")
            with col_b:
                st.metric("Genres", "3")
        except Exception as e:
            st.info("Données en cours de chargement...")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("**Astuce** : Plus vous explorez de films, meilleures seront nos recommandations !")
        st.markdown('</div>', unsafe_allow_html=True)

# Page Recommandations
elif page == "reco":
    st.markdown('<h2 class="section-header">Trouvez votre prochain film</h2>', unsafe_allow_html=True)

    try:
        # Chargement des données
        df_films = pd.read_csv("df_français_comedy_action03.csv")
        liste_films = sorted(df_films['titre_original'].tolist())

        col1, col2 = st.columns([2, 1])

        with col1:
            film_recherche = st.selectbox(
                "Sélectionnez un film",
                options=liste_films,
                help="Choisissez un film pour obtenir des recommandations similaires"
            )

        with col2:
            nombre_reco = st.slider(
                "Nombre de recommandations",
                min_value=1,
                max_value=10,
                value=5
            )

        if st.button("Obtenir des recommandations", use_container_width=True):
            with st.spinner("Analyse en cours..."):
                # Chargement du modèle
                X = pd.read_csv("df_X.csv")

                df_film_recherche = X.loc[X['titre_original'] == film_recherche]
                df_autres_films = X.loc[X['titre_original'] != film_recherche]

                if not df_film_recherche.empty:
                    # Modèle KNN
                    model = NearestNeighbors(n_neighbors=nombre_reco, metric='cosine')
                    model.fit(df_autres_films.drop(["titre_original", "index_original"], axis=1))

                    distances, indices = model.kneighbors(
                        df_film_recherche.drop(["titre_original", "index_original"], axis=1).values
                    )

                    voisins = [df_autres_films.iloc[idx]['titre_original'] for idx in indices[0]]
                    recommandations = df_films[df_films['titre_original'].isin(voisins)]

                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.success(f"{nombre_reco} films similaires trouvés !")
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Affichage des recommandations
                    for idx, (_, film) in enumerate(recommandations.iterrows(), 1):
                        # Créer deux colonnes : infos à gauche, vidéo à droite
                        col_info, col_video = st.columns([1, 1])

                        with col_info:
                            st.markdown(f"""
                            <div class="film-card">
                                <div class="film-title">{idx}. {film['titre_original']}</div>
                                <div class="film-info">Année : {film.get('annee_sortie', 'N/A')}</div>
                                <div class="film-info">Note : {film.get('moyenne_notes', 'N/A')}/10</div>
                                <div class="film-info">Réalisateur : {film.get('directeur', 'N/A')}</div>
                                <div class="film-info">Genre : {film.get('genres', 'N/A')}</div>
                            </div>
                            """, unsafe_allow_html=True)

                        with col_video:
                            # Bande annonce si disponible
                            if 'trailer_url' in film and pd.notna(film['trailer_url']):
                                st.video(film['trailer_url'])
                            else:
                                st.info("Bande-annonce non disponible")

                        if idx < len(recommandations):
                            st.markdown("---")

    except FileNotFoundError:
        st.error("❌ Fichiers de données introuvables. Assurez-vous que les CSV sont dans le dossier.")
    except Exception as e:
        st.error(f"❌ Une erreur s'est produite : {str(e)}")

# Page Machine Learning
elif page == "ml":
    st.markdown('<h2 class="section-header">Fonctionnement du modèle</h2>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Prétraitement des données")
    st.write("""
    Le système de recommandation repose sur un traitement rigoureux des données :
    """)

    steps = [
        ("1. Exploration", "Analyse des corrélations et distributions"),
        ("2. Nettoyage", "Gestion des valeurs manquantes"),
        ("3. Pondération", "Distinction variables numériques/catégoriques"),
        ("4. Normalisation", "Mise à l'échelle des variables numériques"),
        ("5. Encodage", "Transformation des variables catégoriques"),
        ("6. Concaténation", "Création de la matrice finale")
    ]

    for step, desc in steps:
        st.markdown(f"**{step}** : {desc}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Algorithme K-Nearest Neighbors")

    st.code("""
# Modèle de recommandation
model = NearestNeighbors(n_neighbors=5, metric='cosine')
model.fit(X_films)

# Trouver les films similaires
distances, indices = model.kneighbors(film_recherché)
recommandations = films.iloc[indices[0]]
    """, language="python")

    st.info("""
    **Le modèle utilise la distance cosinus** pour mesurer la similarité entre films 
    en se basant sur leurs caractéristiques (genre, réalisateur, acteurs, etc.)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Page Améliorations
elif page == "improve":
    st.markdown('<h2 class="section-header">Axes d\'amélioration</h2>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Objectif")
    st.write("""
    Enrichir notre catalogue et diversifier l'offre pour attirer de nouveaux publics 
    tout en fidélisant les spectateurs existants.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Onglets pour les différentes catégories
    tab1, tab2, tab3 = st.tabs(["Animation", "Noël", "Horreur"])

    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Public cible")
        st.write("Familles, enfants et amateurs d'animation adulte")

        st.markdown("#### Stratégies")
        st.write("""
        - **Programmation variée** : Films classiques, récents et indépendants
        - **Activités interactives** : Ateliers créatifs, séances de coloriage
        - **Marketing ciblé** : Partenariats avec écoles et plateformes familiales
        - **Fidélisation** : Cartes de fidélité et réductions familles
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Public cible")
        st.write("Familles, couples et groupes d'amis en période festive")

        st.markdown("#### Stratégies")
        st.write("""
        - **Ambiance festive** : Décorations thématiques et effets lumineux
        - **Animations spéciales** : Séances photos, ateliers décorations
        - **Partenariats** : Collaborations pour promotions croisées
        - **Expériences gourmandes** : Menus thématiques (chocolats chauds, etc.)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Public cible")
        st.write("Jeunes adultes et amateurs de sensations fortes")

        st.markdown("#### Stratégies")
        st.write("""
        - **Expériences immersives** : Projections nocturnes, marathons thématiques
        - **Activités thématiques** : Escape games, soirées costumées
        - **Marketing créatif** : Concours de costumes, défis sur réseaux sociaux
        - **Offres exclusives** : Pass soirée horreur, réductions groupes
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 2rem;'>
    <p>CinéMatch - Système de recommandation de films</p>
    <p style='font-size: 0.9rem; opacity: 0.8;'>Projet réalisé dans le cadre de la formation Data Analyst</p>
</div>
""", unsafe_allow_html=True)