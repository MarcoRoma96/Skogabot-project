import os
import random
import datetime
import json
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Custom libs
from typedef import *
from functions import *


# Comandi del Bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /start: messaggio di benvenuto.
    """
    welcome_text = (
        "Ciao! Sono il bot del viaggio in Islanda 😎.\n\n"
        "Per conoscere tutte le funzionalità, usa il comando /help."
    )
    await update.message.reply_text(welcome_text, parse_mode='markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /help: mostra le funzionalità disponibili.
    """
    help_text = (
        "Ecco cosa posso fare per te:\n\n"
        "/start              - Avvia il bot e mostra il messaggio di benvenuto.\n"
        "/help               - Mostra questo messaggio di aiuto.\n"
        "/piano <num_giorno> - Visualizza il piano del giorno specifico (es.: /piano 1).\n"
        "/cacca <num_giorno> - Visualizza il calendario Cacca.\n"
        "/weather <città>    - Mostra le previsioni meteo per la città richiesta (default: Reykjavik).\n"
        "/volcano            - Controlla lo stato vulcanico attuale.\n"
        "/curiosita          - Ricevi una curiosità divertente del giorno."
        "/subscribe_recipe   - Iscriviti per ricevere automaticamente le ricette del giorno (dal 19/04 al 27/04).\n"
    )
    await update.message.reply_text(help_text, parse_mode='markdown')

async def piano(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /piano: restituisce il messaggio statico del piano del giorno richiesto.
    """
    if not context.args:
        await update.message.reply_text("Per favore, specifica il numero del giorno. Es.: /piano 2")
        return

    day_requested = context.args[0]
    message = STATIC_ITINERARY.get(day_requested)

    if message:
        reply_text = f"🚀 Ehi, ecco il piano per il Giorno {day_requested}:\n\n" + message
    else:
        reply_text = f"Ops, non ho trovato il piano per il Giorno {day_requested}. Controlla il numero e riprova!"
    
    await update.message.reply_text(reply_text, parse_mode='markdown')

async def cacca(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /cacca: restituisce il calendario Cacca per il giorno selezionato (o il giorno attuale).
    """
    try:
        if not context.args:
            day = datetime.datetime.now().day - 18
        else:
            day = int(context.args[0])

        if day < 1 or day > 9:
            status = "Non sei ancora in viaggio o hai scelto un giorno non valido! Non puoi usare il calendario Cacca!💩"
        else:
            status = CALENDARIO_CACCA.get(str(day))

    except ValueError as ve:
        status = "Stai cercando di fare dei danni 😡"

    await update.message.reply_text(status, parse_mode='markdown')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /weather: fornisce le previsioni meteo per la città specificata (default: Reykjavik).
    """
    location = "Reykjavik"
    if context.args:
        location = " ".join(context.args)
        print(f"Location: {location}")
    forecast = get_weather_forecast(city=location)
    print(f"Forecast: {forecast}")
    print(type(update.message))
    await update.message.reply_text(forecast, parse_mode='markdown')

async def volcano(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /volcano: restituisce lo stato vulcanico attuale.
    """
    status = get_volcano_status()
    await update.message.reply_text(status, parse_mode='markdown')

async def curiosita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /curiosita: invia una curiosità divertente del giorno.
    """
    reply = random.choice(curiosities)
    await update.message.reply_text(f"🌋 Curiosità del giorno: {reply}", parse_mode='markdown')

async def scheduled_recipe(context: ContextTypes.DEFAULT_TYPE):
    """
    Funzione schedulata per inviare una ricetta dalla lista RECIPES.
    Viene eseguita giornalmente alle ore 12:00 e alle 19:30 solo dal 19/04 al 27/04.
    """
    global RECIPE_INDEX
    today = datetime.date.today()
    start_date = datetime.date(2025, 4, 14)
    end_date = datetime.date(2025, 4, 27)
    if today < start_date or today > end_date:
        # Se siamo fuori dal range, se siamo dopo il 27 aprile, il job può rimuoversi.
        if today > end_date:
            context.job.schedule_removal()
        return
    if RECIPE_INDEX >= len(RECIPES):
        RECIPE_INDEX = 0  # oppure potresti decidere di non ripetere le ricette
    chat_id = context.job.data  # il job data contiene l'ID della chat
    print(f"chat: {chat_id}\n")
    recipe_text = RECIPES[RECIPE_INDEX]
    RECIPE_INDEX += 1
    await context.bot.send_message(chat_id=chat_id, text=f"🍽️ *Ricetta del momento:*\n\n{recipe_text}")

async def subscribe_recipe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /subscribe_recipe: iscrive la chat corrente per ricevere automaticamente i messaggi programmati
    (ricette a mezzogiorno e alle 19:30 dal 19/04 al 27/04).
    """
    chat_id = update.effective_chat.id
    job_queue = context.job_queue
    # Pianifica il job per mezzogiorno (12:00)
    job_queue.run_daily(
        callback=scheduled_recipe,
        time=datetime.time(12, 0, tzinfo=TIMEZONE),
        data=chat_id,
        name=f"recipe_noon_{chat_id}"
    )
    # Pianifica il job per le 19:30
    job_queue.run_daily(
        callback=scheduled_recipe,
        time=datetime.time(19, 30, tzinfo=TIMEZONE),
        data=chat_id,
        name=f"recipe_evening_{chat_id}"
    )

    job_queue.run_daily(
        callback=scheduled_recipe,
        time=datetime.time(20, 5, tzinfo=TIMEZONE),
        data=chat_id,
        name=f"recipe_evening_{chat_id}"
    )

    await update.message.reply_text("Iscrizione avvenuta! Riceverai le ricette programmate a mezzogiorno e alle 19:30 dal 19/04 al 27/04.")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Gestisce comandi sconosciuti.
    """
    await update.message.reply_text("Comando non riconosciuto. Usa /help per vedere i comandi disponibili.")

def load_token(file_path='token.json', env_var='TOKEN'):
    # Prova a caricare il token da file (per lavorare in locale)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            token = data.get('token')
            if token is not None and token != "INSERT-YOUR-TOKEN-FROM-BOTFATHER-HERE":
                return token
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # Ignora e prova con la variabile d'ambiente

    # Prova a caricare il token dalla variabile d'ambiente (per server production)
    load_dotenv(dotenv_path="/home/abertagnon/skogabot/.env")
    token = os.getenv("TOKEN")
    if token:
        return token

    raise ValueError(
        f"Token non trovato. Assicurati che '{file_path}' esista o che la variabile d'ambiente '{env_var}' sia impostata.")


def main() -> None:
    """
    Funzione principale per avviare il bot.
    Sostituisci 'YOUR_TELEGRAM_BOT_TOKEN' con il token fornito da BotFather.
    """

    token = load_token()

    # Crea l'istanza dell'applicazione Telegram
    application = Application.builder().token(token).build()

    # Aggiunge gli handler per i comandi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("piano", piano))
    application.add_handler(CommandHandler("cacca", cacca))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("volcano", volcano))
    application.add_handler(CommandHandler("curiosita", curiosita))
    #subscription recipe of the day
    application.add_handler(CommandHandler("subscribe_recipe", subscribe_recipe))
    
    # Handler per comandi sconosciuti
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    logger.info("Bot in esecuzione...")
    application.run_polling()


if __name__ == "__main__":
    main()
