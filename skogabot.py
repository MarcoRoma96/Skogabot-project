import os
import random
import datetime
import json
from collections import Counter
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ConversationHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

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
    global HELP
    """
    Comando /help: mostra le funzionalità disponibili.
    """
    if len(context.args) == 0:
        text = HELP["general"]
    else:
        try:
            text = HELP[context.args[0]]
        except Exception as e:
            text = "Errore! Non riesco a capire cosa tu mi stia chiedendo, riprova. Help me to help you!"
    await update.message.reply_text(text)


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


async def nanna(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /nanna: restituisce le info per la notte per il giorno selezionato (o il giorno attuale).
    """
    try:
        if not context.args:
            day = datetime.datetime.now().day - 18
        else:
            day = int(context.args[0])

        if day < 1 or day > 9:
            status = "Non sei ancora in viaggio o hai scelto un giorno non valido! Dormi a casa tua!😴"
        else:
            status = SLEEPING_PLACES.get(str(day))

    except ValueError as ve:
        status = "Stai cercando di fare dei danni 😡"

    await update.message.reply_text(status, parse_mode='markdown')


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


async def ahah(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Comando /curiosita: invia una curiosità divertente del giorno.
    """
    reply = random.choice(BATTUTE_CRINGINE_DI_CHATGPT)
    await update.message.reply_text(f"{reply}", parse_mode='markdown')


async def giocatori(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global NUM_GIOCATORI
    if len(context.args) == 0:
        reply = "I giocatori sono: " + str(NUM_GIOCATORI) + "\n"
    else:
        try:
            n = int(context.args[0])
        except Exception as e:
            reply = "Errore! Non riesco a leggere il numero che hai inserito.\n"
        NUM_GIOCATORI = n
        reply = "Numero di giocatori modificato in: " + str(NUM_GIOCATORI) + "\n"
    await update.message.reply_text(f"{reply}", parse_mode='markdown')


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


async def car1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global VOTI_GIOCHINO_AUTO1
    if len(context.args) > 0:
        if context.args[0].startswith("stat"):
            # Mostra statistiche
            stats_text = "Statistiche del gioco:\n"
            for player, score in PUNTEGGI_STUPIDINI1.items():
                stats_text += f"🥇 {player}: {score} punti\n"
            await update.message.reply_text(stats_text)
        elif context.args[0] == "reset":
            for k in PUNTEGGI_STUPIDINI1.keys():
                PUNTEGGI_STUPIDINI1[k] = 0
    else:
        domanda = random.choice(CARGAMES_STUPIDINI_DI_CHATGPT)
        VOTI_GIOCHINO_AUTO1 = {}  # Reset: necessario?
        # Bottoni per la risposta
        keyboard = [
            [InlineKeyboardButton("AleB", callback_data="cargame1_AleB"),
             InlineKeyboardButton("AleD", callback_data="cargame1_AleD"),
             InlineKeyboardButton("Bianca",    callback_data="cargame1_B")
             ],
            [InlineKeyboardButton("Dalia",    callback_data="cargame1_D"),
             InlineKeyboardButton("Filippo",    callback_data="cargame1_F"),
             InlineKeyboardButton("Marco2",   callback_data="cargame1_MG")
             ],
            [InlineKeyboardButton("MR",   callback_data="cargame1_MR"),
             InlineKeyboardButton("Viola",    callback_data="cargame1_V")
             ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Invia la domanda e i bottoni
        await update.message.reply_text(f"{domanda}\n", reply_markup=reply_markup)


async def car1_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global VOTI_GIOCHINO_AUTO1
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    user_id = query.from_user.id

    if user_id in VOTI_GIOCHINO_AUTO1:
        await query.answer("Hai già votato! " + str(VOTI_GIOCHINO_AUTO1[user_id]), show_alert=True)
        return
    VOTI_GIOCHINO_AUTO1[user_id] = query.data.split('_')[1]

    # Controlla se tutti hanno votato
    total_members = await context.bot.get_chat_member_count(chat_id)
    total_users = total_members - 1
    if len(VOTI_GIOCHINO_AUTO1) >= min([NUM_GIOCATORI, total_users]):
        order = Counter(VOTI_GIOCHINO_AUTO1.values()).most_common(8)
        max = -1
        winner = []
        for el in order:
            if el[1] >= max:
                winner.append(el)
                max = el[1]
        reply = "Congratulazioni a: \n"
        for w in winner:
            reply += "🥇 " + str(w[0]) + " (" + str(w[1]) + " punti)\n"
            PUNTEGGI_STUPIDINI1[w[0]] += 1
        await context.bot.send_message(chat_id, reply)


async def car2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global VOTI_GIOCHINO_AUTO2
    VOTI_GIOCHINO_AUTO2 = {}
    domanda = random.choice(LO_SAI_CHE)
    protagonista = random.choice(NOMI_VIAGGIATORI)
    # Bottoni per la risposta
    keyboard = [
        [InlineKeyboardButton("0%",     callback_data="cargame2_0"),
         InlineKeyboardButton("20%",    callback_data="cargame2_20"),
         InlineKeyboardButton("40%",    callback_data="cargame2_40"),
         InlineKeyboardButton("60%",    callback_data="cargame2_60"),
         InlineKeyboardButton("80%",    callback_data="cargame2_80"),
         InlineKeyboardButton("100%",   callback_data="cargame2_100")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Invia la domanda e i bottoni
    domanda = domanda.replace("[NOME]", protagonista)
    await update.message.reply_text(f"{domanda}\n", reply_markup=reply_markup)


async def car2_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    user_id = query.from_user.id

    VOTI_GIOCHINO_AUTO2[user_id] = query.data.split('_')[1]

    total_members = await context.bot.get_chat_member_count(chat_id)
    total_users = total_members - 1
    if len(VOTI_GIOCHINO_AUTO2) >= min([NUM_GIOCATORI, total_users]):
        sum = 0
        for el in VOTI_GIOCHINO_AUTO2.values():
            sum += int(el)
        reply = "Congratulazioni!💥\nSecondo i tuoi amici, rispecchi questa frase al " + \
            str(sum) + "%!\n"
        await context.bot.send_message(chat_id, reply)


async def car3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global VOTI_GIOCHINO_AUTO3, USER_SEGRETO3
    if len(context.args) > 0:
        if context.args[0].startswith("stat"):
            # Mostra statistiche
            stats_text = "Statistiche del gioco:\n"
            for player, score in PUNTEGGI_STUPIDINI3.items():
                stats_text += f"🥇 {player}: {score} punti\n"
            await update.message.reply_text(stats_text)
        elif context.args[0] == "reset":
            for k in PUNTEGGI_STUPIDINI3.keys():
                PUNTEGGI_STUPIDINI3[k] = 0
        else:
            segreto = ' '.join(context.args)
            USER_SEGRETO3 = update.message.from_user.name[-2:]
            VOTI_GIOCHINO_AUTO3 = {}  # Reset: necessario?
            # Bottoni per la risposta
            keyboard = [
                [InlineKeyboardButton("Vero", callback_data="cargame3_vero"),
                 InlineKeyboardButton("Falso", callback_data="cargame3_falso"),
                 ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            # Invia la domanda e i bottoni
            await update.message.reply_text(f"Interessante! Voi che ne dite? Vero o Falso?\n", reply_markup=reply_markup)
    else:
        await update.message.reply_text(f"Errore! Indica un segreto🤫\n")


async def car3_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global VOTI_GIOCHINO_AUTO3
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    user_id = query.from_user.id
    user_code = query.from_user.name[-2:]

    if user_id in VOTI_GIOCHINO_AUTO3:
        await query.answer("Hai già votato! " + str(VOTI_GIOCHINO_AUTO3[user_id]), show_alert=True)
        return
    VOTI_GIOCHINO_AUTO3[user_code] = query.data.split('_')[1]

    total_members = await context.bot.get_chat_member_count(chat_id)
    total_users = total_members - 1
    giocatori = min([NUM_GIOCATORI, total_users])
    if len(VOTI_GIOCHINO_AUTO3) == giocatori:
        t = 0
        f = 0
        for el in VOTI_GIOCHINO_AUTO3.values():
            if el == "vero":
                t += 1
            else:
                f += 1
        sol = VOTI_GIOCHINO_AUTO3[USER_SEGRETO3]

        if sol == "vero" and (t-1) > f:
            reply = "Congratulazioni! Il segreto era vero!\n" + \
                str(t-1) + " persone hanno indovinato!\n"
            for u, r in VOTI_GIOCHINO_AUTO3.items():
                if r == "vero" and u != USER_SEGRETO3:
                    PUNTEGGI_STUPIDINI3[CONV[u]] += 1
            if t == giocatori:
                reply += "Tutti hanno indovinato! Il segreto era troppo facile, " + str(giocatori) + " punti verranno decrementati al sussurratore di segreti."
                PUNTEGGI_STUPIDINI3[USER_SEGRETO3] -= giocatori
        elif sol == "vero" and (t-1) < f:
            reply = "Oh no! Il segreto era vero ma non ci avete creduto! In " + \
                str(f) + " avete sbagliato."
            PUNTEGGI_STUPIDINI3[CONV[USER_SEGRETO3]] += f
        elif sol == "vero" and (t-1) == f:
            reply = "Nessuna maggioranza! Nessun punto da assegnare."
        elif sol == "falso" and (f-1) > t:
            reply = "Congratulazioni! Il segreto era Falso!\n" + \
                str(f-1) + " persone hanno indovinato!\n"
            for u, r in VOTI_GIOCHINO_AUTO3.items():
                if r == "falso" and u != USER_SEGRETO3:
                    PUNTEGGI_STUPIDINI3[CONV[u]] += 1
            if f == giocatori:
                reply += "Tutti hanno indovinato! Il segreto era troppo facile, " + str(giocatori) + " punti verranno decrementati al sussurratore di segreti."
                PUNTEGGI_STUPIDINI3[USER_SEGRETO3] -= giocatori
        elif sol == "falso" and (f-1) < t:
            reply = "Oh no! Il segreto era falso e ci siete cascati! In " + \
                str(t) + " avete sbagliato."
            PUNTEGGI_STUPIDINI3[CONV[USER_SEGRETO3]] += t
        elif sol == "falso" and (f-1) == t:
            reply = "Nessuna maggioranza! Nessun punto da assegnare."
        await context.bot.send_message(chat_id, reply)


async def fanta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global PUNTEGGI_STUPIDINI_FANTA, FANTA_DICT_BONUS, FANTA_DICT_MALUS, FANTA_USER_CHOSEN, FANTA_EVENT_CHOSEN
    if len(context.args) > 0:
        if context.args[0].startswith("stat"):
            # Mostra statistiche
            stats_text = "Statistiche del gioco:\n"
            for player, score_list in PUNTEGGI_STUPIDINI_FANTA.items():
                score = sum(score_list)
                stats_text += f"🥇 {player}: {score} punti\n"
            await update.message.reply_text(stats_text)
        elif context.args[0] == "reset":
            if len(context.args) <= 1:
                await update.message.reply_text(f"Manca un parametro! Se vuoi annullare un evento del FantaIslanda usa la sintassi: /fanta reset [nome_utente] [numero_evento]\n")
            elif context.args[1] == "all":
                # Reset tutto
                for k in PUNTEGGI_STUPIDINI_FANTA.keys():
                    PUNTEGGI_STUPIDINI_FANTA[k] = [0] * (100 + len(FANTA_DICT_MALUS))
            else:
                # Reset [user] [key]
                user = context.args[1]
                try:
                    key = int(context.args[2])
                    PUNTEGGI_STUPIDINI_FANTA[user][key] = 0
                    await update.message.reply_text(f"Rimossi punti assegnati a {user} per {key}\n")
                except Exception as e:
                    await update.message.reply_text(f"Errore! Se vuoi annullare un evento del FantaIslanda usa la sintassi: /fanta reset [nome_utente] [numero_evento]\n")
        elif context.args[0] == "show":
            text = "Ecco tutti i Bonus e i Malus!\n"
            text += "\n------ Bonus ------\n"
            for item in list(FANTA_DICT_BONUS.items()):
                text += str(item[0]) + ": " + item[1][0]
                text += ' - Punti: ' + str(item[1][1]) + '\n'
            text += "\n------ Malus ------\n"
            for item in list(FANTA_DICT_MALUS.items()):
                text += str(item[0]) + ": " + item[1][0]
                text += ' - Punti: ' + str(item[1][1]) + '\n'
            await update.message.reply_text(text)
        elif context.args[0] == "add":
            e = ' '.join(context.args[1:-1])
            p = int(context.args[-1])
            if p > 0:
                for i in range(100):
                    try:
                        item = FANTA_DICT_BONUS[i]
                    except KeyError:
                        FANTA_DICT_BONUS[i] = [e, p]
                        break
                # FANTA_DICT_BONUS[max(FANTA_DICT_BONUS.keys()) + 1] = [e, p]
                text = "Bonus '" + str(e) + "' aggiunto con " + str(p) + " punti!\n"
            else:
                for i in range(100, 200):
                    try:
                        item = FANTA_DICT_MALUS[i]
                    except KeyError:
                        FANTA_DICT_MALUS[i] = [e, p]
                        break
                # FANTA_DICT_MALUS[max(FANTA_DICT_MALUS.keys()) + 1] = [e, p]
                text = "Malus '" + str(e) + "' aggiunto con " + str(p) + " punti!\n"
                for k in PUNTEGGI_STUPIDINI_FANTA.keys():
                    PUNTEGGI_STUPIDINI_FANTA[k].append(0)
            await update.message.reply_text(text)
        elif context.args[0] == "del":
            if len(context.args) == 1:
                await update.message.reply_text("Errore! Specifica la chiave dell'evento da cancellare!\n")
            else:
                e = int(context.args[1])
                try:
                    if e < 100:
                        FANTA_DICT_BONUS.pop(e)
                    else:
                        FANTA_DICT_MALUS.pop(e)
                except Exception as e:
                    await update.message.reply_text("Errore! Non riesco a cancellare l'evento " + str(e) + "\n")
                # Reset punteggi giocatori: se l'evento è tolto, i punti dell'evento sono cancellati
                for k in PUNTEGGI_STUPIDINI_FANTA.keys():
                    PUNTEGGI_STUPIDINI_FANTA[k][e] = 0
                # Slittamento tutti gli altri eventi indietro di 1, a partire dall'evento tolto
                # for item in FANTA_DICT_BONUS.items():
                #     if item[0] > e:
                #         FANTA_DICT_BONUS[item[0]-1] = [item[1][0], int(item[1][1])]
                # for item in FANTA_DICT_MALUS.items():
                #     if item[0] > e:
                #         FANTA_DICT_MALUS[item[0]-1] = [item[1][0], int(item[1][1])]
                # for item in PUNTEGGI_STUPIDINI_FANTA.keys():
                #     PUNTEGGI_STUPIDINI_FANTA[item] = PUNTEGGI_STUPIDINI_FANTA[item][:e]+PUNTEGGI_STUPIDINI_FANTA[item][e-1:]
                await update.message.reply_text("Evento " + str(e) + " cancellato!\n")
        else:
            await update.message.reply_text(f"Non so cosa tu mi stia chiedendo!\n")
    else:
        # Scelta 1: Quale persona?
        keyboard = [
            [InlineKeyboardButton("AleB", callback_data="fanta1_AleB"),
             InlineKeyboardButton("AleD", callback_data="fanta1_AleD"),
             InlineKeyboardButton("Bianca",    callback_data="fanta1_B")
             ],
            [InlineKeyboardButton("Dalia",    callback_data="fanta1_D"),
             InlineKeyboardButton("Filippo",    callback_data="fanta1_F"),
             InlineKeyboardButton("Marco2",   callback_data="fanta1_MG")
             ],
            [InlineKeyboardButton("MR",   callback_data="fanta1_MR"),
             InlineKeyboardButton("Viola",    callback_data="fanta1_V")
             ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(f"A quale persona vuoi aggiungere un Fanta Bonus o un Fanta Malus?\n", reply_markup=reply_markup)
        return fanta_1


async def fanta_callback1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global FANTA_USER_CHOSEN
    query = update.callback_query
    await query.answer()

    FANTA_USER_CHOSEN = query.data.split('_')[1]

    # Scelta 2: Quale evento?
    keyboard = [[InlineKeyboardButton(
        item[1][0], callback_data="fanta2_" + str(item[0]))] for item in (list(FANTA_DICT_BONUS.items())+list(FANTA_DICT_MALUS.items()))]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(f"Quale Fanta Bonus o Fanta Malus vuoi aggiungere a " + FANTA_USER_CHOSEN + "?\n", reply_markup=reply_markup)
    return fanta_2


async def fanta_callback2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global FANTA_DICT, FANTA_EVENT_CHOSEN
    query = update.callback_query
    await query.answer()

    k = int(query.data.split('_')[1])
    if k < 100:
        FANTA_EVENT_CHOSEN = (k, FANTA_DICT_BONUS[k])
    else:
        FANTA_EVENT_CHOSEN = (k, FANTA_DICT_MALUS[k])
    # Notifica inserimento
    PUNTEGGI_STUPIDINI_FANTA[FANTA_USER_CHOSEN][FANTA_EVENT_CHOSEN[0]
                                                ] = FANTA_EVENT_CHOSEN[1][1]
    await query.edit_message_text("Fanta Evento '" + str(FANTA_EVENT_CHOSEN[1][0]) + "' aggiunto a " + FANTA_USER_CHOSEN + "!\nPunti evento: " + str(FANTA_EVENT_CHOSEN[1][1]) + "\n", parse_mode='markdown')
    return ConversationHandler.END


async def leggi_storia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = []
    for story_id, story in STORIES.items():
        keyboard.append([InlineKeyboardButton(
            story["title"], callback_data=f"select_{story_id}_0")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Scegli la storia che vuoi ascoltare:", reply_markup=reply_markup)


async def story_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Il callback_data è strutturato così: "select_<story_id>_<page_number>" o "page_<story_id>_<page_number>"
    data = query.data.split('_')
    if len(data) < 3:
        return
    mode, story_id, page_str = data[0], data[1], data[2]
    page_number = int(page_str)

    # Verifica che la storia esista
    if story_id not in STORIES:
        await query.edit_message_text("Storia non trovata.")
        return

    story = STORIES[story_id]
    pages = story["pages"]
    total_pages = len(pages)

    # Costruisci il testo e l'immagine per la "slide"
    text = f"*{story['title']}* (Pagina {page_number+1}/{total_pages})\n\n"
    text += pages[page_number]

    # Se abbiamo un'immagine per la pagina (opzionale)
    image_path = None
    if "images" in story and len(story["images"]) > page_number:
        image_path = story["images"][page_number]

    # Costruisci i pulsanti per navigare
    buttons = []
    if page_number > 0:
        buttons.append(InlineKeyboardButton(
            "◀ Indietro", callback_data=f"select_{story_id}_{page_number-1}"))
    if page_number < total_pages - 1:
        buttons.append(InlineKeyboardButton(
            "Avanti ▶", callback_data=f"select_{story_id}_{page_number+1}"))
    reply_markup = InlineKeyboardMarkup([buttons])

    # Modifica il messaggio in base alla presenza dell'immagine:
    if image_path:
        with open(image_path, 'rb') as img:
            # Se si vuole usare un media group, è necessario usare l'editMessageMedia che accetta InputMediaPhoto.
            new_media = InputMediaPhoto(
                media=img, caption=text, parse_mode="Markdown")
        try:
            await query.edit_message_media(new_media, reply_markup=reply_markup)
        except Exception as e:
            logger.error("Errore nell'edit della media: %s", e)
            # Se l'edit non funziona, manda un nuovo messaggio
            await query.message.reply_photo(photo=image_path, caption=text, parse_mode="Markdown", reply_markup=reply_markup)
    else:
        await query.edit_message_text(text=text, parse_mode="Markdown", reply_markup=reply_markup)


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
    application.add_handler(CommandHandler("nanna", nanna))
    application.add_handler(CommandHandler("cacca", cacca))
    application.add_handler(CommandHandler("meteo", weather))
    application.add_handler(CommandHandler("vulcano", volcano))
    application.add_handler(CommandHandler("curiosita", curiosita))
    application.add_handler(CommandHandler("ahah", ahah))
    application.add_handler(CommandHandler("giocatori", giocatori))
    application.add_handler(CommandHandler("car1", car1))
    application.add_handler(CallbackQueryHandler(
        car1_callback, pattern=r"^(cargame1_).*"))
    application.add_handler(CommandHandler("car2", car2))
    application.add_handler(CallbackQueryHandler(
        car2_callback, pattern=r"^(cargame2_).*"))
    application.add_handler(CommandHandler("car3", car3))
    application.add_handler(CallbackQueryHandler(
        car3_callback, pattern=r"^(cargame3_).*"))
    application.add_handler(ConversationHandler(entry_points=[CommandHandler("fanta", fanta)],
                            states={
        fanta_1: [CallbackQueryHandler(fanta_callback1, pattern="^fanta1_")],
        fanta_2: [CallbackQueryHandler(fanta_callback2, pattern="^fanta2_")],
    },
        fallbacks=[CommandHandler("unknown", unknown)]))
    application.add_handler(CommandHandler(
        "ricetta", subscribe_recipe))
    application.add_handler(CommandHandler("storia", leggi_storia))
    application.add_handler(CallbackQueryHandler(
        story_callback, pattern=r"^(select_).*"))

    # Handler per comandi sconosciuti
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    logger.info("Bot in esecuzione...")
    application.run_polling()


if __name__ == "__main__":
    main()
