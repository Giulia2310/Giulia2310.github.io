# Giulia La Paglia — Portfolio

Sito portfolio statico (HTML/CSS/JS puro, nessuna build necessaria) — copia
ricreata a mano del sito Webflow
[vt545yc654wty45cct45wcct5c3q.webflow.io](https://vt545yc654wty45cct45wcct5c3q.webflow.io/),
stesse pagine e stessi contenuti, pronta per essere pubblicata su GitHub
Pages.

## Design

| Token | Valore |
|---|---|
| Accent | `#fc5071` |
| Dark | `#1a1a1a` |
| Light | `#ededed` |
| Font titoli | [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) (Google Fonts) |
| Font testi | [Satoshi](https://www.fontshare.com/fonts/satoshi) (Fontshare) |

Tutti i colori e i font sono definiti come variabili CSS in cima a
[`css/style.css`](css/style.css) — per cambiarli basta modificare quelle
righe, si aggiornano ovunque.

## Struttura

```
index.html                                  Home
curriculum/index.html                       Curriculum
projects/fairly-tails/index.html            Progetto
projects/genova-matsuri/index.html          Progetto
projects/officine-iadr/index.html           Progetto
projects/ringo-tropicale/index.html         Progetto
projects/iconography-and-iconology/index.html   Progetto
404.html                                     Pagina errore
css/style.css                                Tutti gli stili
js/main.js                                   Menu a scomparsa + animazioni allo scroll
images/                                      Le tue immagini (vedi IMAGES.md)
```

Le pagine usano cartelle con `index.html` così gli indirizzi restano puliti,
identici all'originale: `/curriculum/`, `/projects/fairly-tails/`, ecc.

## Immagini

Le immagini **non sono incluse** — vanno caricate a mano nella cartella
[`images/`](images). L'elenco preciso dei nomi file richiesti (e dove viene
usata ciascuna) è in [`IMAGES.md`](IMAGES.md). Finché un file non c'è, il sito
mostra un riquadro grigio al suo posto invece di un errore.

## Anteprima in locale

Sono solo file statici: puoi aprire `index.html` direttamente nel browser, ma
per vedere gli indirizzi puliti (`/curriculum/` invece di
`/curriculum/index.html`) conviene usare un piccolo server locale, ad esempio
uno di questi (da eseguire nella cartella del progetto):

```bash
npx serve .
```

oppure, con Python già installato:

```bash
python -m http.server 8000
```

## Pubblicare su GitHub Pages

1. Crea un repository su GitHub e carica (push) il contenuto di questa
   cartella.
2. Nel repository, vai su **Settings → Pages**.
3. In **Source**, seleziona il branch principale (es. `main`) e la cartella
   `/ (root)`.
4. Salva: dopo un minuto il sito sarà online all'indirizzo
   `https://<tuo-utente>.github.io/<nome-repository>/`.

Tutti i link interni del sito usano percorsi relativi, quindi funzionano sia
se il sito è pubblicato alla radice di un dominio, sia se è pubblicato in un
sottopercorso come `/nome-repository/`.

## Cose volutamente diverse dal sito Webflow originale

- **Font**: nel sito Webflow live i font "Clashdisplay" e "Crimsonpro" erano
  impostati ma non caricavano davvero (mancava l'embed), quindi il sito
  mostrava i font di riserva del browser. Qui invece Plus Jakarta Sans e
  Satoshi sono collegati correttamente e si vedono come previsto.
- **Colore accent**: il sito Webflow usava ancora `#ff6f61` (arancione,
  colore di default del template) in alcuni punti; qui è stato sostituito
  ovunque con `#fc5071` come richiesto.
- **Interazioni**: le animazioni (menu, testo rotante nell'hero, ticker a
  scorrimento, comparsa delle sezioni allo scroll) sono state ricreate in CSS/JS
  puro al posto delle interazioni proprietarie di Webflow — stesso effetto
  visivo, senza dipendere da Webflow.
