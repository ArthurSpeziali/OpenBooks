#Importanto as bibliotecas:
from time import sleep
from platform import system
import os
from selenium import webdriver
import selenium.common.exceptions

#Função da codificar o nome do livro em url. Substituindo caracteres especias por códigos de indentificação.
#Não funcina o quote(), nem o quote_plus() do ullib.parse! O VisionVox tem sua própia codificação:
def UrlCodVisionvox(string: str):
    new_string = string.replace('%', '%25').replace('+', '%2B').replace('á', r'%E1').replace('ç', r'%E7').replace(' ', '+').replace('é', r'%E9').replace('ã', r'%E3').replace('â', r'%E2').replace('ê', r'%EA').replace('ó', r'%F3').replace('õ', r'%F5').replace('ô', r'%F4').replace('í', r'%ED').replace('ú', r'%FA').replace('à', r'%E0').replace('è', r'%E8').replace('ò', r'%F2').replace('ì', r'%EC').replace('ù', r'%F9').replace('!', '%21').replace('@', '%40').replace('#', '%23').replace('$', '%24').replace('&', '%26').replace('(', '%28').replace(')', '%29').replace('{', '%7B').replace('}', '%7D').replace('[', '%5B').replace(']', '%5D').replace('ª', '%AA').replace('º', '%BA').replace('=', '%3D').replace('§', '%A7').replace(':', '%3A').replace(';', '%3B').replace('/', r'%2F').replace('\\', '%5C').replace('|', '%7C').replace(',', '%2C').replace('°', '%B0').replace('?', r'%3F').replace('¬', '%AC').replace("'", '%27').replace('"', '').replace('¹', '%B9').replace('²', '%B2').replace('³', '%B3').replace('£', '%A3').replace('¢', '%A2')

    return new_string

#Função para manipular uma URL, para evitar a pesquisa no site. Depois retorna a URL:
def url_finder(nome: str, extensão: str):
    
    nome = UrlCodVisionvox(nome)
    url_base = f'https://visionvox.com.br/busca.php?pagina=Nao&busca={nome}&ext={extensão}&buscar=Buscar'    
    
    return url_base
    

#Função para limpar o terminal de acordo com o terminal:
def clear_os():

    #Se for Windows, ele limpa o terminal com "cls":
    if system() == 'Windows': 
        os.system('cls')
    
    #Se for Linux ou Mac, limpa o terminal com "clear":
    else:
        os.system('clear')

#Introdução:
clear_os()
print('Bem vindo ao OpenBooks!')
print('By: Arthur Speziali.\n')
sleep(1)
print('Este programa abre o navegador e busca automaticamente por livros e o baixa (Fonte: VisionVox).')
print('PS: Este programa usa o Selenium, sempre tenha instalado os drivers do seu navegador.')
sleep(2)
clear_os()

#Calcula se ele pega um arquivo e formata, ou espera o usuário digitar:
print('Deseja digitar manualmente ou selecionar um arquivo? [M/F]\n')
while True:
    opção = input('> ').strip().lower()
    
    if opção != 'm' and opção != 'f':
        print('Opção inválida, tente novamente!')
        
    else:
        break

#Se for manualmente, transforma os livros em uma lista, depois, retira os espaços em branco com o strip() de cada item da lista
if opção == 'm':
    clear_os()
    print('Digite todos os nomes dos autores + livros (Primeiro os autores!), que deseja baixar! Separe por ";;".\n')
    books = input('> ').lower().split(';;')
    
    books_formated = list()
    for b in books:
        books_formated.append(b.strip())
    
    
elif opção == 'f':
    clear_os()
    
    #Verifica se o arquivo existe, tentando abrir ele:
    print('Digite o caminho até o arquivo:\n')
    while True:
        pathe = input('> ').strip()
        
        try:
            with open(pathe, encoding='utf-8') as v_path:
                #Pega todo o conteudo o arquivo, e transforma cada linha em um item de uma lista:
                books = v_path.read().split('\n')
                books_formated = list()
                
                #Tira todos os espaços em brancos da lista.
                #Substitui os espaços, e adciona em uma nova lista:                    
                for i in books:
                    if not i == '':
                        
                        books_formated.append(i)
                
                clear_os()                
                break
                
        except FileNotFoundError:
            print('\nCaminho mal-sucedido! Tente novamente!\n')

