import requests
API_key = "408423e21ee18be60fa2d1328b5abbfb"


def get_data(place, forcast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    filtered_content = filtered_content[:forcast_days*8]
    return filtered_content


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=3))
