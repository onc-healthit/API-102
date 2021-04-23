import requests

base_url = "https://healthit.gov/test-method"
criterion = "standardized-api-patient-and-population-services"


entity_ids = requests.get("{}/{}?_format=json".format(base_url, criterion))
print(entity_ids.json())