from Arab.core.logger import logging
from telethon import TelegramClient, client, events

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped, AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from Arab import iqthon

from ..Config import Config
from telethon.sessions import StringSession

import asyncio
LOGS = logging.getLogger(__name__)

new_iqthon = TelegramClient(StringSession(Config.STRING_SESSION), Config.APP_ID, Config.API_HASH)
new_iqthon.start()

async def PyStart():
    global iqthon_py
    try:
        iqthon_py = PyTgCalls(new_iqthon)
        await iqthon_py.start()
    except Exception as error:
        print (error)

async def JoinThenStreamVideo(chat_id, StreamFile):
    global iqthon_py
    await PyStart()
    await iqthon_py.join_group_call(
        int(chat_id),
        AudioVideoPiped(
            StreamFile,
            HighQualityAudio(),
            HighQualityVideo(),
        ),
        stream_type=StreamType().local_stream,
    )
    await idle()
    
async def JoinThenStreamAudio(chat_id, StreamFile):
    global iqthon_py
    await PyStart()
    await iqthon_py.join_group_call(
        int(chat_id),
        AudioPiped(
            StreamFile,
            HighQualityAudio(),
        ),
        stream_type=StreamType().local_stream,
    )
    await idle()
    
async def LeaveStream(chat_id):
    global iqthon_py
    await iqthon_py.leave_group_call(
        chat_id,
    )


# DOWNLOAD THEN STREAM AUDIO
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.تشغيل صوتي'))
async def AudioFileToVoiceChat(event):
    if event.reply_to != None:
        try:
            from telethon.tl.functions.channels import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(channel=event.chat_id, id=[event.reply_to.reply_to_msg_id]))
        except:
            from telethon.tl.functions.messages import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(id=[event.reply_to.reply_to_msg_id]))
            
        try:
            if message_media.messages[0].media != None and str(message_media.messages[0].media.document.mime_type).startswith('audio'):
                edit = await event.edit('**في طور المعالجة و الانجاز**')
                filename = await event.client.download_media(message_media.messages[0], 'audio')
                
                edit = await event.edit('**سيبدأ البث قريبا..**')
                try:
                    stream = await JoinThenStreamAudio(f'{event.chat_id}', filename)
                    edit = await event.edit('**البث جاري الان**')
                except Exception as error:
                    print (error)
                    edit = await event.edit('**البث جاري, اذا لم يبدأ اوقف البث و حاول مرة اخرى**')
            else:
                edit = await event.edit('**يجب الرد على صوتية**')
                
        except Exception as error:
            edit = await event.edit('**يجب الرد على صوتية**')
    else:
        edit = await event.edit('**يجب الرد على صوتية**')
    

# DOWNLOAD THEN STREAM VIDEO
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.تشغيل فيديو'))
async def VideoFileToVoiceChat(event):
    if event.reply_to != None:
        try:
            from telethon.tl.functions.channels import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(channel=event.chat_id, id=[event.reply_to.reply_to_msg_id]))
        except:
            from telethon.tl.functions.messages import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(id=[event.reply_to.reply_to_msg_id]))
            
        try:
            if message_media.messages[0].media != None and str(message_media.messages[0].media.document.mime_type).startswith('video'):
                edit = await event.edit('**في طور المعالجة و الانجاز**')
                filename = await event.client.download_media(message_media.messages[0], 'video')
                
                edit = await event.edit('**سيبدأ البث قريبا..**')
                try:
                    stream = await JoinThenStreamVideo(f'{event.chat_id}', filename)
                    edit = await event.edit('**البث جاري الان**')
                except Exception as error:
                    print (error)
                    edit = await event.edit('**البث جاري, اذا لم يبدأ اوقف البث و حاول مرة اخرى**')
            else:
                edit = await event.edit('**يجب الرد على الفيديو**')
                
        except Exception as error:
            edit = await event.edit('**يجب الرد على الفيديو**')
    else:
        edit = await event.edit('**يجب الرد على الفيديو**')

# LEAVE STREAM
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.غادر البث'))
async def LeaveStreamFunc(event):
    try:
        leave = await LeaveStream(int(event.chat_id))
        edit = await event.edit('**تمت مغادرة البث**')
    except:
        edit = await event.edit('**تمت مغادرة البث مسبقا**')
    

