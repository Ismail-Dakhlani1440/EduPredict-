# Dictionnaire des donnÃ©es

Source : [Student Performance Factors (Kaggle)](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)

Le jeu de donnÃ©es contient **19 variables explicatives** et **1 variable cible** (`Exam_Score`).

## Variables numÃ©riques

| Colonne | Description |
|---|---|
| `Hours_Studied` | Heures d'Ã©tude hebdomadaires |
| `Attendance` | Taux de prÃ©sence en cours (en %) |
| `Sleep_Hours` | Heures de sommeil moyennes par nuit |
| `Previous_Scores` | Scores obtenus aux examens prÃ©cÃ©dents |
| `Tutoring_Sessions` | Nombre de sÃ©ances de tutorat suivies par mois |
| `Physical_Activity` | ActivitÃ© physique hebdomadaire (en heures) |

## Variables catÃ©gorielles nominales (sans ordre)

Encodage utilisÃ© : **one-hot encoding**.

| Colonne | Description | Valeurs |
|---|---|---|
| `Gender` | Genre | Male / Female |
| `School_Type` | Type d'Ã©tablissement | Public / Private |
| `Extracurricular_Activities` | Pratique d'activitÃ©s extrascolaires | Yes / No |
| `Internet_Access` | AccÃ¨s Ã  internet | Yes / No |
| `Learning_Disabilities` | PrÃ©sence de troubles d'apprentissage | Yes / No |
| `Peer_Influence` | Influence des pairs | Positive / Neutral / Negative |

## Variables catÃ©gorielles ordinales (avec ordre)

Encodage utilisÃ© : **encodage ordinal** (0, 1, 2 selon l'ordre croissant).

| Colonne | Description | Ordre des valeurs |
|---|---|---|
| `Parental_Involvement` | Implication parentale | Low < Medium < High |
| `Access_to_Resources` | AccÃ¨s aux ressources pÃ©dagogiques | Low < Medium < High |
| `Motivation_Level` | Niveau de motivation | Low < Medium < High |
| `Family_Income` | Revenu familial | Low < Medium < High |
| `Teacher_Quality` | QualitÃ© perÃ§ue des enseignants (valeurs manquantes) | Low < Medium < High |
| `Parental_Education_Level` | Niveau d'Ã©ducation des parents (valeurs manquantes) | High School < College < Postgraduate |
| `Distance_from_Home` | Distance domicile-Ã©tablissement (valeurs manquantes) | Near < Moderate < Far |

## Variable cible

| Colonne | Description |
|---|---|
| `Exam_Score` | Score final Ã  l'examen (valeur continue) |

## Valeurs manquantes

Les colonnes `Teacher_Quality`, `Parental_Education_Level` et `Distance_from_Home` contiennent des valeurs manquantes. Elles sont remplacÃ©es par le **mode** (valeur la plus frÃ©quente) de chaque colonne.