import requests

# Gets IP address of the user
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

# Gets data by taking IP as an input
def get_data(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    data = {
        "ip": ip_address,
        "version": response.get('version') or "N/A",
        "city": response.get("city") or "N/A",
        "region": response.get("region") or "N/A",
        "country": response.get("country_name") or "N/A",
        "latitude": response.get("latitude") or "N/A",
        "longitude": response.get("longitude") or "N/A",
        "postal": response.get("postal") or "N/A",
        "org": response.get("org") or "N/A",
    }
    return data