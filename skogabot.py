import logging
import random
import requests
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Itinerario statico: messaggi definiti a mano (hard-coded)
STATIC_ITINERARY = {
    "1": (
        "**Giorno 1 (19/04/2025):**\n"
        "Arrivo a Keflavik, recupero bagagli e noleggio auto. Trasferimento al Downtown Reykjavík Apartments, "
        "cena e visita opzionale a Reykjavík."
    ),
    "2": (
        "**Giorno 2 (20/04/2025):**\n"
        "Colazione e spesa al supermercato. Partenza per Þingvellir, visita al Parco Nazionale, poi attrazioni come "
        "Haukadalur, il geyser Strokkur, la cascata Gullfoss e Seljalandsfoss. Fine giornata con trasferimento "
        "alla Countryhouse e cena a Hvolsvöllur."
    ),
    "3": (
        "**Giorno 3 (21/04/2025):**\n"
        "Partenza mattutina per Butra, visita a Skógafoss (con pranzo al sacco), Sólheimajökull e Solheimasandur. "
        "Proseguimento verso Dyrhólaey Beach con pernottamento all’Hotel Katla e cena in albergo."
    ),
    "4": (
        "**Giorno 4 (22/04/2024):**\n"
        "Partenza presto per il canyon Fjaðrárgljúfur, seguito dal pranzo. Tour del ghiacciaio Vatnajökull, visita a "
        "Diamond beach e pernottamento presso Höfn Inn Guesthouse. Cena inclusa."
    ),
    "5": (
        "**Giorno 5 (23/04/2025):**\n"
        "Lungo viaggio in auto con tappe a Hofn e visita al Stuðlagil Canyon, Dettifoss, Hverir e ai Mývatn "
        "Nature Baths. Pernottamento al Fosshótel Mývatn, cena al sacco."
    ),
    "6": (
        "**Giorno 6 (24/04/2025):**\n"
        "Sumardagurinn fyrsti: viaggio in auto e tappe a Goðafoss, Reykjavjafoss, Víðimýri e Berserkjahraun con "
        "eventuale visita al museo dello squalo. Pernottamento presso Snæfellsjökull Apartments."
    ),
    "7": (
        "**Giorno 7 (25/04/2025):**\n"
        "Tour locale con visite a Faro Svortuloft, Saxholl crater, Holaholar, Djupalonssandur, Londrangar, "
        "Arnarstapi, Budakirkja, Ytri Tunga e faro di Akranes. Pernottamento al Moar guesthouse."
    ),
    "8": (
        "**Giorno 8 (26/04/2025):**\n"
        "Partenza per Fagradalsfjall. Visita a terme Hvammsvik, alla cascata Glymur e al relitto Beached Whalers "
        "vicino a Reykjavík. Pernottamento a Guesthouse Maximilian a Keflavik."
    ),
    "9": (
        "**Giorno 9 (27/04/2025):**\n"
        "Ultima giornata in Islanda: consegna dell'auto, imbarco bagagli e partenza per il volo di ritorno a Milano Berlusconi."
    )
}

# Mappatura di alcune città a coordinate (latitudine, longitudine)
PREDEFINED_COORDINATES = {
    "reykjavik": (64.1466, -21.9426)
}

def get_coordinates(city: str):
    """
    Restituisce le coordinate (latitudine, longitudine) per la città richiesta.
    Se la città è definita in PREDEFINED_COORDINATES, le usa direttamente;
    altrimenti, utilizza l'API di geocoding di Open-Meteo.
    """
    key = city.lower()
    if key in PREDEFINED_COORDINATES:
        return PREDEFINED_COORDINATES[key]
    
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                result = data["results"][0]
                return (result["latitude"], result["longitude"])
    except Exception as e:
        logger.error("Errore durante il geocoding per %s: %s", city, e)
    return PREDEFINED_COORDINATES["reykjavik"]

def map_weather_code(code: int) -> str:
    """
    Mappa il codice meteo di Open-Meteo a una descrizione testuale.
    """
    weather_code_mapping = {
        0: "Cielo sereno",
        1: "Cielo per lo più sereno",
        2: "Parzialmente nuvoloso",
        3: "Nuvoloso",
        45: "Nebbia",
        48: "Nebbia con brina",
        51: "Lieve pioggia",
        53: "Pioggia moderata",
        55: "Pioggia intensa",
        56: "Pioggia ghiacciata leggera",
        57: "Pioggia ghiacciata intensa",
        61: "Lieve pioggia",
        63: "Pioggia moderata",
        65: "Pioggia intensa",
        66: "Pioggia ghiacciata leggera",
        67: "Pioggia ghiacciata intensa",
        71: "Lieve nevicata",
        73: "Nevicata moderata",
        75: "Nevicata intensa",
        77: "Granelli di neve",
        80: "Rovesci leggeri di pioggia",
        81: "Rovesci moderati di pioggia",
        82: "Rovesci intensi di pioggia",
        85: "Leggera sciarpa nevosa",
        86: "Sciarpa nevosa intensa",
        95: "Temporale leggero",
        96: "Temporale con grandine leggera",
        99: "Temporale con grandine intensa"
    }
    return weather_code_mapping.get(code, f"Codice meteo {code}")

