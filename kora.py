import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="kora", layout="centered")


st.sidebar.title("☕ kora")
menu = st.sidebar.radio(
    "Vai a:",
    ["📘 Introduzione", "📊 Business Plan", "🔢 Simulazione", "🔍 Analisi Rischi e Opportunità"]
    ,index=0
)
st.sidebar.info("Versione 1.1.1 – 4 Luglio 2025")

# === Pagina: Introduzione ===
if menu == "📘 Introduzione":
    st.title("KORA")
    st.header("🌱 Chi siamo")
    st.write("Benvenuto! Siamo una coppia unita dalla passione per il cibo etico, il rispetto per gli animali e la sostenibilità. Il nostro sogno è aprire un locale a Cuneo, che non sia solo un luogo dove mangiare e bere bene, ma uno spazio vivo e multifunzionale, che unisca cucina vegetale, artigianato e cultura.")
    st.header("🥗 Cosa vogliamo realizzare")
    st.write("Il nostro locale sarà 100% vegetale, con prodotti provenienti da fornitori locali, colazioni, pranzi e aperitivi artigianali. Il piano superiore sarà uno spazio dedicato alla cultura, al co-working e galleria d’arte per artisti emergenti della zona. Sarà un luogo inclusivo, sostenibile, aperto alla comunità. Vogliamo offrire non solo cibo, ma anche cultura, ispirazione e condivisione.")
    st.write("""Puoi navigare tra:
    \n- Il **business plan** (investimenti, costi fissi, break-even, analisi stagionalità)
    \n- Una sezione di **simulazione dinamica** giornaliera
    """)

# === Pagina: Sintesi Economica ===
elif menu == "📊 Business Plan":
    st.title("📊 Business Plan")
