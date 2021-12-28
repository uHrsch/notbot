const {SlashCommandBuilder} = require('@discordjs/builders');
const {REST} = require('@discordjs/rest');
const {Routes} = require('discord-api-types/v9');
const {clientId, guildId} = require('./config.json');

const commands = [];

for(File of commandFiles){
    const command =require(`./commands/${File}`);
    commands.push(command.data.toJSON());
}

const rest = new REST({version: '9'}).setToken(token);

rest.put(Routes.applicationGuildCommands(clientId, guildId), {body: commands})
    .then(() => console.log('Sucessfully registered application commands.'))
    .catch(console.error);