#Espera um tempo antes do próximo item, para evitar, quando aperta enter 2 vezes seguidas:
sleep(0.5)
clear_os()
print('Digite o nome da pasta de destino dos livros:\n')

#Cria a pasta com o "os", se já existir uma pasta com mesmo nome, repete a situação:
while True:
    folder = input(r'> ')
    
    try:
        os.mkdir(folder)
        break
    
    except:
        print('\nA pasta já existe, digite outro nome, tente novamente!\n')

sleep(0.5)
clear_os()
print('Digite na ordem qual é a preferencia para o formato dos arquivos. Separe por ";". Pdf, EPub, Txt [P/E/T]:\n')
while True:
    #Calcula se a ordem das extensões do arquivo digitada são válidas:
    ext = input('> ').strip().lower()

    #Tem que ter obrigatóriamente 3 dígitos:
    if len(ext) != 3:
        print('\nOrdem inválida, tente novamente!\n')
    
    #Tem que ter somente aquelas 3 letras:
    #Se quiser só baixar o livro de uma extensão, digite os três digitos da mesma letra:
    else:
        ext_v = False
        
        for i in ext:
            ext_allow = 'pet'
            
            if not i in ext_allow:
                ext_v = True
                
        if ext_v:
            print('\nOrdem inválida, tente novamente!\n')
        
        else:
            break

#Transforma as extensões em lista, e renomea elas corretamente:
ext_format = list()
for e in ext:
    if e == 'e':
        ext_format.append('epub')
        
    elif e == 'p':
        ext_format.append('pdf')
        
    elif e == 't':
        ext_format.append('txt')
        

sleep(0.5)    
clear_os()
print('Digite seu navegador. Chrome, Firefox, Edge ou Safari [C/F/E/S].\n')
while True:
    nav = input('> ').strip().lower()
    
    if nav != 'c' and nav != 'f' and nav != 'e' and nav != 's':
        print('\nOpção inválida, tente novamente!\n')
        
    else:
        break
    

#De acordo com o menu, abre o navegador correspondente:
if nav == 'c':
    driver = webdriver.Chrome()
    
    
elif nav == 'f':
    driver = webdriver.Firefox()
    

elif nav == 'e':
    driver = webdriver.Edge()
    
    
elif nav == 's':
    driver = webdriver.Safari()
    
clear_os()
print('Abrindo navegador... Aguarde!')

#Entra em um loop, para ir em cada extensão de casa livro:
clear_os()
for livro in books_formated:
    for extensão in ext_format:
            sleep(1)
        
            #Entra na URL formatada, com o nome do livro e extensão
            driver.get(url_finder(livro, extensão))
            
            #Tenta achar algum livro, se não achar, ele passa para próxima extensão:
            try:
                #Pega o nome e o link de download do livro:
                name_book = driver.find_element('xpath', '/html/body/a[3]').get_attribute('textContent')
                link_book = driver.find_element('xpath', '/html/body/a[3]').get_attribute('href')
                print('\nBaixando livro...\n')
                
                try:
                    #Se achar, ele usa o cmd para usar o curl. Baixando o livro pelo link de download. Depois quebra o loop:
                    os.system(f'cd "{folder}" && curl -o "{name_book}" "{link_book}"')
                    print(f'\nLivro baixado com êxito:\n{name_book}\n\n')
                    break
                
                except:
                    print('\nAlgum erro desconhecido aconteceu!\n')
                
            except:
                print('\nNenhum livro encontrado!\n')
                pass

driver.quit()
clear_os()        
print('Processo finalizado com êxito! Volte sempre!')
