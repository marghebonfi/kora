import streamlit as st
import pandas as pd

st.set_page_config(page_title="kora", layout="centered")


st.sidebar.title("☕ kora")
menu = st.sidebar.radio(
    "Vai a:",
    ["📘 Introduzione", "📊 Sintesi Economica", "🔢 Simulazione"]
    ,index=0
)
st.sidebar.info("Versione 1.0 – 3 Luglio 2025")

# === Pagina: Introduzione ===
if menu == "📘 Introduzione":
    st.title("KORA")
    st.header("🌱 Chi siamo")
    st.write("Benvenuto! Siamo una coppia unita dalla passione per il cibo etico, il rispetto per gli animali e la sostenibilità. Il nostro sogno è aprire un locale a Cuneo, che non sia solo un luogo dove mangiare e bere bene, ma uno spazio vivo e multifunzionale, che unisca cucina vegetale, artigianato e cultura.")
    st.header("🥗 Cosa vogliamo realizzare")
    st.write("Il nostro locale sarà 100% vegetale, con prodotti provenienti da fornitori locali, colazioni, pranzi e aperitivi artigianali. Il piano superiore sarà uno spazio dedicato alla cultura, al co-working e galleria d’arte per artisti emergenti della zona. Sarà un luogo inclusivo, sostenibile, aperto alla comunità. Vogliamo offrire non solo cibo, ma anche cultura, ispirazione e condivisione.")
    st.write("""Puoi navigare tra:
    \n- Il **business plan** (investimenti, costi fissi, break-even)
    \n- Una sezione di **simulazione dinamica** giornaliera
    """)

# === Pagina: Sintesi Economica ===
elif menu == "📊 Business Plan":
    st.title("📊 Business Plan")
