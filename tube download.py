import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
import os

def download_video():
    video_url = url_entry.get()
    save_path = path_entry.get()
    if not video_url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return
    if not save_path:
        messagebox.showerror("Erro", "Por favor, insira o caminho para salvar o vídeo.")
        return
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        messagebox.showinfo("Sucesso", f'Vídeo "{yt.title}" baixado com sucesso em {save_path}')
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def browse_path():
    path = tk.filedialog.askdirectory()
    if path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)

# Criar a janela principal
root = tk.Tk()
root.title("YouTube Video Downloader")

# Criar widgets
url_label = tk.Label(root, text="URL do Vídeo do YouTube:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

path_label = tk.Label(root, text="Caminho para Salvar o Vídeo:")
path_label.pack(pady=5)

path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

browse_button = tk.Button(root, text="Procurar", command=browse_path)
browse_button.pack(pady=5)

download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

# Iniciar o loop principal da interface gráfica
root.mainloop()