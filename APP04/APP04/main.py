import flet as ft

#se importa la libreria random
import random

def main(page: ft.Page):
    #se crean las variables globales
    global numero_secreto,entrada_numero,text_resultado,boton_adivinar

    page.title = "adivina el numero"
    
    #se genera un numero random del 1 al 100
    numero_secreto = random.randit(1,100)
    
    #se genera la interfaz grafica
    titulo=ft.text("adivina el numero",size=25,color="white")
    entrada_numero=ft.TextField(label="tu adivinanza entre 1 y 100",width=300)
    boton_adivinar=ft.ElevatedButton("adivinar")
    text_resultado=ft.Text("",size=20,color="white")
    
    #se crea el contenedor
    contenedor_principal=ft.Container(
        content=ft.Column(
        controls=[
            titulo,
            entrada_numero,
            text_resultado,
            ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=300
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor=("black"),
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    
    page.add(contenedor_principal)