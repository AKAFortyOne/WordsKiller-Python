import csv
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

with open("cet4+6.csv", newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        rawWord = row["Words"]
        print(rawWord)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents="Explain how AI works in a few words"
        )
        print(response.text)