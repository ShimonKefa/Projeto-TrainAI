import google.generativeai as genai



genai.configure(api_key="")

model = genai.GenerativeModel(model_name='models/gemini-2.0-flash-thinking-exp')

def obter_grupo_muscular():
    grupo = input("Qual grupo muscular você pretende malhar hoje?\n")
    return grupo

def gerar_treino(grupo_muscular):
    prompt = f"Gere um treino de musculação instantâneo para o grupo muscular: {grupo_muscular}. Inclua o nome do exercí­cio, número de séries e repetições."
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    grupo = obter_grupo_muscular()
    if grupo:
        treino = gerar_treino(grupo)
        print("\nSeu treino de hoje:")
        print(treino)
