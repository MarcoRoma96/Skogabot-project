import os
import logging
import random
import requests
import datetime
import json
from telegram import Update
from dotenv import load_dotenv
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
        "Happy Birthday!🐋"
        "Ultima giornata in Islanda: consegna dell'auto, auguri di compleanno, imbarco bagagli e partenza per il volo di ritorno a Milano Berlusconi."
    )
}

CALENDARIO_CACCA = {
    "1": "19/04 🟡 - Solo in caso di emergenza!💩",
    "2": "20/04 🔴 - No no no!💩",
    "3": "21/04 🟢 - Via liberaaa💩",
    "4": "22/04 🟢 - Corri che il bagno è libero!💩",
    "5": "23/04 🟢 - Libera tutto oggi, che domani c'è il bollino rosso💩",
    "6": "24/04 🔴 - Niente bagno oggi!💩",
    "7": "25/04 🟢 - Vai vai vaii💩",
    "8": "26/04 🔴 - Viva la stitichezza💩",
    "9": "27/04 🔴 - Solo Bianca è autorizzata oggi, per prepararsi al viaggio💩",
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
        0: "Cielo sereno (si va beh ma impossibile)",
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
        85: "Leggera sciarpa nevosa🧣",
        86: "Sciarpa nevosa intensa🧣",
        95: "Temporale leggero",
        96: "Temporale con grandine leggera",
        99: "Temporale con grandine intensa"
    }
    return weather_code_mapping.get(code, f"Codice meteo {code}")

def get_weather_forecast(city: str = "Reykjavik") -> str:
    """
    Recupera le condizioni meteo correnti dalla API di Open-Meteo per la città specificata.
    """
    if city.endswith("goro"):
        return ("ah-ah so funny")
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
        "/start              - Avvia il bot e mostra il messaggio di benvenuto.\n"
        "/help               - Mostra questo messaggio di aiuto.\n"
        "/piano <num_giorno> - Visualizza il piano del giorno specifico (es.: /piano 1).\n"
        "/cacca <num_giorno> - Visualizza il calendario Cacca.\n"
        "/weather <città>    - Mostra le previsioni meteo per la città richiesta (default: Reykjavik).\n"
        "/volcano            - Controlla lo stato vulcanico attuale.\n"
        "/curiosita          - Ricevi una curiosità divertente del giorno."
        "/subscribe          - Iscriviti per ricevere automaticamente le ricette del giorno (dal 19/04 al 27/04).\n"
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

    await update.message.reply_text(status)

