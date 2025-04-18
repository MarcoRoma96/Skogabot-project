import json
import os
import typedef

SAVE_FILE = "bot_state.json"

# Solo queste variabili verranno salvate e caricate da typedef.py
STATE_VARIABLES = [
    "PUNTEGGI_STUPIDINI1",
    "PUNTEGGI_STUPIDINI3",
    "PUNTEGGI_STUPIDINI_FANTA",
    "FANTA_DICT_BONUS",
    "FANTA_DICT_MALUS",
    "FANTA_USER_CHOSEN",
    "FANTA_EVENT_CHOSEN",
    "RECIPE_INDEX"
]

STATE_VARIABLES1 = [
    typedef.PUNTEGGI_STUPIDINI1,
    typedef.PUNTEGGI_STUPIDINI3,
    typedef.PUNTEGGI_STUPIDINI_FANTA,
    typedef.FANTA_DICT_BONUS,
    typedef.FANTA_DICT_MALUS,
    typedef.FANTA_USER_CHOSEN,
    typedef.FANTA_EVENT_CHOSEN,
    typedef.RECIPE_INDEX
]


def save_state(var=None, varname=None):
    """
    Salva nel file SAVE_FILE tutte le variabili definite in STATE_VARIABLES
    prendendole dal modulo typedef.
    """
    if var is not None:
        save_state_var(var, varname)
        return
    # data = {}
    # for var in STATE_VARIABLES:
    #     if hasattr(typedef, var):
    #         data[var] = getattr(typedef, var)
    # with open(SAVE_FILE, "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=2)
    for n,var in enumerate(STATE_VARIABLES1):
        save_state_var(var, STATE_VARIABLES[n])
    print("Updated state file")

def save_state_var(var, varname):
    """
    Salva nel file SAVE_FILE una singola variabile definita in STATE_VARIABLES
    prendendola dal modulo typedef.
    """

    data = {}
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    data[varname] = var
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_state():
    """
    Carica da SAVE_FILE le variabili in STATE_VARIABLES
    e le imposta nel modulo typedef.
    """
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            for n, (varname, value) in enumerate(data.items()):
                STATE_VARIABLES1[n] = value

