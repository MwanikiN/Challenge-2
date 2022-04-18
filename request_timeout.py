""" a Python code to send a request to a web page and stop waiting for a response
after a given number of seconds. In the event of a time out on the request, raise the
timeout exception.
 """



def timeout_request(url, timeout):
    import requests
    try:
        res = requests.get(url, timeout=timeout)
    except requests.Timeout as err:
        return "Timeout exceeded"
    return res.status_code

# print(timeout_request("https://api.github.com", 0.0001))