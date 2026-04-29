import discord

from nekosbest import Client as Neko
from src.bot import DiscordBot
from discord import app_commands
from src.neko.embeds import act_embed

positive_acts = [
    (
        "blush",
        "Blush",
        "is blushing like crazy!",
        "Turn red with embarrassment or flattery!",
    ),
    ("clap", "Clap", "is clapping it up!", "Give a round of applause!"),
    ("dance", "Dance", "is busting a move!", "Bust a move on the dance floor!"),
    ("happy", "Happy", "is super happy!", "Radiate pure joy and happiness!"),
    ("laugh", "Laugh", "is dying of laughter!",
     "Burst out in contagious laughter!"),
    ("nod", "Nod", "is nodding along!", "Show your agreement with a nod!"),
    ("nom", "Nom", "is nomming away!", "Munch away on something delicious!"),
    ("run", "Run", "just zoomed off!", "Zoom off at full speed!"),
    ("salute", "Salute", "threw a salute!", "Give a sharp, respectful salute!"),
    ("sip", "Sip", "is sipping away~", "Take a slow, satisfying sip!"),
    ("smile", "Smile", "is all smiles!", "Flash a warm, cheerful smile!"),
    ("spin", "Spin", "is spinning around!", "Twirl around like a top!"),
    ("teehee", "Giggle", "is giggling away!",
     "Let out an adorable little giggle!"),
    (
        "thumbsup",
        "Thumbsup",
        "gives a thumbs up!",
        "Show your approval with a thumbs up!",
    ),
    ("wag", "Wag", "is wagging like crazy!", "Wag with excitement and delight!"),
]

neutral_acts = [
    ("baka", "Baka", "just called you baka!!", "Call someone a silly dummy!"),
    ("bleh", "Bleh", "stuck their tongue out!", "Stick your tongue out cheekily!"),
    ("bored", "Bored", "is so bored rn...", "Yep, nothing to do here..."),
    (
        "confused",
        "Confused",
        "has no idea what's going on",
        "Tilt your head in total confusion!",
    ),
    ("nya", "Meow", "went full cat mode!", "Unleash your inner cat!"),
    ("shrug", "Shrug", "just shrugged lol", "Shrug it off — who knows!"),
    ("sleep", "Sleep", "is out cold!", "Catch some well-deserved Zzz's!"),
    ("smug", "Smug", "is looking real smug rn", "Flash that signature smug look!"),
    ("stare", "Stare", "is just... staring",
     "Fix an unblinking stare into the void!"),
    ("think", "Think", "is big brain thinking rn", "Hmm... deep in thought!"),
    ("yawn", "Yawn", "let out a huge yawn!", "Let out a big, sleepy yawn!"),
]

negative_acts = [
    ("angry", "Angry", "is absolutely fuming!!",
     "Let everyone know you're fuming!"),
    ("cry", "Cry", "is literally crying rn", "Let the tears flow freely!"),
    (
        "facepalm",
        "Facepalm",
        "just facepalmed so hard",
        "Express your disbelief with a facepalm!",
    ),
    ("nope", "Nope", "said NOPE and left", "Shut it down with a firm nope!"),
    ("pout", "Pout", "is pouty and not ok", "Puff those cheeks and pout away!"),
    ("shocked", "Shocked", "is totally shocked omg", "Drop your jaw in utter shock!"),
    (
        "tableflip",
        "Tableflip",
        "just flipped a table lmao",
        "Flip that table in frustration!",
    ),
]

interactable_acts = [
    (
        "lappillow",
        "Lap Pillow",
        "cradles",
        "Offer a cozy lap to rest on!",
    ),
    ("lurk", "Lurk", "is creeping around", "Sneak around in the shadows!"),
    (
        "bite",
        "Bite",
        "just took a bite out of",
        "Sink your teeth in for a little nibble!",
    ),
    ("bonk", "Bonk", "bonked", "Bop someone right on the noggin!"),
    ("blowkiss", "Blow Kiss", "blew a kiss at",
     "Send a sweet kiss through the air!"),
    ("carry", "Carry", "just picked up and carried", "Sweep someone off their feet!"),
    ("cuddle", "Cuddle", "cuddles", "Snuggle up nice and close!"),
    (
        "handshake",
        "Handshake",
        "went for a handshake with",
        "Seal it with a firm handshake!",
    ),
    (
        "handhold",
        "Hand Hold",
        "holds hands of",
        "Reach out and hold someone's hand!",
    ),
    ("highfive", "High Five", "high fived", "Smack hands for an epic high five!"),
    ("feed", "Feed", "feeds", "Share a tasty treat with someone!"),
    ("hug", "Hug", "hugs", "Wrap someone in a warm, big hug!"),
    (
        "kabedon",
        "Kabedon",
        "wall-pinned",
        "Pin someone dramatically to the wall!",
    ),
    ("kick", "Kick", "kicked", "Give a swift kick!"),
    ("kiss", "Kiss", "kissed", "Plant a sweet kiss on someone!"),
    ("peck", "Peck", "snuck a peck on", "Give a quick, cute little peck!"),
    ("pat", "Pat", "gave a pat to", "Give someone a gentle, reassuring pat!"),
    ("poke", "Poke", "poked", "Prod someone with a cheeky poke!"),
    ("punch", "Punch", "threw a punch at", "Throw a playful punch their way!"),
    ("shoot", "Shoot", "shot", "Take aim and fire!"),
    ("shake", "Shake", "is shaking", "Give someone a good shake!"),
    ("slap", "Slap", "slapped", "Deliver a dramatic slap!"),
    ("tickle", "Tickle", "tickles", "Go for the tickle attack!"),
    ("wave", "Wave", "waved at", "Give a friendly wave hello!"),
    ("wink", "Wink", "winked at", "Flash a flirty little wink!"),
    ("yeet", "Yeet", "just yeeted", "Launch someone into the stratosphere!"),
]


def get_act(term):
    all_acts = positive_acts + neutral_acts + negative_acts + interactable_acts

    for act in all_acts:
        if act[1].lower() == term.lower():
            return act

    return None


class ActGroup(app_commands.Group):
    def __init__(self, bot: DiscordBot, neko: Neko, acts: list, **kwargs):
        super().__init__(**kwargs)

        self.bot = bot
        self.neko = neko

        for endpoint, name, message, desc in acts:
            self.create_act_command(endpoint, name, message, desc)

    def create_act_command(self, endpoint: str, name: str, message: str, desc: str):
        @app_commands.command(name=name.lower(), description=desc)
        async def act_command(inter: discord.Interaction):
            data = await self.neko.get_image(endpoint)
            message_ = f"**{inter.user.display_name}** {message}"

            await inter.response.send_message(embed=act_embed(name, message_, data))

        self.add_command(act_command)


def add_act_commands(group, bot, neko):
    group.add_command(
        ActGroup(bot, neko, positive_acts, name="act1", description="uWu +ve")
    )
    group.add_command(
        ActGroup(bot, neko, neutral_acts, name="act2", description="uWu -_-")
    )
    group.add_command(
        ActGroup(bot, neko, negative_acts, name="act3", description="uWu -ve")
    )
