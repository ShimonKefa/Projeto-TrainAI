import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

try:
    models = genai.list_models()
    for model in models:
        print(f"Nome do modelo: {model.name}")
        print(f"Versões disponíveis: {model.versions}")
        print(f"Métodos suportados: {model.supported_generation_methods}")
        print("-" * 20)
except Exception as e:
    print(f"Ocorreu um erro: {e}")