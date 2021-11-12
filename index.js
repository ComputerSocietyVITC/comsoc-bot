const discord = require('discord.js')
const client = new discord.Client()

client.on('ready', () => {
    console.log("Bot is up")
})

client.login(process.env.TOKEN)