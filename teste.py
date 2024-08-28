def enviando_mensagem(browser, mensagem_grupo):
    print("Acessando o elemento")
    time.sleep(15)
    barra_mensagem = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))

    print("Clicando no elemento")
    time.sleep(15)
    barra_mensagem.click()

    time.sleep(10)
    print('continuar...')
    input()
    print("Primeiro tempo")
    barra_mensagem.send_keys(mensagem_nova)
    time.sleep(10)

    print("Segundo tempo")
    barra_mensagem.send_keys(Keys.ENTER)
    time.sleep(10)

    # pesquisa_barra(driver, "Grupo da Enfermagem")

    # enviando_mensagem(driver, mensagem_grupo)