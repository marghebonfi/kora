import streamlit as st
import matplotlib.pyplot as plt
import dati

def mostra_introduzione():
    st.title("KORA")
    st.header("🌱 Chi siamo")
    st.write("Benvenuto! Siamo una coppia unita dalla passione per il cibo etico, il rispetto per gli animali e la sostenibilità. Il nostro sogno è aprire un locale a Cuneo, che non sia solo un luogo dove mangiare e bere bene, ma uno spazio vivo e multifunzionale, che unisca cucina vegetale, artigianato e cultura.")
    st.header("🥗 Cosa vogliamo realizzare")
    st.write("Il nostro locale sarà 100% vegetale, con prodotti provenienti da fornitori locali, colazioni, pranzi e aperitivi artigianali. Il piano superiore sarà uno spazio dedicato alla cultura, al co-working e galleria d’arte per artisti emergenti della zona. Sarà un luogo inclusivo, sostenibile, aperto alla comunità. Vogliamo offrire non solo cibo, ma anche cultura, ispirazione e condivisione.")
    st.write("""Puoi navigare tra:
    \n- Il **business plan** (investimenti, costi fissi, break-even, analisi stagionalità)
    \n- Una sezione di **simulazione dinamica** giornaliera
    \n- Una sezione di **analisi dei rischi e sviluppi futuri**
    """)
def mostra_business_plan():

    st.title("📊 Business Plan")
# === Costi Attrezzature ===


    st.header("Investimento iniziale")

    st.write(f"Investimento iniziale ad oggi: {dati.totale_attrezzature:,.2f}€")
    st.write(f"Rata mensile restituzione prestito: {dati.restituzione_prestito:,.2f}€")
    st.write(f"Tempo restituzione prestito: {dati.tempi_restituzione_prestito:.0f} anni")
    with st.expander("🔍 Dettaglio"):
        for voce, valore in dati.voci.items():
            st.write(f"{voce}: {valore:>10,.2f}€")
        st.write(f"**Totale: {dati.totale_attrezzature:>10,.2f}€**")
    st.divider()

    st.header("Dettaglio costi e coperti necessari")
    # Ricavo medio per coperto (approssimazione)
    with st.expander("🧾 Modifica parametri per scontrino medio"):
        st.markdown("Personalizza la quantità e il valore medio per categoria.")
        incasso_medio_giornaliero=dati.input_numeri_per_pasto()
    # === Quantità vendute giornalmente (stimate per un bar in centro storico) ===
    st.header("Dettaglio incasso giornaliero basato su statistiche di un bar in centro storico (50.000 abitanti/città)")
    with st.expander("🔧 Modifica volumi giornalieri (opzionale)"):
        st.markdown("Inserisci qui i valori stimati per ogni voce di incasso giornaliero.")
        dati_input_numeri_alimenti(incasso_medio_giornaliero)



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
