import tkinter as tk
from tkinter import ttk

def actualizar_resultado(*args):
    datos = [
        proveedor.get(),
        tipo_documento.get(),
        numero_documento.get(),
        numero_contrato.get(),
        numero_comunicacion.get(),
        comprobante_relacionado.get(),
        objeto_transaccion.get(),
        numero_cuenta.get()
    ]
    resultado = ";".join(datos)
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert(tk.END, resultado)

def copiar_al_portapapeles():
    resultado = texto_resultado.get("1.0", tk.END).strip()
    if resultado:
        root.clipboard_clear()
        root.clipboard_append(resultado)
        root.update()

# Crear ventana principal
root = tk.Tk()
root.title("GENERARDOR DE GLOSAS")

# Hacer columnas expandibles
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Variables
proveedor = tk.StringVar()
tipo_documento = tk.StringVar()
numero_documento = tk.StringVar()
numero_contrato = tk.StringVar()
numero_comunicacion = tk.StringVar()
comprobante_relacionado = tk.StringVar()
objeto_transaccion = tk.StringVar()
numero_cuenta = tk.StringVar()

# Asociar actualizaciones automáticas
for var in [
    proveedor, tipo_documento, numero_documento, numero_contrato,
    numero_comunicacion, comprobante_relacionado,
    objeto_transaccion, numero_cuenta
]:
    var.trace_add("write", actualizar_resultado)

# Lista de campos
campos = [
    ("Proveedor", proveedor, "entry"),
    ("Tipo Documento", tipo_documento, "combobox"),
    ("Número Documento", numero_documento, "entry"),
    ("Número Contrato", numero_contrato, "entry"),
    ("Número Comunicación Interna", numero_comunicacion, "entry"),
    ("Comprobante Relacionado", comprobante_relacionado, "entry"),
    ("Objeto de la Transacción", objeto_transaccion, "entry"),
    ("Número de Cuenta Bancaria", numero_cuenta, "entry"),
]

# Crear campos
for i, (etiqueta, variable, tipo) in enumerate(campos):
    tk.Label(root, text=etiqueta).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    if tipo == "entry":
        entry = tk.Entry(root, textvariable=variable)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
    elif tipo == "combobox":
        cb = ttk.Combobox(root, textvariable=variable, values=["RC", "FC"], state="readonly")
        cb.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
        cb.current(0)

# Campo de texto multilinea
texto_resultado = tk.Text(root, height=4, wrap="word")
texto_resultado.grid(row=len(campos), column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Botón para copiar
tk.Button(root, text="Copiar", command=copiar_al_portapapeles).grid(row=len(campos)+1, column=0, columnspan=2, pady=5)

# Hacer que el campo de texto se expanda
root.rowconfigure(len(campos), weight=1)

# Iniciar aplicación
root.mainloop()