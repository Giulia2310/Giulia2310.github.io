# Portfolio — Giulia La Paglia

Sito ricostruito da zero in HTML / CSS / JS puro, a partire dal portfolio
Webflow (https://vt545yc654wty45cct45wcct5c3q.webflow.io/), pronto per
essere pubblicato su GitHub Pages.

## Struttura del progetto

```
portfolio-site/
├── index.html                  → Home
├── curriculum.html             → Curriculum
├── projects/
│   ├── fairly-tails.html
│   ├── genova-matsuri.html
│   ├── curricraft.html
│   ├── ringo-tropicale.html
│   └── iconography-and-iconology.html
├── css/style.css               → tutto lo stile del sito
├── js/main.js                  → menu, marquee, rotazione titoli hero
└── images/
    ├── projects/                → immagini principali/secondarie dei progetti
    └── gallery/                 → immagini della galleria di ogni progetto
```

## Palette e font (come richiesto)

- Accent: `#fc5071`
- Dark: `#1a1a1a`
- Light: `#ededed`
- Titoli: **Plus Jakarta Sans** (Google Fonts)
- Testi: **Satoshi** (Fontshare)

Entrambi i font sono caricati via CDN nell'`<head>` di ogni pagina — non
serve installare nulla, funzionano appena il sito è online. Se preferisci
averli in locale nel repo (invece che via CDN), posso preparare anche
quella versione.

## Immagini: sostituire i placeholder con le foto vere

Per adesso ogni immagine è un **placeholder generato** con la palette del
sito (li riconosci dal nome del progetto scritto sopra), così il sito è già
completamente navigabile. Le foto vere del tuo Webflow **non sono state
scaricate automaticamente** (il dominio Webflow non è raggiungibile dal
mio ambiente), quindi vanno sostituite a mano: basta scaricare ogni
immagine dal link qui sotto (tasto destro → "Salva immagine come") e
salvarla nella cartella `images/...` con **lo stesso nome** già presente
nel progetto, così i file HTML la trovano subito.

### Fairly Tails
| File locale | Immagine originale |
|---|---|
| `images/projects/fairly-tails.webp` | [scatole-tutti](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e859b0b2771ec9c42e0c_FairlyTales-scatole-tutti.webp) |
| `images/projects/fairly-tails-render.webp` | [render](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e95cd3e99c19b99658ee_FairlyTales-render.webp) |
| `images/gallery/fairly-tails-1.webp` | [Giappone](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85d81cb6e274e672714_Giappone_il%20matrimonio%20della%20topolina_rosa.webp) |
| `images/gallery/fairly-tails-2.webp` | [Danimarca](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85e7462d1ffa5207efc_Danimarca_il%20principe%20biancorso_viola.webp) |
| `images/gallery/fairly-tails-3.webp` | [India](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85ece8f7179fe785467_India_la%20volpe%20e%20il%20bramino_verde.webp) |
| `images/gallery/fairly-tails-4.webp` | [Nord America](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85dbd05c4ec28ea1949_Nord%20America_come%20il%20coyote%20rub%C3%B2%20il%20fuoco_verdeacqua.webp) |

### Genova Matsuri
| File locale | Immagine originale |
|---|---|
| `images/projects/genova-matsuri.webp` | [Brochure](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e7a0033d31229b378980_Brochure%20copia.webp) |
| `images/projects/genova-matsuri-mockup.webp` | [mockup social](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e87773645b7c8c21e319_mockup%20social.webp) |
| `images/gallery/genova-matsuri-1.webp` | [ambiente01](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8827462d1ffa520915e_ambiente01.webp) |
| `images/gallery/genova-matsuri-2.webp` | *placeholder generico Webflow* (nel sito originale) |
| `images/gallery/genova-matsuri-3.webp` | [Tavola da disegno 2](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8821b9ff789277216b9_Tavola%20da%20disegno%202.webp) |
| `images/gallery/genova-matsuri-4.webp` | *placeholder generico Webflow* (nel sito originale) |

### CurriCraft
| File locale | Immagine originale |
|---|---|
| `images/projects/curricraft.webp` | [WebDesign_1](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e89d6c7acfa242c7a69a_WebDesign_1.webp) |
| `images/projects/curricraft-secondary.webp` | [WebDesign_2](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8a26f6a051ed0ddf3c4_WebDesign_2.webp) |
| `images/gallery/curricraft-1.webp` | [WebDesign-pagine](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e92bd847827794eaaa0e_WebDesign-pagine.webp) |
| `images/gallery/curricraft-2.webp` | *placeholder generico Webflow* |
| `images/gallery/curricraft-3.webp` | *placeholder generico Webflow* |
| `images/gallery/curricraft-4.webp` | *placeholder generico Webflow* |

### Ringo Tropicale
| File locale | Immagine originale |
|---|---|
| `images/projects/ringo-tropicale.webp` | [cerchio mano](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8bed2100cf06d593ebe_cerchio%20mano.webp) |
| `images/projects/ringo-tropicale-gusti.webp` | [RingoTropicale_gusti](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8cecda1f1354fb723e1_RingoTropicale_gusti.webp) |
| `images/gallery/ringo-tropicale-1.webp` | [cerchio aprendo](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8d80f8bfcfce79386ef_cerchio%20aprendo.webp) |
| `images/gallery/ringo-tropicale-2.webp` | *placeholder generico Webflow* |
| `images/gallery/ringo-tropicale-3.webp` | [cerchio render finale](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8d8c403085c1a9b3e16_cerchio%20render%20finale.webp) |
| `images/gallery/ringo-tropicale-4.webp` | *placeholder generico Webflow* |

### Iconography and Iconology
| File locale | Immagine originale |
|---|---|
| `images/projects/iconography-iconology.webp` | [StoriaSocialeArte_2](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e913bcde832dc28edf3b_StoriaSocialeArte_2.webp) |
| `images/projects/iconography-secondary.webp` | [StoriaSocialeArte_6](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e91a4e6eeb8778232b58_StoriaSocialeArte_6.webp) |
| `images/gallery/iconography-1.webp` | [StoriaSocialeArte_1](https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e9227d0b7c41c3e59d90_StoriaSocialeArte_1.webp) |
| `images/gallery/iconography-2.webp` | *placeholder generico Webflow* |
| `images/gallery/iconography-3.webp` | *placeholder generico Webflow* |
| `images/gallery/iconography-4.webp` | *placeholder generico Webflow* |

> Le voci "placeholder generico Webflow" corrispondono a immagini stock
> del template originale (non foto tue) — è il momento buono per
> sostituirle con scatti reali dei progetti, se li hai.

Le immagini possono restare in formato `.webp` (leggero e già supportato
da tutti i browser moderni) oppure essere sostituite con `.jpg`/`.png`,
aggiornando semplicemente l'estensione nel relativo file HTML.

## Pubblicare su GitHub Pages

1. Crea un nuovo repository su GitHub (es. `portfolio`).
2. Carica **tutto il contenuto** di questa cartella nella root del
   repository (non la cartella `portfolio-site` stessa, ma i file al suo
   interno).
3. Vai su **Settings → Pages**, seleziona come source il branch
   principale (`main`) e la cartella `/ (root)`.
4. Dopo qualche minuto il sito sarà online su
   `https://<tuo-username>.github.io/<nome-repo>/`.

## Provare il sito in locale

Basta aprire `index.html` con un browser, oppure — per evitare eventuali
limitazioni del browser su file locali — lanciare un piccolo server dalla
cartella del progetto:

```
python3 -m http.server 8000
```

e visitare `http://localhost:8000`.
