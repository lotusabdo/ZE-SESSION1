from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⩩ بدء استخراج الجلسة ☆.", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="⩩ الصفحة الرئيسية ☆.", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝑋𝐷 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸", url="https://t.me/LLFLLFF"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/lSlJI")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
البوت متخصص في استخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
َժٍᥱُ᥎ :- @lSlJI 
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت البوت
"""

    # About Message
    ABOUT = """
**حول البوت** 
╔━━━━━𓌹 ↱  𝑋𝐷 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸 ↲ 𓌺━━━━━━╗  
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس اكس دي
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/LLFLLFF)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : @lSlJI
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
╚━━━━━𓌹 ↱ 𝑋𝐷 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸 ↲ 𓌺━━━━━━╝
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━𖠙𝑋𝐷𖠙━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس اكس دي
╔━━━━━𓌹 ↱ 𝑋𝐷 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸 ↲ 𓌺━━━━━━╗  

⩩ السورس [𝑋𝐷 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸](https://t.me/LLFLLFF)

╚━━━━━𓌹 ↱  𝑋𝐷 𖣂 ᥉᥆υᖇᥴᥱ ↲ 𓌺━━━━━━╝
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] @lSlJI
⋖━━❲𖣂❳━━𖠙𝑋𝐷𖠙━━❲𖣂❳━━⋗
   """
