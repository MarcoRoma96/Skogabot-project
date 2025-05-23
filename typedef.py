# Itinerario statico: messaggi definiti a mano (hard-coded)
import os

# if previous state file exists, then True
PREVIOUS_STATE_FILE_EXISTS = os.path.exists("bot_state.json")
prev_state_dict = {}
# Se il file esiste, carica le variabili di stato
if PREVIOUS_STATE_FILE_EXISTS:
    import json

    with open("bot_state.json", "r", encoding="utf-8") as f:
        prev_state_dict = json.load(f)
            


STATIC_ITINERARY = {
    "1": (
        "*Giorno 1 (19/04/2025):*\n"
        "(19:45 circa) Arrivo a Keflavik, recupero bagagli e noleggio auto. Trasferimento al Downtown Reykjavík Apartments, "
        "cena e visita opzionale a Reykjavík."
        "Link utili della giornata:\n"
        "Rental auto: [Blue Car Rental](https://www.bluecarrental.is/)\n"
        "Mappa per raggiungere il noleggio auto a piedi: (https://www.bluecarrental.is/useful-information/deliveries/office-pick-up/)"
        "Aeroporto - Alloggio (https://maps.app.goo.gl/cThxLUWXpugVaxvS9)"
        "ALLOGGIO: Downtown Reykjavík Apartments - 2 bagni (https://www.booking.com/Share-9J3Xdfu)"
    ),
    "2": (
        "* Giorno 2 (20/04/2025): * \n"
        "Colazione (8:30) e spesa al supermercato (9:00 - 10:00). Partenza per Þingvellir, visita al Parco Nazionale, poi attrazioni come "
        "Haukadalur (famosa vallata con diversi geyser geotermici antichi, sorgenti termali e pozze di fango ribollenti.), "
        "il geyser Strokkur (geyser geotermico molto visitato che erutta ogni 8-10 minuti e raggiunge altezze di 20 metri), "
        "Sorgenti termali di Geysir: famoso geyser che erutta ogni pochi minuti e spara acqua fino a 70 metri in aria.\n"
        "la cascata Gullfoss, cascata iconica, nota per il suo salto a più gradini lungo una curva di 90° del fiume Hvitá, "
        "e Seljalandsfoss, dove i visitatori possono passeggiare dietro questa cascata alta 60 metri, alimentata da un ghiacciaio vulcanico, che precipita da una parete scoscesa."
        "\n Fine giornata con trasferimento alla Countryhouse e cena volendo a Hvolsvöllur, paesino vicino da visitare."
        "Link utili della giornata:\n"
        "Reykjavík - Þingvellir (https://maps.app.goo.gl/bAgQwxKHeedWdTey7) (1h) \n I parcheggi sono a pagamento (500 - 1000 ISK). Il parcheggio P1 ha i servizi igienici"
        "Þingvellir - Haukadalur (https://maps.app.goo.gl/Wn5fdbsN12uCbJ1f)"
        "Strokkur - Gullfoss (https://maps.app.goo.gl/y3GM5UQwJDXW7NPm7) (15 min)"
        "Gullfoss - Seljalandsfoss (https://maps.app.goo.gl/XRwmiWGngp7Xc2fj9) (1h e 45 min)"
        "ALLOGGIO: Countryhouse with great view on Eyjafjallajökull - 1 bagno (https://www.booking.com/Share-EeRs87)"
    ),
    "3": (
        "* Giorno 3 (21/04/2025): * \n"
        "Partenza mattutina (9:30) per Butra, visita a Skógafoss (con pranzo al sacco): suggestive cascate alte 60 metri da una parete rocciosa a strapiombo lungo l'antica linea costiera, dotate di piattaforma panoramica.\n"
        "* Riccardo Consiglia: * lunghezza massima del sentiero porta fino a Skalabrekkufoss passando per altre 2 cascate, andata e ritorno sono sue 7 km, circa 2h15 minuti."
        "Prosegue la giornata con, Sólheimajökull, questo grande ghiacciaio offre escursioni guidate molto apprezzate, in un ambiente sereno e panoramico."
        "Senza escursione, solo per raggiungere il ghiacciaio ci vogliono 20 minuti dal parcheggio (40 minuti a/r)."
        "Raggiungiamo quindi Solheimasandur: resti di un aereo della Marina degli Stati Uniti precipitato nel 1973 senza vittime, abbandonati su una spiaggia di sabbia nera."
        "* Riccardo Consiglia: * da fare a piedi e dista quasi 4km dal parcheggio, da fare in piena spiaggia lavica. Sono circa 40 minuti andare e 40 tornare. Serviranno all’incirca 2 ore a piedi."
        "C’è un bus in alternativa ma dicono che si paga 15-20€\n"
        "Proseguimento verso Dyrhólaey Beach, la spiaggia nera, Promontorio Dyrhólaey. \n Pernottamento all’Hotel Katla e cena in albergo."
        "Link utili della giornata:\n"
        "Butra - Skógafoss (https://maps.app.goo.gl/iaN5ewtDpuStuUhaA) (1h)"
        "Skógafoss - Sólheimajökull (https://maps.app.goo.gl/NuK61z9C8se4gtTS6) (30 min)"
        "Sólheimajökull - Solheimasandur (30 min)"
        "Solheimasandur - Dyrhólaey Beach (40 min)"
        "Dyrhólaey Beach: spiaggia nera (https://maps.app.goo.gl/oZww5kwPNooD19qMA)"
        "ALLOGGIO: Hotel Katla by Keahotels - 3 bagni (https://www.booking.com/Share-HfF8z5)"
    ),
    "4": (
        "* Giorno 4 (22/04/2024): * \n"
        "ORE 8:30!!!!!!!     Dai, veloci a togliere la neve, si parte!\n"
        "Partenza presto per il canyon Fjaðrárgljúfur, Fjaðrárgljúfur: profondo e tortuoso canyon fluviale, risalente a circa 2 milioni di anni fa, con percorso pedonale e viste panoramiche."
        "Dal parcheggio al punto panoramico sono 20 minuti a piedi. \nSegue pranzo. \nTour del ghiacciaio Vatnajökull!"
        "- Se, e dico SOLO sei, dovesse restare del tempo e delle forze in noi, si può tornare un po' indietro e vedere "
        "Svartifoss (Skaftafell): una cascata sottile, alta 20 metri, che precipita al centro di una spettacolare parete tridimensionale di colonne esagonali di basalto."
        "Il percorso dal parcheggio alla cascata sono 30/40 minuti a piedi -"
        "D'obbligo è invece Diamond beach suggestiva spiaggia di sabbia nera, famosa per gli enormi e luccicanti frammenti di iceberg che finiscono sulla riva."
        "Pernottamento presso Höfn Inn Guesthouse. Cena inclusa."
        "Link utili della giornata:\n"
        "Tour del ghiacciaio Vatnajökull"
        "dove ? a che ora ? durata ? costo ?"
        "https://drive.google.com/file/d/1Xh2YAj33JVGERJqaZ47xXH_C1ZQTXlsj/view?usp=drive_link (biglietti)"
        "https://maps.app.goo.gl/SUgBxyny23CFSMax9 (luogo incontro) "
        "[Link al tour] (https://troll.is/ice-caves-in-iceland/ice-cave-tours/crystal-blue-ice-cave/?_gl=1*1b6x4kl*_up*MQ..*_gs*MQ..&gclid=CjwKCAiAyJS7BhBiEiwAyS9uNU3gcTtzSi2U0K60W4xzRLxtnJZHLnEtCtj7xIXyzRKhQ_c-XqckkhoC890QAvD_BwE) 150€"
        "\nALLOGGIO: Höfn Inn Guesthouse - 3 bagni https://www.booking.com/Share-UCSfQO"
    ),
    "5": (
        "* Giorno 5 (23/04/2025): * \n"
        "Sveglia sveglia Skogabimbetti! sono le 8:30 ed è ora di partire, tanta strada Islandese all'orizzonte! \n"
        "Il lungo viaggio di oggi prevede dopo un lungo viaggio in macchina tappe a Hofn con visita al Stuðlagil Canyon: "
        "sentieri, panorami e cascate (Stuðlafoss) attorno a colonne di basalto, con avvistamenti primaverili di oche zamperose che nidificano.\n"
        "Pausetta per il pranzo al sacco, e poi via! fino a Dettifoss, la cascata più potente d'Europa, apparsa nel film 'Prometheus', si trova nel Parco nazionale di Vatnajökull."
        "Si raggiunge dal parcheggio in 15-20 minuti.\n"
        "_Riccardo consiglia:_ Per il lato est prendere la F864. Per il lato ovest prendere la strada 862 per arrivare sul lato ovest. Lato est è più bello se si vuole vedere anche Selfoss, "
        "mentre arrivi di lato a Dettifoss. Lato ovest vedi Dettifoss da davanti ma vedi meno Selfoss. Solitamente viene suggerito il lato est, meno schizzi e si vedono entrambe le cascate.\n"
        "Ci spostiamo in serata a Hverir, luogo geotermico noto per le sue pozze di fango gorgoglianti e le fumarole fumanti che emettono gas solforico (= puzza di marcio). \n C’è anche una grotta con dentro un laghetto in zona: Grjótagjá"
        "Per concludere con un po' di relax, e soprattutto ghiaccione al pipo, per chi ce l'ha, e a tutto il resto ai restanti, tappa a Mývatn Nature Baths, terme a 52 euro a persona.\n"
        "_Riccardo consiglia:_ Porta accappatoio, salvietta e ciabatte per non pagare il supplemento e ovviamente il costume da bagno.\n"
        "Pernottamento al Fosshótel Mývatn, cena al sacco.\n"
        "Link e info utili della giornata:\n"
        "Hofn - Stuðlagil Canyon (240km-310km a seconda della strada) (3h e 45 min)\n"
        "Stuðlagil Canyon - Dettifoss (lato ovest) (https://maps.app.goo.gl/GbGuA2fqbWFskfwE7) (1h e 40 min)\n"
        "Dettifoss - Hverir (40 min di strada)\n"
        "10 minuti per le terme\n"
        "ALLOGGIO: Fosshótel Mývatn - 4 bagni (https://www.booking.com/Share-1fNvUWs)"
        "\n *ATTENZIONE: * \n"
        "Attenzione a tunnel Vaðlaheiðargöng, che si trova sulla Ring Road 1 a pochi chilometri da Akureyri. \n"
        "Questo tunnel consente di saltare la guida sul Monte Víkurskarð, accorciando la strada di circa 16 chilometri. \n"
        "\nIl pedaggio costa 1.500 Isk (circa € 10,30) e si può pagare solamente online sul sito Veggjald.is, in quanto non ci sono caselli o macchinette automatiche prima di entrare nel tunnel. \n"
        "Questa tassa deve essere pagata _entro 24 ore prima_ di passare attraverso il tunnel, oppure _entro 24 ore dopo_ il passaggio."
    ),
    "6": (
        "* Giorno 6 (24/04/2025): * \n"
        "NB: oggi è il Sumardagurinn fyrsti, ossia, secondo la tradizione islandese il primo giorno d’estate e ci sono parate, concerti, feste e barbecue in molte località.\n"
        "Sono le 8:30 ed è tempo di scongelare la Diacia. Il viaggio sarò moooooooooooooooooooolto lungo, ma ci sono un sacco di cose da vedere!\n"
        "Prima tappa indovinate cos'è? EEEESATTO, proprio una cascata: Goðafoss, spettacolare cascata che si getta in un precipizio curvo alto 12 metri, con sentieri che conducono a numerosi punti panoramici."
        "Non le più grandi ma molto belle !\n"
        "Poi ci spostiamo a Akureyri, la capitale del nord, per una passeggiata e un pranzo al sacco. Cosa importantissima, spesa per la cena e per la sopravvivenza.\n"
        "Parte un lungo viaggio in macchina con svariate tappe:\n"
        "Reykjavjafoss (Fosslaug),\nVíðimýri, con piccola deviazione verso l'entroterra, paesino sul mare (spiaggia nera) con chiesa molto caratteristica da visitare (d’inverno è chiusa e non si visita)."
        "C’è supermercato e benzinaio.\n"
        "Berserkjahraun passaggio per strada 59 e 54 in parte non asfaltate, sicuramente un’esperienza avventurosa ma controlla prima le condizioni meteo e la neve!"
        "Qui troviamo anche in Museo dello squalo (si può assaggiare lo squalo).\n"
        "Grundarfoss si raggiunge con circa 1Km di percorso in salita dal parcheggio, potrebbero esserci animali lungo il percorso, ultimo tratto roccioso.\n"
        "Arriviamo infine a Ólafsvík. Pernottamento presso Snæfellsjökull Apartments.\n"
        "Link e info utili della giornata:\n"
        "Grande viaggio in auto in due versioni: "
        "https://maps.app.goo.gl/mZdgd2WB7JDQrb7T8;\n"
        "Versione senza Berserkjahraun, evitiamo la strada non asfaltata: https://maps.app.goo.gl/YtKgoYnrWYzNdEX86\n"
        "In 45 min si raggiunge Goðafoss. Il lungo viaggio con tappe durerà circa 6 ore.\n"
        "ALLOGGIO: Snæfellsjökull Apartments - 1 bagno https://www.booking.com/Share-eIKfZmL, Appartamento con fregatura sicura"
    ),
    "7": (
        "* Giorno 7 (25/04/2025): * \n"
        "Giunti a questo punto pure noi ci siamo stufati di fare i piani fatti per bene quindi vi butterò giù un po' di cose da vedere e voi scegliete.\n"
        "dato che ormai siete in culandia, lw proposte sono:\n"
        "- Tour locale con visite a Faro Svortuloft, e altro faro e spiaggia,\n"
        "- Saxholl crater, \n"
        "- Holaholar, \n"
        "- Djupalonssandur, spiaggia nera\n"
        "- Londrangar, scogliera particolare (chi ha dato ste descrizioni? Degne del miglior 'elmetto tizio'),\n"
        "- Arnarstapi, \n"
        "- Budakirkja, \n"
        "- Ytri Tunga, spiaggia delle foche - BELLISSIMA (tutto evidenziato in verde come se fosse la scelta della vita, boh),\n"
        "- Vecchio faro di Akranes.\n"
        "Pernottamento al [Moar guesthouse](https://www.booking.com/hotel/is/moar-cottage.it.html?aid=318615&label=New_English_EN_IT_26638522465-WTxTFkQr%2AG2pb71kPCiLNQS640819034622%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atidsa-64415224945%3Alp1008297%3Ali%3Adec%3Adm%3Aag26638522465%3Acmp393949585&sid=a1a12e9a8580030012c363ccdb4115a8&dest_id=-2641256;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1727084288;srpvid=947b43a2c84902ce;type=total;ucfs=1&#map_opened-hotel_sidebar_static_map_capla)"
    ),
    "8": (
        "* Giorno 8 (26/04/2025): * \n"
        "Partenza per Fagradalsfjall (https://maps.app.goo.gl/aC3DtUjssqVuYeDZA), circa un'ora di viaggio da Reykjavík. \n"
        "A 30km dall’alloggio ci sono le terme Hvammsvik. In zona c’è anche la cascata Glymur con il lago Hvalvatn.Anche relitto navale Beached Whalers Hvalfjörður."
        "Vedete voi, a me n'me frega 'n cazzo, s'annamo a pià er gelato?\n"
        "oppure cose vicino Reykjavík (che sicuramente la prima sera non gireremo molto) "
        "- Hallgrimskirkja Church (si sale sul campanile),\n"
        "Sun Voyager Sculpture"
        "Harpa Concert Hall,\n"
        "Tjornin Pond,\n"
        "Vecchio porto,\n"
        "Kattakaffihúsið cat cafe,\n"
        "Kirsuberjatréð, un negozio gestito da un collettivo di artisti e designer dove si trovano in vendita tanti oggetti particolari e originali.\n"
        "mercatino delle pulci Kolaportid, dove potrete trovare oggetti usati, d'antiquariato e i maglioni di lana islandesi.\n"
        "Alloggio:\n"
        "Pernottamento a [Guesthouse Maximilian](https://www.booking.com/hotel/is/guesthouse-maximilian.it.html) a Keflavik, con ben 1 bagno.\n"
    ),
    "9": (
        "* Giorno 9 (27/04/2025): * \n"
        "Happy Birthday!🐋"
        "Signori, siamo giunti al termine di questo incredibile viaggio. E' stato un piacere viaggiare con voi, ma ora è tempo di tornare a casa, e questo sarà probabilmente l'ultimo mesaggio con cui vi guiderò in questa avventura.\n"
        "Ultima giornata in Islanda: \n"
        " 7:30: consegna dell'auto, \n"
        " 8:00: Veloci, in aeroporto con imbarco bagagli\n"
        "10:00: Partenza con il volo di ritorno a Milano Berlusconi (Italia).\n"
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


curiosities = [
    "Lo sapevi che in Islanda il sole di mezzanotte può riscaldare anche il cuore più freddo?",
    "Le eruzioni vulcaniche in Islanda sono quasi come concerti rock della natura!",
    "Il vento in Islanda sembra sussurrare antiche leggende… e magari qualche segreto!",
    "🌋 L’Islanda è giovane... geologicamente parlando. È uno dei territori più giovani del pianeta, nato circa 16-18 milioni di anni fa grazie all’attività vulcanica. E ancora oggi, ha circa 130 vulcani attivi!",
    "💡 Energia al 100% rinnovabile. L’Islanda produce quasi tutta la sua energia da fonti rinnovabili: geotermica e idroelettrica. È uno dei paesi più 'green' del mondo.",
    "🧊 Non ci sono zanzare! Sì, hai letto bene. In Islanda non vivono zanzare. Nessuno è del tutto sicuro del motivo, ma si pensa che sia dovuto al clima e ai cicli di congelamento/scongelamento del suolo.",
    "📬 Puoi spedire una lettera anche se non conosci l’indirizzo. In Islanda è successo davvero: una lettera con una mappa disegnata al posto dell’indirizzo è arrivata a destinazione. Le persone sono poche, quindi… ci si conosce un po’ tutti!",
    "❄️ Hanno una parola solo per 'neve portata dal vento'. La lingua islandese è piena di parole poetiche: ad esempio, 'snjófoka' indica la neve che il vento spazza via.",
    "👶 I nomi sono regolati dal governo. In Islanda esiste un Comitato per i Nomi che approva o rifiuta i nuovi nomi dati ai bambini, per assicurarsi che siano compatibili con la grammatica islandese.",
    "📖 Il Natale è magico e un po’ strano. Invece di Babbo Natale, ci sono 13 Jólasveinar (gli 'Yule Lads') ognuno con un comportamento bizzarro — come rubare cibo o spiare i bambini. Compaiono uno alla volta, dal 12 dicembre fino a Natale."
]

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

# Indice globale per inviare la ricetta successiva
RECIPE_INDEX = prev_state_dict["RECIPE_INDEX"] if PREVIOUS_STATE_FILE_EXISTS and "RECIPE_INDEX" in prev_state_dict else 0

SLEEPING_PLACES = {
    "1": "https://www.booking.com/Share-kCiEwO - https://maps.app.goo.gl/MLYAZZLjycgMxsv18",
    "2": "https://www.booking.com/Share-EeRs87 - https://maps.app.goo.gl/fFd5VSjMVdMLxxFHA",
    "3": "https://www.booking.com/Share-HfF8z5 - https://maps.app.goo.gl/RS6QNrwwNAWafpCD8",
    "4": "https://www.booking.com/Share-UCSfQO - https://maps.app.goo.gl/6zZ6vqPGH7UA3SHg7",
    "5": "https://www.booking.com/Share-1fNvUWs - https://maps.app.goo.gl/UVAoCZ3vgUwy7csGA",
    "6": "https://www.booking.com/Share-eIKfZmL - https://maps.app.goo.gl/vpJijwQESn1izMZ96",
    "7": " - https://maps.app.goo.gl/b6EnT93At2xFBXjV7",
    "8": " - https://maps.app.goo.gl/UjoavVxJQt5pZiXB8"
}

BATTUTE_CRINGINE_DI_CHATGPT = [
    # Pre-partenza
    "Hai fatto la valigia o stai ancora cercando il passaporto nel cassetto del 2011?",
    "Ricordati: mutande pulite > outfit instagrammabili.",
    "Sei sicuro di aver prenotato tutto o ti stai affidando all’universo?",
    "Oggi è il giorno giusto per comprare quei mini-shampoo da 100ml che ti dimentichi sempre.",
    "🔥 News flash: Google Maps non funziona se non scarichi le mappe offline. Just sayin’.",
    "Ultima chiamata per controllare se hai preso il caricabatterie. O vuoi litigare in aeroporto?",
    "Bevi acqua, non solo ansia da check-in.",
    "Regola d’oro: ogni gruppo ha uno che dimentica qualcosa. Non essere TU.",
    "Hai fatto colazione? O punti tutto sul croissant a 7€ del gate?",
    "Chi ha detto ‘ci vediamo direttamente là’? Non fidarti, è una trappola.",
    "Inizia a pensare a dove mettere il passaporto... e a non spostarlo ogni 3 minuti.",
    "Ti serve davvero il cuscino da collo o vuoi solo sembrare esperto?",
    "Check-in mentale completato? No? Neanche il fisico? Perfetto.",
    "Sei sicuro che l’aeroporto sia quello giusto? Controlla. Di nuovo.",
    "Non dimenticare di sorridere alla security. Loro hanno potere assoluto.",
    "Hai controllato se il tuo documento non scade tipo... domani?",
    "Non è troppo tardi per fare una lista. È troppo tardi per ignorarla.",
    "Il trolley entra in cabina solo nei tuoi sogni. Provalo prima che Ryanair ti faccia piangere.",
    "Porta una felpa. Anche se vai nel deserto. Fidati, ti servirà.",
    # Durante il viaggio
    "Hai già chiesto ‘che si fa oggi?’ almeno tre volte? Smettila. Respira.",
    "Non hai ancora litigato con nessuno. Ottimo inizio. Forse.",
    "Mangia qualcosa di vero. Non puoi sopravvivere solo di patatine e birra.",
    "Il sole è bello, ma la crema solare è meglio. 🧴",
    "È l’ora del caffè. Ma anche dell’aperitivo. Decidi tu che fuso orario vuoi seguire.",
    "Ti ricordi dov’è l’hotel? Nemmeno io. Buona fortuna.",
    "Pro tip: se ti perdi, sorridi e cammina deciso. Nessuno sospetterà nulla.",
    "Livello batteria: 12%. Come la tua forza di volontà.",
    "Hai già detto ‘questo lo ricorderemo per sempre’ oggi? Se no, fallo ora.",
    "Hai bevuto acqua oggi o solo cocktail colorati e sogni?",
    "Fai una foto bella, che poi ci serve per la story di gruppo.",
    "Non lasciare che Google decida dove mangiare. Chiedi a un vecchietto del posto.",
    "Se vedi un gatto per strada, fai una pausa. È legge universale.",
    "Ogni volta che ti lamenti, un altro turista ti supera nella fila.",
    "Livello stress: basso. Livello zuccheri: tragico. Rimedia.",
    "Chi ha il controllo del navigatore? Spero non tu.",
    "Questa giornata ha bisogno di un gelato. Non discutere col bot.",
    "Hai già detto ‘è l’esperienza che conta’? Bravo, ora dillo mentre ti perdi.",
    "L’umore del gruppo è direttamente proporzionale alla disponibilità di Wi-Fi.",
    "Hai mai pensato a quanto sia poco affidabile il tuo senso dell’orientamento? Il gruppo sì.",
    "Un minuto di silenzio per la dignità persa ieri sera. Amen.",
    "Questo gruppo ha bisogno di un leader. O di un panino. Forse entrambi.",
    "Ricorda: se nessuno sa dove siete, non siete persi. Siete misteriosi.",
    "Stai facendo finta di sapere cosa stai facendo? Bravo. Continua così.",
    "Hai appena detto ‘una birretta tranquilla’? Ecco, ora hai ufficialmente mentito al destino.",
    "Oggi è il giorno perfetto per prendere decisioni sbagliate con grande convinzione.",
    "Se il piano A fallisce, niente panico. Abbiamo il piano C. Come ‘caos’.",
    "Stai ancora usando il roaming o ti sei evoluto? Chiediamo per il tuo conto.",
    "Ogni volta che procrastini, un volo viene cancellato. Coincidenze?",
    "Il tuo zaino è pieno di sogni, snack e probabilmente un calzino solo.",
    "L’universo ti sta mandando segnali. Peccato che siano in sanscrito.",
    "Hai chiesto al barista consigli sul posto? Bravo. Ora fidati zero.",
    "Hai fame, sete, sonno o solo bisogno di un abbraccio? Il bot non giudica. Però ride.",
    "Questa vacanza è sponsorizzata da: imprevisti, piani confusi e spirito d’adattamento.",
    "Se oggi non succede niente di assurdo, ritenta domani.",
    "Consiglio del giorno: abbraccia il caos. Ma prima mangia qualcosa.",
    "Non c’è GPS per l’anima. Ma forse c’è per il ristorante più vicino.",
    "Hai già cantato qualcosa a caso oggi? È terapeutico. E fastidioso per gli altri.",
]

CARGAMES_STUPIDINI_DI_CHATGPT = [
    "Chi è più probabile che dimentichi il passaporto?",
    "Chi è più probabile che si addormenti durante una visita guidata?",
    "Chi è più probabile che finisca in una foto con sconosciuti?",
    "Chi è più probabile che si perda anche con Google Maps?",
    "Chi è più probabile che ordini qualcosa di strano al ristorante?",
    "Chi è più probabile che si innamori di qualcuno in viaggio?",
    "Chi è più probabile che rovini la playlist del viaggio?",
    "Chi è più probabile che prenda troppi souvenir inutili?",
    "Chi è più probabile che chieda 'quanto manca?' ogni 10 minuti?",
    "Chi è più probabile che dimentichi dove ha messo le chiavi della stanza?",
    "Chi è più probabile che faccia amicizia con il tassista?",
    "Chi è più probabile che si ustioni il primo giorno?",
    "Chi è più probabile che finisca in una festa senza sapere come?",
    "Chi è più probabile che faccia tardi ogni mattina?",
    "Chi è più probabile che parli una lingua inventata pensando sia quella locale?",
    "Chi è più probabile che faccia pipì in un posto discutibile?",
    "Chi è più probabile che si lamenti per il cibo?",
    "Chi è più probabile che faccia troppe foto agli stessi tre edifici?",
    "Chi è più probabile che venga scambiato per un abitante del posto?",
    "Chi è più probabile che si presenti all’aeroporto con 5 minuti di anticipo... o 3 ore?",
    "Chi è più probabile che scambi una guida turistica per un venditore di gelati?",
    "Chi è più probabile che provi a parlare con gli animali del posto?",
    "Chi è più probabile che sbagli treno, autobus e anche direzione?",
    "Chi è più probabile che dimentichi il PIN della carta proprio al ristorante?",
    "Chi è più probabile che si finga esperto del posto dopo 2 ore di permanenza?",
    "Chi è più probabile che si perda in un museo a tema 'una stanza sola'?",
    "Chi è più probabile che esageri con lo shopping e non abbia spazio in valigia?",
    "Chi è più probabile che faccia amicizia con una nonna locale e venga invitato a cena?",
    "Chi è più probabile che prenda una multa per aver attraversato dove non si può?",
    "Chi è più probabile che finisca in una foto promozionale dell’hotel per sbaglio?",
    "Chi è più probabile che rovini il momento romantico con una battuta fuori luogo?",
    "Chi è più probabile che dimentichi il nome della città in cui ci troviamo?",
    "Chi è più probabile che dorma tutto il tragitto in pullman con la bocca aperta?",
    "Chi è più probabile che chieda informazioni nella lingua sbagliata con sicurezza assoluta?",
    "Chi è più probabile che finisca su TikTok senza saperlo?",
    "Chi è più probabile che confonda un monumento famoso con una pizzeria?",
    "Chi è più probabile che rompa qualcosa in un negozio di souvenir?",
    "Chi è più probabile che finisca in una conversazione di un’ora con uno sconosciuto?",
    "Chi è più probabile che dimentichi un amico in bagno e vada via sereno?",
    "Chi è più probabile che racconti questa vacanza come se fosse un viaggio spirituale in India?",
    "Chi è più probabile che scivoli sul ghiaccio entro i primi 10 minuti?",
    "Chi è più probabile che si faccia una foto con una balena... gonfiabile?",
    "Chi è più probabile che dimentichi i guanti nel posto più inospitale?",
    "Chi è più probabile che si perda in mezzo a una distesa di neve dicendo 'so la strada'?",
    "Chi è più probabile che chieda se può fare il bagno in un geyser bollente?",
    "Chi è più probabile che dica 'non fa poi così freddo' e poi sparisca sotto 4 strati?",
    "Chi è più probabile che fotografi 87 rocce credendo siano puffin?",
    "Chi è più probabile che parli con le renne come se capissero l’italiano?",
    "Chi è più probabile che dimentichi il costume per la Laguna Blu?",
    "Chi è più probabile che venga spazzato via dal vento cercando di fare una story?",
    "Chi è più probabile che scambi l'aurora boreale per un riflesso sulla lente?",
    "Chi è più probabile che cada in una buca di neve ridendo da solo?",
    "Chi è più probabile che si faccia amico un islandese e venga adottato?",
    "Chi è più probabile che confonda un vulcano con una collina qualsiasi?",
    "Chi è più probabile che dica 'potremmo vivere qui' mentre nevica orizzontalmente?",
    "Chi è più probabile che abbia sempre le mani congelate, ma voglia fare foto a tutto?",
    "Chi è più probabile che entri in un negozio di maglioni di lana e ne esca vestito come un vichingo?",
    "Chi è più probabile che non riesca a distinguere tra una pecora e un masso innevato?",
    "Chi è più probabile che si addormenti durante il tour per vedere l'aurora e la manchi completamente?",
    "Chi è più probabile che chieda se può portare una balena a casa come souvenir?",
    "Chi è più probabile che finisca dentro una pozza termale con il telefono in tasca?",
    "Chi è più probabile che saluti ogni cavallo islandese che vede?",
    "Chi è più probabile che faccia una gara di resistenza al freddo... e perda subito?",
    "Chi è più probabile che si fermi ogni 30 metri per dire 'wow, guarda che paesaggio!'?",
    "Chi è più probabile che provi a cuocere un uovo sopra un geyser?",
    "Chi è più probabile che parli con un troll pensando sia una statua?",
    "Chi è più probabile che cerchi di imitare un verso di balena in pubblico?",
    "Chi è più probabile che si ostini a voler trovare gli elfi nei boschi?",
    "Chi è più probabile che venga sgridato per aver toccato il muschio protetto?",
    "Chi è più probabile che faccia cadere il drone nel cratere di un vulcano?",
    "Chi è più probabile che tenti di attraversare a piedi una strada bloccata dalla neve?",
    "Chi è più probabile che dica 'dai, un tuffo nel lago ghiacciato lo faccio!' e poi ci ripensi a metà?",
    "Chi è più probabile che si perda inseguendo un'orsa polare... che non c'è?",
    "Chi è più probabile che confonda un hot dog islandese con una preghiera norrena?",
    "Chi è più probabile che inizi a parlare inglese con accento nordico per integrarsi?",
    "Chi è più probabile che spenda metà del budget in snack del distributore?",
    "Chi è più probabile che fotografi più pecore che persone durante il viaggio?",
    "Chi è più probabile che si faccia un selfie con una cascata e venga lavato via?",
    "Chi è più probabile che porti a casa un sasso 'perché era bello'?",
    "Chi è più probabile che provi a cucinare un piatto locale con risultati catastrofici?",
    "Chi è più probabile che provochi una valanga mentre sta cercando di fare un selfie?",
    "Chi è più probabile che non capisca che non si può mangiare la neve come se fosse gelato?",
    "Chi è più probabile che chieda dove sono le balene mentre sta passeggiando nel deserto di ghiaccio?",
    "Chi è più probabile che scivoli e finisca nel ghiaccio, poi si rialzi e dica 'era tutto sotto controllo'?",
    "Chi è più probabile che si addormenti sotto una coperta termica mentre tutti sono fuori a vedere l'aurora?",
    "Chi è più probabile che chieda 'ma se facciamo il bagno qui, non moriamo congelati?' mentre è già nel ghiaccio?",
    "Chi è più probabile che torni con un broncio perché il caffè è troppo caldo e non sa come raffreddarlo?",
    "Chi è più probabile che provi a fare snowboard senza sapere nemmeno come si mettono gli sci?",
    "Chi è più probabile che dica 'non è poi così freddo' mentre il vento artico lo sta investendo?",
    "Chi è più probabile che tenti di fare un pic-nic sulla neve e finisca sepolto?",
    "Chi è più probabile che dia l’impressione di essere un esperto di geologia islandese dopo aver visto 10 rocce?",
    "Chi è più probabile che faccia una battaglia a palle di neve con una renna pensando che sia un cervo?",
    "Chi è più probabile che si metta a cantare 'Let It Go' quando il vento è così forte che sembra un uragano?",
    "Chi è più probabile che confonda una panchina con una roccia e si sieda sopra una lastra di ghiaccio?",
    "Chi è più probabile che salga sulla cima di una montagna ghiacciata e poi si accorga di non aver messo i guanti?",
    "Chi è più probabile che si dimentichi il termos per il tè caldo mentre è in mezzo al nulla?",
    "Chi è più probabile che faccia un selfie con un vulcano e poi si dimentichi del resto del paesaggio?",
    "Chi è più probabile che si rifiuti di entrare in acqua gelata solo per fare il tuffo nell’oceano ghiacciato?",
    "Chi è più probabile che inizi a parlare con una pecora?",
    "Chi è più probabile che faccia un tuffo nel mare artico, anche se il meteo prevede un clima da deserto?",
    "Chi è il più probabile a comprare una maglietta con scritto 'I love Reykjavík' e metterla il giorno dopo a una sauna?",
    "Chi è il più probabile a cercare di entrare in un vulcano pensando che sia una pizzeria?",
    "Chi probabilmente si metterebbe a ballare in mezzo alla strada, aspettando che un geyser esploda?",
    "Chi probabilmente cercherebbe di fare amicizia con una foca, ma finirebbe per cadere nel mare?",
    "Chi è più probabile che si chieda se gli elfi esistono, mentre cammina nel bel mezzo di una tempesta di neve?",
    "Chi è più probabile che si metta a fare una guerra di palle di neve con un gruppo di turisti asiatici?",
    "Chi probabilmente si dimenticherà di indossare i guanti e dirà: 'Ah, ma tanto è solo una leggera brezza!'",
    "Chi sarebbe il più probabile a provare a fare una foto con un geyser, ma finirà per bagnarsi completamente?",
    "Chi probabilmente cercherebbe di fare una corsa con una renna pensando che sia un cavallo?",
    "Chi è più probabile che si addormenti sulla panca di una stazione di servizio e si svegli convinto di essere in un altro continente?",
    "Chi probabilmente cercherebbe di entrare in un museo pensando che sia un ristorante per assaporare 'la cucina islandese'?",
    "Chi è il più probabile a chiedere alla guida se la neve è commestibile?",
    "Chi probabilmente salirebbe su un ghiacciaio e finirebbe per fare snowboard... su un sasso?",
    "Chi è più probabile che inizi a urlare 'Siamo in un film d'avventura!' quando vede una montagna troppo alta?",
    "Chi probabilmente sbaglierebbe la strada e finirebbe in un campo di lava senza sapere come tornare indietro?",
    "Chi è il più probabile a fermarsi davanti a un'auto per fare un selfie con la neve, invece di fare attenzione alla strada?",
    "Chi probabilmente farebbe un picnic in mezzo alla tempesta di neve, solo per poi lamentarsi del freddo?",
    "Chi è il più probabile a fare una battuta sul 'Vulcano di Reykjavik', pur non esistendo un vulcano lì?",
    "Chi probabilmente guarderebbe un falco in volo e lo confonderebbe con un drone?",
    "Chi è più probabile che inizi a parlare con una balena, pensando che stia cercando di fare amicizia?",
    "Chi probabilmente cercherebbe di guidare in un fiume ghiacciato, convinto che sia la strada più corta?",
    "Chi è il più probabile a chiedere se ci sono i bagni alla base di ogni geyser, senza capire come funzionano?",
    "Chi probabilmente cercherebbe di fare il tuffo in una laguna termale e finirebbe per cadere nel fango?",
    "Chi è il più probabile a voler fare una foto con ogni singolo manto di neve, anche se sono tutti uguali?",
    "Chi probabilmente farebbe una danza tribale davanti a una cascata, senza sapere cosa stia facendo?",
]

LO_SAI_CHE = [
    "Potrebbe essere vero che... [NOME] parla fluentemente con i piccioni?",
    "Potrebbe essere vero che... [NOME] colleziona tappi di bottiglia per motivi spirituali?",
    "Potrebbe essere vero che... [NOME] una volta ha litigato con un distributore automatico?",
    "Potrebbe essere vero che... [NOME] crede fermamente che il ketchup sia una bevanda?",
    "Potrebbe essere vero che... [NOME] ha provato a insegnare yoga a un cactus?",
    "Potrebbe essere vero che... [NOME] pensa che i semafori siano solo consigli?",
    "Potrebbe essere vero che... [NOME] ha vinto il premio 'Persona più probabilmente confusa' nel 2017?",
    "Potrebbe essere vero che... [NOME] si è autoproclamato sindaco della propria stanza?",
    "Potrebbe essere vero che... [NOME] crede che il Wi-Fi funzioni meglio se lo guardi male?",
    "Potrebbe essere vero che... [NOME] ha un talento speciale per perdere oggetti mentre li tiene in mano?",
    "Potrebbe essere vero che... [NOME] ha tentato di cucinare il ghiaccio?",
    "Potrebbe essere vero che... [NOME] ha una playlist intitolata 'Colonne sonore per entrare in un supermercato'?",
    "Potrebbe essere vero che... [NOME] una volta ha cercato di ordinare una pizza da Google Translate?",
    "Potrebbe essere vero che... [NOME] sogna di diventare influencer di parcheggi creativi?",
    "Potrebbe essere vero che... [NOME] sa imitare perfettamente... nessuno?",
    "Potrebbe essere vero che... [NOME] ha confuso uno specchio con una finestra e ha salutato se stesso per 5 minuti?",
    "Potrebbe essere vero che... [NOME] chiama il GPS con un nome affettuoso?",
    "Potrebbe essere vero che... [NOME] una volta ha fatto il pieno al motorino con la Fanta?",
    "Potrebbe essere vero che... [NOME] ha paura delle stampanti quando restano in silenzio troppo a lungo?",
    "Potrebbe essere vero che... [NOME] crede che le patatine parlino tra loro quando nessuno guarda?",
    "Potrebbe essere vero che.. [NOME] ha cercato di caricare il telefono mettendolo nel microonde?",
    "Potrebbe essere vero che.. [NOME] ha scritto una lettera d'amore al proprio cuscino?",
    "Potrebbe essere vero che.. [NOME] pensa che gli aerei volino grazie alla magia?",
    "Potrebbe essere vero che.. [NOME] ha tentato di domare una zanzara con la gentilezza?",
    "Potrebbe essere vero che.. [NOME] si esercita a piangere per finta davanti allo specchio?",
    "Potrebbe essere vero che.. [NOME] una volta ha confuso un asciugacapelli con un walkie-talkie?",
    "Potrebbe essere vero che.. [NOME] ha detto 'grazie' a un semaforo?",
    "Potrebbe essere vero che.. [NOME] si è iscritto a un corso online per diventare ninja?",
    "Potrebbe essere vero che.. [NOME] crede che i segnali stradali siano messaggi personali?",
    "Potrebbe essere vero che.. [NOME] tiene un diario segreto... scritto in emoticon?",
    "Potrebbe essere vero che.. [NOME] ha cercato 'come respirare correttamente' su Google?",
    "Potrebbe essere vero che.. [NOME] si è complimentato con una pianta per la sua crescita?",
    "Potrebbe essere vero che.. [NOME] ha applaudito al microonde quando ha finito il timer?",
    "Potrebbe essere vero che.. [NOME] crede che le scale mobili abbiano emozioni?",
    "Potrebbe essere vero che.. [NOME] ha sognato di essere un cetriolo con una missione segreta?",
    "Potrebbe essere vero che.. [NOME] ha tentato di inviare un messaggio vocale a Siri?",
    "Potrebbe essere vero che.. [NOME] usa il deodorante come profumo di emergenza?",
    "Potrebbe essere vero che.. [NOME] ha chiesto consiglio sentimentale a un cartellone pubblicitario?",
    "Potrebbe essere vero che.. [NOME] crede che i biscotti abbiano un lato oscuro?",
    "Potrebbe essere vero che.. [NOME] ha cercato l’anima gemella tra i nomi dei Pokémon?",
    "Potrebbe essere vero che.. [NOME] saluta ogni volta che entra in ascensore... anche se è vuoto?",
    "Potrebbe essere vero che.. [NOME] ha una teoria secondo cui le chiavi spariscono per dispetto?",
    "Potrebbe essere vero che.. [NOME] ha cercato di adottare una nuvola?",
    "Potrebbe essere vero che.. [NOME] pensa che le luci automatiche siano controllate da un mago?",
    "Potrebbe essere vero che.. [NOME] una volta ha provato a fotocopiare una banana?",
    "Potrebbe essere vero che.. [NOME] crede che i sogni abbiano il copyright?",
    "Potrebbe essere vero che.. [NOME] ha nominato tutte le sue calze con nomi propri?",
    "Potrebbe essere vero che.. [NOME] ha provato a barare a briscola contro se stesso?",
    "Potrebbe essere vero che.. [NOME] ogni tanto parla con i semini del pane?",
    "Potrebbe essere vero che.. [NOME] ha cercato 'come diventare invisibile' su YouTube?",
    "Potrebbe essere vero che.. [NOME] tiene un elenco segreto dei suoi colpi di tosse preferiti?",
    "Potrebbe essere vero che.. [NOME] è convinto che i peluche abbiano opinioni politiche?",
    "Potrebbe essere vero che.. [NOME] ha detto 'scusa' a un muro dopo averlo urtato?",
    "Potrebbe essere vero che.. [NOME] considera il frigorifero un suo confidente?",
    "Potrebbe essere vero che.. [NOME] ha cercato di inviare un selfie via fax?",
    "Potrebbe essere vero che.. [NOME] crede che il lunedì sia una forma di vendetta cosmica?",
    "Potrebbe essere vero che.. [NOME] ha cercato di fare amicizia con una stampante?",
    "Potrebbe essere vero che.. [NOME] si fida solo delle sedie con braccioli?",
    "Potrebbe essere vero che.. [NOME] ha partecipato a un torneo immaginario di salto con la scopa?",
    "Potrebbe essere vero che.. [NOME] una volta ha provato a prendere il Wi-Fi con un retino per farfalle?",
    "Potrebbe essere vero che.. [NOME] una volta ha cercato di aprire una porta automatica... a chiave?",
    "Potrebbe essere vero che.. [NOME] crede che il formaggio abbia memoria?",
    "Potrebbe essere vero che.. [NOME] ha fatto una petizione per rendere legale parlare con le scarpe?",
    "Potrebbe essere vero che.. [NOME] è stato bannato da una chat... con se stesso?",
    "Potrebbe essere vero che.. [NOME] ascolta podcast per piante solo per sentirsi incluso?",
    "Potrebbe essere vero che.. [NOME] ha messo la sveglia alle 3 di notte solo per controllare se funziona?",
    "Potrebbe essere vero che.. [NOME] ha dichiarato guerra a un ventilatore?",
    "Potrebbe essere vero che.. [NOME] ha provato a ricaricare le batterie mettendole al sole?",
    "Potrebbe essere vero che.. [NOME] considera il cuscino il suo life coach?",
    "Potrebbe essere vero che.. [NOME] ha provato a ordinare sushi... al citofono?",
    "Potrebbe essere vero che.. [NOME] ha litigato con una sedia girevole e ha perso?",
    "Potrebbe essere vero che.. [NOME] una volta ha creduto che 'modalità aereo' significasse che il telefono può volare?",
    "Potrebbe essere vero che.. [NOME] saluta i semafori con un cenno del capo?",
    "Potrebbe essere vero che.. [NOME] si allena per diventare il primo campione mondiale di sospiri drammatici?",
    "Potrebbe essere vero che.. [NOME] una volta ha provato a impostare un promemoria su una banana?",
    "Potrebbe essere vero che.. [NOME] si è iscritto a un corso per parlare fluentemente... con le finestre?",
    "Potrebbe essere vero che.. [NOME] tiene una classifica dei suoi sogni più confusi?",
    "Potrebbe essere vero che.. [NOME] crede che le tende lo stiano spiando?",
    "Potrebbe essere vero che.. [NOME] una volta ha detto 'buon appetito' a un'automobile?",
    "Potrebbe essere vero che.. [NOME] ha fatto finta di essere impegnato per non rispondere... a sé stesso?",
    "Potrebbe essere vero che.. [NOME] ha tentato di sbucciare un kiwi con un cacciavite?",
    "Potrebbe essere vero che.. [NOME] si mette il casco per leggere messaggi troppo intensi?",
    "Potrebbe essere vero che.. [NOME] pensa che il caffè funzioni meglio se lo guardi con rispetto?",
    "Potrebbe essere vero che.. [NOME] ha provato a mettere in pausa la radio... battendo le mani?",
    "Potrebbe essere vero che.. [NOME] chiama il frigorifero 'Fred' e ci litiga ogni venerdì?",
    "Potrebbe essere vero che.. [NOME] una volta ha cercato di accendere la TV con una patatina?",
    "Potrebbe essere vero che.. [NOME] ha fondato un fan club per il proprio ombrello?",
    "Potrebbe essere vero che.. [NOME] ride da solo quando sente la parola 'biscotto'?",
    "Potrebbe essere vero che.. [NOME] ha tentato di fare smart working dal bagno di un autogrill?",
    "Potrebbe essere vero che.. [NOME] crede che i divani siano portali per mondi paralleli?",
    "Potrebbe essere vero che.. [NOME] si sveglia ogni mattina convinto di essere un personaggio secondario?",
    "Potrebbe essere vero che.. [NOME] ha fatto amicizia con il rumore della lavatrice?",
    "Potrebbe essere vero che.. [NOME] parla con le zanzare prima di schiacciarle per sportività?",
    "Potrebbe essere vero che.. [NOME] ha provato ad accarezzare una stampante per farla funzionare?",
    "Potrebbe essere vero che.. [NOME] ogni tanto si applaude da solo quando fa il parcheggio perfetto?",
    "Potrebbe essere vero che.. [NOME] una volta ha chiesto consiglio a una lattina di tonno?",
    "Potrebbe essere vero che.. [NOME] pensa che i distributori automatici abbiano preferenze personali?",
    "Potrebbe essere vero che.. [NOME] una volta ha provato a scrollare un libro cartaceo?",
    "Potrebbe essere vero che.. [NOME] ha creato una playlist intitolata 'musica per quando piove dentro'?",
    "Potrebbe essere vero che.. [NOME] ha fatto voto di silenzio... ma solo con le forchette?",
    "Potrebbe essere vero che.. [NOME] si è messo la crema solare a mezzanotte... in Islanda?",
    "Potrebbe essere vero che.. [NOME] ha cercato di sciogliere la neve con lo sguardo?",
    "Potrebbe essere vero che.. [NOME] ha tentato di abbracciare una balena 'per scaldarsi un attimo'?",
    "Potrebbe essere vero che.. [NOME] pensa che i geyser siano solo draghi timidi?",
    "Potrebbe essere vero che.. [NOME] ha cercato Wi-Fi sotto un ghiacciaio?",
    "Potrebbe essere vero che.. [NOME] ha chiesto a una renna se parlava inglese?",
    "Potrebbe essere vero che.. [NOME] ha fatto pipì controvento e ora è conosciuto come 'il ghiaccio vivente'?",
    "Potrebbe essere vero che.. [NOME] ha provato a ordinare una cioccolata calda a un vulcano?",
    "Potrebbe essere vero che.. [NOME] parla con le aurore boreali e si offende se non rispondono?",
    "Potrebbe essere vero che.. [NOME] ha fatto amicizia con un blocco di ghiaccio e lo ha chiamato Steve?",
    "Potrebbe essere vero che.. [NOME] ha tentato di dormire in un igloo di ghiaccioli?",
    "Potrebbe essere vero che.. [NOME] è convinto che i fiocchi di neve abbiano una personalità?",
    "Potrebbe essere vero che.. [NOME] una volta ha confuso una balena con un traghetto low cost?",
    "Potrebbe essere vero che.. [NOME] ha detto 'brrr' per tutto un giorno solo per integrarsi meglio?",
    "Potrebbe essere vero che.. [NOME] ha chiesto ad una guida turistica se si può cavalcare un iceberg?",
    "Potrebbe essere vero che.. [NOME] ha cercato di asciugarsi i capelli al vento artico?",
    "Potrebbe essere vero che.. [NOME] ha provato a fare l'angelo sulla neve... ma era ghiaccio vivo.",
    "Potrebbe essere vero che.. [NOME] ha cercato un McDonald's dentro un cratere?",
    "Potrebbe essere vero che.. [NOME] ha urlato 'SPLASH' a ogni balena avvistata?",
    "Potrebbe essere vero che.. [NOME] pensa che la parola 'fjord' sia un insulto gentile?"
]

NOMI_VIAGGIATORI = ["Ale B", "Ale D", "Bianca",
                    "Dalia", "Filippo", "Marco2", "MarcoRoma", "Viola"]

NUM_GIOCATORI = 8

PUNTEGGI_STUPIDINI1 = prev_state_dict["PUNTEGGI_STUPIDINI1"] if PREVIOUS_STATE_FILE_EXISTS and "PUNTEGGI_STUPIDINI1" in prev_state_dict else {
    "AleB": 0,
    "AleD": 0,
    "B": 0,
    "D": 0,
    "F": 0,
    "MG": 0,
    "MR": 0,
    "V": 0
}

PUNTEGGI_STUPIDINI3 = prev_state_dict["PUNTEGGI_STUPIDINI3"] if PREVIOUS_STATE_FILE_EXISTS and "PUNTEGGI_STUPIDINI3" in prev_state_dict else {
    "AleB": 0,
    "AleD": 0,
    "B": 0,
    "D": 0,
    "F": 0,
    "MG": 0,
    "MR": 0,
    "V": 0
}
USER_SEGRETO3 = -1

# Bonus: chiave tra 0 e 100
# Visibili fino alla colonna 79
FANTA_DICT_BONUS = {int(k): v for k, v in prev_state_dict["FANTA_DICT_BONUS"].items()} if PREVIOUS_STATE_FILE_EXISTS and "FANTA_DICT_BONUS" in prev_state_dict else {
    0: ["Comprare la cosa più strana che c’è sotto le 725 corone", 5],
    1: ["Uscire in costume da bagno in mezzo alla neve", 5], 
    2: ["Vedere l’aurora boreale", 5], 
    3: ["Parlare con un turista australiano", 5], 
    4: ["Riuscire a fare centro nel lancio dell'accetta", 5],
    5: ["Mangiare carne di squalo standard", 5],
    6: ["Vincere il premio 'Miglior playlist dell’Islanda'", 5],
    7: ["Dormire con MR", 5],
    8: ["Avvistata un'aurora boreale", 10],
    9: ["Immersione completa in una hot spring", 5],
    10: ["Pronuciare correttamente una città islandese al primo colpo", 3],
    11: ["Fare amicizia con un locale", 4],
    12: ["Trovare una pecora sul ciglio della strada e accarezzarla", 2],
    13: ["Foto epica sotto una cascata", 5],
    14: ["Resistere al vento islandese senza lamentarsi per un giorno", 6],
    15: ["Mangiare lo squalo fermentato senza sputarlo", 10],
    16: ["Guidare nel nulla senza sbagliare strada", 4],
    17: ["Camminare su un campo di lava senza inciampare", 4],
    18: ["Assaggiare un pylsur (hot dog islandese) e definirlo 'il migliore'", 3],
    19: ["Fare il bagno nell’oceano Atlantico senza urlare", 8],
    20: ["Scattare una foto ad un cavallo islandese mentre sorride", 6],
    21: ["Imparare a dire 'takk' e usarlo almeno 5 volte al giorno", 2],
    22: ["Trovare una chiesetta sperduta nel nulla e fare un video", 5],
    23: ["Resistere a non postare storie Instagram per 24 ore", 5],
    24: ["Fare pipì dietro una roccia senza essere visto né congelato", 2],
    25: ["Preparare il caffè nel thermos per tutto il gruppo", 3],
    26: ["Fare pipì in mezzo alla natura e sentirsi in armonia col cosmo", 4],
    27: ["Vedere un geyser esplodere proprio al momento giusto per la foto", 6],
    28: ["Raccogliere una pietra vulcanica da portare a casa", 3],
    29: ["Cucinare qualcosa in una cucina di ostello (nessuno si lamenta)", 4],
    30: ["Fare il pieno alla macchina *prima* che accenda la spia", 5],
    31: ["Guidare nel vento laterale islandese senza andare fuori strada", 7],
    32: ["Trovare un luogo segreto non segnato su Google Maps", 8],
    33: ["Riconoscere un paesaggio da una scena di Game of Thrones", 2],
    34: ["Svegliare tutti nel cuore della notte per l’aurora (c'era)", 10],
    35: ["Fare una playlist da viaggio che ha gasato tutti", 3],
}


# Malus: chiave tra 100 e 200
FANTA_DICT_MALUS = {int(k): v for k, v in prev_state_dict["FANTA_DICT_MALUS"].items()} if PREVIOUS_STATE_FILE_EXISTS and "FANTA_DICT_MALUS" in prev_state_dict else {
    100: ["Mettere la sveglia per l’aurora… ma riaddormentarsi", -5],
    101: ["Dimenticare i guanti e perdere la sensibilità alle dita", -5],
    102: ["Avere un attacco di diarrea", -5],
    103: ["Rimanere con i vestiti bagnati dopo la prima cascata", -5],
    104: ["Dimenticare qualcosa in albergo tra un giorno e l’altro", -5],
    105: ["Fermare la macchina per fare la cacca", -5],
    106: ["Chiamare Reykjavík 'Reikjavic'", -3],
    107: ["Perdere l’equilibrio camminando sul ghiaccio", -4],
    108: ["Bagnarsi completamente cercando di fare una foto a una cascata", -6],
    109: ["Spaventare una pecora suonando il clacson", -2],
    110: ["Chiedere se esistono i McDonald’s in Islanda", -3],
    111: ["Toccare l'acqua del mare senza motivo e urlare 'è fredda!'", -1],
    112: ["Dimenticare di fare il pieno nel mezzo del nulla", -7],
    113: ["Indossare jeans sotto la pioggia", -2],
    114: ["Lamentarsi del prezzo di una birra", -3],
    115: ["Scambiare un cavallo islandese per un pony e dirlo ad alta voce", -3],
    116: ["Mettere le mani nude nella neve per fare una palla e pentirsene", -2],
    117: ["Tentare di scalare una collina senza ramponi e rotolare giù", -6],
    118: ["Dimenticare di ricaricare la GoPro nel giorno più epico", -5],
    119: ["Mettere Spotify a tutto volume disturbando il silenzio mistico islandese", -4],
    120: ["Fare una battuta su Elsa di Frozen davanti a un ghiacciaio", -3],
    121: ["Aprire la portiera dell’auto col vento e quasi perderla", -7],
    122: ["Chiedere 'quando andiamo a vedere il vulcano?' mentre ne stavate già osservando uno", -2],
    123: ["Comprare acqua in bottiglia invece di bere quella del rubinetto", -3],
    124: ["Confondere muschio con tappeto erboso e saltarci sopra", -4],
    126: ["Cercare di usare Google Maps in mezzo al nulla senza segnale", -2],
    125: ["Lasciare la macchina fotografica accesa, scaricandola", -2],
    127: ["Provare a camminare su muschio islandese nonostante i cartelli", -6],
    128: ["Dimenticare l’adattatore della corrente", -3],
    129: ["Fare cadere lo zaino in una pozza geotermica", -5],
    130: ["Scambiare un elfo per un troll e offendere una leggenda locale", -2],
    131: ["Spoilerare a tutti l'aurora... che però non è apparsa", -4],
    132: ["Rompere una regola non scritta del gruppo", -3],
}


PUNTEGGI_STUPIDINI_FANTA = prev_state_dict["PUNTEGGI_STUPIDINI_FANTA"] if PREVIOUS_STATE_FILE_EXISTS and "PUNTEGGI_STUPIDINI_FANTA" in prev_state_dict else {
    "AleB": [0] * (100 + len(FANTA_DICT_MALUS)),
    "AleD": [0] * (100 + len(FANTA_DICT_MALUS)),
    "B": [0] * (100 + len(FANTA_DICT_MALUS)),
    "D": [0] * (100 + len(FANTA_DICT_MALUS)),
    "F": [0] * (100 + len(FANTA_DICT_MALUS)),
    "MG": [0] * (100 + len(FANTA_DICT_MALUS)),
    "MR": [0] * (100 + len(FANTA_DICT_MALUS)),
    "V": [0] * (100 + len(FANTA_DICT_MALUS))
}

FANTA_USER_CHOSEN = prev_state_dict["FANTA_USER_CHOSEN"] if PREVIOUS_STATE_FILE_EXISTS and "FANTA_USER_CHOSEN" in prev_state_dict else ""
FANTA_EVENT_CHOSEN = prev_state_dict["FANTA_EVENT_CHOSEN"] if PREVIOUS_STATE_FILE_EXISTS and "FANTA_EVENT_CHOSEN" in prev_state_dict else "" # Oggetto "Evento" (elemento di FANTA_DICT)
fanta_1, fanta_2 = range(2)

CONV = {
    "on": "AleB",
    "96": "AleD",
    "24": "B",
    "0k": "D",
    "lo": "F",
    "se": "MG",
    "co": "MR",
    "ni": "V",
}


VOTI_GIOCHINO_AUTO1 = {}
VOTI_GIOCHINO_AUTO2 = {}
VOTI_GIOCHINO_AUTO3 = {}

# Lista di 20 ricette islandesi (le più strane per un italiano)
RECIPES = [
    "1. Hákarl – Carne di squalo fermentata, dal sapore fortemente ammoniacale.\n"
    "Ingredienti:\n"
    "  - Carne di squalo (preferibilmente squalo della Groenlandia)\n"
    "  - Sale grosso\n"
    "  - Acqua\n"
    "Procedimento:\n"
    "  1. Tagliare la carne in pezzi e salarla abbondantemente.\n"
    "  2. Conservare in un ambiente controllato per 6-12 mesi per permettere la fermentazione.\n"
    "  3. Risciacquare, affettare sottilmente e servire a piccoli morsi.\n",

    "2. Svið – Testa di pecora bollita, con orecchie e pelle.\n"
    "Ingredienti:\n"
    "  - Testa di pecora fresca\n"
    "  - Acqua abbondante\n"
    "  - Sale e aromi (alloro, pepe)\n"
    "Procedimento:\n"
    "  1. Pulire accuratamente la testa per rimuovere peli e impurità.\n"
    "  2. Bollirla in acqua salata con aromi per 2-3 ore.\n"
    "  3. Servire calda, tagliata in pezzi, come piatto tradizionale.\n",

    "3. Slátur – Salsiccia di sangue islandese.\n"
    "Ingredienti:\n"
    "  - Sangue fresco di agnello\n"
    "  - Interiora e grasso per legare\n"
    "  - Spezie (pepe nero, noce moscata)\n"
    "  - Budelli naturali per insaccare\n"
    "Procedimento:\n"
    "  1. Mescolare il sangue con interiora tritate e spezie.\n"
    "  2. Insaccare il composto nei budelli naturali.\n"
    "  3. Cuocere a fuoco basso fino a completa cottura; servire a fette.\n",

    "4. Súrsaðir hrútspungar – Testicoli di montone fermentati.\n"
    "Ingredienti:\n"
    "  - Testicoli di montone puliti\n"
    "  - Soluzione salina\n"
    "  - Ingredienti per la fermentazione secondo la tradizione locale\n"
    "Procedimento:\n"
    "  1. Pulire i testicoli e immergerli in una soluzione salina.\n"
    "  2. Lasciar fermentare in condizioni controllate per diverse settimane.\n"
    "  3. Affettare sottilmente e servire come antipasto o contorno.\n",

    "5. Kiviak – Piccoli auks fermentati in pelle di foca, una prelibatezza tradizionale groenlandese.\n"
    "Ingredienti:\n"
    "  - Piccoli auks interi (o uccelli marini simili)\n"
    "  - Sale per aiutare la conservazione\n"
    "  - Pelle di foca, pulita e preparata come contenitore\n"
    "Procedimento:\n"
    "  1. Pulire gli uccelli, lasciandoli quasi interi per preservare la tradizione.\n"
    "  2. Riempire una pelle di foca pulita con gli uccelli, sigillando il contenitore in maniera ermetica.\n"
    "  3. Lasciare fermentare in un ambiente freddo (tradizionalmente una buca nel terreno) per diverse settimane, di solito durante l'inverno.\n"
    "  4. Aprire la pelle, rimuovere il contenuto e servire in occasioni speciali.\n",

    "6. Harðfiskur – Pesce secco tradizionale (eglefino o merluzzo).\n"
    "Ingredienti:\n"
    "  - Filetti di pesce fresco\n"
    "  - Sale\n"
    "  - Burro per accompagnare\n"
    "Procedimento:\n"
    "  1. Pulire e salare i filetti di pesce.\n"
    "  2. Esposizione all'aria per diversi giorni per l'essiccazione naturale.\n"
    "  3. Tagliare a strisce e servire con burro morbido.\n",

    "7. Þorramatur – Piatto misto tradizionale servito durante il Þorrablót.\n"
    "Ingredienti:\n"
    "  - Selezione di carni fermentate, pesce secco, formaggi e pane tradizionale\n"
    "Procedimento:\n"
    "  1. Disporre in un grande piatto diverse specialità in piccole porzioni.\n"
    "  2. Servire come buffet per far assaggiare più prelibatezze agli ospiti.\n",

    "8. Brennivín – Schnapps islandese, detto anche “Black Death”.\n"
    "Ingredienti:\n"
    "  - Distillato a base di patate o cereali\n"
    "  - Erbe aromatiche per l'infusione\n"
    "Procedimento:\n"
    "  1. Distillare e affinare il liquido in botti o a temperatura controllata.\n"
    "  2. Servire freddo in piccoli bicchieri, come digestivo.\n",

    "9. Rúgbrauð – Pane di segale geotermico, dolce e denso.\n"
    "Ingredienti:\n"
    "  - Farina di segale\n"
    "  - Acqua, lievito, sale e un pizzico di zucchero\n"
    "Procedimento:\n"
    "  1. Impastare gli ingredienti fino a ottenere un composto omogeneo.\n"
    "  2. Lasciare lievitare e cuocere lentamente in forno a bassa temperatura o sfruttare il calore geotermico.\n"
    "  3. Raffreddare, affettare e servire.\n",

    "10. Kjötsúpa – Zuppa rustica d’agnello islandese.\n"
    "Ingredienti:\n"
    "  - Carne d’agnello con osso\n"
    "  - Patate, carote, cipolle, sedano\n"
    "  - Erbe aromatiche (timo, alloro) e pepe\n"
    "Procedimento:\n"
    "  1. Bollire la carne insieme alle verdure e alle erbe per almeno 2 ore.\n"
    "  2. Filtrare il brodo e servire caldo con abbondanti pezzi di carne e verdura.\n",

    "11. Pylsur – Hot dog islandese.\n"
    "Ingredienti:\n"
    "  - Carne mista (agnello, maiale, manzo) macinata e insaccata\n"
    "  - Spezie per salsiccia\n"
    "  - Panini, ketchup, senape e cipolle fritte\n"
    "Procedimento:\n"
    "  1. Preparare le salsicce con la miscela di carni e spezie e cuocerle alla griglia.\n"
    "  2. Servirle nel panino con i condimenti preferiti.\n",

    "12. Skyr – Latticino simile a uno yogurt denso, tradizionale e antichissimo.\n"
    "Ingredienti:\n"
    "  - Latte scremato\n"
    "  - Fermenti lattici\n"
    "  - Miele o frutta (opzionale)\n"
    "Procedimento:\n"
    "  1. Fermentare il latte con i fermenti fino a ottenere una consistenza cremosa.\n"
    "  2. Separare il siero per ottenere una consistenza densa.\n"
    "  3. Servire freddo, eventualmente dolcificato o con frutta.\n",

    "13. Fiskisúpa islandese – Zuppa di pesce locale ricca di aromi marini.\n"
    "Ingredienti:\n"
    "  - Pesce misto (merluzzo, eglefino)\n"
    "  - Patate, cipolle e pomodori\n"
    "  - Erbe di mare e un po’ di panna\n"
    "Procedimento:\n"
    "  1. Cuocere il pesce e le verdure in un leggero brodo di pesce.\n"
    "  2. Aggiungere la panna e gli aromi verso la fine della cottura.\n"
    "  3. Servire caldo con una spolverata di prezzemolo fresco.\n",

    "14. Hvalkjötsúpa – Zuppa di carne di balena (piatto controverso).\n"
    "Ingredienti:\n"
    "  - Carne di balena tagliata a cubetti\n"
    "  - Patate, carote, cipolle, sedano\n"
    "  - Brodo di carne e aromi (timo, alloro)\n"
    "Procedimento:\n"
    "  1. Cuocere lentamente la carne con le verdure in un brodo ricco di aromi.\n"
    "  2. Lasciare insaporire per diverse ore fino a ottenere una zuppa saporita.\n"
    "  3. Servire caldo in piccole porzioni.\n",

    "15. Hvalhjarta – Fette sottili di cuore di balena.\n"
    "Ingredienti:\n"
    "  - Cuore di balena fresco\n"
    "  - Sale, pepe e succo di limone\n"
    "Procedimento:\n"
    "  1. Affettare il cuore in modo molto sottile.\n"
    "  2. Marinare rapidamente con limone, sale e pepe.\n"
    "  3. Servire crudo o leggermente scottato come antipasto.\n",

    "16. Cozze geotermiche – Cozze cotte sfruttando il calore naturale.\n"
    "Ingredienti:\n"
    "  - Cozze fresche ben pulite\n"
    "  - Sale, limone e erbe aromatiche\n"
    "Procedimento:\n"
    "  1. Disporre le cozze in una teglia e condirle con sale ed erbe.\n"
    "  2. Cuocere a bassa temperatura, sfruttando se possibile una fonte di calore naturale o in forno.\n"
    "  3. Servire con una spruzzata di limone.\n",

    "17. Blóðmör – Pudding di sangue d’agnello.\n"
    "Ingredienti:\n"
    "  - Sangue d’agnello\n"
    "  - Farina (o altro legante)\n"
    "  - Spezie (pepe, noce moscata)\n"
    "  - Latte\n"
    "Procedimento:\n"
    "  1. Mescolare il sangue con farina, spezie e latte fino a ottenere una pastella omogenea.\n"
    "  2. Cuocere in forno a bagnomaria fino a raggiungere una consistenza solida ma morbida.\n"
    "  3. Lasciare raffreddare, quindi tagliare a fette e servire.\n",

    "18. Ferszt lamm – Agnello locale servito crudo o poco cotto.\n"
    "Ingredienti:\n"
    "  - Filetto di agnello freschissimo\n"
    "  - Erbe aromatiche (rosmarino, timo)\n"
    "  - Olio extravergine, sale e pepe\n"
    "Procedimento:\n"
    "  1. Marinare brevemente il filetto con erbe, olio, sale e pepe.\n"
    "  2. Tagliare a fettine sottili (tipo tartare) o cuocere velocemente su una griglia ben calda.\n"
    "  3. Servire immediatamente con una spruzzata di limone.\n",

    "19. Marinated Whale Liver – Fegato di balena marinato con erbe aromatiche.\n"
    "Ingredienti:\n"
    "  - Fegato di balena fresco\n"
    "  - Aceto (vino bianco o di mele)\n"
    "  - Erbe aromatiche (rosmarino, timo) e aglio\n"
    "  - Sale e pepe\n"
    "Procedimento:\n"
    "  1. Affettare sottilmente il fegato.\n"
    "  2. Marinare in una miscela di aceto, erbe, aglio, sale e pepe per 4-6 ore.\n"
    "  3. Servire come antipasto freddo, accompagnato da pane rustico.\n",

    "20. Súrmjólk – Latte fermentato tradizionale, acidulo e inusuale.\n"
    "Ingredienti:\n"
    "  - Latte fresco\n"
    "  - Fermenti lattici (o seguire la tecnica tradizionale artigianale)\n"
    "  - Eventuale dolcificante (miele)\n"
    "Procedimento:\n"
    "  1. Riscaldare leggermente il latte e aggiungere i fermenti lattici.\n"
    "  2. Lasciare fermentare a temperatura controllata per 8-12 ore fino a ottenere un latte denso e acidulo.\n"
    "  3. Raffreddare e servire freddo, eventualmente con dolcificante o frutta.\n",

    "21. Særsuð fiskur – Pesce sottaceto con tradizione antica.\n"
    "Ingredienti:\n"
    "  - Filetti di pesce fresco (es. merluzzo)\n"
    "  - Aceto, sale e zucchero\n"
    "  - Spezie (alloro, pepe in grani)\n"
    "Procedimento:\n"
    "  1. Pulire e tagliare il pesce a filetti.\n"
    "  2. Preparare una marinata con aceto, sale, zucchero e spezie.\n"
    "  3. Immergere i filetti nella soluzione e lasciar marinare per 24-48 ore in frigorifero.\n"
    "  4. Servire come antipasto o contorno, con una spolverata di erbe fresche.\n",

    "22. Laufabrauð – Pane tradizionale islandese decorato, tipico delle festività natalizie.\n"
    "Ingredienti:\n"
    "  - Farina di frumento\n"
    "  - Acqua, lievito e sale\n"
    "  - Un generoso quantitativo di burro (per ottenere un impasto morbido)\n"
    "Procedimento:\n"
    "  1. Preparare un impasto morbido con farina, acqua, lievito e una punta di sale.\n"
    "  2. Lasciare lievitare l'impasto fino al raddoppio.\n"
    "  3. Stendere sottilmente l'impasto e decorarlo con motivi incisi a mano con un coltello o stampi appositi.\n"
    "  4. Cuocere su una piastra ben calda o su una padella antiaderente fino a doratura.\n"
    "  5. Servire tiepido o a temperatura ambiente, magari accompagnato da burro.\n"
]


# this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Definisco un dizionario di storie, ciascuna divisa in "pagine" (ovvero paragrafi).
STORIES = {
    "selkie": {
        "title": "La Leggenda della Selkie",
        "pages": [
            "Una volta, nella parte orientale di Mýrdalur, un uomo percorse le scogliere lungo la riva del mare all'alba. Giunse all'ingresso di una caverna e udì il suono dei festeggiamenti e delle danze che vi riecheggiavano. Vicino vide numerose pelli di foca. Ne prese una e la portò a casa, chiudendola in un baule.",
            "Durante il giorno, ritornò alla caverna e trovò una giovane donna nuda in lacrime. Ella era la foca della quale aveva rubato la pelle. L'uomo le permise di vestirsi, la consolò e la portò a casa. Presto si affezionò a lui, benché il suo sguardo fosse sempre rivolto al mare.",
            "Poco tempo dopo la sposò e insieme ebbero dei figli. Il contadino custodiva la pelle nel baule e portava la chiave sempre con sé. Ma un giorno, dimenticando la chiave, al suo ritorno trovò il baule aperto – la donna e la sua pelle erano sparite.",
            "La donna, trovata la chiave, vide la sua pelle e, incapace di resistere, si la indossò e scomparve nel mare. Prima di andarsene, sussurrò: 'Dov’io fuggire? Ho sette figli nel mare e sette figli sulla terra.' Da quel giorno, si dice che il pescatore, pur avendo avuto fortuna nel pescato, porti nel cuore la tristezza di quella perdita."
        ],
        # Per ogni pagina si potrebbe associare anche un'immagine (qui come URL di esempio)
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-selkie-pag1.png"),
            os.path.join(THIS_FOLDER, "figures", "story-selkie-pag2.png"),
            os.path.join(THIS_FOLDER, "figures", "story-selkie-pag3.png"),
            os.path.join(THIS_FOLDER, "figures", "story-selkie-pag4.png")
        ]
    },
    "huldufolk": {
        "title": "La Leggenda del Popolo Nascosto (Huldufólk)",
        "pages": [
            "In Islanda, si narra di esseri misteriosi chiamati Huldufólk, ovvero 'popolo nascosto'. Queste creature, simili agli elfi, vivono in armonia con la natura, nascoste agli occhi umani. Abitano tra le rocce, le colline e i paesaggi incontaminati dell'isola, conducendo una vita parallela alla nostra. Si dice che siano visibili solo a pochi fortunati o in momenti particolari, come durante il solstizio d'estate. ",
            "Il popolo islandese ha sempre mostrato grande rispetto per gli Huldufólk. Durante la costruzione di strade o edifici, è comune modificare i progetti per evitare di disturbare le loro presunte dimore. Ci sono racconti di macchinari che si guastano inspiegabilmente o di incidenti evitati quando si presta attenzione a non invadere i loro territori. ",
            "Molti islandesi affermano di aver avuto incontri con il popolo nascosto. Si racconta di bambini che giocano con amici invisibili o di viaggiatori che ricevono aiuto misterioso durante tempeste improvvise. Queste storie, tramandate di generazione in generazione, rafforzano la credenza nella presenza degli Huldufólk e nell'importanza di vivere in armonia con la natura. ",
            "Secondo un racconto, un giorno, un contadino di nome Jón stava lavorando nei campi quando vide una bellissima donna danzare tra le rocce. Era una huldufólk. Jón rimase incantato dalla sua bellezza e decise di seguirla.",
            "La donna lo portò in un mondo incantato, dove la musica e la danza regnavano sovrane. Jón trascorse giorni meravigliosi con lei, dimenticando il suo lavoro e la sua vita quotidiana.",
            "Quando finalmente tornò a casa, scoprì che erano passati anni. La sua fattoria era in rovina e la sua famiglia lo aveva dato per disperso. Da quel giorno, Jón raccontò la sua storia a chiunque volesse ascoltarla, avvertendo tutti di non sottovalutare il potere del popolo nascosto."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-huldufolk.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-huldufolk.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-huldufolk.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-huldufolk.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-huldufolk.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-huldufolk.jpg")
        ]
    },
    "draugr": {
        "title": "Draugr – Il Non-Morto Vendicativo",
        "pages": [
            "*Il guardiano della tomba* \nNelle gelide terre d'Islanda, si racconta di creature non morte chiamate Draugar. Questi esseri, una volta uomini, si rifiutano di trovare pace nella morte. Restano nei loro tumuli, vigilando sui tesori sepolti e tormentando chi osa avvicinarsi. Non sono semplici spiriti: i Draugar possiedono corpi fisici, spesso gonfi e maleodoranti, con una forza sovrumana e la capacità di crescere di dimensioni a piacimento. ",
            "*Poteri oscuri* \nI Draugar non si limitano a custodire le loro tombe. Sono noti per la loro abilità nel cambiare forma, diventando animali o nebbia, e per la loro capacità di entrare nei sogni dei vivi, portando follia e morte. Alcuni racconti narrano di Draugar che escono dalle loro tombe per attaccare i vivi, spinti da invidia o desiderio di vendetta. La loro presenza è spesso annunciata da un odore nauseabondo e da un senso opprimente di terrore.",
            "*Protezioni e rituali* \nPer proteggersi dai Draugar, gli islandesi adottavano vari rituali. Si credeva che seppellire i morti con le mani legate o con oggetti sacri potesse impedire loro di tornare. Alcuni tumuli venivano circondati da pietre magiche o rune protettive. Inoltre, era pratica comune seppellire i defunti lontano dalle abitazioni, per evitare che i Draugar potessero tornare a tormentare i vivi. "
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-draugr.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-draugr.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-draugr.jpg")
        ]

    },
    "nykur": {
        "title": "Nykur – Il Cavallo d’Acqua",
        "pages": [
            "*L’incontro ingannevole* \nIn Islanda, tra le nebbie che avvolgono laghi e fiumi, si cela una creatura misteriosa: il Nykur, un cavallo d’acqua dalle sembianze affascinanti. Apparentemente simile a un normale cavallo grigio, il Nykur si distingue per un dettaglio inquietante: i suoi zoccoli sono rivolti all’indietro. Questo essere leggendario attira i viandanti ignari, offrendo loro un passaggio attraverso acque pericolose. Ma chiunque salga sulla sua groppa si ritrova incollato al suo dorso, incapace di scendere. Il Nykur allora si lancia nelle profondità, trascinando la sua vittima verso una fine tragica. ",
            "*Le metamorfosi del Nykur* \nIl Nykur non è solo un cavallo d’acqua; è una creatura mutaforma. Può assumere l’aspetto di un giovane affascinante per sedurre le sue vittime o trasformarsi in un enorme salmone o in un toro selvaggio. Tuttavia, mantiene sempre un elemento distintivo: gli zoccoli invertiti. In alcune leggende, il Nykur appare come una creatura mostruosa con dodici zampe o come un essere massiccio con la pelle pendente. ",
            "*Difendersi dal Nykur* \nFortunatamente, esistono modi per proteggersi dal Nykur. Se si sospetta che un cavallo sia in realtà un Nykur, pronunciare ad alta voce il suo nome lo costringerà a liberare la sua vittima e a fuggire nelle acque. Inoltre, il Nykur teme il fuoco e l’acqua santa. In alcune storie, si racconta che una giovane ragazza, trascinata nel sonno dal Nykur, riuscì a salvarsi pronunciando il suo nome, costringendolo a ritirarsi. "
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-nykur1.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-nykur2.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-nykur2.jpg")
        ]
    },
    "stregaBarcaPietra": {
        "title": "Skessan á Steinnökkvanum – La Strega sulla Barca di Pietra",
        "pages": [
            "*Il viaggio e l'inganno*\nIl principe Sigurd, dopo aver sposato una principessa straniera e aver avuto un figlio, decide di tornare nel suo regno. Durante la traversata, una calma improvvisa ferma la nave. Mentre Sigurd riposa sottocoperta, una strega su una barca di pietra si avvicina silenziosamente, rapisce la regina e il bambino, e assume l'aspetto della regina grazie a un incantesimo. La vera regina viene spedita, priva di sensi, verso il regno sotterraneo del fratello della strega.",
            "*Sospetti e scoperte*\nLa falsa regina, ora a bordo della nave, cerca di calmare il bambino in lacrime, ma senza successo. Sigurd nota un cambiamento nel comportamento della moglie: è diventata fredda e distante. Al loro arrivo, Sigurd assume il trono, ma il figlio continua a piangere inconsolabilmente. Una nutrice viene incaricata di prendersi cura del bambino, e sotto la sua custodia, il piccolo finalmente trova pace.",
            "*La verità emerge*\nDue giovani cortigiani, giocando a scacchi vicino alla stanza della regina, sentono strani rumori. Spiando attraverso una fessura, vedono la regina trasformarsi in una mostruosa trolla mentre sbadiglia. Un gigante a tre teste emerge dal pavimento, le porta un trogolo di carne, che lei divora avidamente. Dopo il pasto, la regina ritorna al suo aspetto umano. I giovani, terrorizzati, decidono di non rivelare ciò che hanno visto.",
            "*Il ritorno della vera regina*\nNel frattempo, la nutrice del principe nota un evento straordinario: ogni notte, una donna vestita di bianco emerge dal pavimento, abbraccia il bambino e scompare. La terza notte, la donna sussurra: 'Due sono passate, ne resta una sola.' La nutrice informa Sigurd, che decide di affrontare la situazione. La notte seguente, armato di spada, attende la misteriosa figura. Quando la donna appare, lui riconosce la vera regina e spezza la catena che la lega. Un tremore scuote il palazzo: il gigante, legato all'altra estremità della catena, cade nel suo regno sotterraneo.",
            "*Giustizia e riconciliazione*\nLa vera regina racconta a Sigurd l'inganno della strega e la sua prigionia. Sigurd ordina l'arresto della falsa regina, che viene condannata a morte per i suoi crimini. La vera regina riprende il suo posto accanto al re, e il regno celebra il ritorno dell'armonia."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-strega.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-strega.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-strega.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-strega.jpg"),
            os.path.join(THIS_FOLDER, "figures", "story-strega.jpg")
        ]
    },
    "bukolla": {
        "title": "Búkolla – La Mucca Magica",
        "pages": [
            "*Il ragazzo e la mucca scomparsa*\nIn un remoto angolo d'Islanda, vivevano un uomo e una donna con il loro unico figlio. Nonostante la presenza del ragazzo, i genitori non gli mostravano affetto. La loro unica fonte di sostentamento era una mucca di nome Búkolla. Un giorno, Búkolla scomparve misteriosamente. I genitori, infuriati, ordinarono al figlio di trovarla e di non tornare senza di lei.",
            "*La ricerca di Búkolla*\nIl ragazzo partì, portando con sé solo del cibo e un paio di scarpe nuove. Durante il cammino, si fermava e chiamava: 'Muggisci ora, mia Búkolla, se sei viva!' Dopo il terzo richiamo, udì il muggito provenire da sotto i suoi piedi. Scoprì una grotta dove Búkolla era incatenata. La liberò e insieme iniziarono il viaggio di ritorno.",
            "*L'inseguimento dei troll*\nMentre tornavano, una gigantesca trolla e sua figlia iniziarono a inseguirli. Spaventato, il ragazzo chiese a Búkolla cosa fare. Lei gli disse di prendere un pelo dalla sua coda e posarlo a terra, pronunciando: 'Diventa un fiume così largo che solo un uccello possa attraversarlo.' Immediatamente, un vasto fiume si formò tra loro e le troll. Tuttavia, le troll non si arresero. La più giovane andò a prendere il toro del padre, che bevve tutto il fiume.",
            "*Il muro di fuoco*\nIl ragazzo, ancora in fuga, chiese nuovamente consiglio a Búkolla. Lei gli disse di prendere un altro pelo e posarlo a terra, dicendo: 'Diventa una fiamma così alta che solo un uccello possa volare sopra di essa.' Un muro di fuoco si eresse, ma le troll usarono il toro per spegnerlo, facendogli urinare sopra.",
            "*La montagna e la salvezza*\nPer l'ultima volta, Búkolla consigliò al ragazzo di prendere un pelo e dire: 'Diventa una montagna così alta che solo un uccello possa sorvolarla.' Una montagna imponente si formò. La trolla maggiore, determinata, iniziò a scavare un tunnel con un trapano magico. Tuttavia, nel tentativo di attraversarlo, rimase incastrata e si trasformò in pietra. Il ragazzo e Búkolla tornarono a casa sani e salvi, accolti con gioia dai genitori."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-bukolla-pag1.png"),
            os.path.join(THIS_FOLDER, "figures", "story-bukolla-pag2.png"),
            os.path.join(THIS_FOLDER, "figures", "story-bukolla-pag3.png"),
            os.path.join(THIS_FOLDER, "figures", "story-bukolla-pag4.png"),
            os.path.join(THIS_FOLDER, "figures", "story-bukolla-pag5.png")
        ]
    },
    "gryla": {
        "title": "Grýla – L’Ogressa del Natale",
        "pages": [
            "*La leggenda di Grýla*\nGrýla è una figura temibile del folklore islandese, descritta come una gigantesca trolla con un insaziabile appetito per i bambini disobbedienti. Vive in una caverna nelle montagne islandesi e, durante il periodo natalizio, scende nei villaggi per catturare i piccoli che si sono comportati male, portandoli nella sua tana per cucinarli in un enorme calderone.",
            "*La famiglia di Grýla*\nGrýla è sposata con Leppalúði, un troll pigro che raramente lascia la caverna. Insieme hanno tredici figli noti come i Jólasveinar o 'Yule Lads'. Questi tredici troll compaiono uno dopo l'altro nei tredici giorni precedenti al Natale, ognuno con un comportamento particolare, come rubare cibo o spiare attraverso le finestre.",
            "*Il Jólakötturinn – Il Gatto di Natale*\nOltre ai suoi figli, Grýla possiede anche un enorme gatto nero chiamato Jólakötturinn. Questo felino mostruoso si aggira durante il periodo natalizio e divora chiunque non abbia ricevuto nuovi vestiti per Natale, punendo così i pigri che non hanno lavorato abbastanza durante l'anno.",
            "*L'evoluzione della leggenda*\nOriginariamente, Grýla non era associata al Natale. Le prime menzioni risalgono al XIII secolo, dove era descritta come una creatura che mendicava cibo dai genitori, minacciando di portare via i loro figli se non le veniva dato nulla. Solo successivamente, nel XVII secolo, la sua figura fu legata alle festività natalizie, diventando la madre dei Jólasveinar.",
            "*Grýla oggi*\nNonostante le sue origini spaventose, Grýla è ancora una figura popolare in Islanda. Viene spesso rappresentata in racconti, canzoni e decorazioni natalizie, servendo come monito per i bambini affinché si comportino bene durante l'anno. La sua leggenda continua a essere una parte integrante delle tradizioni natalizie islandesi."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-gryla1.png"),
            os.path.join(THIS_FOLDER, "figures", "story-gryla2.png"),
            os.path.join(THIS_FOLDER, "figures", "story-gryla3.png"),
            os.path.join(THIS_FOLDER, "figures", "story-gryla4.png"),
            os.path.join(THIS_FOLDER, "figures", "story-gryla5.png")
        ]
    },
    "dimmuborgir": {
        "title": "Dimmuborgir – La Fortezza Oscura",
        "pages": [
            "*Le origini di Dimmuborgir*\nCirca 2.300 anni fa, un'eruzione vulcanica nella regione del lago Mývatn diede origine a un vasto campo di lava. Il flusso lavico incontrò un lago, causando l'ebollizione dell'acqua e la formazione di colonne di vapore che modellarono la lava in strutture uniche. Il risultato fu Dimmuborgir, un labirinto di formazioni laviche che ricordano castelli e torri, da cui il nome 'Fortezza Oscura'.",
            "*Dimora di creature leggendarie*\nSecondo il folklore islandese, Dimmuborgir è abitata da esseri soprannaturali come elfi e troll. Tra questi, la più famosa è Grýla, una trolla che, insieme al marito Leppalúði, vive nelle caverne di Dimmuborgir. La coppia ha tredici figli noti come i Jólasveinar o 'Yule Lads', che durante il periodo natalizio scendono nei villaggi per fare scherzi ai bambini.",
            "*Portale verso l'inferno*\nIn alcune leggende cristiane nordiche, Dimmuborgir è considerata il luogo dove Satana cadde sulla Terra dopo essere stato espulso dal Paradiso. Si dice che da lì abbia creato le catacombe dell'inferno, rendendo Dimmuborgir un punto di connessione tra il nostro mondo e gli inferi.",
            "*La Kirkjan – La Chiesa di Lava*\nAll'interno di Dimmuborgir si trova una formazione chiamata 'Kirkjan' o 'La Chiesa', una grotta naturale con archi che ricordano le navate di una cattedrale. Questo luogo suggestivo è talvolta utilizzato per concerti e cerimonie, aggiungendo un tocco mistico alla già affascinante atmosfera di Dimmuborgir.",
            "*Dimmuborgir oggi*\nOggi, Dimmuborgir è una popolare attrazione turistica, parte del percorso del 'Diamond Circle' nel nord dell'Islanda. I visitatori possono esplorare i sentieri che si snodano tra le formazioni laviche, immergendosi nella bellezza naturale e nelle leggende che permeano questo luogo unico."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-dimmuborgir.png"),
            os.path.join(THIS_FOLDER, "figures", "story-dimmuborgir.png"),
            os.path.join(THIS_FOLDER, "figures", "story-dimmuborgir.png"),
            os.path.join(THIS_FOLDER, "figures", "story-dimmuborgir.png"),
            os.path.join(THIS_FOLDER, "figures", "story-dimmuborgir.png")
        ]
    },
    "lagarfljot": {
        "title": "Lagarfljót – Il Serpente del Lago",
        "pages": [
            "*La leggenda del Lagarfljótsormur*\nNel folklore islandese, il Lagarfljótsormur è un mostro lacustre che si dice abiti nel lago Lagarfljót, situato vicino alla città di Egilsstaðir. La leggenda risale almeno al 1345, quando fu registrata per la prima volta negli annali islandesi. Secondo la storia, una giovane ragazza ricevette un anello d'oro da sua madre, che le consigliò di posizionarlo sotto un piccolo verme (un tipo di mini-drago) in una cassa, credendo che ciò avrebbe fatto crescere sia il verme che l'oro. Tuttavia, il verme crebbe rapidamente, diventando così grande da rompere la cassa. Spaventata, la ragazza gettò il verme e l'anello nel lago, dove la creatura continuò a crescere, diventando il mostro leggendario del lago.",
            "*Avvistamenti nel corso dei secoli*\nNel 1589, si dice che il serpente abbia sollevato il suo dorso così in alto sopra il lago che una nave a vela piena avrebbe potuto passarci sotto. Quando la creatura si tuffò nuovamente nell'acqua, l'impatto fu così massiccio che la terra tremò. Nel XVII secolo, ci furono 14 avvistamenti del serpente.",
            "*Avvistamenti moderni*\nNel 1963, operai che costruivano una centrale idroelettrica lungo il fiume che alimenta il Lagarfljót riferirono di aver visto una grande figura simile a un verme muoversi controcorrente. Questo avvistamento è spesso citato perché le condizioni rendevano meno probabili le illusioni ottiche.",
            "*Il video del 2012*\nNel febbraio 2012, un agricoltore di nome Hjörtur Kjerúlf filmò un fenomeno molto strano nel lago Lagarfljót: una forma serpentina che sembrava nuotare nelle acque ghiacciate. Il video attirò l'attenzione internazionale e nel 2014 una commissione locale dichiarò che non c'era motivo di dubitare dell'esistenza della creatura.",
            "*Il Lagarfljótsormur oggi*\nOggi, il Lagarfljótsormur è una parte affascinante del folklore islandese. Il lago Lagarfljót è una popolare destinazione turistica, e la leggenda del mostro continua a incuriosire sia i locali che i visitatori."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-lagarfljot.png"),
            os.path.join(THIS_FOLDER, "figures", "story-lagarfljot.png"),
            os.path.join(THIS_FOLDER, "figures", "story-lagarfljot.png"),
            os.path.join(THIS_FOLDER, "figures", "story-lagarfljot.png"),
            os.path.join(THIS_FOLDER, "figures", "story-lagarfljot.png")
        ]
    },
    "draugur": {
        "title": "Draugur – Il Fantasma dei Mari",
        "pages": [
            "*Il ritorno degli inquieti*\nNel folklore islandese, il Draugur è un non-morto che ritorna dalla tomba per tormentare i vivi. A differenza dei fantasmi incorporei, i Draugar possiedono un corpo fisico e conservano ricordi e abilità della vita passata. Spesso sono associati a persone malvagie o avide, che dopo la morte non trovano pace e tornano per vendicarsi o proteggere i loro beni sepolti.",
            "*Poteri e caratteristiche*\nI Draugar sono noti per la loro forza sovrumana e la capacità di aumentare le proprie dimensioni a volontà. Emanano un odore nauseabondo di decomposizione e possono uccidere i vivi in vari modi: schiacciandoli, divorandoli o inducendoli alla follia. Alcuni Draugar possiedono poteri magici, come la capacità di cambiare forma, controllare il tempo atmosferico e predire il futuro.",
            "*Il Draugur dei mari*\nNella tradizione norvegese, il termine Draugur è spesso associato ai fantasmi di marinai annegati, noti come 'Draugr del mare'. Queste entità appaiono su imbarcazioni fantasma o lungo le coste, annunciando tempeste imminenti o la morte di qualcuno. Si dice che indossino abiti da pescatore e abbiano la testa avvolta in alghe.",
            "*Episodi nelle saghe*\nLe saghe islandesi raccontano numerosi incontri con i Draugar. Nell'Eyrbyggja saga, ad esempio, un pastore viene ucciso da un Draugur e ritorna come non-morto per infestare la fattoria. In un altro racconto, il protagonista Grettir Ásmundarson combatte contro il Draugur Glámr, che lo maledice prima di essere distrutto.",
            "*Affrontare un Draugur*\nPer sconfiggere un Draugur, spesso non bastano le armi comuni. Gli eroi delle saghe ricorrono a rituali specifici: bruciare il corpo del non-morto, seppellirlo in luoghi remoti o costruire barriere intorno alla tomba. In alcuni casi, l'intervento di figure religiose o l'uso di oggetti sacri è necessario per placare l'anima inquieta."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "Theodor_Kittelsen_-_Sjotrollet_1887_The_Sea_Troll.jpg"),
            os.path.join(THIS_FOLDER, "figures", "Theodor_Kittelsen_-_Sjotrollet_1887_The_Sea_Troll.jpg"),
            os.path.join(THIS_FOLDER, "figures", "Theodor_Kittelsen_-_Sjotrollet_1887_The_Sea_Troll.jpg"),
            os.path.join(THIS_FOLDER, "figures", "Theodor_Kittelsen_-_Sjotrollet_1887_The_Sea_Troll.jpg"),
            os.path.join(THIS_FOLDER, "figures", "Theodor_Kittelsen_-_Sjotrollet_1887_The_Sea_Troll.jpg")
        ]
    },
    "marman": {
        "title": "L’Uomo Marinaio – Il Marman",
        "pages": [
            "*L’incontro con il Marman*\nUn pescatore islandese cattura una creatura marina metà uomo e metà pesce, nota come marman. La creatura, parlando con voce umana, implora il pescatore di essere liberata, promettendo in cambio saggezza e previsioni sul futuro.",
            "*La lezione di umiltà*\nIl marman rivela al pescatore eventi futuri e lo ammonisce per aver maltrattato il suo cane. Gli insegna che ogni creatura, grande o piccola, merita rispetto, e che l’arroganza può portare alla rovina.",
            "*Il rilascio e la trasformazione*\nCommosso dalle parole del marman, il pescatore lo libera. Da quel giorno, tratta tutte le creature del mare con rispetto, diventando un uomo più saggio e umile."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-marman.png"),
            os.path.join(THIS_FOLDER, "figures", "story-marman.png"),
            os.path.join(THIS_FOLDER, "figures", "story-marman.png")
        ]
    },
    "saemundur": {
        "title": "Sæmundur il Saggio e il Diavolo",
        "pages": [
            "*Il patto oscuro*\nSæmundur Sigfússon, noto come 'il Saggio', desiderava apprendere le arti magiche. Si recò in Germania per studiare alla 'Scuola Nera', dove fece un patto con il Diavolo per ottenere conoscenze proibite.",
            "*Il ritorno in Islanda*\nDopo anni di studio, Sæmundur chiese al Diavolo di riportarlo in Islanda. Il Diavolo si trasformò in una foca per trasportarlo, ma Sæmundur lo colpì con una Bibbia appena giunti a riva, rompendo il patto e liberandosi dalla sua influenza.",
            "*L'inganno finale*\nIn un'altra versione, Sæmundur cucì un pezzo di carne nel suo mantello. Quando il Diavolo cercò di afferrarlo, prese solo la carne, permettendo a Sæmundur di fuggire illeso."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-saemundur.png"),
            os.path.join(THIS_FOLDER, "figures", "story-saemundur.png"),
            os.path.join(THIS_FOLDER, "figures", "story-saemundur.png")
        ]
    },
    "diaconoMyrka": {
        "title": "Djákninn á Myrká – Il Diacono di Myrká",
        "pages": [
            "*La promessa infranta*\nIl diacono di Myrká promise a Guðrún di prenderla a Natale, ma morì annegato nel fiume Hörgá prima di mantenere la promessa.",
            "*Il ritorno spettrale*\nLa notte di Natale, Guðrún sentì bussare alla porta. Era il diacono, con la testa fasciata, venuto a prenderla. Durante il tragitto, si rese conto che era uno spettro intenzionato a portarla nella tomba.",
            "*La salvezza*\nGuðrún riuscì a salvarsi afferrando la corda della campana della chiesa, svegliando gli abitanti del villaggio. Il fantasma fuggì, lasciando dietro di sé solo il silenzio della notte."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-diacono_myrka.png"),
            os.path.join(THIS_FOLDER, "figures", "story-diacono_myrka.png"),
            os.path.join(THIS_FOLDER, "figures", "story-diacono_myrka.png")
        ]
    },
    "kopakonan": {
        "title": "Kópakonan – La Donna delle Foche",
        "pages": [
            "*La notte delle foche*\nNelle Fær Øer, si crede che le foche siano esseri umani che, una volta l’anno, nella notte sacra, tornano sulla terra, si spogliano della pelle di foca e danzano come esseri umani fino all’alba.",
            "*Il furto della pelle*\nUn uomo, vedendo una di queste donne, rubò la sua pelle di foca, impedendole di tornare in mare. La costrinse a sposarlo e vissero insieme per anni, avendo figli.",
            "*Il ritorno al mare*\nUn giorno, la donna trovò la sua pelle nascosta, la indossò e tornò in mare, lasciando la sua famiglia umana per sempre."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-kopakonan.png"),
            os.path.join(THIS_FOLDER, "figures", "story-kopakonan.png"),
            os.path.join(THIS_FOLDER, "figures", "story-kopakonan.png")
        ]
    },
    "alfadrottning": {
        "title": "Álfadrottning í Álögum – La Regina degli Elfi in Maledizione",
        "pages": [
            "*La maledizione*\nUna regina degli elfi fu colpita da un incantesimo che le impediva di trovare pace. Costretta a vagare tra i mondi, cercava un modo per spezzare la maledizione.",
            "*L’attesa del salvatore*\nLa leggenda narra che solo un mortale puro di cuore, durante una notte sacra, poteva liberarla. Molti tentarono, ma fallirono.",
            "*La liberazione*\nFinalmente, un giovane riuscì nell’impresa. La regina, libera, guidò il suo popolo in una danza di ringraziamento tra i fiordi, celebrando la fine della sua prigionia."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-alfadrottning.png"),
            os.path.join(THIS_FOLDER, "figures", "story-alfadrottning.png"),
            os.path.join(THIS_FOLDER, "figures", "story-alfadrottning.png")
        ]
    },
    "snotra": {
        "title": "Snotra Álfkona – La Saggia Donna Elfica",
        "pages": [
            "*L'incontro misterioso*\nIn una notte d'inverno, Jón, un giovane vedovo di Nes nel Borgarfjörður, incontrò una donna di straordinaria bellezza che raccoglieva fieno nei campi. Si chiamava Snotra, e nessuno conosceva le sue origini. Ogni vigilia di Natale, Snotra scompariva misteriosamente, per poi riapparire la notte di Natale.",
            "*Il segreto rivelato*\nJón, incuriosito, decise di seguirla durante una delle sue sparizioni. La vide entrare in una collina e scomparire. Scoprì così che Snotra era un'álfkona, una donna elfica, legata al mondo degli umani da un destino misterioso.",
            "*La scelta di Jón*\nNonostante la rivelazione, Jón decise di unirsi a Snotra nel suo mondo. Lasciò la vita umana per vivere con lei nel regno nascosto degli elfi, dove trovò saggezza e prosperità."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-snotra.png"),
            os.path.join(THIS_FOLDER, "figures", "story-snotra.png"),
            os.path.join(THIS_FOLDER, "figures", "story-snotra.png")
        ]
    },
    "silfrunarstadir": {
        "title": "Il Pastore di Silfrúnarstaðir",
        "pages": [
            "*La nebbia ingannevole*\nUn pastore di Silfrúnarstaðir si perse in una valle avvolta dalla nebbia. Lì incontrò dei troll che cercarono di ingannarlo, offrendogli cibo e bevande per farlo restare con loro.",
            "*La fuga astuta*\nIl pastore, sospettando un inganno, gettò dietro di sé un bastone che si trasformò in un fitto bosco, impedendo ai troll di seguirlo. Riuscì così a fuggire e tornare al villaggio.",
            "*Il custode delle tradizioni*\nTornato a casa, il pastore raccontò la sua avventura, diventando un custode delle antiche tradizioni e un avvertimento vivente contro le creature oscure delle valli nebbiose."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-silfrunarstadir.png"),
            os.path.join(THIS_FOLDER, "figures", "story-silfrunarstadir.png"),
            os.path.join(THIS_FOLDER, "figures", "story-silfrunarstadir.png")
        ]
    },
    "harpansKraft": {
        "title": "Harpans Kraft – La Forza dell’Arpa",
        "pages": [
            "*Il rapimento*\nDurante una festa di nozze, una giovane sposa fu rapita da un nøkk, uno spirito acquatico, e trascinata nel fiume. Il marito, disperato, afferrò la sua arpa e iniziò a suonare.",
            "*La melodia salvifica*\nLa musica dell'arpa era così potente e commovente che il nøkk fu costretto a risalire dalle profondità del fiume, restituendo la sposa al marito.",
            "*Il potere della musica*\nDa allora, si crede che la musica abbia il potere di tenere lontani gli spiriti maligni e proteggere gli innamorati, e l'arpa divenne simbolo di amore e salvezza."
        ],
        "images": [
            os.path.join(THIS_FOLDER, "figures", "story-harpans_kraft.png"),
            os.path.join(THIS_FOLDER, "figures", "story-harpans_kraft.png"),
            os.path.join(THIS_FOLDER, "figures", "story-harpans_kraft.png")
        ]
    }
}


