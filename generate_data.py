import csv

# 🔹 Define intents and example sentences per language
intents = {
    "cancel_order": {
        "en": [
            "I want to cancel my order", "Cancel my order", "Please cancel it", "I don't want this order", "Abort the order"
        ],
        "hi": [
            "मुझे अपना ऑर्डर रद्द करना है", "ऑर्डर रद्द करो", "इसे रद्द कर दो", "मैं ऑर्डर नहीं चाहता", "ऑर्डर कैंसिल करें"
        ],
        "es": [
            "Quiero cancelar mi pedido", "Cancela mi pedido", "Por favor, cancela esto", "No quiero este pedido", "Anula el pedido"
        ]
    },
    "confirm_order": {
        "en": [
            "I want to confirm my order", "Confirm the order", "Please confirm it", "Confirm it now", "Yes, place the order"
        ],
        "hi": [
            "मुझे अपना ऑर्डर कन्फर्म करना है", "ऑर्डर कन्फर्म करो", "इसे कन्फर्म कर दो", "हां, ऑर्डर दो", "ऑर्डर पक्का करो"
        ],
        "es": [
            "Quiero confirmar mi pedido", "Confirma el pedido", "Por favor, confirma esto", "Sí, haz el pedido", "Confírmalo"
        ]
    },
    "order_status": {
        "en": [
            "What's the status of my order?", "Where is my order?", "Is my order shipped?", "Track my order", "Has it been delivered?"
        ],
        "hi": [
            "मेरा ऑर्डर कहाँ है?", "मेरे ऑर्डर की स्थिति क्या है?", "क्या मेरा ऑर्डर भेजा गया है?", "ऑर्डर ट्रैक करें", "क्या ऑर्डर आ गया?"
        ],
        "es": [
            "¿Dónde está mi pedido?", "¿Cuál es el estado de mi pedido?", "¿Mi pedido fue enviado?", "Rastrear mi pedido", "¿Ya llegó mi pedido?"
        ]
    },
    "change_address": {
        "en": [
            "Change my address", "Update my delivery address", "I want to edit my address", "Modify address", "Delivery address change"
        ],
        "hi": [
            "मेरा पता बदल दो", "डिलीवरी का पता बदलें", "मुझे पता अपडेट करना है", "पता संपादित करें", "नया पता डालो"
        ],
        "es": [
            "Cambiar mi dirección", "Actualizar la dirección", "Quiero cambiar mi dirección", "Editar dirección", "Modificar dirección"
        ]
    },
    "contact_advisor": {
        "en": [
            "I want to talk to support", "Contact customer care", "Call me please", "Need help", "Talk to agent"
        ],
        "hi": [
            "मुझे ग्राहक सेवा से बात करनी है", "कस्टमर केयर से बात कराओ", "मुझे कॉल करें", "मदद चाहिए", "एजेंट से बात करनी है"
        ],
        "es": [
            "Quiero hablar con atención al cliente", "Contactar soporte", "Llámame por favor", "Necesito ayuda", "Hablar con un agente"
        ]
    },
    "get_list_of_products": {
        "en": [
            "Show me the products", "List all items", "I want to see what's available", "Display items", "Available products please"
        ],
        "hi": [
            "मुझे उत्पाद दिखाओ", "सभी आइटम सूचीबद्ध करें", "क्या-क्या उपलब्ध है?", "आइटम दिखाओ", "उपलब्ध उत्पाद बताओ"
        ],
        "es": [
            "Muéstrame los productos", "Lista todos los artículos", "Quiero ver lo que hay disponible", "Mostrar productos", "Productos disponibles"
        ]
    },
    "not_ecommerce": {
        "en": [
            "How's the weather?", "Tell me a joke", "Who are you?", "Play a song", "What's your name?"
        ],
        "hi": [
            "मौसम कैसा है?", "कोई जोक सुनाओ", "तुम कौन हो?", "गाना चलाओ", "तुम्हारा नाम क्या है?"
        ],
        "es": [
            "¿Cómo está el clima?", "Cuéntame un chiste", "¿Quién eres?", "Pon una canción", "¿Cuál es tu nombre?"
        ]
    }
}

# 🔸 Write to CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['text', 'intent', 'lang'])

    for intent, lang_data in intents.items():
        for lang, sentences in lang_data.items():
            for sentence in sentences:
                writer.writerow([sentence, intent, lang])

print("✅ data.csv generated successfully with multiple intents and languages.")
