import discord
import random
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

client = discord.Client()

command_prefix = ['krpya ', 'Krpya ', 'kRPYA ']
client = commands.Bot(command_prefix)
client.remove_command('help')


globalmember = ' '
godmember = 'GODX'
boolean = False
godmodelist = ['abhi godmode me hai, you are not authorized to use command on him 1',
               'abhi godmode me hai, you are not authorized to use command on him 2',
               'abhi godmode me hai, you are not authorized to use command on him 3',
               'abhi godmode me hai, you are not authorized to use command on him 4',
               'abhi godmode me hai, you are not authorized to use command on him 5',
               'abhi godmode me hai, you are not authorized to use command on him 6',
               'abhi godmode me hai, you are not authorized to use command on him 7',
               'abhi godmode me hai, you are not authorized to use command on him 8',
               'abhi godmode me hai, you are not authorized to use command on him 9',
               'abhi godmode me hai, you are not authorized to use command on him 10',
               'abhi godmode me hai, you are not authorized to use command on him 11']






@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Sooryavansham"))
    print("Bot is ready!")






@client.event
async def on_message(message):
    author=message.author.name
    nospacereplies = [author + ', apko krpya and command ke beech me space dalna hoga 1',
                      author + ', apko krpya and command ke beech me space dalna hoga 2',
                      author + ', apko krpya and command ke beech me space dalna hoga 3',
                      author + ', apko krpya and command ke beech me space dalna hoga 4',
                      author + ', apko krpya and command ke beech me space dalna hoga 5',
                      author + ', apko krpya and command ke beech me space dalna hoga 6',
                      author + ', apko krpya and command ke beech me space dalna hoga 7',
                      author + ', apko krpya and command ke beech me space dalna hoga 8']
                    
    
    lowercaseword = message.content.lower()
    wrongprefixlist = ["krpyabezzati", "krpyadua", "krpyashayari", "krpyakick", "krpyaban", "krpyaclear", "krpyahelp"]
    for wrongprefix in wrongprefixlist:
        if lowercaseword.startswith(wrongprefix):
            await message.channel.send(random.choice(nospacereplies))
            break



    await client.process_commands(message)
    







    

@client.event
async def on_command_error(ctx, error):
    global globalmember
    globalmember = ctx.message.author



    cooldownlist = [format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 1',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 2',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 3',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 4',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 5',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 6',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 7',
                    format(globalmember.name) + ', please command ko spam na kare...command cooldown me h, thodi der baad try kare 8']
                    
                  

    
    tagnotfound = [format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 1',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 2',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 3',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 4',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 5',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 6',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 7',
                   format(globalmember.name) + ', krpya command dalne ke baad tag bhi kare jiske liye command use karna chahte h 8']




    
    tag_error_response = [format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 1',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 2',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 3',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 4',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 5',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 6',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 7',
                          format(globalmember.name) + ' ye galat username tag kiya hai...this username doesnt exist in this server, sahi karo 8']
 


    
    command_error_response = [format(globalmember.name) + ' please apni command check karo, its incorrect 1',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 2',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 3',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 4',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 5',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 6',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 7',
                              format(globalmember.name) + ' please apni command check karo, its incorrect 8']




    permissionlist = [format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 1',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 2',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 3',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 4',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 5',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 6',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 7',
                      format(globalmember.name) + ' ap is command ko use krne ke liye authorized nahi hai 8']




    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(random.choice(cooldownlist))


    if isinstance(error, commands.MissingRequiredArgument):   
        await ctx.send(random.choice(tagnotfound))


    if isinstance(error, commands.MissingPermissions):
        await ctx.send(random.choice(permissionlist))

  
    if isinstance(error, commands.BadArgument):
        await ctx.send(random.choice(tag_error_response))

        
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(random.choice(command_error_response))
    
  
    










def godmodecheck(ctx):
    global godmember
    return ctx.author.name == godmember




@client.command(aliases=['Haoshoku!!', 'haoshoku!!'])
@commands.check(godmodecheck)
async def _Haoshoku(ctx):    
    global boolean
    if boolean == False:
        boolean = True
        embed = discord.Embed(title="Mirza's Conqueror Haki Activated!" , colour = discord.Colour.red())
        embed.set_image(url='https://pa1.narvii.com/5753/8bcbf8da41632a0e155974a3293ffc5c4559ea32_00.gif')
        await ctx.send(embed=embed)
    else:
        return

    


@client.command(aliases=['HaoshokuCooldown', 'haoshokucooldown', 'Haoshokucooldown'])
@commands.check(godmodecheck)
async def _haoshokucooldown(ctx):
    global boolean
    if boolean == True:
        boolean = False
        messagelist = ['Shockwaves are decreasing...', 'Haoshoku no Haki at 75%', 'Haoshoku no Haki at 43%', 'Haoshoku no Haki at 29%', 'Haoshoku no Haki at 11%','Haoshoku no Haki at 3%', "Mirza's Haoshoku no Haki Deactivated!"]
        message = await ctx.send('Cooling Down...')
        for messages in messagelist:            
            await message.edit(content=messages)
            await asyncio.sleep(1.2)
    else:
        return    












