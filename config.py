"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/d750805742875ce957625.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
    
  ══✿══╡°˖✧ 🇮🇳 sɴᴏᴡ ʙᴏᴛᴢ ɪɴᴅɪᴀ 🇮🇳 ✧˖°╞══✿══ 
    
ᴛᴇʟᴇɢʀᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴘʀɪᴠᴀᴛᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs
ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ 
ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴀɴᴅ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ʙʏ sɴᴏᴡ ʙᴏᴛᴢ
ᴡɪᴛʜ ᴍᴀɴʏ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴇɴᴊᴏʏ !!!!! ;)

Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @KDRAMSHINDI</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/PYRO_BOTZ/53>ᴛᴇᴀᴍ sɴᴏᴡ ʙᴏᴛs</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://github.com/lntechnical2>sɪʀɪsʜ</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: sɴᴏᴡ V6.0.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b><u>    Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/PYRO_BOTZ_CHAT>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛ ʟᴀᴢʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴀɴᴅ ᴛᴇᴀᴍ🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
• ❣️ <a href=https://github.com/lazydeveloperr>ʟᴀᴢʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</a>
• ❣️ <a href=https://t.me/Sirisha_lahari>sɪʀɪsʜᴀ</a>
• ❣️ <a href=https://t.me/SIRISH_KRISHNA_CHOWDHARY>ᴠɪᴊᴀʏ ᴋʀɪsʜɴᴀ</a>
• ❣️ <a href=https://t.me/SIRISH_123>sɪʀɪsʜ</a>
• ❣️ <a href=https://t.me/about_jeol>ᴜᴊᴊᴡᴀʟ</a>"""
    
    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ 

 ╰┈➤ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʀᴏʙʟᴇᴍ ʟɪᴋᴇ sᴛᴏᴘᴘɪɴɢ ᴀɴᴅ ᴋɪɴᴅ ᴏғ ᴛʜɪɴɢᴇs
 sʜᴏᴜʟᴅ ʙᴇ ʀᴇᴘᴏʀᴛᴇᴅ ᴛᴏ ᴜs ᴡᴇ ᴡɪʟʟ ғɪx ɪᴛ ᴏʀ ᴛᴇʟʟ ʏᴏᴜ ᴛʜᴇ 
 sᴏʟᴜᴛɪᴏɴ ᴀɴᴅ ʜᴇʟᴘ ʏᴏᴜ ᴛᴇᴀᴍ sɴᴏᴡ ʙᴏᴛᴢ ɪɴᴅɪᴀ</b>"""
    
    SNOW_TXT = """<b>\n
    
    ᴄʜᴜᴛɪʏᴀ ɢʜᴀʀ ᴊᴀ ʙsᴅᴋ sᴏᴜʀᴄᴇ ɴᴇʜɪ ᴍɪʟᴇɢᴀ ᴀɴᴅ ᴋᴇsᴇ ᴋᴏ
    ᴛʀᴜsᴛ ᴍᴀᴛʜ ᴋᴀʀ ɴᴀ ɪsssᴀ ʀᴇᴘᴏ ʙᴀss ᴇᴋᴋ ʜᴇ ʜᴀɪ ᴀɴᴅ ᴡᴏ
    ᴛᴇᴀᴍ sɴᴏᴡ ʙᴏᴛs ɴᴇ ʙᴀɴᴀʏᴀ ʜᴀɪ ᴀɢᴀʀ ʏᴇ ʀᴇᴘᴏ ᴄʜᴀʏɪᴇ
    ᴛʜᴏ ᴘᴀʏ ᴋᴀʀ ɴᴀ ᴘᴀᴅᴇɢᴀ ᴀɴᴅ ᴏɴʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀs ᴅᴏɴᴛ 
    ᴅᴏ ᴛʜɪʀᴅ ᴘᴀʀᴛʏ ᴘᴀʏᴍᴇɴᴛs ᴀʟʟ ᴘᴀʏᴍᴇɴᴛs ᴏɴʟʏ ɪɴ ʀᴇᴅᴇᴇᴍ ᴄᴏᴅᴇs
    
    ᴛʜᴀɴᴋs ;) ᴇɴᴊᴏʏ ʙᴏᴛ !!</b>"""
   
    
    LINKS_TXT = """<b>\n 
    
    ᴊᴏɪɴ ᴀɴᴅ ᴀʟʟ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴀʟʟ ᴀʀᴇ ғɪʟᴇs ᴄʜᴀɴɴᴇʟs 
    ᴇɴᴊᴏʏ ғʟᴏᴋs ᴀɴᴅ ᴍᴏᴢ ʟᴏ sᴏ ᴊᴏɪɴ ᴀʟʟ ᴀɴᴅ sʜᴀʀᴇ ᴀɴᴅ
    sᴜᴘᴘᴏʀᴛ ᴜs ᴡᴇ ᴡɪʟʟ ᴅᴏ ᴍᴏʀᴇ ᴛʜɪɴɢᴇs ᴀɴᴅ sᴏ ᴍᴀɴʏ 
    ʙᴏᴛs ᴀʀᴇ ᴀʙᴏᴜᴛ ᴛᴏ ᴄᴏᴍᴇ sᴏ ᴇɴᴊᴏʏ !!!
    
    ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ -  <a href=https://t.me/KDRAMSHINDI>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
    ᴋᴅʀᴀᴍᴀs ᴄʜᴀɴɴᴇʟ - <a href=https://t.me/k_Drama_Hindi_Dubbed_avl>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
    ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ - <a href=https://t.me/k_Drama_Hindi_Dubbed_avl
    sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ - <a href=https://t.me/k_Drama_Hindi_Dubbed_avl
    
    ᴊᴏɪɴ ᴛʜᴇᴍ ᴀʟʟ ᴀɴᴅ ᴍᴏᴢ ʟᴏ ᴇɴᴊᴏʏ </b>"""



    SR_TXT = """<b>\n
    
