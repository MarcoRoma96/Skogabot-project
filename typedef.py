# Itinerario statico: messaggi definiti a mano (hard-coded)
import os


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
RECIPE_INDEX = 0

SLEEPING_PLACES = {
    "1": "https://www.booking.com/Share-kCiEwO - https://maps.app.goo.gl/MLYAZZLjycgMxsv18",
    "2": "https://www.booking.com/Share-EeRs87 - https://maps.app.goo.gl/fFd5VSjMVdMLxxFHA",
    "3": "https://www.booking.com/Share-HfF8z5 - https://maps.app.goo.gl/RS6QNrwwNAWafpCD8",
    "4": "https://www.booking.com/Share-UCSfQO - https://maps.app.goo.gl/6zZ6vqPGH7UA3SHg7",
    "5": "https://www.booking.com/Share-1fNvUWs - https://maps.app.goo.gl/UVAoCZ3vgUwy7csGA",
    "6": " - https://maps.app.goo.gl/vpJijwQESn1izMZ96",
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
    "Chi è più probabile che si rifiuti di entrare in acqua gelata solo per fare il tuffo nell’oceano ghiacciato?"
]

PUNTEGGI_STUPIDINI = {
    "AleB": 0,
    "AleD": 0,
    "B": 0,
    "D": 0,
    "F": 0,
    "MG": 0,
    "MR": 0,
    "V": 0
}

VOTI_GIOCHINO_AUTO1 = {}

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
    }
    # Altre storie possono essere aggiunte con una struttura simile, ad es. "kopakonan": { ... }
}
