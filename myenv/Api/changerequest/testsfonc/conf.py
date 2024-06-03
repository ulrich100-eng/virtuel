import pandas as pd
import matplotlib.pyplot as plt



# Charger le fichier Excel
report_path = "C:\\Users\\ZBHQ8349\\virt\\myenv\\Api\\changerequest\\testsfonc\\rapportsoft\\31-05-2024 10-54-57.xlsx"
df = pd.read_excel(report_path)

# Vérifier la structure du DataFrame
print(df.head())

# Créer une liste de couleurs en fonction des résultats des tests
# Assurez-vous que la colonne 'result' existe et contient les valeurs 'PASSED' et 'FAILED'
color_map = {'PASSED': 'green', 'FAILED': 'red'}
colors = df['result'].map(color_map)

# Graphique des résultats des tests
plt.figure(figsize=(7, 8))
bars = plt.bar( df['test_name'], df['duration'], color=colors)
plt.xlabel('Nom du test')
plt.ylabel('Duree des tests en secondes')
plt.title('Résultats du test fonctionnel')


# Ajuster les labels pour qu'ils ne se chevauchent pas
plt.xticks(rotation=90)
# Afficher les valeurs des durées sur l'axe des ordonnées

plt.tight_layout()

plt.show()