# === Costi Attrezzature ===
    voci = {
        "Cucina": 100000,
        "Macchina del caffè": 13000,
        "Bancone bar": 20000,
        "Utensili vari": 7500,
        "Piatti e tazzine": 6600,
        "Arredamento": 35000,
        "Ristrutturazione": 30000,
        "Piastrelle e sanitari": 11500,
        "Impianti": 10000,
        "Infissi": 5000,
        "Termosifoni e posa": 10000,
        "Architetti e pratiche": 8000,
        "Elettricista": 30000,
        "Luci (ipotesi media)": 4000,
        "Fondo di emergenza": 20000
    }


    # Calcolo della somma totale
    totale_attrezzature = sum(voci.values())


    # Costi fissi mensili
    costo_dipendenti = 8000
    costo_affitto = 2500
    costo_luce = 1500
    restituzione_prestito = 3000
    costo_materie_prime = 6200
    costi_fissi_mensili = costo_dipendenti + costo_affitto + costo_luce + restituzione_prestito + costo_materie_prime
    costi_fissi_annuali = costi_fissi_mensili * 12

    # Tempi restituzione prestiti
    tempi_restituzione_prestito = totale_attrezzature/restituzione_prestito/12

    st.header("Investimento iniziale")

    st.write(f"Investimento iniziale ad oggi: {totale_attrezzature:,.2f}€")
    st.write(f"Rata mensile restituzione prestito: {restituzione_prestito:,.2f}€")
    st.write(f"Tempo restituzione prestito: {tempi_restituzione_prestito:.0f} anni")
    with st.expander("🔍 Dettaglio"):
        for voce, valore in voci.items():
            st.write(f"{voce}: {valore:>10,.2f}€")
        st.write(f"**Totale: {totale_attrezzature:>10,.2f}€**")
    st.divider()

    st.header("Dettaglio costi e coperti necessari")
    # Ricavo medio per coperto (approssimazione)
    with st.expander("🧾 Modifica parametri per scontrino medio"):
        st.markdown("Personalizza la quantità e il valore medio per categoria.")

        colazioni = st.number_input("Numero colazioni giornaliere", min_value=0, value=50)
        media_colazioni = st.number_input("Scontrino medio colazioni (€)", min_value=0.0, value=3.50, step=0.10)

        pranzi = st.number_input("Numero pranzi giornalieri", min_value=0, value=60)
        media_pranzi = st.number_input("Scontrino medio pranzi (€)", min_value=0.0, value=10.00, step=0.50)

        aperitivi = st.number_input("Numero aperitivi giornalieri", min_value=0, value=40)
        media_aperitivi = st.number_input("Scontrino medio aperitivi (€)", min_value=0.0, value=7.50, step=0.50)

    # Calcolo scontrino medio
    if (colazioni + pranzi + aperitivi) > 0:
        scontrino_medio = (
            (colazioni * media_colazioni) +
            (pranzi * media_pranzi) +
            (aperitivi * media_aperitivi)
        ) / (colazioni + pranzi + aperitivi)
    else:
        scontrino_medio = 0

    st.write(f"**Scontrino medio calcolato:** {scontrino_medio:,.2f} €")

    # Coperti necessari giornalieri per andare in pari
    coperti_annuali_necessari = costi_fissi_annuali / scontrino_medio
    coperti_giornalieri_necessari = coperti_annuali_necessari / 250
    incasso_medio_giornaliero = coperti_giornalieri_necessari * scontrino_medio
    incasso_medio_mensile = incasso_medio_giornaliero * 250 / 12






    # Output

    st.write(f"Costi fissi mensili totali (dipendenti + affitto + luce + materie prime): {costi_fissi_mensili:,.2f}€")
    st.write(f"Costi fissi annuali totali (dipendenti + affitto + luce + materie prime): {costi_fissi_annuali:,.2f}€")
    #print(f"Incasso annuo stimato attuale: {incasso_annuale_attuale:,.2f}€")
    st.write(f"Scontrini medi giornalieri ({scontrino_medio:,.2f}€ a coperto) necessari per coprire i costri: {coperti_giornalieri_necessari:.0f}")
    st.write(f"Incasso medio giornalierio con {coperti_giornalieri_necessari:.0f} scontrini, scontrino medio di {scontrino_medio:,.2f}€ : {incasso_medio_giornaliero:,.2f}€")
    st.write(f"Incasso medio mensile con {coperti_giornalieri_necessari:.0f} scontrini, con uno scontrino medio di {scontrino_medio:,.2f}€ : {incasso_medio_mensile:,.2f}€")

    # === Prezzi di vendita (modificabili) ===
    prezzo_caffe = 1.40
    prezzo_cappuccino = 2.00
    prezzo_brioche = 1.50
    prezzo_pranzo = 10.00
    prezzo_asporto = 7.50
    prezzo_birra = 5.00
    prezzo_spritz = 5.00
    prezzo_drink_base = 7.50
    prezzo_drink_premium = 10

    # === Costo materie prime (modificabili) ===
    costo_caffe = 0.20
    costo_cappuccino = 0.50
    costo_brioche = 0.75
    costo_pranzo = 1.00  # piatto pasta/insalata + acqua + caffè
    costo_asporto = 1.00
    costo_birra = 1.75
    costo_spritz = 1.50
    costo_drink_base = 2.00
    costo_drink_premium = 3.00

    # === Quantità vendute giornalmente (stimate per un bar in centro storico) ===
    st.header("Dettaglio incasso giornaliero basato su statistiche di un bar in centro storico (50.000 abitanti/città)")
    with st.expander("🔧 Modifica volumi giornalieri (opzionale)"):
        st.markdown("Inserisci qui i valori stimati per ogni voce di incasso giornaliero.")

        num_caffe = st.number_input("Caffè venduti al giorno", min_value=0, value=100)
        num_cappuccini = st.number_input("Cappuccini venduti al giorno", min_value=0, value=25)
        num_brioche = st.number_input("Brioches vendute al giorno", min_value=0, value=15)
        num_pranzi = st.number_input("Pranzi serviti al giorno", min_value=0, value=40)
        num_asporto = st.number_input("Piatti asporto al giorno", min_value=0, value=15)
        num_birre = st.number_input("Birre vendute al giorno", min_value=0, value=15)
        num_spritz = st.number_input("Spritz venduti al giorno", min_value=0, value=20)
        num_drink_base = st.number_input("Drink base venduti al giorno", min_value=0, value=10)
        num_drink_premium = st.number_input("Drink premium venduti al giorno", min_value=0, value=5)

    # === Calcolo incassi per voce ===
    incasso_caffe = num_caffe * prezzo_caffe
    incasso_cappuccino = num_cappuccini * prezzo_cappuccino
    incasso_brioche = num_brioche * prezzo_brioche
    incasso_pranzi = num_pranzi * prezzo_pranzo
    incasso_asporto = num_asporto * prezzo_asporto
    incasso_birre = num_birre * prezzo_birra
    incasso_spritz = num_spritz * prezzo_spritz
    incasso_drink_base = num_drink_base * prezzo_drink_base
    incasso_drink_premium = num_drink_premium * prezzo_drink_premium

    # === Incasso totale ===
    incasso_totale = (
        incasso_caffe + incasso_cappuccino + incasso_brioche +
        incasso_pranzi + incasso_asporto +
        incasso_birre + incasso_spritz + incasso_drink_base + incasso_drink_premium
    )

    # === Incassi giornalieri ===
    incasso = (
        num_caffe * prezzo_caffe +
        num_cappuccini * prezzo_cappuccino +
        num_brioche * prezzo_brioche +
        num_pranzi * prezzo_pranzo +
        num_asporto * prezzo_asporto +
        num_birre * prezzo_birra +
        num_spritz * prezzo_spritz +
        num_drink_base * prezzo_drink_base +
        num_drink_premium * prezzo_drink_premium
    )

    # === Costi materie prime giornalieri ===
    costi_materie_prime = (
        num_caffe * costo_caffe +
        num_cappuccini * costo_cappuccino +
        num_brioche * costo_brioche +
        num_pranzi * costo_pranzo +
        num_asporto * costo_asporto +
        num_birre * costo_birra +
        num_spritz * costo_spritz +
        num_drink_base * costo_drink_base +
        num_drink_premium * costo_drink_premium
    )
    costi_materie_prime_annuali = costi_materie_prime *260
    costi_materie_prime_mensili = costi_materie_prime_annuali /12

    # === Guadagno netto giornaliero ===
    guadagno = incasso - costi_materie_prime

    # === Output ===
    # === Output dettagliato ===

    st.write(f"Caffè:           {num_caffe} x {prezzo_caffe:,.2f}€ = {incasso_caffe:,.2f} €")
    st.write(f"Cappuccini:      {num_cappuccini} x {prezzo_cappuccino:,.2f}€ = {incasso_cappuccino:,.2f} €")
    st.write(f"Brioches:        {num_brioche} x {prezzo_brioche:,.2f}€ = {incasso_brioche:,.2f} €")
    st.write(f"Pranzi:          {num_pranzi} x {prezzo_pranzo:,.2f}€ = {incasso_pranzi:,.2f} €")
    st.write(f"Asporto:         {num_asporto} x {prezzo_asporto:,.2f}€ = {incasso_asporto:,.2f} €")
    st.write(f"Birre:           {num_birre} x {prezzo_birra:,.2f}€ = {incasso_birre:,.2f} €")
    st.write(f"Spritz:          {num_spritz} x {prezzo_spritz:,.2f}€ = {incasso_spritz:,.2f} €")
    st.write(f"Drink base:      {num_drink_base} x {prezzo_drink_base:,.2f}€ = {incasso_drink_base:,.2f} €")
    st.write(f"Drink premium:   {num_drink_premium} x {prezzo_drink_premium:,.2f}€ = {incasso_drink_premium:,.2f} €")
    st.header ("Totale")
    st.write(f"**Totale Incasso Giornaliero: {incasso_totale:,.2f} €**")

    #DETTAGLIO CON ADEGUAMENTO

    # === Quantità vendute giornalmente (stimate per un bar in centro storico) con adeguamento===
    adeguamento = incasso_medio_giornaliero/incasso_totale*1.03
    num_caffe_adeguamento = int(adeguamento * num_caffe)
    num_cappuccini_adeguamento = int(adeguamento * num_cappuccini)
    num_brioche_adeguamento = int(adeguamento * num_brioche)
    num_pranzi_adeguamento = int(adeguamento * num_pranzi)
    num_asporto_adeguamento = int(adeguamento * num_asporto)
    num_birre_adeguamento = int(adeguamento * num_birre)
    num_spritz_adeguamento = int(adeguamento * num_spritz)
    num_drink_base_adeguamento = int(adeguamento * num_drink_base)
    num_drink_premium_adeguamento = int(adeguamento * num_drink_premium)

    # === Calcolo incassi per voce ===
    incasso_caffe_adeguamento = num_caffe_adeguamento * prezzo_caffe
    incasso_cappuccino_adeguamento = num_cappuccini_adeguamento * prezzo_cappuccino
    incasso_brioche_adeguamento = num_brioche_adeguamento * prezzo_brioche
    incasso_pranzi_adeguamento = num_pranzi_adeguamento * prezzo_pranzo
    incasso_asporto_adeguamento = num_asporto_adeguamento * prezzo_asporto
    incasso_birre_adeguamento = num_birre_adeguamento * prezzo_birra
    incasso_spritz_adeguamento = num_spritz_adeguamento * prezzo_spritz
    incasso_drink_base_adeguamento = num_drink_base_adeguamento * prezzo_drink_base
    incasso_drink_premium_adeguamento = num_drink_premium_adeguamento * prezzo_drink_premium

    # === Incasso totale ===
    incasso_totale_adeguamento= (
        incasso_caffe_adeguamento + incasso_cappuccino_adeguamento + incasso_brioche_adeguamento +
        incasso_pranzi_adeguamento + incasso_asporto_adeguamento +
        incasso_birre_adeguamento + incasso_spritz_adeguamento + incasso_drink_base_adeguamento + incasso_drink_premium_adeguamento
    )

    # === Incassi giornalieri ===
    incasso_adeguamento = (
        num_caffe_adeguamento * prezzo_caffe +
        num_cappuccini_adeguamento * prezzo_cappuccino +
        num_brioche_adeguamento * prezzo_brioche +
        num_pranzi_adeguamento * prezzo_pranzo +
        num_asporto_adeguamento * prezzo_asporto +
        num_birre_adeguamento * prezzo_birra +
        num_spritz_adeguamento * prezzo_spritz +
        num_drink_base_adeguamento * prezzo_drink_base +
        num_drink_premium_adeguamento * prezzo_drink_premium
    )

    # === Costi materie prime giornalieri ===
    costi_materie_prime_adeguamento = (
        num_caffe_adeguamento * costo_caffe +
        num_cappuccini_adeguamento * costo_cappuccino +
        num_brioche_adeguamento * costo_brioche +
        num_pranzi_adeguamento * costo_pranzo +
        num_asporto_adeguamento * costo_asporto +
        num_birre_adeguamento * costo_birra +
        num_spritz_adeguamento * costo_spritz +
        num_drink_base_adeguamento * costo_drink_base +
        num_drink_premium_adeguamento * costo_drink_premium
    )
    costi_materie_prime_annuali_adeguamento = costi_materie_prime_adeguamento *260
    costi_materie_prime_mensili_adeguamento = costi_materie_prime_annuali_adeguamento /12

    # === Guadagno netto giornaliero ===
    guadagno = incasso - costi_materie_prime

    # === Output ===
    # === Output dettagliato ===
    st.markdown("---")
    st.info("💡 Questa sezione mostra una **simulazione automatica** per raggiungere l'incasso minimo necessario a coprire i costi fissi. \
I volumi di vendita giornalieri (caffè, pranzi, aperitivi, ecc.) vengono modificati in proporzione fino a generare l’incasso medio necessario, \
con un margine del 3%.")
    st.header("Dettaglio incasso giornalieri con adeguamento all'incasso minimo")
    st.write(f"Caffè:        {num_caffe_adeguamento} x {prezzo_caffe:,.2f}€ = {incasso_caffe_adeguamento:,.2f} €")
    st.write(f"Cappuccini:   {num_cappuccini_adeguamento} x {prezzo_cappuccino:,.2f}€ = {incasso_cappuccino_adeguamento:,.2f} €")
    st.write(f"Brioches:     {num_brioche_adeguamento} x {prezzo_brioche:,.2f}€ = {incasso_brioche_adeguamento:,.2f} €")
    st.write(f"Pranzi:       {num_pranzi_adeguamento} x {prezzo_pranzo:,.2f}€ = {incasso_pranzi_adeguamento:,.2f} €")
    st.write(f"Asporto:      {num_asporto_adeguamento} x {prezzo_asporto:,.2f}€ = {incasso_asporto_adeguamento:,.2f} €")
    st.write(f"Birre:        {num_birre_adeguamento} x {prezzo_birra:,.2f}€ = {incasso_birre_adeguamento:,.2f} €")
    st.write(f"Spritz:       {num_spritz_adeguamento} x {prezzo_spritz:,.2f}€ = {incasso_spritz_adeguamento:,.2f} €")
    st.write(f"Drink base:   {num_drink_base_adeguamento} x {prezzo_drink_base:,.2f}€ = {incasso_drink_base_adeguamento:,.2f} €")
    st.write(f"Drink premium:{num_drink_premium_adeguamento} x {prezzo_drink_premium:,.2f}€ = {incasso_drink_premium_adeguamento:,.2f} €")
    st.header ("Totale")
    st.write(f"**Totale Incasso Giornaliero: {incasso_totale_adeguamento:,.2f} €**")

    with st.expander("🔍 Dettaglio"):
        # Confronto Incassi
        col1, col2 = st.columns(2)
        col1.metric("Incasso attuale", f"{incasso_totale:,.2f} €")
        col2.metric("Incasso minimo necessario", f"{incasso_medio_giornaliero:,.2f} €")

        # Calcolo della differenza
        delta_incasso = incasso_medio_giornaliero - incasso_totale
        col2.metric("Differenza da colmare", f"{delta_incasso:,.2f} €")

        st.markdown("---")

        # Confronto volumi tra vendite attuali e adeguate
        st.subheader("📈 Confronto volumi di vendita")

        data = {
            "Prodotto": ["Caffè", "Cappuccini", "Brioches", "Pranzi", "Asporto", "Birre", "Spritz", "Drink base", "Drink premium"],
            "Volume attuale": [
                num_caffe, num_cappuccini, num_brioche,
                num_pranzi, num_asporto,
                num_birre, num_spritz,
                num_drink_base, num_drink_premium
            ],
            "Volume adeguato": [
                num_caffe_adeguamento, num_cappuccini_adeguamento, num_brioche_adeguamento,
                num_pranzi_adeguamento, num_asporto_adeguamento,
                num_birre_adeguamento, num_spritz_adeguamento,
                num_drink_base_adeguamento, num_drink_premium_adeguamento
            ],
        }

        df_confronto = pd.DataFrame(data)
        st.table(df_confronto.set_index("Prodotto"))

    st.divider()
    st.header("Proiezione mensile degli incassi")
    with st.expander("ℹ️ Informazioni sulla stagionalità"):
        st.markdown("""
        I parametri di stagionalità sono stati definiti tenendo conto del comportamento tipico dei consumi in una città di medie dimensioni (come Cuneo), 
        considerando sia l’afflusso di persone nel centro storico sia le abitudini legate al clima e agli eventi locali.
    
        - **Gennaio e Febbraio**: mesi tendenzialmente più deboli, con minore affluenza e consumi ridotti dopo le festività.
        - **Primavera (Marzo–Maggio)**: graduale aumento grazie a giornate più lunghe, clima favorevole e prime attività all’aperto.
        - **Estate (Giugno–Luglio)**: picco di incassi grazie a turisti, eventi e socialità serale. 
        - **Agosto**: lieve calo per ferie e città più vuota.
        - **Settembre**: ritorno alla routine, incassi stabili.
        - **Ottobre**: aumento significativo stimato per la **Fiera del Marrone**, che richiama migliaia di visitatori in centro storico.
        - **Novembre**: mese storicamente debole, uscite ridotte.
        - **Dicembre**: risalita grazie a feste, mercatini e shopping natalizio.
    
        I coefficienti sono espressi in termini relativi (es. 1.10 = +10%) e applicati al numero di giorni lavorativi previsti.
        """)

    incasso_giornaliero_base = incasso_totale
    break_even_mensile = costi_fissi_mensili

    # === Dizionario stagionalità e giorni apertura ===
    stagionalità = {
        "Gen": 0.85, "Feb": 0.90, "Mar": 1.00, "Apr": 1.02,
        "Mag": 1.04, "Giu": 1.05, "Lug": 1.08, "Ago": 0.95,
        "Set": 1.00, "Ott": 1.05, "Nov": 0.90, "Dic": 1.05
    }
    giorni_apertura = {
    "Gen": 20, "Feb": 20, "Mar": 21, "Apr": 22, "Mag": 22, "Giu": 25,
    "Lug": 27, "Ago": 21, "Set": 22, "Ott": 23, "Nov": 21, "Dic": 23
}

    # === Calcoli ===
    mesi = list(stagionalità.keys())
    incassi_previsti = [
        incasso_giornaliero_base * giorni_apertura[mese] * stagionalità[mese]
        for mese in mesi
    ]
    break_even = [break_even_mensile] * len(mesi)

    # === DataFrame riepilogativo ===
    df = pd.DataFrame({
        "Mese": mesi,
        "Giorni apertura": [giorni_apertura[m] for m in mesi],
        "Fattore stagionale": [stagionalità[m] for m in mesi],
        "Incasso previsto (€)": incassi_previsti,
        "Break-even (€)": break_even
    })
    df["Differenza (€)"] = df["Incasso previsto (€)"] - df["Break-even (€)"]


    # === Grafico a barre ===
    fig_incassi, ax_incassi = plt.subplots(figsize=(10, 5))
    x = range(len(mesi))
    bar_width = 0.35
    fig_incassi.patch.set_facecolor("#eae6ca")        # sfondo esterno
    ax_incassi.set_facecolor("#F5F5DC")               # sfondo dell'area del grafico

    # Cambia anche i testi e le etichette in bianco per visibilità
    #ax.tick_params(colors="white")
    #ax.yaxis.label.set_color("white")
    #ax.xaxis.label.set_color("white")
    #ax.title.set_color("white")
    #ax.spines['bottom'].set_color("white")
    #ax.spines['top'].set_color("white")
    #ax.spines['right'].set_color("white")
    #ax.spines['left'].set_color("white")

    ax_incassi.bar(x, df["Incasso previsto (€)"], width=bar_width, label="Incasso previsto", color="tab:olive")
    ax_incassi.bar([i + bar_width for i in x], df["Break-even (€)"], width=bar_width, label="Break-even", color="tab:cyan")

    ax_incassi.set_xticks([i + bar_width / 2 for i in x])
    ax_incassi.set_xticklabels(mesi)
    ax_incassi.set_ylabel("€ al mese")
    ax_incassi.set_title("Confronto mensile: Incasso previsto vs Break-even")
    ax_incassi.legend()

    # === Output in Streamlit ===

    totale_row = {
    "Mese": "Totale",
    "Giorni apertura": df["Giorni apertura"].sum(),
    "Incasso previsto (€)": df["Incasso previsto (€)"].sum(),
    "Break-even (€)": df["Break-even (€)"].sum(),
    "Differenza (€)": df["Differenza (€)"].sum()
    }
    df = pd.concat([df, pd.DataFrame([totale_row])], ignore_index=True)

    # Separazione della riga 'Totale'
    df_valori = df[df["Mese"] != "Totale"].copy()
    df_totale = df[df["Mese"] == "Totale"].copy()

    # Styling della parte dati
    styler_valori = (
        df_valori.set_index("Mese")
        .style
        .highlight_max(subset=["Differenza (€)"], color="olive", axis=0)
        .highlight_min(subset=["Differenza (€)"], color="#800000", axis=0)
        .format({
            "Fattore stagionale": "{:,.2f}",
            "Incasso previsto (€)": "{:,.2f}",
            "Break-even (€)": "{:,.2f}",
            "Differenza (€)": "{:+,.2f}"
        })
    )

    # Styling Totale (es. grassetto + sfondo grigio chiaro)

    df_totale = df_totale.set_index("Mese")
    styler_totale = df_totale.style.format({
        "Fattore stagionale": "{:,.2f}",
        "Incasso previsto (€)": "{:,.2f}",
        "Break-even (€)": "{:,.2f}",
        "Differenza (€)": "{:+,.2f}"
    })

    # Unisci visivamente i due stili
    # NB: Streamlit accetta un solo `st.dataframe`, quindi si mostra prima uno, poi l'altro
    st.dataframe(styler_valori, use_container_width=True, height=457)
    st.dataframe(styler_totale, use_container_width=True, height=70)
    st.divider()
    # Assumiamo che df sia già definito, con colonna "Differenza (€)"
    df_diff = df[df["Mese"] != "Totale"]  # Escludi riga totale
    mesi = df_diff["Mese"]
    differenze = df_diff["Differenza (€)"]

    # Colori condizionati: verde per positivo, rosso per negativo
    colori = ["olive" if val >= 0 else "#800000" for val in differenze]

    # Grafico
    fig_diff, ax_diff = plt.subplots(figsize=(10, 5))
    bars = ax_diff.bar(mesi, differenze, color=colori)
    fig_diff.patch.set_facecolor("#eae6ca")        # sfondo esterno
    ax_diff.set_facecolor("#F5F5DC")               # sfondo dell'area del grafico

    # Asse x centrale
    ax_diff.axhline(0, color="black", linewidth=1)
    ax_diff.set_title("Differenza mensile tra incasso e break-even")
    ax_diff.set_ylabel("€ di guadagno (+) o perdita (−)")
    ax_diff.set_xlabel("Mese")

    # Mostra etichetta su ogni barra
    for bar, val in zip(bars, differenze):
        ax_diff.text(bar.get_x() + bar.get_width()/2, val + (100 if val >= 0 else -200),
                f"{val:,.0f}", ha='center', va='bottom' if val >= 0 else 'top', color="white")

    # Layout finale
    st.header("Grafici")
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(fig_incassi)

    with col2:
        st.pyplot(fig_diff)

