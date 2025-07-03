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

print("=== INVESTIMENTO INIZIALE ===")

print(f"Investimento iniziale ad oggi: {totale_attrezzature:.2f}€")
print(f"Rata mensile restituzione prestito: {restituzione_prestito:.2f}€")
print(f"Tempo restituzione prestito: {tempi_restituzione_prestito:.0f} anni")




# Output
print("\n=== DETTAGLIO COPERTI ===")
print(f"Costi fissi mensili totali (dipendenti + affitto + luce + materie prime): {costi_fissi_mensili:.2f}€")
print(f"Costi fissi annuali totali (dipendenti + affitto + luce + materie prime): {costi_fissi_annuali:.2f}€")
#print(f"Incasso annuo stimato attuale: {incasso_annuale_attuale:.2f}€")
print(f"Coperti medi giornalieri ({scontrino_medio:.2f}€ a coperto) necessari per andare in pari: {coperti_giornalieri_necessari:.0f}")
print(f"Incasso medio giornalierio con {coperti_giornalieri_necessari:.0f} coperti con uno scontrino medio di {scontrino_medio:.2f}€ : {incasso_medio_giornaliero:.2f}€")
print(f"Incasso medio mensile con {coperti_giornalieri_necessari:.0f} scontrini, con uno scontrino medio di {scontrino_medio:.2f}€ : {incasso_medio_mensile:.2f}€")

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
num_caffe = 120
num_cappuccini = 30
num_brioche = 20
num_pranzi = 60
num_asporto = 20
num_birre = 20
num_spritz = 30
num_drink_base = 20
num_drink_premium = 10

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
print("\n=== DETTAGLIO INCASSO GIORNALIERO BASATO SU STATISTICHE DI UN BAR IN CENTRO STORICO (50.000 abitanti/città) ===")
print(f"Caffè:        {num_caffe} x {prezzo_caffe:.2f}€ = {incasso_caffe:.2f} €")
print(f"Cappuccini:   {num_cappuccini} x {prezzo_cappuccino:.2f}€ = {incasso_cappuccino:.2f} €")
print(f"Brioches:     {num_brioche} x {prezzo_brioche:.2f}€ = {incasso_brioche:.2f} €")
print(f"Pranzi:       {num_pranzi} x {prezzo_pranzo:.2f}€ = {incasso_pranzi:.2f} €")
print(f"Asporto:      {num_asporto} x {prezzo_asporto:.2f}€ = {incasso_asporto:.2f} €")
print(f"Birre:        {num_birre} x {prezzo_birra:.2f}€ = {incasso_birre:.2f} €")
print(f"Spritz:       {num_spritz} x {prezzo_spritz:.2f}€ = {incasso_spritz:.2f} €")
print(f"Drink base:   {num_drink_base} x {prezzo_drink_base:.2f}€ = {incasso_drink_base:.2f} €")
print(f"Drink premium:{num_drink_premium} x {prezzo_drink_premium:.2f}€ = {incasso_drink_premium:.2f} €")
print("------------------------------------------")
print(f"Totale Incasso Giornaliero: {incasso_totale:.2f} €")
print(f"Costi materie prime: {costi_materie_prime:.2f} €")
print(f"Costi materie prime mensili: {costi_materie_prime_mensili:.2f} €")
print(f"Costi materie prime annuali: {costi_materie_prime_annuali:.2f} €")

#DETTAGLIO CON ADEGUAMENTO

# === Quantità vendute giornalmente (stimate per un bar in centro storico) con adeguamento===
adeguamento = incasso_medio_giornaliero/incasso_totale*1.03
num_caffe_adeguamento = int(adeguamento * 120)
num_cappuccini_adeguamento = int(adeguamento * 30)
num_brioche_adeguamento = int(adeguamento * 20)
num_pranzi_adeguamento = int(adeguamento * 60)
num_asporto_adeguamento = int(adeguamento * 20)
num_birre_adeguamento = int(adeguamento * 20)
num_spritz_adeguamento = int(adeguamento * 30)
num_drink_base_adeguamento = int(adeguamento * 20)
num_drink_premium_adeguamento = int(adeguamento * 10)

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
print("\n=== DETTAGLIO INCASSO GIORNALIERO CON ADEGUAMENTO ALL'INCASSO MINIMO ===")
print(f"Caffè:        {num_caffe_adeguamento} x {prezzo_caffe:.2f}€ = {incasso_caffe_adeguamento:.2f} €")
print(f"Cappuccini:   {num_cappuccini_adeguamento} x {prezzo_cappuccino:.2f}€ = {incasso_cappuccino_adeguamento:.2f} €")
print(f"Brioches:     {num_brioche_adeguamento} x {prezzo_brioche:.2f}€ = {incasso_brioche_adeguamento:.2f} €")
print(f"Pranzi:       {num_pranzi_adeguamento} x {prezzo_pranzo:.2f}€ = {incasso_pranzi_adeguamento:.2f} €")
print(f"Asporto:      {num_asporto_adeguamento} x {prezzo_asporto:.2f}€ = {incasso_asporto_adeguamento:.2f} €")
print(f"Birre:        {num_birre_adeguamento} x {prezzo_birra:.2f}€ = {incasso_birre_adeguamento:.2f} €")
print(f"Spritz:       {num_spritz_adeguamento} x {prezzo_spritz:.2f}€ = {incasso_spritz_adeguamento:.2f} €")
print(f"Drink base:   {num_drink_base_adeguamento} x {prezzo_drink_base:.2f}€ = {incasso_drink_base_adeguamento:.2f} €")
print(f"Drink premium:{num_drink_premium_adeguamento} x {prezzo_drink_premium:.2f}€ = {incasso_drink_premium_adeguamento:.2f} €")
print("------------------------------------------")
print(f"Totale Incasso Giornaliero: {incasso_totale_adeguamento:.2f} €")
print(f"Costi materie prime: {costi_materie_prime_adeguamento:.2f} €")
print(f"Costi materie prime mensili: {costi_materie_prime_mensili_adeguamento:.2f} €")
print(f"Costi materie prime annuali: {costi_materie_prime_annuali_adeguamento:.2f} €")
