import os
import telebot

CHAVE_API = "6285537111:AAHdBUD5BiFTmqx_PS3nCwmqeQ6sTZRlRfs"
chat_id = "413556518"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Link"])
def Link(mensagem):
    bot.reply_to(mensagem, "Aqui está o link dos calendários:\nhttps://prograd.ufes.br/calendario-academico")

@bot.message_handler(commands=["Download"])
def Download(mensagem):
    textoAviso = "Lembrando mais uma vez de que este BOT é apenas para as turmas dos cursos presenciais da UFES!"
    bot.reply_to(mensagem, textoAviso)
    bot.send_photo(chat_id=chat_id, photo=open("Calendario_UFES_2023.png", "rb"))

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    aviso = "BOT DESENVOLVIDO APENAS PARA OS CURSOS PRESENCIAIS DA UNIVERSIDADE FEDERAL DO ESPIRITO SANTO!"
    bot.send_message(chat_id, aviso, parse_mode= 'Markdown')
    texto = """
Escolhe ai o que você quer, se é link ou foto(clicando é mais facil em gênio):\n
/Link Link para o site com todos os calendários;
/Download Menu pra saber qual modo(EAD ou PRESENCIAL) e baixar direto do tele.
Se você mandar qualquer outra coisa eu vou te ignorar jae? ENTÃO CLICA NAS OPÇÕES"""
    bot.reply_to(mensagem, texto)


bot.polling()