def get_weather_forecast(city: str = "Reykjavik") -> str:
    """
    Recupera le condizioni meteo correnti dalla API di Open-Meteo per la città specificata.
    """
    lat, lon = get_coordinates(city)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "current_weather" in data:
                current = data["current_weather"]
                temp = current.get("temperature")
                windspeed = current.get("windspeed")
                winddirection = current.get("winddirection")
                weathercode = current.get("weathercode")
                description = map_weather_code(weathercode)
                forecast_text = (
                    f"Condizioni meteo per {city}:\n"
                    f"Temperatura: {temp}°C\n"
                    f"Vento: {windspeed} km/h (direzione {winddirection}°)\n"
                    f"Condizioni: {description}"
                )
                return forecast_text
            else:
                return "Nessun dato meteo disponibile al momento."
        else:
            return "Impossibile ottenere il meteo per la località richiesta."
    except Exception as e:
        logger.error("Errore durante il recupero del meteo: %s", e)
        return "Si è verificato un errore nel recupero del meteo."

def get_volcano_status() -> str:
    """
    Simula il recupero dello status vulcanico.
    """
    status_list = [
        "Nessuna attività vulcanica significativa rilevata al momento.",
        "Attività vulcanica in lieve aumento nelle regioni orientali.",
        "Attenzione: possibili eruzioni minori, controlla gli aggiornamenti!"
    ]
    status = random.choice(status_list)
    return f"Stato vulcanico: {status}"

# Comandi del Bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /start: messaggio di benvenuto.
    """
    welcome_text = (
        "Ciao! Sono il bot del viaggio in Islanda 😎.\n\n"
        "Per conoscere tutte le funzionalità, usa il comando /help."
    )
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /help: mostra le funzionalità disponibili.
    """
    help_text = (
        "Ecco cosa posso fare per te:\n\n"
        "/start - Avvia il bot e mostra il messaggio di benvenuto.\n"
        "/help - Mostra questo messaggio di aiuto.\n"
        "/piano <numero_giorno> - Visualizza il piano del giorno specifico (es.: /piano 1).\n"
        "/weather <città> - Mostra le previsioni meteo per la città richiesta (default: Reykjavik).\n"
        "/volcano - Controlla lo stato vulcanico attuale.\n"
        "/curiosita - Ricevi una curiosità divertente del giorno."
    )
    await update.message.reply_text(help_text)

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
    
    await update.message.reply_text(reply_text)

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
    await update.message.reply_text(forecast)

async def volcano(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /volcano: restituisce lo stato vulcanico attuale.
    """
    status = get_volcano_status()
    await update.message.reply_text(status)

async def curiosita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /curiosita: invia una curiosità divertente del giorno.
    """
    curiosities = [
        "Lo sapevi che in Islanda il sole di mezzanotte può riscaldare anche il cuore più freddo?",
        "Le eruzioni vulcaniche in Islanda sono quasi come concerti rock della natura!",
        "Il vento in Islanda sembra sussurrare antiche leggende… e magari qualche segreto!"
    ]
    reply = random.choice(curiosities)
    await update.message.reply_text(f"🌋 Curiosità del giorno: {reply}")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Gestisce comandi sconosciuti.
    """
    await update.message.reply_text("Comando non riconosciuto. Usa /help per vedere i comandi disponibili.")

def main() -> None:
    """
    Funzione principale per avviare il bot.
    Sostituisci 'YOUR_TELEGRAM_BOT_TOKEN' con il token fornito da BotFather.
    """

    # lettura token da file json separato
    with open('token.json', 'r') as file:
        token = json.load(file).get('token')
    if not token:   
        raise ValueError("Token non trovato nel file token.json")
    
    # Crea l'istanza dell'applicazione Telegram
    application = Application.builder().token(token).build()

    # Aggiunge gli handler per i comandi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("piano", piano))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("volcano", volcano))
    application.add_handler(CommandHandler("curiosita", curiosita))
    
    # Handler per comandi sconosciuti
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    logger.info("Bot in esecuzione...")
    application.run_polling()

if __name__ == "__main__":
    main()
