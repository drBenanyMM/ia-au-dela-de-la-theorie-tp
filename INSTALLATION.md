# Guide d'installation — Windows, macOS, Linux

Objectif : avoir Python, les bibliothèques des TP et Jupyter, puis ouvrir les notebooks.
Comptez 15 à 30 minutes selon votre connexion.

Deux chemins possibles, **choisissez-en un seul** :

| Chemin | Pour qui | Taille |
|--------|----------|--------|
| **A. Python + venv** (recommandé) | installation légère, la plus courante | ~ 500 Mo |
| **B. Anaconda / Miniconda** | si vous utilisez déjà Anaconda, ou si le chemin A échoue | Miniconda ~ 1 Go, Anaconda ~ 5 Go |

Pas envie d'installer ? Utilisez Google Colab (voir le README).

---

## Étape 0 — Récupérer les TP

- **Avec Git** : `git clone https://github.com/drBenanyMM/ia-au-dela-de-la-theorie-tp.git`
- **Sans Git** : sur la page GitHub, bouton vert **Code → Download ZIP**, puis décompressez.

Ouvrez ensuite un terminal **dans le dossier du projet** :

- **Windows** : ouvrez le dossier dans l'Explorateur, tapez `powershell` dans la barre d'adresse, puis Entrée.
- **macOS** : application *Terminal*, puis `cd ` suivi du dossier glissé dans la fenêtre.
- **Linux** : clic droit dans le dossier → *Ouvrir dans un terminal*.

---

## Chemin A — Python + environnement virtuel

### A1. Installer Python (3.10 ou plus récent)

**Windows**

1. Téléchargez l'installateur sur <https://www.python.org/downloads/windows/>.
2. Lancez-le et **cochez « Add python.exe to PATH »** avant de cliquer sur *Install Now*.
3. Vérifiez dans PowerShell : `python --version`

**macOS**

1. Téléchargez l'installateur sur <https://www.python.org/downloads/macos/> et lancez-le,
   ou, avec Homebrew : `brew install python`
2. Vérifiez dans le Terminal : `python3 --version`

**Linux (Ubuntu / Debian)**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 --version
```

Fedora : `sudo dnf install python3 python3-pip` · Arch : `sudo pacman -S python python-pip`

### A2. Créer et activer l'environnement virtuel

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Quand l'environnement est actif, `(.venv)` apparaît au début de la ligne du terminal.
Il faut le réactiver à chaque nouvelle fenêtre de terminal.

### A3. Installer les bibliothèques et vérifier

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python verifier_installation.py
```

Toutes les lignes doivent afficher `[OK ]`.

### A4. Lancer Jupyter

```bash
jupyter lab
```

Le navigateur s'ouvre : entrez dans le dossier `notebooks/` et ouvrez `TP1_Fondements_IA.ipynb`.
Pour arrêter Jupyter : `Ctrl + C` dans le terminal.

---

## Chemin B — Anaconda ou Miniconda

### B1. Installer

- **Miniconda** (léger, recommandé) : <https://www.anaconda.com/docs/getting-started/miniconda/install>
- **Anaconda Distribution** (complet, avec interface graphique) : <https://www.anaconda.com/download>

Sous Windows, ouvrez ensuite **Anaconda Prompt** depuis le menu Démarrer.
Sous macOS / Linux, fermez puis rouvrez le terminal après l'installation.

### B2. Créer l'environnement des TP

Dans le dossier du projet :

```bash
conda env create -f environment.yml
conda activate ia-techforge
python verifier_installation.py
jupyter lab
```

Les fois suivantes, il suffit de : `conda activate ia-techforge` puis `jupyter lab`.

---

## Utiliser VS Code (facultatif)

1. Installez VS Code (<https://code.visualstudio.com>) et les extensions **Python** et **Jupyter**.
2. *Fichier → Ouvrir le dossier* : choisissez le dossier du projet.
3. Ouvrez un notebook, puis en haut à droite **Sélectionner le noyau** → `.venv` ou `ia-techforge`.

---

## Problèmes fréquents

| Symptôme | Solution |
|----------|----------|
| Windows : `python` n'est pas reconnu | Réinstallez Python en cochant « Add python.exe to PATH », ou utilisez la commande `py` à la place de `python`. |
| Windows : « l'exécution de scripts est désactivée » à l'activation | Exécutez une fois : `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, puis réessayez. Autre solution : utilisez l'invite de commandes classique avec `.venv\Scripts\activate.bat`. |
| macOS / Linux : `python` introuvable | Utilisez `python3` et `pip3`. |
| Linux : `ensurepip is not available` | `sudo apt install python3-venv` |
| Linux : `externally-managed-environment` | Vous installez hors de l'environnement virtuel : activez `.venv` (étape A2) avant `pip install`. |
| `pip install` très lent ou interrompu | Relancez la commande ; ajoutez `--default-timeout=100` si la connexion est instable. |
| `ModuleNotFoundError` dans un notebook | Le notebook n'utilise pas le bon noyau : vérifiez que l'environnement est activé avant `jupyter lab`, ou choisissez le bon noyau (menu *Kernel → Change Kernel*). |
| `jupyter` n'est pas reconnu | Lancez `python -m jupyter lab`. |
| Erreur de téléchargement d'un jeu de données | Il faut une connexion Internet à la première exécution ; relancez la cellule une fois connecté. |
| Les curseurs interactifs ne s'affichent pas | `pip install --upgrade ipywidgets jupyterlab`, puis redémarrez Jupyter. Les TP fonctionnent aussi sans les curseurs. |

Si le problème persiste, utilisez Google Colab (voir le README) et signalez-le via le formulaire
de retour de la conférence en indiquant votre système et le message d'erreur complet.