async def curiosita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /curiosita: invia una curiosità divertente del giorno.
    """
    curiosities = [
        "Lo sapevi che in Islanda il sole di mezzanotte può riscaldare anche il cuore più freddo?",
        "Le eruzioni vulcaniche in Islanda sono quasi come concerti rock della natura!",
        "Il vento in Islanda sembra sussurrare antiche leggende… e magari qualche segreto!",
        "🌋 L’Islanda è giovane... geologicamente parlando. È uno dei territori più giovani del pianeta, nato circa 16-18 milioni di anni fa grazie all’attività vulcanica. E ancora oggi, ha circa 130 vulcani attivi!",
        "💡 Energia al 100% rinnovabile. L’Islanda produce quasi tutta la sua energia da fonti rinnovabili: geotermica e idroelettrica. È uno dei paesi più “green” al mondo.",
        "🧊 Non ci sono zanzare! Sì, hai letto bene. In Islanda non vivono zanzare. Nessuno è del tutto sicuro del motivo, ma si pensa che sia dovuto al clima e ai cicli di congelamento/scongelamento del suolo.",
        "📬 Puoi spedire una lettera anche se non conosci l’indirizzo. In Islanda è successo davvero: una lettera con una mappa disegnata al posto dell’indirizzo è arrivata a destinazione. Le persone sono poche, quindi… ci si conosce un po’ tutti!",
        "❄️ Hanno una parola solo per 'neve portata dal vento'. La lingua islandese è piena di parole poetiche: ad esempio, “snjófoka” indica la neve che il vento spazza via.",
        "👶 I nomi sono regolati dal governo. In Islanda esiste un Comitato per i Nomi che approva o rifiuta i nuovi nomi dati ai bambini, per assicurarsi che siano compatibili con la grammatica islandese.",
        "📖 Il Natale è magico e un po’ strano. Invece di Babbo Natale, ci sono 13 Jólasveinar (gli “Yule Lads”), ognuno con un comportamento bizzarro — come rubare cibo o spiare i bambini. Compaiono uno alla volta, dal 12 dicembre fino a Natale."
    ]
    reply = random.choice(curiosities)
    await update.message.reply_text(f"🌋 Curiosità del giorno: {reply}")



# Lista di 20 ricette islandesi (le più strane per un italiano)
RECIPES = [
    "1. Hákarl – Carne di squalo fermentata, dal sapore fortemente ammoniacale.",
    "2. Svið – Testa di pecora bollita, con orecchie e pelle.",
    "3. Slátur – Salsiccia di sangue islandese.",
    "4. Súrsaðir hrútspungar – Testicoli di montone fermentati.",
    "5. Harðfiskur – Pesce secco, solitamente eglefino o merluzzo, tradizionale e gustato con burro.",
    "6. Þorramatur – Piatto misto tradizionale servito durante il Þorrablót.",
    "7. Brennivín – Schnapps islandese, detto anche “Black Death”.",
    "8. Rúgbrauð – Pane di segale geotermico, dolce e denso.",
    "9. Kjötsúpa – Zuppa rustica d’agnello islandese.",
    "10. Pylsur – Hot dog islandese con agnello, maiale e manzo.",
    "11. Skyr – Latticino simile a uno yogurt denso, tradizionale e antichissimo.",
    "12. Fiskisúpa islandese – Zuppa di pesce locale ricca di aromi marini.",
    "13. Hvalkjötsúpa – Zuppa di carne di balena (piatto controverso).",
    "14. Hvalhjarta – Fette sottili di cuore di balena.",
    "15. Cozze geotermiche – Cozze cotte sfruttando il calore naturale.",
    "16. Blóðmör – Pudding di sangue d’agnello.",
    "17. Ferszt lamm – Agnello locale servito crudo o poco cotto.",
    "18. Marinated Whale Liver – Fegato di balena marinato con erbe.",
    "19. Súrmjólk – Latte fermentato tradizionale, acidulo ed inusuale.",
    "20. Særsuð fiskur – Pesce sottaceto con tradizione antica."
]

# Indice globale per inviare la ricetta successiva
RECIPE_INDEX = 0

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
    chat_id = context.job.context  # il job context contiene l'ID della chat
    recipe_text = RECIPES[RECIPE_INDEX]
    RECIPE_INDEX += 1
    await context.bot.send_message(chat_id=chat_id, text=f"🍽️ **Ricetta del momento:**\n\n{recipe_text}")

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /subscribe: iscrive la chat corrente per ricevere automaticamente i messaggi programmati
    (ricette a mezzogiorno e alle 19:30 dal 19/04 al 27/04).
    """
    chat_id = update.effective_chat.id
    job_queue = context.job_queue
    # Pianifica il job per mezzogiorno (12:00)
    job_queue.run_daily(scheduled_recipe, time=datetime.time(12, 0), context=chat_id, name=f"recipe_noon_{chat_id}")
    # Pianifica il job per le 19:30
    job_queue.run_daily(scheduled_recipe, time=datetime.time(18, 43), context=chat_id, name=f"recipe_evening_{chat_id}")
    #debug: pianifica tra 1 minuto
    job_queue.run_daily(scheduled_recipe, time=datetime.time(datetime.datetime.now() + datetime.timedelta(minutes=1)), context=chat_id, name=f"recipe_evening_{chat_id}")
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

    raise ValueError(f"Token non trovato. Assicurati che '{file_path}' esista o che la variabile d'ambiente '{env_var}' sia impostata.")

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
    application.add_handler(CommandHandler("subscribe", subscribe))
    
    # Handler per comandi sconosciuti
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    logger.info("Bot in esecuzione...")
    application.run_polling()

if __name__ == "__main__":
    main()
