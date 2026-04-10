from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

categorias = [
    {"nombre": "BOOK INFANTIL", "slug": "infantil", "portada": "portada-infantil.webp"},
    {"nombre": "15 AÑOS", "slug": "quince", "portada": "portada-15.webp"},
    {"nombre": "BODAS", "slug": "bodas", "portada": "portada-bodas.webp"}
]

TRABAJOS_DATA = {
    "infantil": [
        {
            "slug": "melina", 
            "nombre": "Melina", 
            "año": "2026", 
            "fotos": ["mel1.webp", "mel2.webp", "mel3.webp", "mel4.webp", "mel5.webp", "mel6.webp", "mel7.webp", "mel8.webp", "mel9.webp", "mel10.webp"]
        }, 
        {
            "slug": "victoria", 
            "nombre": "Victoria", 
            "año": "2024", 
            "fotos": ["victoria1.webp", "victoria2.webp", "victoria3.webp"]
        }
    ],
    "quince": [
        {
            "slug": "martina",
            "nombre": "Martina", 
            "año": "2023", 
            "fotos": ["martina1.webp", "martina2.webp", "martina3.webp"]}
    ],
    "bodas": []
}
@app.route("/")
def inicio():
    return render_template("inicio.html", categorias=categorias)

@app.route("/galeria/<categoria_slug>")
def ver_categoria(categoria_slug):
    trabajos = TRABAJOS_DATA.get(categoria_slug, [])
    return render_template("categoria.html", categoria=categoria_slug, trabajos=trabajos)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/galeria/<categoria>/<trabajo>")
def ver_fotos_trabajo(categoria, trabajo):
    lista_trabajos = TRABAJOS_DATA.get(categoria, [])
    trabajo_info = next((t for t in lista_trabajos if t["slug"].lower() == trabajo.lower()), None)

    if not trabajo_info:
        return "Trabajo no encontrado", 404
    
    return render_template("trabajo_detalle.html", 
                           categoria=categoria, 
                           trabajo=trabajo_info, 
                           fotos=trabajo_info["fotos"])

if __name__ == "__main__":
    app.run(debug=True)