import customtkinter as ctk
from pymongo import MongoClient
from cryptography.fernet import Fernet
from datetime import datetime
from bson.objectid import ObjectId
import os  # usado pra verificar se o arquivo da chave existe

# --------------------------
# Conexão com MongoDB
# --------------------------
def conectar_mongo():
    cliente = MongoClient(
        "mongodb+srv://isarangel:01isarafa@lista3bim.5ptiy8e.mongodb.net/?retryWrites=true&w=majority"
    )
    db = cliente["halloween_db"]
    return db["cofre_doces"]

collection = conectar_mongo()

# --------------------------
# Criptografia
# --------------------------
def carregar_ou_gerar_chave():
    """Gera uma chave Fernet se não existir e salva em 'chave.key'"""
    if not os.path.exists("chave.key"):
        nova_chave = Fernet.generate_key()
        with open("chave.key", "wb") as arquivo:
            arquivo.write(nova_chave)
        print("🔑 Nova chave gerada e salva em 'chave.key'")
        return nova_chave
    else:
        with open("chave.key", "rb") as arquivo:
            return arquivo.read()

chave = carregar_ou_gerar_chave()
fernet = Fernet(chave)

def criptografar(texto):
    return fernet.encrypt(texto.encode())

def descriptografar(texto):
    return fernet.decrypt(texto).decode()

# --------------------------
# Interface moderna
# --------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.configure(fg_color="#2b1a1a")
app.title("🍬 Cofre de Doces Interativo 🎃")
app.geometry("800x500")

# --------------------------
# Janela customizada de mensagem
# --------------------------
def mostrar_msg(titulo, texto, cor="#ff7518"):
    win = ctk.CTkToplevel(app)
    win.title(titulo)
    win.geometry("300x180")
    win.configure(fg_color="#1e0f0f")

    ctk.CTkLabel(win, text=texto, font=("Comic Sans MS", 16), text_color=cor, wraplength=250).pack(pady=30)
    ctk.CTkButton(win, text="Fechar", command=win.destroy, fg_color=cor, hover_color="#e25d00", corner_radius=10).pack(pady=10)
    win.grab_set()

# --------------------------
# Funções principais
# --------------------------
def adicionar_doce():
    nome = entry_nome.get()
    doce = entry_doce.get()
    qtd = entry_qtd.get()

    if not nome or not doce or not qtd.isdigit():
        mostrar_msg("Erro ⚠️", "Preencha todos os campos corretamente!", cor="#ff4444")
        return
    
    doc = {
        "child": nome,
        "candy_type": criptografar(doce),
        "qty": int(qtd),
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(doc)
    mostrar_msg("Sucesso 🍭", f"Doce adicionado para {nome}!", cor="#fb28bc")

    entry_nome.delete(0, 'end')
    entry_doce.delete(0, 'end')
    entry_qtd.delete(0, 'end')

    listar_doces()  # atualiza a lista automaticamente

def deletar_doce(doc_id):
    collection.delete_one({"_id": ObjectId(doc_id)})
    mostrar_msg("Removido 🗑️", "Cadastro removido com sucesso!", cor="#00cc66")
    listar_doces()

def listar_doces():
    for widget in frame_lista.winfo_children():
        widget.destroy()

    docs = collection.find().sort("timestamp", -1)
    for doc in docs:
        item_frame = ctk.CTkFrame(frame_lista, fg_color="#2a1515", corner_radius=8)
        item_frame.pack(fill="x", pady=5, padx=5)

        texto = f"🎃 {doc['child']} — {descriptografar(doc['candy_type'])} ({doc['qty']})"
        label = ctk.CTkLabel(item_frame, text=texto, font=("Comic Sans MS", 16), anchor="w")
        label.grid(row=0, column=0, sticky="w", padx=(10,5), pady=10)

        ctk.CTkButton(
            item_frame,
            text="Excluir",
            width=80,
            command=lambda id=doc["_id"]: deletar_doce(id),
            fg_color="#ff4444",
            hover_color="#cc3333",
            corner_radius=10
        ).grid(row=0, column=1, padx=10, pady=8, sticky="e")

def alternar_lista():
    global lista_visivel
    if lista_visivel:
        frame_lista.pack_forget()
        btn_listar.configure(text="Mostrar\n Lista de Doces")
    else:
        frame_lista.pack(pady=20)
        listar_doces()
        btn_listar.configure(text="Esconder\n Lista de Doces")
    lista_visivel = not lista_visivel

# --------------------------
# Layout
# --------------------------
frame_menu = ctk.CTkFrame(app, width=200, corner_radius=15)
frame_menu.pack(side="left", fill="y", padx=10, pady=10)

ctk.CTkLabel(frame_menu, text="🍬 Menu", font=("Comic Sans MS", 22, "bold")).pack(pady=15)

ctk.CTkButton(
    frame_menu,
    text="Cadastrar Doce",
    command=adicionar_doce,
    font=("Comic Sans MS", 14),
    fg_color="#ff7518",
    hover_color="#e25d00",
    corner_radius=10
).pack(pady=10)

btn_listar = ctk.CTkButton(
    frame_menu,
    text="Mostrar\n Lista de Doces",
    command=alternar_lista,
    font=("Comic Sans MS", 14),
    fg_color="#800080",
    hover_color="#a020f0",
    corner_radius=10
)
btn_listar.pack(pady=10)

frame_main = ctk.CTkFrame(app, corner_radius=15)
frame_main.pack(side="right", fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(
    frame_main,
    text="🎃 Cofre de Doces Interativo 🍭",
    font=("Comic Sans MS", 26, "bold")
).pack(pady=20)

entry_nome = ctk.CTkEntry(frame_main, placeholder_text="Nome da criança", width=300, height=40, font=("Comic Sans MS", 14))
entry_nome.pack(pady=10)

entry_doce = ctk.CTkEntry(frame_main, placeholder_text="Tipo de doce", width=300, height=40, font=("Comic Sans MS", 14))
entry_doce.pack(pady=10)

entry_qtd = ctk.CTkEntry(frame_main, placeholder_text="Quantidade", width=300, height=40, font=("Comic Sans MS", 14))
entry_qtd.pack(pady=10)

frame_lista = ctk.CTkScrollableFrame(frame_main, width=500, height=150, corner_radius=10)
lista_visivel = False

app.mainloop()