@client.command()
async def help(ctx):
    embed = discord.Embed(title='Commands For Mr.India', description='Use Krypya before every command!', colour = discord.Colour.green())

    listofurl = ['https://cdn.countryflags.com/thumbs/india/flag-button-round-250.png',
                 'https://cdn.countryflags.com/thumbs/india/flag-button-round-250.png',
                 'https://cdn.countryflags.com/thumbs/india/flag-button-round-250.png',
                 'https://cdn.countryflags.com/thumbs/india/flag-button-round-250.png']


    embed.set_footer(text='Developed by M1rza')
    embed.set_thumbnail(url=random.choice(listofurl))
    embed.add_field(name='Bezzati', value='bezzati keejiye', inline=True)
    embed.add_field(name='Dua', value='dua deejiye', inline=True)
    embed.add_field(name='Shayari', value='shayari keejiye', inline=True)
    embed.add_field(name='Kick', value='kick keejiye', inline=True)
    embed.add_field(name='Clear', value='clear screen keejiye', inline=True)
    embed.add_field(name='Ban', value='ban keejiye', inline=True)

    await ctx.send(embed=embed)

















@client.command(aliases=['dua', 'Dua'])
@cooldown(5, 90, BucketType.user)
async def _dua(ctx, member: discord.Member):

    global godmember
    global boolean
    global godmodelist





    author=ctx.author.name
    mrindialist = [author + ' aap commands me bot ko tag nahi kar sakte 1',
                     author + ' aap commands me bot ko tag nahi kar sakte 2',
                     author + ' aap commands me bot ko tag nahi kar sakte 3',
                     author + ' aap commands me bot ko tag nahi kar sakte 4',
                     author + ' aap commands me bot ko tag nahi kar sakte 5',
                     author + ' aap commands me bot ko tag nahi kar sakte 6',
                     author + ' aap commands me bot ko tag nahi kar sakte 7',
                     author + ' aap commands me bot ko tag nahi kar sakte 8']
    if((format(member.name) == author)):
       await ctx.send(author + ', aap commands me khud ko tag nahi kar sakte')
       return
    if((format(member.name) == 'Mr.India')):
       await ctx.send(random.choice(mrindialist))
       return


    
    
    response_dua = ['Dua sentence 1',
                    'Dua sentence 2',
                    'Dua sentence 3',
                    'Dua sentence 4',
                    'Dua sentence 5',
                    'Dua sentence 6',
                    'Dua sentence 7',
                    'Dua sentence 8']
                  

    if((format(member.name) == godmember) and (boolean == True)):
        await ctx.send(format(member.name)+ ' ' + random.choice(godmodelist))
        
    else:        
        await ctx.send(format(member.name)+ ' '+ random.choice(response_dua))


    













             

@client.command(aliases=['bezzati', 'Bezzati'])
@cooldown(5, 90, BucketType.user)
async def _bezzati(ctx, member: discord.Member):

    global godmember
    global boolean
    global godmodelist





    
    author=ctx.author.name
    mrindialist = [author + ' aap commands me bot ko tag nahi kar sakte 1',
                     author + ' aap commands me bot ko tag nahi kar sakte 2',
                     author + ' aap commands me bot ko tag nahi kar sakte 3',
                     author + ' aap commands me bot ko tag nahi kar sakte 4',
                     author + ' aap commands me bot ko tag nahi kar sakte 5',
                     author + ' aap commands me bot ko tag nahi kar sakte 6',
                     author + ' aap commands me bot ko tag nahi kar sakte 7',
                     author + ' aap commands me bot ko tag nahi kar sakte 8']
    if((format(member.name) == author)):
       await ctx.send(author + ', aap commands me khud ko tag nahi kar sakte')
       return
    if((format(member.name) == 'Mr.India')):
       await ctx.send(random.choice(mrindialist))
       return



    
    
    response_bezzati = ['bezzati sentence 1',
                       'bezzati sentence 2',
                       'bezzati sentence 3',
                       'bezzati sentence 4',
                       'bezzati sentence 5',
                       'bezzati sentence 6',
                       'bezzati sentence 7',
                       'bezzati sentence 8']
                      
                    

    if((format(member.name) == godmember) and (boolean == True)):
        await ctx.send(format(member.name)+ ' ' + random.choice(godmodelist))
        
    else:        
        await ctx.send(format(member.name)+ ' ' + random.choice(response_bezzati))


        









        


    




@client.command(aliases=['shayari', 'Shayari'])
@cooldown(5, 90, BucketType.user)
async def _shayari(ctx):
    response_shayari = ['shayari sentence 1',
                        'shayari sentence 2',
                        'shayari sentence 3',
                        'shayari sentence 4',
                        'shayari sentence 5',
                        'shayari sentence 6',
                        'shayari sentence 7',
                        'shayari sentence 8']
                    
    await ctx.send(random.choice(response_shayari))

         
        
    

    













@client.command(aliases=['clear', 'Clear'])
@commands.has_permissions(manage_messages=True)
async def _clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)








@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    








@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

        








client.run(os.environ['DISCORD_TOKEN'])
