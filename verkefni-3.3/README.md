1. Nánast sama dótið nema webservice er eldra, ekki open source og hægara. web api er nýrra og liðugara.

2. ```json
    pizza = {
      "crust": "original",
      "toppings": ["cheese", "pepperoni", "garlic"],
      "status": "cooking",
      "customer": {
        "name": "Örn Óli",
        "phone": "1123445
      }
    }
   ```

  ```xml
    <pizza>
      <crust>original</crust>
      <toppings>
        <topping>cheese</topping>
        <topping>pepperoni</topping>
        <topping>garlic</topping>
      </toppings>
      <status>cooking</status>
      <customer>
        <name>Örn Óli</name>
        <number>1234556</number>
      </customer>
    </pizza>
  ```

3.
    1. hér er allt rafmagnið með núll og einn að flæða
    2. hér er pakkað in stuffi til að senda sem núll og einn
    3. flugstjórnin er hér að stjórna mismunandi tengingum
    4. sentir pakkar á milli hér
    5. hérna erum við í beinu sambandi við eitthvern
    6. tölum við forrit hér
    7. hérna er góða stuffið

4. API sem notar HTTP requests til að fá skrá og eyða gögnum

5.
    1. start line með hvaða method er verið að nota, hvert ég er að fara, og HTTP version
       header með allskonar upplýsingum um sendanda, skilaboðin og tenginguna
       body er bara upplysingar um hvað var að gerast, ef þú villt hafa það

    2. start line með protocol version, status code og ehv smá texti svo þetta sé læsilegt
       header með allskonar upplýsingum...
       body er kannski með upplýsingum, kannski ekki... fer eftir hvað þú varst að biðja um

6. Þetta gerir þér kleyft að nota aðra aðganga á öðrum síðum, eins og þegar maður loggar
   sig inná síðu og ýtir á facebook takkan

7. $ curl "http://api.soundcloud.com/playlists/405726?client_id=CLIENT_ID_MITT_VÆRI_HÉR_EF_SOUNDCLOUD_VÆRI_EKKI_BÖGGANDI"
   svo fengi ég bara ehv frábært json svar

9. ```python
     # pip install geolocation-python
     from geolocation.main import GoogleMaps
     address = "Reykjavík"
     gmaps = GoogleMaps(api_key='ætla ekki að setja hann á github')
     location = gmaps.search(location=address)
     result = location.first()
     print(result.lat)
     print(result.lng)
   ```