══✿══╡°˖✧ʀᴜʟᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ✧˖°╞══✿══

╰┈➤😂 ᴡᴀʀɴɪɴɢ ᴘᴏʀɴ ᴄᴏɴᴛᴇɴᴛs ᴀʀᴇ ʙᴀɴɴᴇᴅ
╰┈➤😅 ᴅᴏɴᴛ sᴘᴀᴍ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ғɪʟᴇs 
╰┈➤😇 sᴘᴇᴇᴅ ᴡɪʟʟ ᴅᴇᴘᴇɴᴅs ᴏɴ ᴜsᴇʀs sɪ ᴡᴀɪᴛ
╰┈➤🥺 ᴍᴜsᴛ ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ
╰┈➤🤯 ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴏᴠɪᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ
╰┈➤😍 ʏᴏᴜʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɪs ᴄᴏʟʟᴇᴄᴛᴇᴅ ғᴏʀ sᴇᴄᴜʀɪᴛʏ
╰┈➤😁 ᴛʜɪs ʀᴇᴘᴏ ɪs ɴᴏᴛ ғᴏʀ sᴀʟᴇ ᴅᴏɴᴛ ᴀsᴋ 
╰┈➤🧐 ᴅᴏɴᴛ ᴅɪsᴛᴜʀʙ ᴅᴇᴠᴇʟᴏᴘᴇʀs ʀᴇsᴜʟᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ
╰┈➤😧 ᴛʜɪs ʙᴏᴛ ɪs ᴏᴘᴇɴ ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ ᴜsᴇ ғᴀɪʀʟʏ
╰┈➤🤬 ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴠɪᴏʟᴀᴛɪᴏɴ ᴏғ ʀᴜʟᴇs ʏᴏᴜ ᴡɪʟʟ ʙᴀɴɴᴇᴅ ғᴏʀᴇᴠᴇʀ

     •┈••✦ sɴᴏᴡ ʙᴏᴛᴢ ɪɴᴅɪᴀ ✦••┈•      

╰┈➤ ❝ [ᴀᴄᴄᴇᴘᴛ ᴏʀ ɢᴇᴛ ʟᴏsᴛ]</b>"""


