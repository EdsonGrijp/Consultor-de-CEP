from tkinter import messagebox
import requests
import tkinter as tk


def buscar():
    cep = entry_cep.get().strip()
    cep = cep.replace("-", "").replace(" ", "")

    if len(cep) != 8:
        messagebox.showerror("Erro", "CEP inválido! Digite 8 números.")
        return

    res = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    dados = res.json()

    if 'code' in dados and dados['code'] == 'invalid':
        messagebox.showerror("Erro", "CEP não encontrado!")
        return

    resultado.delete(1.0, tk.END)
    resultado.insert(tk.END, "CEP: " + dados['cep'] + "\n")
    resultado.insert(tk.END, "Endereço: " + dados['address'] + "\n")
    resultado.insert(tk.END, "Estado: " + dados['state'] + "\n")
    resultado.insert(tk.END, "Bairro: " + dados['district'] + "\n")
    resultado.insert(tk.END, "DDD: " + dados['ddd'] + "\n")

janela = tk.Tk()
janela.title("Consulta CEP")
janela.geometry("500x500")

titulo = tk.Label(janela, text="CONSULTA DE CEP", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame para organizar o campo e o botão
frame = tk.Frame(janela)
frame.pack(pady=10)

# Rótulo (texto) do CEP
label_cep = tk.Label(frame, text="CEP:", font=("Arial", 12))
label_cep.pack(side=tk.LEFT, padx=5)

# Campo para digitar
entry_cep = tk.Entry(frame, font=("Arial", 12), width=15)
entry_cep.pack(side=tk.LEFT, padx=5)

# Botão (por enquanto só um placeholder)
botao = tk.Button(frame, text="Buscar", font=("Arial", 10), command=buscar)
botao.pack(side=tk.LEFT, padx=10)

# Área de resultados (caixa de texto)
resultado = tk.Text(janela, width=50, height=10, font=("Courier", 10))
resultado.pack(pady=10)

# Rodapé
rodape = tk.Label(janela, text="Consulta via AwesomeAPI", font=("Arial", 8), fg="gray")
rodape.pack()

janela.mainloop()

