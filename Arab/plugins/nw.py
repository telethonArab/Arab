from ..utils import is_admin
from googletrans import Translator
from Arab import iqthon
from telethon.sync import functions
from telethon import events
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.errors.rpcerrorlist import YouBlockedUserError
translator = Translator()


@iqthon.iq_cmd(pattern="اغلاق تعديل الميديا")
async def cleanup_command(event):
    if await is_admin(event.client, event.chat_id, event.sender_id):
        global handler

        @iqthon.on(events.MessageEdited(incoming=True, chats=event.chat_id))
        async def handler(event):
            if event.media:
                await event.client.delete_messages(event.chat_id, event.id)

        await event.edit("- تم فتح نظام حذف الميديا المعدلة")
    else:
        await event.edit("- ليس لديك الصلاحيات الكافية لأستخدام هذا الامر.")
@iqthon.iq_cmd(pattern="فتح تعديل الميديا")
async def stop_cleanup_command(event):
    if await is_admin(event.client, event.chat_id, event.sender_id):
        iqthon.remove_event_handler(handler)
        await event.edit("- تم اغلاق نظام حذف الميديا المعدلة.")
    else:
        await event.edit("- ليس لديك الصلاحيات الكافية لأستخدام هذا الامر.")                        
@iqthon.iq_cmd(pattern="فتح الترجمة")
async def traenjm(event):
    if gvarstatus("translateen"):
        await edit_delete(event, "**الترجمة التلقائية مفعلة بالأصل**")
        return
    if not gvarstatus("translateen"):
        addgvar("translateen", "Done")
        await edit_delete(            event, "**تم بنجاح فتح الترجمة التلقائية لأي رسالة سترسلها**"        )
        return
@iqthon.iq_cmd(pattern="اغلاق الترجمة")
async def stoptraenjm(event):
    if not gvarstatus("translateen"):
        await edit_delete(event, "**الترجمة التلقائية غير مفعلة بالأصل**")
        return
    if gvarstatus("translateen"):
        delgvar("translateen")
        await edit_delete(event, "**تم اغلاق الترجمة التلقائية لأي رسالة سترسلها**")
        return
@iqthon.on(events.NewMessage(outgoing=True))
async def translateen(event):
    if gvarstatus("translateen"):
        if event.message.message.startswith(("!", ".", "/", "http", "@")):
            return
        try:
            translation = translator.translate(                event.message.message, src="ar", dest="en"            )
            if translation.text != event.message.message:
                await iqthon.edit_message(event.message, translation.text)
        except:
            pass       
                        
@iqthon.iq_cmd(pattern="فتح الزخرفة الانجليزية")
async def zakrafaon(event):
    if not gvarstatus("enzakrafa"):
        addgvar("enzakrafa", "on")
        await edit_delete(event, "**تم بنجاح فتح الزخرفة الانجليزية**")
        return
    if gvarstatus("enzakrafa"):
        await edit_delete(event, "**الزخرفة الانجليزية مفعلة اصلا**")
        return
@iqthon.iq_cmd(pattern="اغلاق الزخرفة الانجليزية")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafa"):
        await edit_delete(event, "*الزخرفة الانجليزية غير مفعلة اصلا**")
        return
    if gvarstatus("enzakrafa"):
        delgvar("enzakrafa")
        await edit_delete(event, "**تم بنجاح اغلاق الزخرفة الانجليزية**")
        return
@iqthon.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafa"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "𝗮")
            .replace("b", "𝗯")
            .replace("c", "𝗰")
            .replace("d", "𝗱")
            .replace("e", "𝗲")
            .replace("f", "𝗳")
            .replace("g", "𝗴")
            .replace("h", "𝗵")
            .replace("i", "𝗶")
            .replace("j", "𝗷")
            .replace("k", "𝗸")
            .replace("l", "𝗹")
            .replace("m", "𝗺")
            .replace("n", "𝗻")
            .replace("o", "𝗼")
            .replace("p", "𝗽")
            .replace("q", "𝗾")
            .replace("r", "𝗿")
            .replace("s", "𝘀")
            .replace("t", "𝘁")
            .replace("u", "𝘂")
            .replace("v", "𝘃")
            .replace("w", "𝘄")
            .replace("x", "𝘅")
            .replace("y", "𝘆")
            .replace("z", "𝘇")        )
        await event.edit(uppercase_text)
@iqthon.ar_cmd(pattern="انشاء ?(.*)")
async def inshai(event):
    msg = event.text.split()
    username = msg[1]
    chat = "@creationdatebot"
    response = await iqthon.send_message("creationdatebot", f"/id {username}")
    async with event.client.conversation(chat) as conv:
        try:
            await event.client.send_message(chat, "/id {reply_message}")
        except YouBlockedUserError:
            await event.reply(                f"يجب عليك الغاء حظر هذا البوت @creationdatebot اولا واعادة استخدام الامر"            )
            return
        response = conv.wait_event(            events.NewMessage(incoming=True, from_users=747653812)        )
        response = await response
        if response.text.startswith("Looks"):
            await event.edit("لقد حدث خطأ ما")
        else:
            await event.edit(                f"**تاريخ انشاء المستخدم هو: **`{response.text.replace('**','')}`"            )            