# === Costi Attrezzature ===
    cucina = 100000
    macchina_caffe = 13000
    bancone_bar = 20000
    utensili_vari = 7500
    piatti_tazzine = 6600
    arredamento = 35000
    ristrutturazione = 30000
    piastrelle_sanitari = 11500
    impianti = 10000
    infissi = 5000
    termosifoni = 10000
    architetti_pratiche = 8000
    luci = 4000  # ipotesi media

    # Calcolo della somma totale
    totale_attrezzature = (
        cucina + macchina_caffe + bancone_bar + utensili_vari +
        piatti_tazzine + arredamento + ristrutturazione +
        piastrelle_sanitari + impianti + infissi +
        termosifoni + architetti_pratiche + luci
    )


    # Costi fissi mensili
    costo_dipendenti = 8000
    costo_affitto = 2500
    costo_luce = 1500
    restituzione_prestito = 2500
    costo_materie_prime = 6200
    costi_fissi_mensili = costo_dipendenti + costo_affitto + costo_luce + restituzione_prestito + costo_materie_prime
    costi_fissi_annuali = costi_fissi_mensili * 12

    # Tempi restituzione prestiti
    tempi_restituzione_prestito = totale_attrezzature/restituzione_prestito/12


    # Ricavo medio per coperto (approssimazione)
    colazioni = 50
    media_colazioni = 3.50
    pranzi = 60
    media_pranzi = 10
    aperitivi = 40
    media_aperitivi = 7.50
    scontrino_medio =  ((colazioni * media_colazioni) + (pranzi * media_pranzi) + (aperitivi*media_aperitivi))/(colazioni + pranzi + aperitivi)

    # Coperti necessari giornalieri per andare in pari
    coperti_annuali_necessari = costi_fissi_annuali / scontrino_medio
    coperti_giornalieri_necessari = coperti_annuali_necessari / 250
    incasso_medio_giornaliero = coperti_giornalieri_necessari * scontrino_medio
    incasso_medio_mensile = incasso_medio_giornaliero * 250 / 12

    st.header("Investimento iniziale")

    st.write(f"Investimento iniziale ad oggi: {totale_attrezzature:.2f}€")
    st.write(f"Rata mensile restituzione prestito: {restituzione_prestito:.2f}€")
    st.write(f"Tempo restituzione prestito: {tempi_restituzione_prestito:.0f} anni")




    # Output
    st.header("Dettaglio coperti")
    st.write(f"Costi fissi mensili totali (dipendenti + affitto + luce + materie prime): {costi_fissi_mensili:.2f}€")
    st.write(f"Costi fissi annuali totali (dipendenti + affitto + luce + materie prime): {costi_fissi_annuali:.2f}€")
    #print(f"Incasso annuo stimato attuale: {incasso_annuale_attuale:.2f}€")
    st.write(f"Coperti medi giornalieri ({scontrino_medio:.2f}€ a coperto) necessari per andare in pari: {coperti_giornalieri_necessari:.0f}")
    st.write(f"Incasso medio giornalierio con {coperti_giornalieri_necessari:.0f} coperti con uno scontrino medio di {scontrino_medio:.2f}€ : {incasso_medio_giornaliero:.2f}€")
    st.write(f"Incasso medio mensile con {coperti_giornalieri_necessari:.0f} scontrini, con uno scontrino medio di {scontrino_medio:.2f}€ : {incasso_medio_mensile:.2f}€")

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

    st.write(f"Caffè:        {num_caffe} x {prezzo_caffe:.2f}€ = {incasso_caffe:.2f} €")
    st.write(f"Cappuccini:   {num_cappuccini} x {prezzo_cappuccino:.2f}€ = {incasso_cappuccino:.2f} €")
    st.write(f"Brioches:     {num_brioche} x {prezzo_brioche:.2f}€ = {incasso_brioche:.2f} €")
    st.write(f"Pranzi:       {num_pranzi} x {prezzo_pranzo:.2f}€ = {incasso_pranzi:.2f} €")
    st.write(f"Asporto:      {num_asporto} x {prezzo_asporto:.2f}€ = {incasso_asporto:.2f} €")
    st.write(f"Birre:        {num_birre} x {prezzo_birra:.2f}€ = {incasso_birre:.2f} €")
    st.write(f"Spritz:       {num_spritz} x {prezzo_spritz:.2f}€ = {incasso_spritz:.2f} €")
    st.write(f"Drink base:   {num_drink_base} x {prezzo_drink_base:.2f}€ = {incasso_drink_base:.2f} €")
    st.write(f"Drink premium:{num_drink_premium} x {prezzo_drink_premium:.2f}€ = {incasso_drink_premium:.2f} €")
    st.write("------------------------------------------")
    st.header ("Totale")
    st.write(f"Totale Incasso Giornaliero: {incasso_totale:.2f} €")
    st.write(f"Costi materie prime: {costi_materie_prime:.2f} €")
    st.write(f"Costi materie prime mensili: {costi_materie_prime_mensili:.2f} €")
    st.write(f"Costi materie prime annuali: {costi_materie_prime_annuali:.2f} €")

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
    st.write(f"Caffè:        {num_caffe_adeguamento} x {prezzo_caffe:.2f}€ = {incasso_caffe_adeguamento:.2f} €")
    st.write(f"Cappuccini:   {num_cappuccini_adeguamento} x {prezzo_cappuccino:.2f}€ = {incasso_cappuccino_adeguamento:.2f} €")
    st.write(f"Brioches:     {num_brioche_adeguamento} x {prezzo_brioche:.2f}€ = {incasso_brioche_adeguamento:.2f} €")
    st.write(f"Pranzi:       {num_pranzi_adeguamento} x {prezzo_pranzo:.2f}€ = {incasso_pranzi_adeguamento:.2f} €")
    st.write(f"Asporto:      {num_asporto_adeguamento} x {prezzo_asporto:.2f}€ = {incasso_asporto_adeguamento:.2f} €")
    st.write(f"Birre:        {num_birre_adeguamento} x {prezzo_birra:.2f}€ = {incasso_birre_adeguamento:.2f} €")
    st.write(f"Spritz:       {num_spritz_adeguamento} x {prezzo_spritz:.2f}€ = {incasso_spritz_adeguamento:.2f} €")
    st.write(f"Drink base:   {num_drink_base_adeguamento} x {prezzo_drink_base:.2f}€ = {incasso_drink_base_adeguamento:.2f} €")
    st.write(f"Drink premium:{num_drink_premium_adeguamento} x {prezzo_drink_premium:.2f}€ = {incasso_drink_premium_adeguamento:.2f} €")
    st.write("------------------------------------------")
    st.header ("Totale")
    st.write(f"Totale Incasso Giornaliero: {incasso_totale_adeguamento:.2f} €")
    st.write(f"Costi materie prime: {costi_materie_prime_adeguamento:.2f} €")
    st.write(f"Costi materie prime mensili: {costi_materie_prime_mensili_adeguamento:.2f} €")
    st.write(f"Costi materie prime annuali: {costi_materie_prime_annuali_adeguamento:.2f} €")

    if st.button("Dettaglio"):
        # Confronto Incassi
        col1, col2 = st.columns(2)
        col1.metric("Incasso attuale", f"{incasso_totale:.2f} €")
        col2.metric("Incasso minimo necessario", f"{incasso_medio_giornaliero:.2f} €")

        # Calcolo della differenza
        delta_incasso = incasso_medio_giornaliero - incasso_totale
        col2.metric("Differenza da colmare", f"{delta_incasso:.2f} €")

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


        st.write(f"**Scontrino medio calcolato:** {scontrino_medio:.2f} €")
        st.write(f"**Scontrini giornalieri per copertura costi:** {coperti_giornalieri_necessari:.0f}")
        st.write(f"**Incasso medio giornaliero necessario:** {incasso_medio_giornaliero:.2f} €")
        st.write(f"**Incasso medio mensile necessario:** {incasso_medio_mensile:.2f} €")

    st.markdown("---")
    st.info("👉 Puoi esportare i dati manualmente o integrarli con Google Sheets/Excel per confronti più avanzati.")
