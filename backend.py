import requests


def get_data(place, forcast_days, API_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    filtered_content = filtered_content[:forcast_days*8]
    return filtered_content


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=3))
