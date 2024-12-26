from seleniumbase import *
import random
import string
import csv
from supabase import create_client, Client


SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "fans"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

email = 'glen60@marattok.com'

counter = 0

def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))


with SB(undetectable=True) as sb:

  

    sb.open("https://scryfall.com/signin?return_path=%2Fsettings%2Fprofile&status=303")
    sb.sleep(5)

    sb.type("#email",email)
    sb.sleep(2)

    sb.click("body > div:nth-child(1) > form:nth-child(6) > button:nth-child(6) > span:nth-child(1)")
    sb.sleep(10)

    first_window = sb.driver.current_window_handle


    sb.open(f"https://generator.email/{email}")
    sb.sleep(5)

    sb.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sb.sleep(1)
    # sb.click('.alt-link')
    # sb.sleep(5)
    url_value = sb.get_attribute(".alt-link", "href")

    sb.open(url_value)
    sb.sleep(3)



    # sb.switch_to_window(1)
    # sb.sleep(1)
    sb.click("button[type='submit']")
    sb.sleep(3)


    with open("x.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            kw = line[0]

            judul =f'{kw} Onlyfans Leaked - Update files ({random_string(5)})' 


            kalimat = kw
            kata_pertama = kalimat.split()[0]
            


            sb.open("https://scryfall.com/account/decks/new")
            sb.sleep(5)


            sb.click("button[name='template'] span[class='deck-wizard-category-stage'] b")
            sb.sleep(2)


            sb.clear("#name")
            sb.sleep(2)
            sb.type("#name",judul)
            sb.sleep(2)

            # konten = f'COPY THIS LINK >> https://clipsfans.com/{kata_pertama} << Get latinsexyter Onlyfans leaked content & files. Updated! Just Copy and Paste the following URL on your browser: >>> https://clipsfans.com/{kata_pertama} <<<'
            konten2 =f'COPY THIS LINK ▶️ https://clipsfans.com/{kata_pertama} ◀️ Get latinsexyter Onlyfans leaked content & files. Updated! Just Copy and Paste the following URL on your browser: ▶️▶️ https://clipsfans.com/{kata_pertama} ◀️◀️ '

            
            # sb.execute_script(f"document.querySelector('#description').innerHTML = 'COPY THIS LINK ▶️ https://clipsfans.com/{kata_pertama} ◀️ Get latinsexyter Onlyfans leaked content & files. Updated! Just Copy and Paste the following URL on your browser: 👉 🔗 ▶️▶️ https://clipsfans.com/{kata_pertama} ◀️◀️ 🔗 👈'")

            sb.sleep(2)
            sb.type("#description",konten2)
            sb.sleep(1)


            sb.click("a[class='button-n tiny primary'] b")
            sb.sleep(2)
            sb.click("a[class='button-n tiny primary'] b")

            sb.sleep(2)
            response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": sb.get_current_url()})
            .execute()
            )

            sb.sleep(2)

            sb.open("https://scryfall.com/account/decks/new")

