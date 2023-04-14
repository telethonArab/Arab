import os
import random
import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent
os.system("pip install user_agent")
from Arab import iqthon
a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"
trys, trys2, trys3 = [0], [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثيات":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسيات":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعيات":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        username = "".join(f)
        username = username + "bot"
    else:
        raise ValueError("اختر يوزر صحيح.")
    return username

@iqthon.iq_cmd(pattern="(الصيد|اوامر الصيد)")
async def _(event):
    await event.edit(
        """
( أوامر الصيد الخاصة بسورس تليثون العرب :  )

تختار واحد من هل انواع بجانب امر صيد :
(  سداسي حرفين - ثلاثيات - سداسيات - بوتات - خماسي حرفين - خماسي - سباعيات )

••••••••••••••••••••••
الامر :  ( .صيد + النوع ) .
- يقوم بصيد معرفات عشوائية حسب النوع
••••••••••••••••••••••
الامر : ( .تثبيت + معرف )
- وظيفة الامر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه
••••••••••••••••••••••
الامر :  ( .حالة الصيد )
• لمعرفة عدد المحاولات للصيد
••••••••••••••••••••••
الامر :  ( .حالة التثبيت )
• لمعرفة عدد المحاولات للصيد
••••••••••••••••••••••
@iqthon
"""
    )
@iqthon.iq_cmd(pattern="صيد بوتات")
async def huntbot(event):
    await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
    isclaim.clear()
    isclaim.append("on")
    botmod = True
    while botmod:
        username = gen_user("بوتات")
        isav = check_user(username)
        if isav == True:
            try:
                await iqthon.send_message("@botfather", "/newbot")
                await iqthon.send_message("@botfather", "@iqthon - @lll5l 🕷️")
                await iqthon.send_message("@botfather", username)
                await event.client.send_file(                    event.chat_id,                    "https://t.me/M8M8M/942",                    caption=" 🕷️ iqthon the original 🕷️\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ bot ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @iqthon - @lll5l ❳ ".format(                        username, trys3                    ),                )
                botmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except telethon.errors.FloodError as e:
                await iqthon.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                botmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await iqthon.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    botmod = False
                    break
        else:
            pass
        trys3[0] += 1
    isclaim.clear()
    isclaim.append("off")
@iqthon.iq_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    if event.text[1:].startswith("صيد بوتات"):
        return
    choice = str(event.pattern_match.group(1))
    await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
    try:
        ch = await iqthon(
            functions.channels.CreateChannelRequest(
                title="IQTHON HUNTER - صيد تليثون العرب",
                about="This channel to hunt username by - @iqthon ",
            )
        )
        ch = ch.updates[1].channel_id
    except Exception as e:
        await iqthon.send_message(
            event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
        )
        sedmod = False

    isclaim.clear()
    isclaim.append("on")
    sedmod = True
    while sedmod:
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يرجى وضع النوع بشكل صحيح**")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await iqthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/M8M8M/942",
                    caption=" 🕷️ iqthon the original 🕷️\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @iqthon - @lll5l ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/M8M8M/942",
                    caption=" 🕷️ iqthon the original 🕷️\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @iqthon - @lll5l ❳ ".format(
                        username, trys, choice
                    ),
                )
                
                sedmod = False
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
                )
                sedmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await iqthon.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    sedmod = False
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
@iqthon.iq_cmd(pattern="تثبيت (.*)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await iqthon(
                functions.channels.CreateChannelRequest(
                    title="IQTHON HUNTER - تثبيت تليثون العرب",
                    about="This channel to hunt username by - @iqthon ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await iqthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    swapmod = True
    while swapmod:
        isav = check_user(username)
        if isav == True:
            try:
                await iqthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/M8M8M/942",
                    caption=" 🕷️ iqthon the original 🕷️\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @iqthon - @lll5l ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/M8M8M/942",
                    caption=" 🕷️ iqthon the original 🕷️\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @iqthon - @lll5l ❳ ".format(
                        username, trys2
                    ),
                )
                
                swapmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                swapmod = False
                break
            except telethon.errors.FloodError as e:
                await iqthon.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                swapmod = False
                break
            except Exception as eee:
                await iqthon.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                swapmod = False
                break
        else:
            pass
        trys2[0] += 1

    isclaim.clear()
    isclaim.append("off")
@iqthon.iq_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) **من المحاولات")
    elif "off" in isclaim:
        await event.edit("**- الصيد بالاصل لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")
@iqthon.iq_cmd(pattern="حالة التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
        