HELP = {
    "general":
            "/start  - Avvia il bot.\n"
            "/help  - Mostra questo messaggio.\n"
            "/piano  <num_giorno>  - Visualizza il piano del giorno.\n"
            "/nanna <num_giorno>  - Visualizza info sulla notte.\n"
            "/cacca   <num_giorno>  - Visualizza il calendario cacca.\n"
            "/meteo <città>                - Mostra le previsioni meteo.\n"
            "/vulcano   - Controlla lo stato vulcanico.\n"
            "/curiosita - Curiosità cringina di ChatGPT.\n"
            "/ahah       - Battutina cringina di ChatGPT\n"
            "/car1 [stat] [reset] - Uno stupendo gioco da macchina!\n"
            "/car2 [stat]              - Uno stupendo gioco da macchina!\n"
            "/car3 [stat] [reset] - Uno stupendo gioco da macchina!\n"
            "/fanta [stat] [reset]- Uno stupendo gioco da viaggio!\n"
            "/giocatori                   - Visualizza o modifica il numero di giocatori.\n"
            "/storia                     - Leggi una storia del folklore islandese.\n",
    "start": "Beh niente di specifico. Semplicemente accende il Bot!\n",
    "help": "Vuoi l'help dell'help??\n",
    "piano": "Comando: \\piano GIORNO\n"
            "Visualizza il piano del giorno!\n"
            "Argomenti:\n  GIORNO: da 1 a 9\n",
    "nanna": "Comando: \\nanna [GIORNO]\n"
            "Visualizza informazioni su dove dormire!\n"
            "Argomenti:\n  Giorno: da 1 a 9\n"
            "  Se il numero del giorno non è indicato, mostra le info per la notte attuale.\n",
    "cacca": "Comando: \\cacca GIORNO\n"
            "Visualizza informazioni sul calendario Cacca!\n"
            "Argomenti:\n  GIORNO: da 1 a 9\n",
    "meteo": "Comando: \\meteo [CITTA']\n"
            "Argomenti:\n  CITTA': Nome della città\n"
            "  Se la città non è indicata, mostra le info per Rejkiavik.\n",
    "vulcano": "Simula il recupero dello status vulcanico. \nA caso. TOTALMENTE a caso.\nGrazie Marco roma per questo tuo prezioso contributo. A caso.\n",
    "curiosita": "Invia una curiosità 'divertente' del giorno. Grazie ChatGPT!\n",
    "ahah": "Invia una battutina cringina. Grazie ChatGPT!\n",
    "car1": "Comando: \\car1 [stat|reset]\n"
            "In questo entusiasmante gioco da macchina, vi verrà chiesto chi tra di voi sia "
            "il più probabile che finisca in una determinata situazione. \nVotate saggiamente! "
            "Il più votato perde!\n"
            "Opzioni:\n  reset: Reset di tutte le statistiche\n"
            "  stat: Mostra le statistiche\n",
    "car2": "Comando: \\car2\n"
            "In questo entusiasmante gioco da macchina, vi verrà chiesto quanto sia proabile che "
            "qualcuno di voi finisca in una determinata situazione. \nVotate saggiamente!\n"
            "In questo gioco non ci sono punteggi e statistiche!\n",
    "car3": "Comando: \\car3 [stat|reset] SEGRETO\n"
            "In questo entusiasmante gioco da macchina, dovrete indovinare se il segreto scritto da "
            "uno di voi è vero o falso. \nVotate saggiamente!\n"
            "Se la maggior parte dei giocatori indovina, a ciascuno viene dato 1 punto.\n"
            "Se la maggior parte dei giocatori non indovina, al sussurratore di segreti vengono dati tanti punti "
            "quanto i giocatori che ha ingannato.\n"
            "Se tutti indovinano, al sussurratore di segreti vengono sottratti tanti punti quanto i giocatori!\n"
            "Opzioni:\n  reset: Reset di tutte le statistiche\n"
            "  stat: Mostra le statistiche\n",
    "fanta": "Comando: \\fanta [stat|reset [all|USER KEY] | show | add EVENTO PUNTI | del KEY]\n"
            "Benvenuti al FantaIslanda! Qua potete vedere e aggiungere bonus e malus, assegnarli ai giocatori"
            " e vedere chi sta scalando la FantaClassifica!\n"
            "Opzioni:\n  stat: Mostra tutte le statistiche\n"
            "  reset all: Resetta tutte le statistiche\n"
            "  reset USER KEY: Elimina l'evento con indice KEY dall'utente USER\n"
            "  show: Mostra tutti i Bonus e i Malus\n"
            "  add EVENTO PUNTI: Aggiunge l'evento con il punteggio indicato. "
            "Il punteggio deve essere un numero e deve essere l'ultima cosa scritta nel comando\n"
            "  del KEY: Elimina l'evento con indice KEY\n",
    "giocatori": "Comando: \\giocatori [numero]\n"
            "Visualizza o imposta il numero di giocatori per i giochini da auto."
            "Opzioni:\n  [numero]: Numero di giocatori\n"
            "  Se il numero non è indicato, mostra quello attuale.\n",
    "storia": "Racconta una storia del folklore islandese!\n"
}
