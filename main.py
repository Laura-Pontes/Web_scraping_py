import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://forbes.com.br/under-30/under30-2024/categoria/musica-literatura-u30-2024/'
driver.get(url)

cards = driver.find_elements(By.CSS_SELECTOR, 'article')

dados = []

for card in cards:
    conteudo = card.text.strip().split("\n")
    idade = conteudo[0] if len(conteudo) > 0 else None
    nome = conteudo[1] if len(conteudo) > 1 else None
    dados.append({'Nome': nome, 'Idade': idade})

df = pd.DataFrame(dados)
df = df.iloc[:6]

print(df)

df.to_csv("Under30 Forbes.csv", index=False, encoding="utf-8")
print("\nArquivo 'Under30 Forbes.csv' criado com sucesso!✅\n")