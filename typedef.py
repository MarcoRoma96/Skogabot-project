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