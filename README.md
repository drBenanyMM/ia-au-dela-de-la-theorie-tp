# L'intelligence artificielle : au-delà de la théorie — Travaux pratiques

Les 4 TP (notebooks Jupyter) de la conférence **« L'intelligence artificielle : au-delà de la théorie »**
organisée par le **TechForge Club** — Faculté des Sciences et Techniques, Université de Nouakchott
(samedi 14 novembre 2026, Amphi 5).

Animée par **Dr. El Benany Med Mahmoud** · Partenaires : InsightEx et brandak

## Les 4 TP

| TP | Partie de la conférence | Notebook | Ouvrir dans Colab |
|----|-------------------------|----------|-------------------|
| 1 | Fondements : de l'information à l'IA | [`TP1_Fondements_IA.ipynb`](notebooks/TP1_Fondements_IA.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP1_Fondements_IA.ipynb) |
| 2 | Apprentissage supervisé (MLS) | [`TP2_Apprentissage_supervise_MLS.ipynb`](notebooks/TP2_Apprentissage_supervise_MLS.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP2_Apprentissage_supervise_MLS.ipynb) |
| 3 | Apprentissage non supervisé (MLNS) | [`TP3_Apprentissage_non_supervise_MLNS.ipynb`](notebooks/TP3_Apprentissage_non_supervise_MLNS.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP3_Apprentissage_non_supervise_MLNS.ipynb) |
| 4 | Deep Learning et Transformers | [`TP4_Deep_Learning_Transformers.ipynb`](notebooks/TP4_Deep_Learning_Transformers.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP4_Deep_Learning_Transformers.ipynb) |

Chaque TP propose trois niveaux de lecture, comme les diapositives :

| Niveau | Public | Ce qu'on y fait |
|--------|--------|-----------------|
| Découverte | Licence 1 – Licence 2 | exécuter, observer, modifier un paramètre |
| Approfondissement | Licence 3 | compléter du code, interpréter les résultats |
| Expert | Master 1 – Master 2 | défis ouverts, analyse critique |

Faites les TP dans l'ordre et arrêtez-vous au niveau qui vous convient : chaque niveau est autonome.

## Démarrage rapide

### Option A — Sans rien installer (Google Colab)

Cliquez sur un badge « Open in Colab » du tableau ci-dessus. Il faut seulement un compte Google
et une connexion Internet.

### Option B — Sur votre ordinateur

```bash
git clone https://github.com/VOTRE-COMPTE/ia-au-dela-de-la-theorie-tp.git
cd ia-au-dela-de-la-theorie-tp
python -m venv .venv
# Windows :        .venv\Scripts\activate
# macOS / Linux :  source .venv/bin/activate
pip install -r requirements.txt
python verifier_installation.py
jupyter lab
```

Sans Git : bouton vert **Code → Download ZIP** sur la page GitHub, puis décompressez l'archive.

Python n'est pas encore installé, ou vous préférez Anaconda ? Suivez le guide pas à pas :
**[INSTALLATION.md](INSTALLATION.md)** (Windows, macOS, Linux).

## Contenu du dépôt

```text
ia-au-dela-de-la-theorie-tp/
├── README.md                    ce fichier
├── INSTALLATION.md              guide d'installation Windows / macOS / Linux
├── requirements.txt             dépendances (pip)
├── environment.yml              dépendances (Anaconda / Miniconda)
├── verifier_installation.py     vérifie que tout est prêt
├── .gitignore
├── .gitattributes
└── notebooks/
    ├── TP1_Fondements_IA.ipynb
    ├── TP2_Apprentissage_supervise_MLS.ipynb
    ├── TP3_Apprentissage_non_supervise_MLNS.ipynb
    └── TP4_Deep_Learning_Transformers.ipynb
```

## Bon à savoir

- **Connexion Internet** : certains jeux de données de scikit-learn (par exemple *California Housing*)
  sont téléchargés à la première utilisation. Exécutez une première fois les TP avec une connexion.
- **Aucun GPU n'est nécessaire** : tous les TP tournent sur un ordinateur portable ordinaire.
- **Travaillez sur une copie** : dupliquez un notebook avant de le modifier pour garder l'original intact.
- **Repartir de zéro** : dans Jupyter, menu *Kernel → Restart Kernel and Run All Cells*.

## Ressources de la conférence

