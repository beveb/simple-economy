    @commands.command()
    @commands.cooldown(1, 3, BucketType.guild)
    @commands.cooldown(1, 3, BucketType.user)
    async def jobs(self, ctx):

        cursor = await db.cursor()
        cursorr = await jobs.cursor()
        USER_ID = ctx.author.id 
        USER_NAME = str(ctx.message.author)
        guild = ctx.guild.id

        default_job_name = "Lemonade Stand"
        await cursorr.execute(f"SELECT job_name FROM jobs WHERE job_name = '{default_job_name}' and guild_id = '{guild}'")
        result = await cursorr.fetchone()

        if result == None:
            await cursorr.execute("INSERT INTO jobs(job_name, job_desc, job_paycheck, job_lvl, owner_id, capacity, guild_id) values(?, ?, ?, ?, ?, ?, ?)",("Lemonade Stand", "Come to us when you cant find another job", 15, 1, 804249828162404392, 100000000, guild))
            await jobs.commit()
            pass

        else:
            pass
    
        await cursorr.execute(f"SELECT * FROM jobs WHERE guild_id = '{guild}'")
        result = await cursorr.fetchall()
        self.jobs_index = 0
            
        e = discord.Embed(title=f'Wait for reactions to load...')

        if len(result) == 1:
                e1 = discord.Embed(title=f'Name: {result[0][0]}', description=f'{result[0][1]}')
                e1.add_field(name='Stats', value=f'Paycheck: ${result[0][2]}\nJob Level: {result[0][3]}\nJob Capacity: {result[0][5]}')
                e1.set_author(name='Showing 1 Job in guild')
                self.all_jobs_embeds = [e1]

        elif len(result) == 2:
                e1 = discord.Embed(title=f'Name: {result[0][0]}', description=f'{result[0][1]}')
                e1.add_field(name='Stats', value=f'Paycheck: ${result[0][2]}\nJob Level: {result[0][3]}\nJob Capacity: {result[0][5]}')
                e1.set_author(name='Showing 2 Jobs in guild')

                e2 = discord.Embed(title=f'Name: {result[1][0]}', description=f'{result[1][1]}')
                e2.add_field(name='Stats', value=f'Paycheck: ${result[1][2]}\nJob Level: {result[1][3]}\nJob Capacity: {result[1][5]}')
                e2.set_author(name='Showing 2 Jobs in guild')
                self.all_jobs_embeds = [e1, e2]

        elif len(result) == 3:
                e1 = discord.Embed(title=f'Name: {result[0][0]}', description=f'{result[0][1]}')
                e1.add_field(name='Stats', value=f'Paycheck: ${result[0][2]}\nJob Level: {result[0][3]}\nJob Capacity: {result[0][5]}')
                e1.set_author(name='Showing 3 Jobs in guild')

                e2 = discord.Embed(title=f'Name: {result[1][0]}', description=f'{result[1][1]}')
                e2.add_field(name='Stats', value=f'Paycheck: ${result[1][2]}\nJob Level: {result[1][3]}\nJob Capacity: {result[1][5]}')
                e2.set_author(name='Showing 3 Jobs in guild')

                e3 = discord.Embed(title=f'Name: {result[2][0]}', description=f'{result[2][1]}')
                e3.add_field(name='Stats', value=f'Paycheck: ${result[2][2]}\nJob Level: {result[2][3]}\nJob Capacity: {result[2][5]}')
                e3.set_author(name='Showing 3 Jobs in guild')
                self.all_jobs_embeds = [e1, e2, e3]

        elif len(result) == 4:
                e1 = discord.Embed(title=f'Name: {result[0][0]}', description=f'{result[0][1]}')
                e1.add_field(name='Stats', value=f'Paycheck: ${result[0][2]}\nJob Level: {result[0][3]}\nJob Capacity: {result[0][5]}')
                e1.set_author(name='Showing 4 Jobs in guild')

                e2 = discord.Embed(title=f'Name: {result[1][0]}', description=f'{result[1][1]}')
                e2.add_field(name='Stats', value=f'Paycheck: ${result[1][2]}\nJob Level: {result[1][3]}\nJob Capacity: {result[1][5]}')
                e2.set_author(name='Showing 3 Jobs in guild')

                e3 = discord.Embed(title=f'Name: {result[2][0]}', description=f'{result[2][1]}')
                e3.add_field(name='Stats', value=f'Paycheck: ${result[2][2]}\nJob Level: {result[2][3]}\nJob Capacity: {result[2][5]}')
                e3.set_author(name='Showing 3 Jobs in guild')

                e4 = discord.Embed(title=f'Name: {result[3][0]}', description=f'{result[3][1]}')
                e4.add_field(name='Stats', value=f'Paycheck: ${result[3][2]}\nJob Level: {result[3][3]}\nJob Capacity: {result[3][5]}')
                e4.set_author(name='Showing 4 Jobs in guild')
                self.all_jobs_embeds = [e1, e2, e3, e4]
                
        elif len(result) == 5:
                e1 = discord.Embed(title=f'Name: {result[0][0]}', description=f'{result[0][1]}')
                e1.add_field(name='Stats', value=f'Paycheck: ${result[0][2]}\nJob Level: {result[0][3]}\nJob Capacity: {result[0][5]}')
                e1.set_author(name='Showing 5 Jobs in guild')

                e2 = discord.Embed(title=f'Name: {result[1][0]}', description=f'{result[1][1]}')
                e2.add_field(name='Stats', value=f'Paycheck: ${result[1][2]}\nJob Level: {result[1][3]}\nJob Capacity: {result[1][5]}')
                e2.set_author(name='Showing 3 Jobs in guild')

                e3 = discord.Embed(title=f'Name: {result[2][0]}', description=f'{result[2][1]}')
                e3.add_field(name='Stats', value=f'Paycheck: ${result[2][2]}\nJob Level: {result[2][3]}\nJob Capacity: {result[2][5]}')
                e3.set_author(name='Showing 3 Jobs in guild')

                e4 = discord.Embed(title=f'Name: {result[3][0]}', description=f'{result[3][1]}')
                e4.add_field(name='Stats', value=f'Paycheck: ${result[3][2]}\nJob Level: {result[3][3]}\nJob Capacity: {result[3][5]}')
                e4.set_author(name='Showing 4 Jobs in guild')

                e5 = discord.Embed(title=f'Name: {result[4][0]}', description=f'{result[4][1]}')
                e5.add_field(name='Stats', value=f'Paycheck: ${result[4][2]}\nJob Level: {result[4][3]}\nJob Capacity: {result[4][5]}')
                e5.set_author(name='Showing 5 Jobs in guild')
                self.all_jobs_embeds = [e1, e2, e3, e4, e5]
                  
        self.jobs_index = 0

        msg: discord.Message = await ctx.send(embed=e)
            
        for emoji in self.jobs_control_emojis:
            await msg.add_reaction(emoji)

        await msg.edit(embed=self.all_jobs_embeds[self.jobs_index])

        self.current_jobs_msg = msg.id
        self.current_jobs_user = ctx.author.id
