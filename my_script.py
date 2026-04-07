import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scam_project.settings')
django.setup()


from scams.models import Scam

def main():
    print("ok")

if __name__ == "__main__":

    #create a new scam:
    Scam.objects.create(
    title="Scam phone call",
    description="Trying to get credit card info",
    scam_type="phishing",
    date_seen="2026-04-01",
    url_or_contact="076 579 46 34"
    )
    
    #read existing data
    scams = Scam.objects.all().values()
    df = pd.DataFrame(scams)
    print(df)
    
    #filter
    Scam.objects.filter(scam_type="phishing")
    Scam.objects.filter(date_seen__year=2026)
    
    #delete a scam
    Scam.objects.get(title="Scam phone call").delete()

    #read existing data
    scams = Scam.objects.all().values()
    df = pd.DataFrame(scams)
    print(df)
    main()