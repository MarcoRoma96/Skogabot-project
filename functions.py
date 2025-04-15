import random
import requests
import logging
import pytz
from typedef import *

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
TIMEZONE = pytz.timezone('Atlantic/Reykjavik')

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

