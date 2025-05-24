# portSniff

## Beskrivning
portSniff är ett enkelt portskanningsverktyg skrivet i Python. Det låter dig skanna en specifik IP-adress för öppna och stängda portar inom ett angivet intervall. Verktyget identifierar även tjänster och kategoriserar dem baserat på portnummer.

## Funktioner
- Skanna öppna och stängda portar.
- Identifiera tjänster kopplade till portar.
- Kategorisammanställning av tjänster.
- Färgad terminalutskrift med hjälp av `colorama`.

## Installation
1. Klona detta repository:
   ```bash
   git clone <repository-url>
   cd portsniffer# portSniff
2. Installera beroenden
    ```bash
    pip install -r requirements.txt

## Användning
1. Kör programmet:
    ```bash
    python scanner.py
2. Ange IP-adress, startport och slutport när du blir ombedd.

## Exempel
```plaintext
Ange IP-adress att scanna: 192.168.1.1
Startport: 20
Slutport: 25

Scannar 192.168.1.1 från port 20 till 25...

[+] Port 22 är ÖPPEN - SSH
[-] Port 23 är stängd
...
```

## Beroenden
- Python 3.x
- `colorama` (installeras via `requirements.txt`)

## Licens
Detta projekt är licensierat under MIT-licensen.