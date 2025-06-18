import pywhatkit as kit
import time
import pyautogui

# Lista de contatos (com código do país)
contatos = [
    "+",  # Número 1
    "+"   # Número 2
]

# Mensagem a ser enviada
mensagem = "Sua mensagem aqui!"

# Tempo de espera antes de fechar a aba (ajuste se necessário)
tempo_fechamento = 5  # Segundos

print("\n==== Iniciando envio de mensagens ====")

for i, numero in enumerate(contatos):
    print(f"\n➡️ Enviando para {numero}...")

    try:
        # Envia a mensagem e não fecha imediatamente
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=5, tab_close=False)

        # Espera um tempo para garantir que a mensagem foi enviada
        time.sleep(tempo_fechamento)

        # Fecha a aba ativa (CTRL + W no Windows)
        pyautogui.hotkey("ctrl", "w")

        print(f"✅ Mensagem enviada e aba fechada para {numero}!")

    except Exception as e:
        print(f"❌ Erro ao enviar para {numero}: {e}")

    # Pequeno intervalo antes de abrir a próxima aba
    time.sleep(2)

print("\n✅✅✅ Envio concluído com sucesso!")
