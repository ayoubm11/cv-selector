
# Sélecteur de CV avec LangChain & Ollama (WSL)

Ce projet permet d’analyser automatiquement des CV au format PDF et de déterminer leur pertinence par rapport à une description de poste donnée, en utilisant les modèles LLM via **Ollama** et la librairie **LangChain**.

---

## Fonctionnalités

- Chargement des CV au format PDF depuis un dossier local  
- Analyse de la pertinence de chaque CV par rapport à une offre d’emploi  
- Réponse concise : "Pertinent" ou "Non pertinent" avec une courte explication  
- Utilisation du modèle `tinyllama` via Ollama sur WSL  
- Pipeline optimisé avec LangChain (`langchain-ollama`, `langchain-community`)

---

## Architecture et modèles utilisés

### Ollama

Ollama est une plateforme locale pour lancer des modèles LLM facilement sur ta machine, sans dépendre du cloud.

![Logo Ollama](assets/ollama-logo.png)

Site officiel : [ollama.com](https://ollama.com)

---

### TinyLlama

TinyLlama est un modèle léger de la famille LLaMA, optimisé pour tourner localement avec une bonne efficacité.

![Logo TinyLlama](assets/tinyllama.png)

---

## Prérequis

- Windows Subsystem for Linux (WSL) configuré  
- Ollama installé et modèle `tinyllama` téléchargé  
- Python 3.8+ avec un environnement virtuel activé  

---

## Installation

1. Cloner ce dépôt

```bash
git clone https://github.com/ton-utilisateur/cv-selector.git
cd cv-selector
```

2. Créer un environnement virtuel Python

- Sur **Linux / WSL / macOS** :

```bash
python3 -m venv myenv
```

- Sur **Windows (PowerShell)** :

```powershell
python -m venv myenv
```

3. Activer l’environnement virtuel

- Sur **Linux / WSL / macOS** :

```bash
source myenv/bin/activate
```

- Sur **Windows (PowerShell)** :

```powershell
.\myenv\Scripts\Activate.ps1
```

- Sur **Windows (Invite de commandes classique)** :

```cmd
myenv\Scripts\activate.bat
```

4. Mettre à jour pip

```bash
pip install --upgrade pip
```

5. Installer les dépendances nécessaires

```bash
pip install langchain langchain-ollama langchain-community pypdf
```

6. Préparer le dossier `cvs/`

Place tes fichiers PDF de CV dans le dossier `cvs/` situé à la racine du projet.

---

## Utilisation

Lancer le script principal `test.py` :

```bash
python3 test.py
```

Le script analysera chaque CV dans le dossier `cvs/` et affichera la pertinence pour la description de poste définie dans le script.

---

## Structure du projet

```
cv-selector/
│
├── cvs/                # Dossier contenant les CV au format PDF
├── test.py             # Script principal d’analyse des CV
├── assets/             # Dossier contenant les images utilisées dans le README
└── README.md           # Ce fichier
```

---

## Personnalisation

- Modifier la variable `job_description` dans `test.py` pour adapter la description du poste.  
- Ajouter ou retirer des CV PDF dans le dossier `cvs/`.

---

## Ressources utiles

- [LangChain Documentation](https://python.langchain.com/)  
- [Ollama](https://ollama.com/)  
- [LangChain Ollama Integration](https://python.langchain.com/en/latest/modules/llms/integrations/ollama.html)  
- [PyPDF Documentation](https://pypdf.readthedocs.io/en/latest/)

---
