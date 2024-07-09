# Passo a passo
# Passo 1 - Entar no sistema
# Passo 2 - Fazer login
# Passo 3 - Importar base de dados
# Passo 4 - Cadastrar o produto
# Passo 5 - Repetir até acabar a lista de produtos

#pip install pyautogui
#pip install pandas openpy numpy

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de teclar (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - Entar no sistema
# Abrir o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

# Passo 2 - Fazer login
pyautogui.click(x=377, y=351)
pyautogui.write("raf.ip@hotmail.com")
# passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("12345")
#clicar no botão de logar
pyautogui.click(x=474, y=498)

time.sleep(2)

# Passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 - Cadastrar o produto
# para cada linha da tabela
for linha in tabela.index:

  # Código do Produto
  pyautogui.click(x=340, y=260)

  codigo = str(tabela.loc[linha, "codigo"]) # string = texto  categoria tipo
  pyautogui.write(codigo)
  
  # Marca do Produto
  marca = str(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
  pyautogui.write(marca)
  
  # Tipo do Produto
  tipo = str(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
  pyautogui.write(tipo)
  
  # Categoria do Produto
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.press("tab")
  pyautogui.write(categoria)
  
  # Preço Unitário do Produto
  preco_unitario = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.press("tab")
  pyautogui.write(preco_unitario)
  
  # Custo do Produto
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.press("tab")
  pyautogui.write(custo)
  
  # OBS
  pyautogui.press("tab")
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":
    pyautogui.write("obs")
  

  # Clicar no botão de enviar
  pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(5000)







