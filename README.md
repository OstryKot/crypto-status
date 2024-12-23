# crypto-status
Wyświetlanie cen kryptowalut za pomocą modułu ***crypto_status.py*** w pasku statusu dla **bumblebee-status version 2.2.0**. Odczyt cen krytowalut z Binance za pomocą skryptu ***crypto_price.py*** uruchomionego jako usługa systemowa.

- [uruchomienie skryptu jako usługi systemowej](#uruchomienie-skryptu-jako-usługa-systemowa)
- [instalacja modułu](#instalacja-modułu) 

## instalacja
### instalacja bumblebee-status dla Debian 12:

`pip install bumblebee-status --break-system-packages`
aktualizacja
`pip install --upgrade bumblebee-status --break-system-packages`

### uruchomienie skryptu jako usługa systemowa:

Utwórz plik usługi `sudo nano /etc/systemd/system/crypto_status.service`

Wpisz następującą konfigurację do pliku:
```
[Unit]
Description=My Python Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/your_username/crypto_status.py
WorkingDirectory=/home/your_username
StandardOutput=inherit
StandardError=inherit
Restart=always
User=your_username

[Install]
WantedBy=multi-user.target
```

Zastąp `your_username` swoją nazwą użytkownika i `/home/your_username/crypto_status.py` ścieżką do swojego skryptu.

Aktywacja usługi `sudo systemctl enable crypto_status.service` następnie uruchomienie usługi 
`sudo systemctl start crypto_status.service`

### instalacja modułu

Wgranie modułu `crypto_price.py` do bumblebee-status. Plik umieścić w katalogu z modułami.
`/home/pc/.local/lib/python3.11/site-packages/bumblebee_status/modules/contrib`

### konfiguracja w pliku config dla i3 window manager

Przykład konfiguracji w pliku `config` w sekcji bar dodać wpis modułu `"-m crypto_price"`
```
bar{
        font pango: Hack Nerd Font 7
        output DP-4
        position top

        status_command /usr/bin/bumblebee-status -m crypto_price git traffic nic publicip uptime time -p nic.exclude=lo -p traffic.exclude -p configfile=~/.config/bumblebee-status/bumblebee_status.toml -t iceberg-dark-powerline 
}
```
