#requisitos Interfase Anaconda libreria OPENAI #licencia activa para el API OPENAI

import os
import openai
import sys

with open("clave_api.txt", encoding="utf-8") as archivo:
    openai.api_key = archivo.readline()
    
with open("productos_ferreteria.csv") as archivo:
    producto_csv = archivo.read()
    
with open("reglas.txt", encoding="utf-8") as archivo:
    reglas = archivo.read()
    
#Creamos la memoria temporal
contexto = []
#registramos las reglas y productos
contexto.append({'role':'system', 'content':f"""{reglas} {producto_csv}"""})

#enviamos mensaje al modelo
def enviar_mensajes(messages, model="gpt-4.1", temperature=0):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

#leemos el mensaje + agregamos al contexto | enviamos el contexto | + agregar respuesta al contexto
def recargar_mensajes(charla):
    contexto.append({'role':'user', 'content':f"{charla}"})
    print()
    print("El asistente está escribiendo ...")
    print()
    response = enviar_mensajes(contexto,temperature=0.5)
    contexto.append({'role':'assistant','content':f"{response}"})
    print()
    print("El asistente está escribiendo ...")
    print()
    print(response)
    
def main():
    print()
    print("¡Hola bienvenido! 🎉")
    print()
    print("Recuerda que puedes escribir 'exit' en cualquier momento para salir. Estoy para ayudarte 😊")
    print()
    while True:
            print()
            mensaje = input("Por favor, ingresa tu mensaje: ")
            print()
            
            if mensaje.lower() =='exit':
                break
            
            recargar_mensajes(mensaje)
            
if __name__=='__main__':
    main()