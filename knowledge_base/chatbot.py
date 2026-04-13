import json

# Cargar la base de conocimiento
def cargar_base():
    with open("baseconocimiento.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Buscar respuesta
def buscar_respuesta(user_input, data):
    user_input = user_input.lower()

    for tema in data.values():
        for entrada in tema:
            for pattern in entrada["patterns"]:
                if pattern in user_input:
                    return entrada["answer"]

    return None

# Chatbot principal
def iniciar_chat():
    data = cargar_base()

    print("🤖 Hola, soy VíaBot CR 🚗, tu asistente de educación vial.")
    print("Escribí 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ")

        if user_input.lower() == "salir":
            print("🤖 ¡Mucha suerte en tu examen! 🚦")
            break

        respuesta = buscar_respuesta(user_input, data)

        if respuesta:
            print("🤖", respuesta)
        else:
            print("🤖 Lo siento, no entendí tu pregunta. Intenta de otra forma.")

# Ejecutar chatbot
if __name__ == "__main__":
    iniciar_chat()