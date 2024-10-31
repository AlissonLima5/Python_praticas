import discord #Bibliotecas para importar
import asyncio #asyncio, que permite escrever código assíncrono, muito utilizado em aplicações que fazem chamadas de rede ou esperam por eventos, como os bots do Discord.

#Intents controlar o que o bot pode ouvir e acessar, garantindo que ele tenha apenas as permissões necessárias para funcionar corretamente.
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

#Cria uma classe do discord.client
class MyClient(discord.Client): 
    async def on_ready(self): #Evento chamado quando o bot está pronto e conectado
        print('Logged on as {0}!'.format(self.user))  # Exibe no console o nome do bot

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))  # Evento chamado sempre que uma nova mensagem é enviada em um canal que o bot pode acessar
        if message.content == '!ativar' :#Comando para criar a mensagem e oque o usuario vai digitar para o bot enviar no chat do discord
            await message.channel.send(f'Estou funcionando') #Comando para escrever a mensagem desejada e enviada para o chat
#Sempre copiar o if message.conte == '': para definir o comando para o usuario digitar no chat e logo em seguida o comando await message.channel.send('') serve para digita a mensagem que será enviada para o usuario
        if message.content == '!comandos':
            await message.channel.send('Todos os comandos: ')

            

client = MyClient(intents=intents)# Cria uma instância do MyClient com os intents definidos
client.run('Token do Bot') #Substitua o Token do Bot para o Token verdadeiro