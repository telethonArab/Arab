import asyncio
import random
import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent
from Arab import iqthon
from user_agent import *
from telethon import events
from telethon.tl import functions

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"
trysiqthon, trysiqthon2 = [0], [0]
iqthonisclaim = ["off"]
iqthonisauto = ["off"]
def check_user_iqthon(username):
    url = "https://t.me/" + str(username)
    headers = {        "User-Agent": generate_user_agent(),        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",        "Accept-Encoding": "gzip, deflate, br",        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",    }

    response = requests.get(url, headers=headers)
    if (        response.text.find(            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'        )        >= 0    ):
        return True
    else:
        return False
def gen_user(choice):
    if choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "ثلاثيات":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "سداسيات":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        # random.shuffle(f)
        username = "".join(f)
        username = username + "bot"

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)

        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعيات":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        return "error"
    return username
@iqthon.iq_cmd(pattern="اوامر تشيكر الصيد")
async def _(event):
    await event.edit(
        """
اوامر التشيكر الصيد :
••••••••••••••••••••••••••
النوع :(  سداسي حرفين/ ثلاثيات/ سداسيات/ بوتات/ خماسي حرفين/خماسي /سباعيات )
••••••••••••••••••••••••••
الامر:  `.صيد` + النوع
• يصيد معرفات عشوائية
••••••••••••••••••••••••••
الامر:  `تثبيت` + معرف
* وظيفة الامر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه
••••••••••••••••••••••••••
الامر:   `.حالة الصيد`
• لمعرفة عدد المحاولات للصيد
••••••••••••••••••••••••••
الامر:  `.حالة التثبيت`
• لمعرفة عدد المحاولات للصيد
••••••••••••••••••••••••••
"""    )
@iqthon.iq_cmd(pattern="صيد (.*)")
async def sade(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء الصيد في @{ch} .")
    except:
        try:
            ch = await iqthon(                functions.channels.CreateChannelRequest(                    title="IQTHON  - صيد تليثون العرب",                    about="This channel to hunt username by - @IQTHON ",                )            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
        except Exception as e:
            await iqthon.send_message(                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"            )
    iqthonisclaim.clear()
    iqthonisclaim.append("on")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يرجى وضع النوع بشكل صحيح**.")
            break
        isav = check_user_iqthon(username)
        if isav == True:
            try:
                await iqthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- تم الانتهاء : @{username} !\n- By : @LLL5L - @IQTHON !\n- Hunting Log {trysiqthon2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await iqthon.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await iqthon.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trysiqthon[0] += 1
    iqthonisclaim.clear()
    iqthonisclaim.append("off")
    await event.client.send_message(event.chat_id, "**- تم بنجاح الانتهاء من الصيد**")
@iqthon.iq_cmd(pattern="تثبيت (.*)")
async def bin(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await iqthon(
                functions.channels.CreateChannelRequest(
                    title="IQTHON  - صيد تليثون العرب",
                    about="This channel to hunt username by - @IQTHON ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await iqthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    iqthonisauto.clear()
    iqthonisauto.append("on")
    username = str(msg[1])

    for i in range(1000000000000):
        isav = check_user_iqthon(username)
        if isav == True:
            try:
                await iqthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n- By : @LLL5L - @IQTHON !\n- Hunting Log {trysiqthon2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                break
            except telethon.errors.FloodError as e:
                await iqthon.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await iqthon.send_message(                    event.chat_id,                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",                )
                break
        else:
            pass
        trysiqthon2[0] += 1

        await asyncio.sleep(1.3)
    iqthonisclaim.clear()
    iqthonisclaim.append("off")
    await iqthon.send_message(event.chat_id, "**- تم الانتهاء من التثبيت بنجاح**")
@iqthon.iq_cmd(pattern="حالة الصيد")
async def helivebin(event):
    if "on" in iqthonisclaim:
        await event.edit(f"**- الصيد وصل لـ({trysiqthon[0]}) **من المحاولات")
    elif "off" in iqthonisclaim:
        await event.edit("**- الصيد بالاصل لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")
@iqthon.iq_cmd(pattern="حالة التثبيت")
async def iqthon(event):
    if "on" in iqthonisauto:
        await event.edit(f"**- التثبيت وصل لـ({trysiqthon2[0]}) من المحاولات**")
    elif "off" in iqthonisauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
