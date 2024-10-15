import pandas as pd
from operacoes import *

champions = pd.read_csv("lol_champions.csv", sep=";")
champions["winrate"] = pd.to_numeric(champions["winrate"], errors="coerce")
champions["releasedate"] = pd.to_datetime(champions["releasedate"], format="%d/%m/%Y", errors="coerce")
champions["role"] = champions["role"].str.split(",")
champions = champions.explode("role") 

campeoesWinrateEntre(champions)
campeoesPorRoleETags(champions)
winrateRole(champions)
popularityRole(champions)
popularidadeCampeosPorAno(champions)