import os
import shutil
from telethon.errors.rpcerrorlist import MediaEmptyError
from Arab import iqthon
from ..core.managers import edit_or_reply
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.utils import reply_id
plugin_category = "@iqthon"
@iqthon.iq_cmd(pattern="رابط الحذف")
async def _(kno):
    await edit_or_reply (kno, "**رابـط الحـذف ↬** https://telegram.org/deactivate \n\n ** بـوت الحـذف  ↬** @LC6BOT ")
