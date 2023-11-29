import requests
import re

url = "http://www.columbia.edu/~fdc/sample.html"


def getH3(url):
    response = requests.get(url)
    htmlText = response.text

    pattern = re.compile(r'<h3.*?>(.*?)</h3>')
    result = pattern.findall(htmlText)

    return result


subheadingsList = getH3(url)
print(subheadingsList)