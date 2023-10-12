import requests
import json
from datetime import datetime, timedelta


def api(searched_date, latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude="
        f"{latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date="
        f"{searched_date}&end_date={searched_date}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print("Nie pobrano danych o pogodzie na wyznaczony dzień.")


def pogoda(data):
    rain_sum = data["daily"]["rain_sum"]
    rain_sum = sum(rain_sum)
    if rain_sum > 0:
        print("Będzie padać :( ")
    elif rain_sum == 0:
        print("Nie będzie padać :) ")
    else:
        print("Nie wiem.")


def wynik_zapisz(data):
    with open("pogoda.txt", "w") as plik:
        plik.write(json.dumps(data))


def wynik_odczytaj(data):
    try:
        with open("pogoda.txt", "r") as plik:
            data = json.load(plik)
            return data
    except FileNotFoundError:
        return None


def main():
    latitude = 50.866077
    longitude = 20.628569
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    next_day = tomorrow.strftime("%Y-%m-%d")
    searched_date = input(
        "\nPodaj dzień na który mam sprawdzić pogodę (miasto Kielce), np. 2023-11-03: "
    )
    if searched_date:
        searched_date = searched_date

    else:
        print(
            f"\nBrak podania daty, została pobrana pogoda na dzień jutrzejszy tj. {next_day}"
        )
        searched_date = next_day

    data = api(searched_date, latitude, longitude)
    data2 = api(next_day, latitude, longitude)
    pobrane_dane = wynik_odczytaj(data)

    if pobrane_dane:
        try:
            pogoda(data)
        except TypeError:
            print(f"\nZostała pobrana pogoda na dzień jutrzejszy tj. {next_day}")
            pogoda(data2)
        print(f'Pogoda dla dnia {searched_date} pobrana z pliku "pogoda.txt"')
    else:
        api(searched_date, latitude, longitude)

    wynik_odczytaj(data)
    wynik_zapisz(data)


if __name__ == "__main__":
    main()