* **Diapositives interactives (site web) :** [ICI](https://a-au-dela-de-la-theorie-2026.vercel.app/)
* **Diapositives PDF (Google Drive) :** [ICI](https://drive.google.com/drive/folders/1ypNl9R_HWqh7QfspmEpyRHs1YPvuraMI)


## Questions et retours

Un formulaire de retour est disponible sur la page Notion de la conférence.
Pour signaler une erreur dans un TP, ouvrez une *issue* sur ce dépôt.































Oui, ajoutez-les directement dans le `README.md` ! C'est très pratique pour les étudiants qui arrivent directement sur GitHub (ou qui téléchargent le dépôt en ZIP et lisent le `README.md` hors ligne).

**Deux corrections importantes avant de commiter :**

1. **Il reste un oubli dans `README.md` :** Dans la section *Option B — Sur votre ordinateur*, la commande `git clone` contient encore `VOTRE-COMPTE` au lieu de `drBenanyMM`.
2. **Nettoyez l'URL Google Drive :** Retirez le `/u/2/` dans `[https://drive.google.com/drive/u/2/folders/](https://drive.google.com/drive/u/2/folders/)...` pour utiliser le lien universel `[https://drive.google.com/drive/folders/1ypNl9R_HWqh7QfspmEpyRHs1YPvuraMI?usp=sharing](https://drive.google.com/drive/folders/1ypNl9R_HWqh7QfspmEpyRHs1YPvuraMI?usp=sharing)` (sinon, les étudiants connectés à plusieurs comptes Google risquent une erreur d'autorisation ou d'ouverture). Vérifiez également que ce dossier Drive est bien partagé en **« Tous les utilisateurs disposant du lien — Lecteur »**.

Voici le `README.md` complet et corrigé, prêt à être copié-collé à la place de l'actuel :

```markdown
# L'intelligence artificielle : au-delà de la théorie — Travaux pratiques

Les 4 TP (notebooks Jupyter) de la conférence **« L'intelligence artificielle : au-delà de la théorie »**
organisée par le **TechForge Club** — Faculté des Sciences et Techniques, Université de Nouakchott
(samedi 14 novembre 2026, Amphi 5).

Animée par **Dr. El Benany Med Mahmoud** · Partenaires : InsightEx et brandak

## Les 4 TP

| TP | Partie de la conférence | Notebook | Ouvrir dans Colab |
|----|-------------------------|----------|-------------------|
| 1 | Fondements : de l'information à l'IA | [`TP1_Fondements_IA.ipynb`](notebooks/TP1_Fondements_IA.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP1_Fondements_IA.ipynb) |
| 2 | Apprentissage supervisé (MLS) | [`TP2_Apprentissage_supervise_MLS.ipynb`](notebooks/TP2_Apprentissage_supervise_MLS.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP2_Apprentissage_supervise_MLS.ipynb) |
| 3 | Apprentissage non supervisé (MLNS) | [`TP3_Apprentissage_non_supervise_MLNS.ipynb`](notebooks/TP3_Apprentissage_non_supervise_MLNS.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP3_Apprentissage_non_supervise_MLNS.ipynb) |
| 4 | Deep Learning et Transformers | [`TP4_Deep_Learning_Transformers.ipynb`](notebooks/TP4_Deep_Learning_Transformers.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drBenanyMM/ia-au-dela-de-la-theorie-tp/blob/main/notebooks/TP4_Deep_Learning_Transformers.ipynb) |

Chaque TP propose trois niveaux de lecture, comme les diapositives :

| Niveau | Public | Ce qu'on y fait |
|--------|--------|-----------------|
| Découverte | Licence 1 – Licence 2 | exécuter, observer, modifier un paramètre |
| Approfondissement | Licence 3 | compléter du code, interpréter les résultats |
| Expert | Master 1 – Master 2 | défis ouverts, analyse critique |

Faites les TP dans l'ordre et arrêtez-vous au niveau qui vous convient : chaque niveau est autonome.

## Démarrage rapide

### Option A — Sans rien installer (Google Colab)

Cliquez sur un badge « Open in Colab » du tableau ci-dessus. Il faut seulement un compte Google
et une connexion Internet.

### Option B — Sur votre ordinateur

```bash
git clone [https://github.com/drBenanyMM/ia-au-dela-de-la-theorie-tp.git](https://github.com/drBenanyMM/ia-au-dela-de-la-theorie-tp.git)
cd ia-au-dela-de-la-theorie-tp
python -m venv .venv
# Windows :        .venv\Scripts\activate
# macOS / Linux :  source .venv/bin/activate
pip install -r requirements.txt
python verifier_installation.py
jupyter lab

```

Sans Git : bouton vert **Code → Download ZIP** sur la page GitHub, puis décompressez l'archive.

Python n'est pas encore installé, ou vous préférez Anaconda ? Suivez le guide pas à pas :
**[INSTALLATION.md](INSTALLATION.md)** (Windows, macOS, Linux).

## Contenu du dépôt

```text
ia-au-dela-de-la-theorie-tp/
├── README.md                    ce fichier
├── INSTALLATION.md              guide d'installation Windows / macOS / Linux
├── requirements.txt             dépendances (pip)
├── environment.yml              dépendances (Anaconda / Miniconda)
├── verifier_installation.py     vérifie que tout est prêt
├── .gitignore
├── .gitattributes
└── notebooks/
    ├── TP1_Fondements_IA.ipynb
    ├── TP2_Apprentissage_supervise_MLS.ipynb
    ├── TP3_Apprentissage_non_supervise_MLNS.ipynb
    └── TP4_Deep_Learning_Transformers.ipynb

```
