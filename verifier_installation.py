"""Vérifie que l'environnement est prêt pour les 4 TP.

Utilisation :  python verifier_installation.py
"""
import importlib
import sys

MINIMUM_PYTHON = (3, 10)
PAQUETS = [
    ("numpy", "numpy"),
    ("scipy", "scipy"),
    ("pandas", "pandas"),
    ("matplotlib", "matplotlib"),
    ("sklearn", "scikit-learn"),
    ("ipywidgets", "ipywidgets"),
    ("jupyterlab", "jupyterlab"),
    ("notebook", "notebook"),
]


def main() -> int:
    ok = True
    v = sys.version_info
    etat = "OK " if v >= MINIMUM_PYTHON else "NON"
    print(f"[{etat}] Python {v.major}.{v.minor}.{v.micro} (minimum {MINIMUM_PYTHON[0]}.{MINIMUM_PYTHON[1]})")
    ok &= v >= MINIMUM_PYTHON

    for module, nom_pip in PAQUETS:
        try:
            m = importlib.import_module(module)
            print(f"[OK ] {nom_pip:<13} {getattr(m, '__version__', '')}")
        except Exception as erreur:  # paquet absent ou cassé
            ok = False
            print(f"[NON] {nom_pip:<13} manquant  ->  pip install {nom_pip}   ({type(erreur).__name__})")

    if ok:
        try:  # mini-test : un modèle s'entraîne réellement
            from sklearn.datasets import load_iris
            from sklearn.linear_model import LogisticRegression

            X, y = load_iris(return_X_y=True)
            score = LogisticRegression(max_iter=500).fit(X, y).score(X, y)
            print(f"[OK ] Mini-test scikit-learn : exactitude = {score:.2f}")
        except Exception as erreur:
            ok = False
            print(f"[NON] Mini-test scikit-learn : {erreur}")

    print()
    if ok:
        print("Tout est prêt. Lancez :  jupyter lab   puis ouvrez le dossier notebooks/")
    else:
        print("Installation incomplète. Relancez :  pip install -r requirements.txt")
        print("Voir INSTALLATION.md, section « Problèmes fréquents ».")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
