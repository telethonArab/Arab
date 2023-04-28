import random, requests, asyncio , os,  time

from fake_useragent import UserAgent
from telethon import TelegramClient, events
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.account import CheckUsernameRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import MessageEntityBold
from Arab import iqthon
os.system("pip install fake_useragent")

# A special file for Arab Telethon fishing for you
# needs
ua = UserAgent()
# ON WATCH
USERNAMES = []

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

# بس توصلة افضحك 😁😂

stop_phishing = True
workers = {
    'ثلاثيات': {
        'worker': False,
        'counter': 0
    },
    'خماسي': {
        'worker': False,
        'counter': 0
    },
    'خماسي حرفين': {
        'worker': False,
        'counter': 0
    },
    'سداسيات': {
        'worker': False,
        'counter': 0
    },
    'سداسي حرفين': {
        'worker': False,
        'counter': 0
    },
    'سباعيات': {
        'worker': False,
        'counter': 0
    },
    'بوتات': {
        'worker': False,
        'counter': 0
    }
}


def gen_user(choice):
    if choice == "ثلاثيات":
        username = f'{random.choice(a)}_{random.choice(b)}_{random.choice(e)}'
        
    elif choice == "خماسي":
        list = random.choices(a)*4 + random.choices(b)
        random.shuffle(list)
        username = "".join(list)

    elif choice == "خماسي حرفين":
        list = random.choices(a)*3 + random.choices(e)*2
        random.shuffle(list)
        username = "".join(list)

    elif choice == "سداسيات":
        list = random.choices(a)*5 + random.choices(e)
        random.shuffle(list)
        username = "".join(list)

    elif choice == "سداسي حرفين":
        list = random.choices(a)*4 + random.choices(b)*2
        random.shuffle(list)
        username = "".join(list)

    elif choice == "سباعيات":
        list = random.choices(a)*6 + random.choices(b)
        random.shuffle(list)
        username = "".join(list)
        
    elif choice == "بوتات":
        username = f'{random.choice(a)}{random.choice(e)}{random.choice(e)}bot'
        
    else:
        raise ValueError("اختر يوزر صحيح.")
    return username



def check_user(username, session, user_agent):
    check_url = f'https://t.me/{username}'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,ar;q=0.8',
        'user-agent': user_agent
    }
    
    response = session.get(check_url, headers=headers)
    if 'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"' in response.text:
        return f'@{username}'
    else:
        return False

@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.ايقاف الصيد'))
async def StopPhishingHundler(event):
    global stop_phishing
    
    stop_phishing = False
    await event.edit('تم ايقاف الصيد')
    
    
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.حالة الصيد'))
async def StopPhishingHundler(event):
    global workers
    
    message = ''
    for wroker_ in workers:
         message += f'__حالة صيد "{wroker_}" : {workers.get(wroker_).get("counter")} محاولة صيد__\n'
    await event.edit(message)
    
    
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.صيد ?(.*)'))
async def PhishingHundler(event):
    global stop_phishing, workers
    
    # get phish type
    valid_types = ['ثلاثيات', 'خماسي', 'خماسي حرفين', 'سداسيات', 'سداسي حرفين', 'سباعيات', 'بوتات']
    PhishType = (event.message.message).replace('.صيد', '').strip()
    
    if PhishType not in valid_types:
        await event.reply(f'__اختر صيد صحيح, الصيد المتاح : {", ".join(valid_types)}__')
    else:
        # create channel
        if workers.get(PhishType).get('worker') == False:
            workers[PhishType]['worker'] = True
            try:
                channel = await event.client(CreateChannelRequest(title=f'صيد : {PhishType}', about=f'IQTHON'))
                await event.edit('تم تفعيل امر الصيد بنجاح')
                
                while stop_phishing == True:
                    session = requests.Session()
                    user_agent = ua.random
                    username = gen_user(PhishType)
                                        
                    valid = check_user(username, session, user_agent)
                    if valid != False:
                        await event.client.send_message(channel.chats[0].id, message=valid)
                    
                    workers[PhishType]['counter'] = workers[PhishType]['counter'] + 1
                    await asyncio.sleep(6)

            except Exception as error:
                await event.reply(f'__حدث خطأ : {error}__')
        else:
            await event.edit('سبق لك تفعيل هذا النوع من الصيد')
    
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.سحب ?(.*)'))
async def CheckAndApply(event):
    username = (event.message.message).replace('.سحب', '').strip()
    username = username.replace('@', '').strip()
    if username not in USERNAMES:
        USERNAMES.append(username)
        
    reply = await event.reply(f'**تم بدأ السحب لـ @{username}**')
    
    # IQTHON
    RUN = await CheckUsername(event, username, event.sender_id)
    if RUN == True:
        RUN = await UpdateUsername(event, username)

# USERNAMES UNCHECK
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.الغاء سحب ?(.*)'))
async def UnCheck(event):
    username = (event.message.message).replace('.الغاء سحب', '').strip()
    username = (event.message.message).replace('@', '').strip()
    
    if username in USERNAMES:
        USERNAMES.remove(username)
        
    reply = await event.reply(f'**تم الغاء سحب لـ @{username}**')
    

async def CheckUsername(event, user, user_id):
    global USERNAMES
    
    while user in USERNAMES:
        try:
            check_first = await event.client(CheckUsernameRequest(username=user))
            if check_first == True:
                if user in USERNAMES:
                    USERNAMES.remove(user)
                MESSAGE = f"اليوزر @{user} اصبح مناح. تم بدأ محاولات الاستلاء عليه. ستتلقى اشعار في حالة الاستلاء عليه"
                NotifyUser = await event.client(SendMessageRequest(peer=user_id, entities=[MessageEntityBold(offset=0, length=len(MESSAGE))], message=MESSAGE))
                break
            
        except Exception as e:
            print (e)
            break
        
        await asyncio.sleep(10)
        
    return True        
    
async def UpdateUsername(event, user):
    from telethon.tl.functions.channels import CreateChannelRequest
    from telethon.tl.functions.channels import UpdateUsernameRequest
    
    # IQTHON
    changed, created_channel = False, await event.client(CreateChannelRequest(title=user, about=user))
    while changed == False:
        try:
            UpdateUsername = await event.client(UpdateUsernameRequest(channel=created_channel.chats[0].id, username=user)) #await event.client(UpdateUsernameRequest(username=user))
            if UpdateUsername == True:
                MESSAGE = f"تم سحب اليوزر @{user}"
                NotifyUser = await event.client(SendMessageRequest(peer=user, entities=[MessageEntityBold(offset=0, length=len(MESSAGE))], message=MESSAGE))
                changed = True
                break
        except Exception as e:
            print (e)
        await asyncio.sleep(10)
    
       
