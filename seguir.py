from flask import Blueprint, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import random
import datetime

app = Blueprint('seguir', __name__)

@app.route('/seguir', methods=['POST'])
def seguir():
    try:
        login = request.form['login']
        senha = request.form['senha']
        pagina = request.form['pagina']
        quantidade = int(request.form['quantidade'])

        # Inicialização do navegador
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')

        navegador = webdriver.Chrome(options=options)
        navegador.get('https://www.instagram.com')

        # Preencher login e senha
        while True:
            try:
                login_input = navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
                senha_input = navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
                entrar_btn = navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
                
                login_input.send_keys(login)
                senha_input.send_keys(senha)
                entrar_btn.click()
                break
            except:
                print('\033[1;31m Elemento não encontrado')
                time.sleep(1)

        # Aguardar carregamento após login
        time.sleep(40)

        # Acessar a página do perfil
        navegador.get(pagina)

        # Clicar em Seguidores
        while True:
            try:
                seguidores = navegador.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd']")
                seguidores.click()
                break
            except:
                print('\033[1;31m Elemento não encontrado')
                time.sleep(1)

        contagem = 0
        # Localizar botão "Seguir"
        for _ in range(quantidade):
            while True:
                try:
                    botao_seguir = navegador.find_element(By.XPATH,"//div[@class='_ap3a _aaco _aacw _aad6 _aade' and contains(text(), 'Seguir')]")
                    print('\033[1;32m Encontrei o botão "Seguir"')
                    
                    # Clicar no botão Seguir
                    botao_seguir.click()
                    horario_clique = datetime.datetime.now()
                    contagem += 1 
                    print(f'\n \033[1;32m Apertei o botao SEGUIR senhor às {horario_clique.strftime("%H:%M:%S")} {contagem} Perfil seguido')
                    tempo_espera = random.randint(72, 120)
                    time.sleep(tempo_espera)
                    break
                
                except:
#Se não encontrar nada, pode ser porque não tem elemento ná pagina, então ele vai rola a barra para baixo
                    print('\033[1;31m Elemento não encontrado')
                    time.sleep(5)
                    # seguir = navegador.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
                    seguir = navegador.find_element(By.CLASS_NAME,'_aano')
                    navegador.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",seguir)
                    time.sleep(1)
        
        navegador.quit()
        return jsonify({"message": "Bot de seguidores concluído"})

    except Exception as e:
        print("Erro:", e)
        return jsonify({"error": str(e)})
