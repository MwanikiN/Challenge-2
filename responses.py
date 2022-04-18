""" python function to retrieve url requests """
def url_requests(url):
    import requests
    response = requests.get(url)
    return response.text, response.content, response.raw.read(10)

# print(url_requests("https://api.google.com"))