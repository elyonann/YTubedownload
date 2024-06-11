import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube

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
    path = filedialog.askdirectory()
    if path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)

# Criar a janela principal
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("550x300")
root.configure(bg="#2c3e50")

# Definir estilo
style = ttk.Style()
style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 12, "bold"))
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=5)
style.map("TButton",
          foreground=[('active', '#ecf0f1')],
          background=[('active', '#2980b9')],
          relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
style.configure("TEntry", font=("Helvetica", 12))



# Criar widgets
url_label = ttk.Label(root, text="URL do Vídeo do YouTube:")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

path_label = ttk.Label(root, text="Caminho para Salvar o Vídeo:")
path_label.pack(pady=10)

path_entry = ttk.Entry(root, width=50)
path_entry.pack(pady=5)

button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

browse_button = ttk.Button(button_frame, text="Selecionar Pasta", command=browse_path, style="Custom.TButton")
browse_button.grid(row=0, column=0, padx=5)

download_button = ttk.Button(button_frame, text="Baixar Vídeo", command=download_video, style="Custom.TButton")
download_button.grid(row=0, column=1, padx=5)

# Customizando cores dos botões
style.configure("Custom.TButton", background="#464848", foreground="#000000")
style.map("Custom.TButton",
          background=[('active', '#c0392b')],
          foreground=[('active', '#000000')])

# Iniciar o loop principal da interface gráfica
root.mainloop()
