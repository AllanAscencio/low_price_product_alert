import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "YOUR EMAIL"
PW = "YOUR PASSWORD"

URL = "https://www.amazon.com/-/es/Razer-Blade-Computadora-generaci%C3%B3n-Thunderbolt/dp/B0B44B94F9/ref=sr_1_2?crid=3HX74V6590QJK&keywords=razer%2Bblade%2B17&qid=1672926773&refinements=p_n_feature_ten_browse-bin%3A28963989011%2Cp_n_feature_seven_browse-bin%3A18107822011&rnid=562234011&s=pc&sprefix=razer%2Bblade%2B1%2Caps%2C284&sr=1-2&th=1"

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language": "es,en-GB;q=0.9,en;q=0.8,de;q=0.7"})

razer_product = response.text

soup = BeautifulSoup(razer_product, "html.parser")

price_tag = soup.find_all(name="span", class_="a-price-whole")

price_str = price_tag[0].getText()

price_int = price_str.replace(".", "")
price_final = int(price_int.replace(",", ""))


# -------------------- LOGIC --------------------------- #
if price_final < 2800:
# EMAIL CONNECTION AND SENDER #
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PW)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="allan.ascencio@gmail.com",
            msg=f"Price is below $2800 USD, you should buy NOW!\n{URL}"
        )





