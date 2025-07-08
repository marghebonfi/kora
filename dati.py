import streamlit as st
import pandas as pd

voci = {
        "Cucina e attrezzatura bar": 100000,
        "Macchina del caffè": 13000,
        "Bancone bar": 20000,
        "Utensili vari bar e cucina": 7500,
        "Piatti e tazzine": 6600,
        "Arredamento": 35000,
        "Ristrutturazione": 30000,
        "Piastrelle e sanitari": 10000,
        "Impianti": 10000,
        "Infissi": 5000,
        "Termosifoni e posa": 10000,
        "Architetti e pratiche": 8000,
        "Luci (ipotesi media)": 4000
    }


# Calcolo della somma totale
totale_attrezzature = sum(voci.values())


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

def input_numeri_per_pasto():
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
        # Coperti necessari giornalieri per andare in pari
        coperti_annuali_necessari = costi_fissi_annuali / scontrino_medio
        coperti_giornalieri_necessari = coperti_annuali_necessari / 250
        incasso_medio_giornaliero = coperti_giornalieri_necessari * scontrino_medio
        incasso_medio_mensile = incasso_medio_giornaliero * 250 / 12

        st.write(f"**Scontrino medio calcolato:** {scontrino_medio:,.2f} €")

        # Output

        st.write(f"Costi fissi mensili totali (dipendenti + affitto + luce + materie prime): {costi_fissi_mensili:,.2f}€")
        st.write(f"Costi fissi annuali totali (dipendenti + affitto + luce + materie prime): {costi_fissi_annuali:,.2f}€")
        #print(f"Incasso annuo stimato attuale: {incasso_annuale_attuale:,.2f}€")
        st.write(f"Scontrini medi giornalieri ({scontrino_medio:,.2f}€ a coperto) necessari per coprire i costri: {coperti_giornalieri_necessari:.0f}")
        st.write(f"Incasso medio giornalierio con {coperti_giornalieri_necessari:.0f} scontrini, scontrino medio di {scontrino_medio:,.2f}€ : {incasso_medio_giornaliero:,.2f}€")
        st.write(f"Incasso medio mensile con {coperti_giornalieri_necessari:.0f} scontrini, con uno scontrino medio di {scontrino_medio:,.2f}€ : {incasso_medio_mensile:,.2f}€")
        return(incasso_medio_giornaliero)

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

def dati_input_numeri_alimenti(incasso_medio_giornaliero):
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

