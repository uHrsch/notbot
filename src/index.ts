import { Client, Collection, Intents, Interaction } from "discord.js";
import * as fs from 'fs';

//create new client
const client = new Client({intents: [Intents.FLAGS.GUILDS]});
//notify bot ready
client.once('ready', () =>{
    console.log('Ready!');
});
//load commands
client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter((file: string) => file.endsWith('.ts'));

for (const file of commandFiles){
    const command = require(`./commands/${file}`);
    client.commands.set(command.data.name, command);
}

client.on('interactionCreate', async (interaction: Interaction) => {
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