elif menu == "🔢 Simulazione":
# === Sezione: Investimento iniziale ===
    st.title("🔢 Simulazione")
    st.header("🧾 Scontrino Medio")
    giorni_lavorati_annui = st.number_input("Numero di giorni lavorativi all'anno (n)", value = 250)
    colazioni = st.number_input("Colazioni (n)", value=50)
    media_colazioni = st.number_input("Scontrino medio colazioni (€)", value=3.50)
    pranzi = st.number_input("Pranzi (n)", value = 60)
    media_pranzi = st.number_input("Scontrino medio pranzi (€)", value=10.00)
    aperitivi = st.number_input("Aperitivi (n)", value = 40)
    media_aperitivi = st.number_input("Scontrino medio aperitivi (€)", value=7.50)

    if st.button("Calcola"):
        st.header("Coperti Necessari")
        scontrino_medio = (
            (colazioni * media_colazioni) +
            (pranzi * media_pranzi) +
            (aperitivi * media_aperitivi)
        ) / max((colazioni + pranzi + aperitivi), 1)
        # Costi fissi mensili
        costo_dipendenti = 8000
        costo_affitto = 2500
        costo_luce = 1500
        restituzione_prestito = 2500
        costo_materie_prime = 6200
        costi_fissi_mensili = costo_dipendenti + costo_affitto + costo_luce + restituzione_prestito + costo_materie_prime
        costi_fissi_annuali = costi_fissi_mensili * 12
        coperti_annuali_necessari = costi_fissi_annuali / scontrino_medio
        coperti_giornalieri_necessari = coperti_annuali_necessari / giorni_lavorati_annui
        incasso_medio_giornaliero = coperti_giornalieri_necessari * scontrino_medio
        incasso_medio_mensile = incasso_medio_giornaliero * giorni_lavorati_annui / 12


        st.write(f"**Scontrino medio calcolato:** {scontrino_medio:,.2f} €")
        st.write(f"**Scontrini giornalieri per copertura costi:** {coperti_giornalieri_necessari:.0f}")
        st.write(f"**Incasso medio giornaliero necessario:** {incasso_medio_giornaliero:,.2f} €")
        st.write(f"**Incasso medio mensile necessario:** {incasso_medio_mensile:,.2f} €")

    st.markdown("---")
    st.info("👉 Puoi esportare i dati manualmente o integrarli con Google Sheets/Excel per confronti più avanzati.")


