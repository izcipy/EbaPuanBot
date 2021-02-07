from selenium.webdriver.common.by import By

class AllLocators:
    frame = (By.TAG_NAME, "iframe")

    tc_input = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/form/div[2]/div/input")
    password_input = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/form/div[3]/div/input")
    sinavlar = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div[5]/a/div/div[2]')
    alert = (By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div')
    tarama_testleri = (By.XPATH, '//*[@id="vcComponentTestCenterView"]/div[2]/div[1]/div')
    okul_list = (By.XPATH, '//*[@id="vc-treeselector-eba"]/div/div[1]/div')
    okul_list_box = (By.XPATH, '//*[@id="vc-treeselector-eba"]/div/div[1]/div/ul')
    sinif_list = (By.XPATH, '//*[@id="vc-treeselector-eba"]/div/div[2]/div')
    sinif_list_box = (By.XPATH, '//*[@id="vc-treeselector-eba"]/div/div[2]/div/ul')
    ders_list = (By.XPATH, '//*[@id="vc-treeselector-eba"]/div/div[3]/div/div[1]')
    ders_list_box = (By.XPATH, '//*[@id="vc-treeselector-eba"]/div/div[3]/div/ul')
    #testler_full = (By.XPATH, '//*[@id="vc-examlist"]')
    testler_full = (By.XPATH, '//*[@id="vc-examlist"]')
    testler_isim = (By.XPATH, '//*[@id="vc-examlist"]/div[{}]/div[2]/div[1]/div/div')
    basla = (By.XPATH, '//*[@id="vc-resource-detail-exam"]')
    sorular = (By.XPATH, "/html/body/div/div[1]/section/div[2]/div/div/div[{}]")
    cevaplar = (By.XPATH, "/html/body/div/div[1]/section/div[2]/div/div/div[{}]/div[{}]")
    unite_list = (By.XPATH, '//*[@id="vc-unitsubjectselector"]/div/div/select')
    unite_option = '//*[@id="vc-unitsubjectselector"]/div/div/select/option[{}]'
    bitir_kapat = (By.XPATH, '//*[@id="finish-button"]/span')
    bitir_1 = (By.XPATH, '/html/body/div[2]/div/div/div[3]/span[1]/span')
    #kapat = (By.XPATH, '//*[@id="finish-button"]/span')
    geri = (By.XPATH, '//*[@id="vc-content-title"]/div/div/a/i')


