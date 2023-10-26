import telegram
import asyncio
import re
import asyncio

# Función para enviar mensajes con formato MarkdownV2 ERROR:
async def enviar_mensaje_asyncerror(mensaje: str, chat_id: str = '-4070197804'):
    bot = telegram.Bot(token='6632174170:AAEIwmjboyA9-9KYJk9cZ2BAlBQfPpWr_mk')
    mensaje = mensaje.replace('_', r'--').replace('*', r'--').replace('`', r'--').replace('\'', r'--').replace('(','--').replace(')','--').replace('-',' ').replace('.', ' ')
    
    # Usamos una expresión regular para encontrar y formatear el mensaje de error en negrita
    mensaje_formateado = re.sub(r'(.*): (.*)', r'*\1:* \2', mensaje)
    
    await bot.send_message(chat_id=chat_id, text=mensaje_formateado, parse_mode='MarkdownV2')

def enviar_mensajerror(mensaje: str, chat_id: str = '-4070197804'):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(enviar_mensaje_asyncexito(mensaje, chat_id))






# Función para enviar mensajes con formato MarkdownV2 EXITO:
async def enviar_mensaje_asyncexito(mensaje: str, chat_id: str = '-4020688258'):
    bot = telegram.Bot(token='6632174170:AAEIwmjboyA9-9KYJk9cZ2BAlBQfPpWr_mk')
    mensaje = mensaje.replace('_', r'--').replace('*', r'--').replace('`', r'--').replace('\'', r'--').replace('(','--').replace(')','--').replace('-',' ').replace('.', ' ')
    
    # Usamos una expresión regular para encontrar y formatear el mensaje de error en negrita
    mensaje_formateado = re.sub(r'(.*): (.*)', r'*\1:* \2', mensaje)
    
    await bot.send_message(chat_id=chat_id, text=mensaje_formateado, parse_mode='MarkdownV2')

def enviar_mensajexito(mensaje: str, chat_id: str = '-4020688258'):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(enviar_mensaje_asyncexito(mensaje, chat_id))
    except Exception as e:
        print(e)



# Función para enviar mensajes con formato MarkdownV2 FRACASO:
async def enviar_mensaje_asyncfracaso(mensaje: str, chat_id: str = '-4085103186'):
    
    bot = telegram.Bot(token='6632174170:AAEIwmjboyA9-9KYJk9cZ2BAlBQfPpWr_mk')
    mensaje = mensaje.replace('_', r'--').replace('*', r'--').replace('`', r'--').replace('\'', r'--').replace('(','--').replace(')','--').replace('-',' ').replace('.', ' ')
    
    # Usamos una expresión regular para encontrar y formatear el mensaje de error en negrita
    mensaje_formateado = re.sub(r'(.*): (.*)', r'*\1:* \2', mensaje)
    
    await bot.send_message(chat_id=chat_id, text=mensaje_formateado, parse_mode='MarkdownV2')

def enviar_mensajefracaso(mensaje: str, chat_id: str = '-4085103186'):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(enviar_mensaje_asyncexito(mensaje, chat_id))
    except Exception as e:
        print(e)

