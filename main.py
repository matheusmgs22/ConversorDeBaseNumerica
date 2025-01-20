import tkinter as tk
from tkinter import ttk

COLORS = {
    "black": "#444466",
    "white": "#feffff",
    "blue": "#6f9fbd",
    "value": "#38576b",
    "text": "#403d3d",
    "orange": "#e89613",
}

janela = tk.Tk()
janela.title("Conversor de Base Numérica")
janela.geometry("400x310")
janela.configure(bg=COLORS["white"])

# Estilo
style = ttk.Style()
style.theme_use("clam")

# Frames
frame_top = tk.Frame(janela, width=400, height=60, bg=COLORS["white"])
frame_top.grid(row=0, column=0, pady=(0, 10))

frame_bottom = tk.Frame(janela, width=400, height=250, bg=COLORS["white"])
frame_bottom.grid(row=1, column=0, padx=20)

# Função de Conversão
def converter():
    def numero_para_decimal(numero, base):
        try:
            decimal = int(numero, base)
            binario = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:].upper()

            l_binario_result["text"] = binario
            l_octal_result["text"] = octal
            l_decimal_result["text"] = decimal
            l_hexadecimal_result["text"] = hexadecimal
        except ValueError:
            l_binario_result["text"] = l_octal_result["text"] = ""
            l_decimal_result["text"] = l_hexadecimal_result["text"] = "Entrada Inválida"

    numero = e_valor.get()
    base = combo.get().upper()
    base_map = {"BINARIO": 2, "OCTAL": 8, "DECIMAL": 10, "HEXADECIMAL": 16}

    if base in base_map:
        numero_para_decimal(numero, base_map[base])
    else:
        l_binario_result["text"] = l_octal_result["text"] = ""
        l_decimal_result["text"] = l_hexadecimal_result["text"] = "Base Inválida"

# Titulo
app_name = tk.Label(
    frame_top,
    text="Conversor de Base Numérica",
    anchor= 'center',
    font=("System 20"),
    bg=COLORS["blue"],
    fg=COLORS["white"],
)
app_name.pack(expand=True)

# Entrada e Botao
bases = ["BINARIO", "OCTAL", "DECIMAL", "HEXADECIMAL"]
combo = ttk.Combobox(frame_bottom, values=bases, width=12, justify="center", font=("Ivy 12 bold"))
combo.place(x=30, y=10)
combo.set("DECIMAL")

e_valor = tk.Entry(frame_bottom, width=9, justify="center", font=("Ivy 13"), highlightthickness=1, relief="solid")
e_valor.place(x=160, y=10)

b_converter = tk.Button(
    frame_bottom,
    text="Converter",
    command=converter,
    font=("Ivy 8 bold"),
    bg=COLORS["white"],
    fg=COLORS["text"],
    relief="raised",
    overrelief="ridge",
)
b_converter.place(x=250, y=10)

# Resultados
labels = [
    ("Binário", 60),
    ("Octal", 100),
    ("Decimal", 140),
    ("Hexadecimal", 180),
]
result_vars = {}

for text, y in labels:
    label = tk.Label(frame_bottom, text=text, width=12, anchor="nw", font=("Verdana 13"), bg=COLORS["orange"], fg=COLORS["white"])
    label.place(x=35, y=y)

    result = tk.Label(frame_bottom, text="", width=13, anchor="center", font=("Verdana 13"), fg=COLORS["text"])
    result.place(x=170, y=y)
    result_vars[text] = result

l_binario_result = result_vars["Binário"]
l_octal_result = result_vars["Octal"]
l_decimal_result = result_vars["Decimal"]
l_hexadecimal_result = result_vars["Hexadecimal"]

janela.mainloop()
