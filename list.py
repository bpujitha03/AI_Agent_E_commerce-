# pyright: reportPrivateImportUsage=false
import google.generativeai as genai

# ✅ Set your Gemini API key here (keep it secure in production)
genai.configure(api_key="AIzaSyA9ItiUpO-kZGBsI4XT5upiIcTuTPt0TvU")

print("🔍 Listing available Gemini models...\n")

# ✅ List all models that support content generation
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f"🧠 Model Name: {model.name}")
        print(f"📘 Description: {model.description}")
        print(f"🔢 Input Token Limit: {model.input_token_limit}")
        print("-" * 40)
