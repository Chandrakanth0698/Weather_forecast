import requests
API_key = "408423e21ee18be60fa2d1328b5abbfb"


def get_data(place, forcast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    filtered_content = filtered_content[:forcast_days*8]
    if kind == "Temperature":
        filtered_content = [observation["main"]["temp"] for observation in filtered_content]
    else:
        filtered_content = [observation["weather"][0]["main"] for observation in filtered_content]

    return filtered_content


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=3, kind="Sky"))
