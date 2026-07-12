from google import genai
from confi import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

for model in client.models.list():
    methods = getattr(model, "supported_actions", None)
    print(model.name, methods)