# Подгрузка модулей
import os

# todo: преременные

serveraddress = '31.148.198.34'
clientname = 'zero_client'
clientpassword = '00020A69177B'
corpPass = '00020A69177B'


# todo: функция формирования ini-файлов
def makefolder(orgname):
    path = 'ini//'
    os.mkdir(path + str(orgname))
    pathini = "ini//" + orgname + "//"
    print(pathini)
    return pathini

def iniFile(orgname, corpId, corpPass):
    pathini = makefolder(orgname)
    filename = pathini + "zeroviewer.ini"
    inifile = open(filename, 'w', encoding="utf-8")
    outinifile = '''[Mode]
    server=0
    client=1
    multiple_instances=1
    
    [Server]
    ssh_port=22
    server_address=''' + str(serveraddress) + '''
    client_user=''' + str(clientname) + '''
    client_password=''' + str(clientpassword) + '''
    operator_user=
    operator_password=
    proxy_none=1
    proxy_http=0
    proxy_socks4=0
    proxy_socks5=0
    proxy_port=3128
    proxy_address=
    proxy_user=
    proxy_password=
    
    [Client]
    client_id=''' + str(corpId) + '''
    client_id_fixed=0
    simple=0
    strong=0
    own=1
    vnc_pwd='''+ str(corpPass) + '''
    autoconnect=0
    send_to_tray=0'''

    inifile.write(outinifile)
    inifile.close()
    print(outinifile)


# todo: формирование справочника оператора
def AddOpListCorp(name, id, password):
    operList = open('zeroviewer.zb', 'a', encoding="utf-8")
    line = str(name) + ',' + str(id) + ',' + password + '\n'
    operList.write(line)
    operList.close()
    iniFile(name, id, password)

# todo: получение нового ID для организации
def LastOpID():
    try:
        operList = open('zeroviewer.zb')
    except IOError as e:
        print(u'не удалось открыть файл')
    else:
        lastLine = operList.readlines()[-1]
        print(lastLine)
        lastID = lastLine.split(',')[1].strip()
        print(lastID)
    return lastID

# todo: получаем новый ID для организации
def NewOpID():
    return str(int(LastOpID()) + 1)


def CheckCompList():
    try:
        compList = open('compList.txt','r', encoding="utf-8")
    except IOError as e:
        print(u'не удалось открыть файл')
    else:
        compArray = []
        with compList as file:
            for row in file:
                compArray.append(row.strip())
        compList.close()
        return compArray


def CheckOperList():
    try:
        operList = open('zeroviewer.zb', 'r', encoding="utf-8")
    except IOError as e:
        print(u'не удалось открыть файл')
    else:
        operArray = []
        with operList as file:
            for row in file:
                operArray.append(row.split(',')[0].strip())
        operList.close()
        return operArray

def addOrg():
    newCompList = list(set(CheckCompList()) - set(CheckOperList()))
    for name in newCompList:
        AddOpListCorp(name, NewOpID(), corpPass)
        print(name)


addOrg()
