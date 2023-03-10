import discord

white = []
black = []
private = True

def setup(whitelist, blacklist, allow_private = True):
	global white
	global black
	global private
	white = [i.strip().lower() for i in whitelist]
	black = [i.strip().lower() for i in blacklist]
	private = allow_private
	bset = set(blacklist)
	for i in white:
		if i in bset:
			raise ValueError('{} is in the blacklist and the whitelist'.format(i))

def check(message):
    allow = False
    if isinstance(message.channel, discord.abc.PrivateChannel):
        allow = private
    else:
        ser = message.guild.name.lower()
        chn = ser + '#' + message.channel.name.lower()
        if len(white) == 0:
            allow = True
        if ser in white:
            allow = True
        if ser in black:
            allow = False
        if chn in white:
            allow = True
        if chn in black:
            allow = False
    return allow
