# Telegram Bot
import telebot

KEY_API = "INSERT_TELEGRAM_KEY_FOR_FATHER_BOT"

bot = telebot.TeleBot(KEY_API)

# Última função
def verificar(mensagem):
    return True

# def verificar(mensagem):
#         if mensagem.text == "Oi":
#             return True
#         else:
#             return False

@bot.message_handler(func=verificar)
def reply(mensagem):
    texto = """Escolha uma opção:
    /opcao1 A
    /opcao2 B
    /opcao3 C
    """
    bot.reply_to(mensagem, texto)

bot.polling()