elif menu == "🔍 Analisi Rischi e Opportunità":

    st.header("🔍 Analisi Rischi e Opportunità")
    st.write("Il progetto nasce con l’obiettivo di proporre un format innovativo di bar e cucina vegetale, accessibile e contemporaneo, nel cuore del centro storico di Cuneo. "
             "L’impostazione attuale prevede un’offerta focalizzata su colazioni, pranzi e aperitivi, "
             "con una visione fresca, attenta alla qualità degli ingredienti, alla sostenibilità e all’estetica del servizio.")
    st.write("#### ✅ Opportunità")
    st.write("- Crescente attenzione del pubblico verso un'alimentazione sana e consapevole")
    st.write("- Curiosità e apertura verso format nuovi e inclusivi, soprattutto tra giovani e professionisti")
    st.write("- Posizione **strategica nel centro città**, con forte visibilità e flusso pedonale")
    st.write("- **Eventi locali ricorrenti** (es. Fiera del Marrone, mercatini), che incrementano l’afflusso")
    st.write("- Possibilità di **ampliare l’offerta**: colazioni prolungate, brunch, degustazioni, collaborazione con produttori locali")
    st.write("#### ⚠️ Rischi e criticità")
    st.write("- **Diffidenza iniziale** da parte di una parte del pubblico, legata alla novità del concept")
    st.write("- **Alti costi di avviamento**, che richiedono un volume di affari costante")
    st.write("- **Stagionalità dei consumi**, con alcuni mesi tendenzialmente più deboli (es. gennaio, novembre)")
    st.write("- Presenza di **concorrenza consolidata** nel centro cittadino")
    st.write("- **Rischio inflazione** sui prezzi delle materie prime")
    st.write("#### 🎯 Strategia di mitigazione")
    st.write("- **Posizionamento chiaro**, comunicazione inclusiva e attenzione all’esperienza del cliente")
    st.write("- **Promozioni e formule di fidelizzazione**, in particolare nei mesi a minor traffico")
    st.write("- **Adattamento dell’organizzazione** del personale ai flussi reali")
    st.write("- **Collaborazioni con realtà del territorio** (associazioni, università, co-working, librerie) per aumentare la visibilità")

    st.header("🚀 Sviluppo futuro e ampliamento dell’offerta")
    st.write("Il presente piano si concentra esclusivamente sull’avviamento e la sostenibilità dell’attività di bistrot.")
    st.write("A partire da gennaio 2026, si prevede una seconda fase di sviluppo, orientata alla valorizzazione della parte superiore del locale con l’obiettivo di trasformarla in un vero e proprio caffè letterario e spazio culturale. Le attività previste includono:")
    st.write("- **Presentazioni di libri**, incontri con autori, eventi divulgativi")
    st.write("- **Serate tematiche**, talk, musica dal vivo acustica e performance artistiche")
    st.write("- **Workshop e laboratori creativi** in collaborazione con realtà locali")
    st.write("- **Creazione di una programmazione culturale stabile**, pensata per coinvolgere una community variegata")

    st.write("Questa evoluzione permetterà al locale di distinguersi ulteriormente, generando valore aggiunto sia economico che sociale. Gli investimenti necessari per questa fase sono già valutati nel business plan e ulteriori inestimenti saranno calcolati sulla base dei risultati dei primi mesi di attività.")
