//require the necessaty classes
const fs = require('fs');
const {Client, Collection, Intents, Interaction} = require('discord.js');
const {token} = require('./config.json');
const { CLIENT_RENEG_WINDOW } = require('tls');
//create new client
const client = new Client({intents: [Intents.FLAGS.GUILDS]});
//notify bot ready
client.once('ready', () =>{
    console.log('Ready!');
});

client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles){
    const command = require(`./commands/${file}`);
    client.commands.set(command.data.name, command);
}

client.on('interactionCreate', async interaction => {
    if(!interaction.isCommand()) return;
    
    const command = client.commands.get(interaction.commandName);

    if(!command) return;

    try{
        await command.execute(interaction);
    }
    catch{
        await interaction.reply({content: 'There was an error while executing this command!', ephemeral: true});
    }
    
})
//login to discord 
client.login(token);
