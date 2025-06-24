# spam-sms-classifier
# Détecteur de SPAM SMS avec Machine Learning

Ce projet a pour objectif de construire un modèle de classification binaire capable de détecter si un message SMS est un spam ou non, en utilisant des techniques classiques de machine learning.

## Objectifs du projet

- Charger et analyser un jeu de données texte (SMS)
- Nettoyer et vectoriser les messages avec TF-IDF
- Entraîner plusieurs modèles de classification
- Évaluer leurs performances avec des métriques adaptées
- Comparer les modèles pour sélectionner le plus performant

## Données utilisées

- Fichier : `SMSSpamCollection`
- Source : UCI Machine Learning Repository
- Contenu : 5574 messages SMS, dont 747 sont des spams

## Modèles testés

- Naive Bayes
- Régression Logistique
- SVM (Support Vector Machine)

### Exemple de résultats

| Modèle              | Accuracy | F1 Score | Recall |
|---------------------|----------|----------|--------|
| Naive Bayes         | 0.97     | 0.90     | 0.81   |
| Régression Logistique | 0.98   | 0.92     | 0.87   |
| SVM                 | 0.98     | 0.92     | 0.89   |

## Étapes du projet

1. Prétraitement du texte (nettoyage, mise en forme)
2. Encodage des étiquettes (ham/spam)
3. Vectorisation avec TF-IDF
4. Séparation des données en entraînement et test
5. Entraînement de plusieurs modèles
6. Évaluation et comparaison des performances

## Installation et exécution

### 1. Cloner le projet

git clone https://github.com/NeimaDaher/spam-sms-classifier.git
cd spam-sms-classifier

## 2. Installer les dépendances

pip install -r requirements.txt
3. Lancer le notebook Jupyter
Ouvrir le fichier suivant avec Jupyter Notebook :


notebooks/01_modeling.ipynb

4. Organisation du projet


spam-sms-classifier/
├── data/                # Données d'entrée (non versionnées)
├── models/              # Modèles et vectorizer sauvegardés
├── notebooks/           # Notebook Jupyter principal
├── src/                 # Fonctions Python pour le ML
├── requirements.txt     # Dépendances du projet
└── README.md            # Présentation du projet
