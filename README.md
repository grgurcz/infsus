# infsus
Treca domaca zadaca iz predmeta Informacijski sustavi

## Upute za instalaciju:

Pokrenuti PostgreSQL u Docker kontejneru, postaviti zaporku na `admin`

Instalirati potrebne python pakete -> `pip install -r requirements.txt`

Pozicionirati se u /infsus/ direktorij u kojem se nalazi `manage.py`

Pokrenuti skriptu za punjenje baze podataka -> `python manage.py fill_database`

Pokrenuti aplikaciju -> `python manage.py runserver`

Pokretanje testova -> `python manage.py test`
