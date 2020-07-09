import requests


def visit_website(url="http://example.com/"):
    r = requests.get(url)
    # These print statements are included, so we can see how mocking replaces the values
    print(f"The type of requests.get is: \n{type(r)}\n")
    print(f"The r.ok is: \n{r.ok}\n")
    print(f"The first 50 characters of the html is: \n{r.text[:50]}\n")
    if r.ok:
        return r.text[:50]
    else:
        return "Bad Response!"


if __name__ == "__main__":
    visit_website()
