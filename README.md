# crypto-status
Wyświetlanie cen kryptowalut w pasku status dla bumblebee-status version 2.2.0

## instalacja
Instalacja bumblebee-status dla Debian 12:
`pip install bumblebee-status --break-system-packages`
aktualizacja
`pip install --upgrade bumblebee-status --break-system-packages`

Uruchomienie skryptu jako usługa systemowa:

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

Wgranie modułu `crypto_price.py` do bumblebee-status:
plik umieścić w katalogu z modułami np.:
`/home/pc/.local/lib/python3.11/site-packages/bumblebee_status/modules/contrib`

Konfiguracja w pliku config dla i3wm np.:
w pliku `config` w sekcji bar dodać wpis modułu `"-m crypto_price"`
```
bar{
        font pango: Hack Nerd Font 7
        output DP-4
        position top

        status_command /usr/bin/bumblebee-status -m crypto_price git traffic nic publicip uptime time -p nic.exclude=lo -p traffic.exclude -p configfile=~/.config/bumblebee-status/bumblebee_status.toml -t iceberg-dark-powerline 
}
```
