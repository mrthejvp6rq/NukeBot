# Nukebot - Discord Bot

## Opis projektu
Nukebot to prosty bot na Discorda, który jest moim pierwszym samodzielnie zaprogramowanym projektem. Bot został stworzony w celach edukacyjnych, aby nauczyć się podstaw programowania oraz integracji z API Discorda.

## Funkcje
- Usuwanie wszystkich kategorii i kanałów z serwera.
- Banowanie członków (z wyjątkiem właściciela i botów).
- Tworzenie nowych kanałów tekstowych o wybranej nazwie.

## Wymagania
- Python 3.8 lub nowszy
- Biblioteka `discord.py`
- Plik konfiguracyjny `config.py` zawierający:
  ```python
  prefix = 'TwójPrefix'
  token = 'TwójTokenDiscord'
  ```

## Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/mrthejvp6rq/NukeBot
   ```
2. Przejdź do katalogu projektu:
   ```bash
   cd Nukebot
   ```
3. Zainstaluj wymagane zależności:
   ```bash
   pip install discord.py
   ```
4. Upewnij się, że masz plik `config.py` z odpowiednim tokenem bota.

## Uruchomienie
Aby uruchomić bota, wykonaj następujące polecenie:
```bash
python main.py
```

## Przestrogi
- **Nukebot** został stworzony wyłącznie w celach edukacyjnych. Pamiętaj, aby przestrzegać zasad Discorda i używać bota odpowiedzialnie.
- Funkcje bota mogą być destrukcyjne dla serwera Discord. Używaj go wyłącznie w testowych środowiskach lub za zgodą właściciela serwera.

---


