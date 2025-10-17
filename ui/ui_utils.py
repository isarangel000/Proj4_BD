import customtkinter as ctk

def mostrar_msg(app, titulo, texto, cor="#ff7518"):
    win = ctk.CTkToplevel(app)
    win.title(titulo)
    win.geometry("320x180")
    win.configure(fg_color="#1e0f0f")
    ctk.CTkLabel(win, text=texto, font=("Comic Sans MS", 15), text_color=cor, wraplength=280).pack(pady=20)
    ctk.CTkButton(win, text="Fechar", command=win.destroy, fg_color=cor, hover_color="#e25d00", corner_radius=10).pack(pady=10)
    win.grab_set()

def confirmar_delete(app, doc_id, descricao, deletar_callback):
    win = ctk.CTkToplevel(app)
    win.title("Confirmar exclusão")
    win.geometry("360x180")
    win.configure(fg_color="#1e0f0f")

    ctk.CTkLabel(win, text=f"Deletar:\n{descricao}", font=("Comic Sans MS", 13), wraplength=320).pack(pady=12)
    btn_frame = ctk.CTkFrame(win, fg_color="#1e0f0f", corner_radius=5)
    btn_frame.pack(pady=8)

    ctk.CTkButton(btn_frame, text="Sim, deletar", command=lambda: [deletar_callback(doc_id), win.destroy()], fg_color="#ff4444", hover_color="#cc3333", corner_radius=8).grid(row=0, column=0, padx=8)
    ctk.CTkButton(btn_frame, text="Cancelar", command=win.destroy, fg_color="#808080", hover_color="#606060", corner_radius=8).grid(row=0, column=1, padx=8)

    win.grab_set()
