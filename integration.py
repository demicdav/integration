import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(color_codes=True)

df = pd.read_csv('datenfinal.csv')
df

sns.scatterplot(x="bip_je_einwohner_in_usd",y="entwicklung_einwohner_seit_2012", data=df)
plt.ylabel("Entwicklung Einwohner seit 2012")
plt.xlabel("BIP je Einwohner in USD")
plt.show()

sns.catplot(x="reifegrad_elektroinfrastruktur_2022", y="land", data=df)
plt.ylabel("Land")
plt.xlabel("Reifegrad Elektroinfrastruktur 2022")

sns.lmplot(x="reifegrad_elektroinfrastruktur_2022", y="einwohner_in_millionen", data=df)
plt.ylabel("Einwohner in Millionen")
plt.xlabel("Reifegrad Elektroinfrastruktur 2022")

sns.regplot(x="einwohner_in_millionen", y="reifegrad_elektroinfrastruktur_2022", data=df);
plt.ylabel("Reifegrad Elektroinfrastruktur 2022")
plt.xlabel("Einwohner in Millionen")

sns.regplot(x="bip_je_einwohner_in_usd", y="reifegrad_elektroinfrastruktur_2022", data=df);
plt.ylabel("Reifegrad Elektroinfrastruktur 2022")
plt.xlabel("BIP pro Einwohner in USD")




sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2021", data=df);
plt.ylabel("Anzahl Ladestationen pro 1000 Einwohner")
plt.xlabel("BIP pro Einwohner in USD")




sns.regplot(x="einwohner_pro_km2", y="ladestationen_pro_1000_einwohner_2021", data=df);
plt.ylabel("Anzahl Ladestationen pro 1000 Einwohner")
plt.xlabel("Anzahl Einwohner pro km2")




sns.regplot(x="gesamtausgaben_bildung_pro_kopf", y="ladestationen_pro_1000_einwohner_2021", data=df);
plt.ylabel("Anzahl Ladestationen pro 1000 Einwohner")
plt.xlabel("Gesamtausgaben für Bildung pro Kopf")




SwissData = df[df['land']=='Schweiz']
SpainData = df[df['land']=='Spanien']
GermanData = df[df['land']=='Deutschland']
PortugueseData = df[df['land']=='Portugal']
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2021", data=SwissData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2020", data=SwissData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2021", data=SpainData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2020", data=SpainData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2021", data=GermanData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2020", data=GermanData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2021", data=PortugueseData)
sns.regplot(x="bip_je_einwohner_in_usd", y="ladestationen_pro_1000_einwohner_2020", data=PortugueseData)
plt.ylabel("Anzahl Ladestationen pro 1000 Einwohner")
plt.xlabel("BIP pro Einwohner in USD")


