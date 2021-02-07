from bs4 import BeautifulSoup


def parser(tag, id):
    soup = BeautifulSoup(open("ARAYUZ/text.html", "r", encoding="utf8").read(), "html.parser")

    a = soup.find(tag, attrs={"id": id})

    return str(a)

