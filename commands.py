async def test(client, message):
    await message.channel.send("meow")

async def repeat(client, message):
    if message.author.id not in client.dpeta_responding:
        client.dpeta_responding.append(message.author.id)
        await message.channel.send("I will now repeat you!")
    else:
        client.dpeta_responding.remove(message.author.id)
        await message.channel.send("I will no longer repeat you!")
    
async def verysad(client, message):
    await message.channel.send("😿 😿 😿\n😿 😿 😿\n😿 😿 😿")

async def help(client, message):
    await message.channel.send(embed=client.help_embed)
