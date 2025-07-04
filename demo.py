import google.generativeai as genai
import time


genai.configure(api_key="AIzaSyAu6XWGYfvb6fknCEYJSBNzd-MyCMIGTu8")

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
        print("\n o sistema será encerrado em 30 segundos, copie e cole o treino antes de desligar...")
        print("\nSeu treino de hoje:")
        print(treino)
        time.sleep(30)