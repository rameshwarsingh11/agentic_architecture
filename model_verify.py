import os
import google.generativeai as genai

# Make sure your key is set
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Listing available models for this API key...\n")
for model in genai.list_models():
    print(model.name)
