# Python 3 code
import urllib.request, urllib.parse, urllib.error,urllib
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import sys
import re
import runter
import donation

ADDON_ID      = 'Kodish.repo.store'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')


logexite = "special://home/media/kodi.txt"
filewk = os.path.join(xbmcvfs.translatePath(logexite))


def link_update():
    updatefile = "special://home/addons/Kodish.repo.store/default2.py"
    update = os.path.join(xbmcvfs.translatePath(logexite))
    
    url = "https://raw.githubusercontent.com/kodishmediacenter/omega/master/default.py"
    url_base = urllib.request.urlopen(url).read()
    link = url_base
    f = open(update, 'w')
    f.write(link)
    f.close()

    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Kodish Store Atualizado com sucesso !!!')





def youtube_api_bkp():
    youtubeapi = "special://home/userdata/addon_data/plugin.video.youtube"
    youtube = os.path.join(xbmcvfs.translatePath(youtubeapi))

    kodish_storehome = "special://home/addons/Kodish.repo.store/data"
    kodish_store = os.path.join(xbmcvfs.translatePath(kodish_storehome))
    shutil.move(youtube, kodish_store)

def youtube_api_res():
    youtubeapi = "special://home/userdata/addon_data/"
    youtube = os.path.join(xbmcvfs.translatePath(youtubeapi))

    kodish_storehome = "special://home/addons/Kodish.repo.store/data/plugin.video.youtube"
    kodish_store = os.path.join(xbmcvfs.translatePath(kodish_storehome))
    shutil.move(kodish_store,youtube)
    
def super_log_fix():
    f = os.path.join(xbmcvfs.translatePath("special://logpath/kodi.log"))
    file = open(f,"w") 
    file.write("Super Log Fixed")
    file.write("\n")
    #main_kodish()

def addon_instalado(ids):
    tamz = len(ids)
    for a in ['special://home/addons/'+ids[0:tamz-4]+'']:
        existe = xbmcvfs.translatePath(a)
        
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
    return ids


def fix_check():
    for a in ['special://home/addons/xbmc.python2']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
  

def limpacache():
    for a in ['special://home/cache']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
		
def updatefix(ids):
    for a in ['special://home/addons/'+ids+'']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)


def limpaelementum():
    for a in ['special://home/addons/plugin.video.elementum','special://home/addons/script.elementum.burst','special://home/addons/context.elementum','special://home/userdata/addon_data/plugin.video.elementum']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
		
    


def execc(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-4]
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/'+filezip2+''


     
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    ativaaddon(filezip21)
    file = open(filewk,"w") 
    file.write(filezip21)
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')

    
    main_kodish()
    
def execc2(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "xbmc.python2"
    fix_check()
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/fix/xbmc.python2.zip'
    filezip2 = "xbmc.python2.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)

    main_kodish()



def execc3(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    
    filezip2 = str(filezip.replace("?file=","").replace('https://kodishmediacenter.github.io/kodi19/repos/repos/',''))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-4]
    
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/'+filezip2+''
    url2 = url.replace('repos/repos','repos').replace('https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/','')
    url3 = url2.replace('https://kodishmediacenter.github.io/kodi19/repos/','https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/repos/')


     
    print("baixando addon ....")
    os.chdir (api_file)
    file = open(filewk,"a")
    file.write('\n')
    file.write(url3)
    file.write('\n')
    file.close()
    #urllib.request.urlretrieve(url3, ""+filezip2+"")
    #urllib.request.urlretrieve(url3)
    import wget 
    wget.download(url3)
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    ativaaddon(filezip21)
    file = open(filewk,"a")
    file.write('\n')
    file.write('Versão Instalada\n')
    file.write(filezip21)
    file.write('\n')
    
    f.close()

    file = open(filewk,"a")
    file.write('Versão a ser Extraida\n')
    file.write(filezip2)
    file.write('\n')
    f.close()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')    
    main_kodish()



def execc4(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = filezip2[0:tam-4]
    url = 'https://raw.githubusercontent.com/kodishmediacenter/repos19/main/repo/'+filezip2+''
    


     
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    ativaaddon(filezip21)
    file = open(filewk,"w") 
    file.write(filezip21)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')

    
    main_kodish()
    

def ativaaddon(ids):
    import database
    nome = ids
    database.insert_id(nome)
    database.enable_addon(nome)


def addDir(title,url,icon):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':icon,'fanart':FANART})
    nome = url
    execc(nome)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def addons_menu():
    link = "https://kodishmediacenter.github.io/kodi19/"
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodish Store Neo Kodi 19', 'music', '', False, False, link)
    fns = str(fn)
    fns2 = fns.replace('https://kodishmediacenter.github.io/kodi19/addons/','')
    file = open(filewk,"w") 
    file.write(fns2)
    file.close()
    addon_instalado(fns2)
    execc(fns2)
    

def addons_fix():
    link = "http://kodishteam.space/fix/k19/"
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodish Store Neo Kodi 19', 'music', '', False, False, link)
    fns = str(fn)
    fns2 = fns.replace('http://kodishteam.space/fix/k19/','https://kodishmediacenter.github.io/kodi19/fix/')
    file = open(filewk,"w") 
    file.write(fns2)
    file.close()
    addon_instalado(fns2)
    execc2(fns2)

def addons_repo():
    link3 = "https://kodishmediacenter.github.io/repos19/"
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(1, 'Kodish Store Neo Kodi 19', 'music', '', False, False, link3)
    fns = str(fn)
    fns2 = fns.replace('https://kodishmediacenter.github.io/repos19/repo/','')
    file = open(filewk,"w") 
    file.write(fns2)
    file.close()
    addon_instalado(fns2)
    execc4(fns2)



def ativaraddon():
    xbmc.executebuiltin("ActivateWindow(addons://sources/video/addons)")

def main_kodish():
    limpacache()
    super_log_fix()   
    dialog = xbmcgui.Dialog()
    link = dialog.select('Kodish Store - Neo', ['Doação','Instalar Addons','Remover o Elementun','Instalar o Fix (Obrigatorio)','Repositorios','Instalar o Elementum','Instalar Torrest','Limpar o Super Cache','Backup da Api do Youtube','Atualizar a Kodish Store'])


    if link == 0:
        donation.donation()
    if link == 1:
        addons_menu()
    if link == 2:
        limpaelementum()
    if link == 3:
        addons_fix()
    if link == 4:
        addons_repo()
    if link == 5:
        import elementum
        elementum.main_elementum()
    if link == 6:
        import torrest
        torrest.main_torrest()
    if link == 7:
        super_log_fix()

    if link == 8:
        dialog = xbmcgui.Dialog()
        linka = dialog.select('Sessão de Backup da Api do youtube ', ['Fazer o Backup','Restaurar o Backup'])

        if linka == 0: 
            youtube_api_bkp()
            dialog = xbmcgui.Dialog()

            kodish_storehome = "special://home/addons/Kodish.repo.store/data"
            kodish_store = os.path.join(xbmcvfs.translatePath(kodish_storehome))

            dialog.ok('Kodish Store', 'Backup feito com sucesso '+kodish_store+' !!!')

        else:
            youtube_api_res()
            dialog = xbmcgui.Dialog()

            dialog.ok('Kodish Store', 'Backup Restaurado com sucesso Renicie seu Kodi para melhor funcionamento !!!')
            
    if link == 9:
            link_update()

        


main_kodish()

 
