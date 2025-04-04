from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler, ContextTypes, MessageHandler
from PIL import ImageDraw, Image, ImageFont
import re

photo_paths = [
    'namunalar/1.jpg',
    'namunalar/2.jpg',
    'namunalar/3.jpg',
    'namunalar/4.jpg',
    'namunalar/5.jpg',
    'namunalar/6.jpg',
    'namunalar/7.jpg',
    'namunalar/8.jpg',
    'namunalar/9.jpg',
    'namunalar/10.jpg',
    'namunalar/11.jpg',
    'namunalar/12.jpg',
    'namunalar/13.jpg',
    'namunalar/14.jpg',
    'namunalar/15.jpg',
    'namunalar/16.jpg',
    'namunalar/17.jpg',
    'namunalar/18.jpg',
    'namunalar/19.jpg',
    'namunalar/20.jpg',
] 
photo_path2 = [
    'namunalar/yozuvli1.png',
    'namunalar/yozuvli2.png',
    'namunalar/yozuvli3.png',
    'namunalar/yozuvli4.png',
    'namunalar/yozuvli5.png',
    'namunalar/yozuvli6.png',
    'namunalar/yozuvli7.png',
    'namunalar/yozuvli8.png',
    'namunalar/yozuvli9.png',
    'namunalar/yozuvli10.png',
] 
async def salom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    userid = update.message.from_user.id
    chat_id = update.effective_message.chat_id
    
    user = update.effective_user
    res = str(chat_id)
    with open('obuna.txt', 'a') as f:
        f.write(" {}".format(res))
    user = await context.bot.get_chat_member(chat_id='@Kompyuter_savdo_Qadr' ,user_id=userid)
    userstatus = user.status 
    boshlash = [
        [InlineKeyboardButton("Gorizontal taklifnomalar", callback_data='boshlash')],
        [InlineKeyboardButton("Vertikal taklifnomalar", callback_data='boshlash1')]
        ]
    bosh = InlineKeyboardMarkup(boshlash)
    if userstatus in ['member', 'administrator', 'creator']:
       await update.message.reply_text('Hurmatli foydalanuvchi botimizga hush kelibsiz', reply_markup=bosh)
    else:
       await update.message.reply_text('Assalomu alaykum Bizninng taklifnoma yozuvchi botimizga xush kelibsiz Iltimos quyidagi kanalga obuna bo\'ling https://t.me/Qadr_dizayn')
async def rasmga(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        salom = update.message.text
        ozg  = re.search(r'<(.*?)>', salom).group(1)
            
        if ozg == ("Dizayn-1"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 800  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/1.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((600, 350), text, fill="#FFFBF8", font=font)

            # Qatorlarni chizish
            ytext = 500
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#FFFBF8", font=font1)
                ytext += 80

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 850), text2, fill="#FFFBF8", font=font2)

            # Uchinchi matn
            chiz.text((200, 1050), text3, fill="#FFFBF8", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-2"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 600  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/2.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 110)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((550, 240), text, fill="#45603F", font=font)

            # Qatorlarni chizish
            ytext = 400
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#45603F", font=font1)
                ytext += 90

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex +50) // 2
            chiz.text((xtext, 850), text2, fill="#45603F", font=font2)

            # Uchinchi matn
            chiz.text((700, 1000), text3, fill="#45603F", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
            
        elif ozg == ("Dizayn-3"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 800  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/3.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((580, 300), text, fill="#BEAB6E", font=font)

            # Qatorlarni chizish
            ytext = 440
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#BEAB6E", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex - 400) // 2
            chiz.text((xtext, 870), text2, fill="#BEAB6E", font=font2)

            # Uchinchi matn
            chiz.text((500, 1050), text3, fill="#BEAB6E", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-4"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 600  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/4.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((620, 250), text, fill="#DADBDC", font=font)

            # Qatorlarni chizish
            ytext = 400
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width +120) // 2
                chiz.text((x_text, ytext), line, fill="#DADBDC", font=font1)
                ytext += 90

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 900), text2, fill="#DADBDC", font=font2)

            # Uchinchi matn
            chiz.text((250, 1050), text3, fill="#DADBDC", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-5"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
                    # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 600  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/5.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 70 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 90)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )

            # Birinchi matn
            chiz.text((320, 200), text, fill="#E6D783", font=font)

            # Qatorlarni chizish
            ytext = 440
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 600) // 2
                chiz.text((x_text, ytext), line, fill="#E6D783", font=font1)
                ytext += 90

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex - 600) // 2
            chiz.text((xtext, 950), text2, fill="#E6D783", font=font2)

            # Uchinchi matn
            chiz.text((300, 1200), text3, fill="#E6D783", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-6"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 600  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/6.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  110 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 110)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((280, 140), text, fill="#D7C49A", font=font)

            # Qatorlarni chizish
            ytext = 340
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 300) // 2
                chiz.text((x_text, ytext), line, fill="#D7C49A", font=font1)
                ytext += 90

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex + 350) // 2
            chiz.text((xtext, 900), text2, fill="#D7C49A", font=font2)

            # Uchinchi matn
            chiz.text((750, 1240), text3, fill="#D7C49A", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-7"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 720  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/7.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((580, 100), text, fill="#D7C49A", font=font)

            # Qatorlarni chizish
            ytext = 300
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#D7C49A", font=font1)
                ytext += 110

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 1000), text2, fill="#D7C49A", font=font2)

            # Uchinchi matn
            chiz.text((500, 1300), text3, fill="#D7C49A", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-8"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
                    # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 600  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/8.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((880, 120), text, fill="#36466F", font=font)

            # Qatorlarni chizish
            ytext = 350
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#36466F", font=font1)
                ytext += 120

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex - 400) // 2
            chiz.text((xtext, 1080), text2, fill="#36466F", font=font2)

            # Uchinchi matn
            chiz.text((100, 1300), text3, fill="#36466F", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-9"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/9.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((440, 250), text, fill="#99866D", font=font)

            # Qatorlarni chizish
            ytext = 400
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#99866D", font=font1)
                ytext += 120

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex-150) // 2
            chiz.text((xtext, 950), text2, fill="#99866D", font=font2)

            # Uchinchi matn
            chiz.text((650, 1180), text3, fill="#99866D", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')

        elif ozg == ("Dizayn-10"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
                    # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/10.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((800, 240), text, fill="#EDF2F8", font=font)

            # Qatorlarni chizish
            ytext = 420
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width + 50) // 2
                chiz.text((x_text, ytext), line, fill="#EDF2F8", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex-150) // 2
            chiz.text((xtext, 940), text2, fill="#EDF2F8", font=font2)

            # Uchinchi matn
            chiz.text((500, 1200), text3, fill="#EDF2F8", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-11"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"

            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

                # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/11.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )

            # Birinchi matn
            chiz.text((800, 240), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 420
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 940), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((500, 1200), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
        
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-12"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/12.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )

            # Birinchi matn
            chiz.text((800, 240), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 420
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 940), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((600, 1200), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-13"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/13.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )

            # Birinchi matn
            chiz.text((800, 240), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 520
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 980), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((600, 1200), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-14"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/14.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((800, 240), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 420
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 200) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex -200) // 2
            chiz.text((xtext, 940), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((600, 1200), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-15"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/15.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((800, 60), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 240
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 200) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex -200) // 2
            chiz.text((xtext, 750), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((300, 1000), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-16"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/16.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((750, 260), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 440
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 200) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex -200) // 2
            chiz.text((xtext, 950), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((300, 1200), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-17"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/17.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((750, 260), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 440
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex) // 2
            chiz.text((xtext, 950), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((300, 1300), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-18"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/18.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 70 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((750, 260), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 440
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 540) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex - 540) // 2
            chiz.text((xtext, 950), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((300, 1300), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-19"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/19.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 70 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 110)
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((500, 360), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 540
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width - 540) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex - 540) // 2
            chiz.text((xtext, 950), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((100, 1300), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Dizayn-20"):
            hur = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            sana = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            man = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            text = "Assalomu alaykum"
            text3 = f"Manzil: {man}"
            text1 = f"Hurmatli {hur}, sizni {sana} kuni NIKOH to‘yimiz munosabati bilan yoziladigan dasturxonimizga tashrif buyurishingizni so‘raymiz. Kamoli ehtirom bilan!!"
            # Matnni qatorlarga bo'lish
            words = text1.split(' ')
            max_width = 750  # Maksimal ruxsat etilgan kenglik (sizga moslab o'zgartiring)
            qatorlar = []
            current_line = ""

            # Qatorlarga bo'lish algoritmi
            for word in words:
                test_line = current_line + word + " "
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype("fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open("Dizaynlar/20.png")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype("fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype("fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype("fonts/ariston_normal.ttf", 100 )
            font3 = ImageFont.truetype("fonts/ariston_normal.ttf", 60 )



            # Birinchi matn
            chiz.text((600, 60), text, fill="#E2B448", font=font)

            # Qatorlarni chizish
            ytext = 340
            eni_rasm, boyi_rasm = rasm.size

            for line in qatorlar:
                line = line.strip()
                text_width = chiz.textbbox((0, 0), line, font=font1)[2]
                x_text = (eni_rasm - text_width) // 2
                chiz.text((x_text, ytext), line, fill="#E2B448", font=font1)
                ytext += 100

            # Ikkinchi matn
            tex = chiz.textbbox((0, 0), text2, font=font2)[2]
            xtext = (eni_rasm - tex - 300) // 2
            chiz.text((xtext, 800), text2, fill="#E2B448", font=font2)

            # Uchinchi matn
            chiz.text((300, 1000), text3, fill="#E2B448", font=font3)

            rasm.save("yozuvli1.png")
            await update.message.reply_photo(photo=open("yozuvli1.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-1"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/21.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""

            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3+50)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 270), text1 , fill="#E1B973", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-2"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/22.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""

            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 430
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik+300) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-50)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#08080A", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-3"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/23.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""

            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3+50)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 270), text1 , fill="#E1B973", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-4"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/24.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""

            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 430
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik+300) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#08080A", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-5"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/25.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""
            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""

            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#796544", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-6"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/26.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""
            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#796544", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-7"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/27.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""
            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#796544", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-8"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/28.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""
            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#796544", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-9"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/29.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""
            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  80 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 400
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 300), text1 , fill="#796544", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 950), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        elif ozg == ("Design-10"):
            text1 = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
            text2 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
            text3 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
            text4 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
            ismlar = text3.split()
            kuyov = ismlar[0]
            kelin = ismlar[1]
            yoz = "Sizni nikoh to`yimizga taklif qilamiz."
            yoz1 = "va"
            rasm = Image.open("Dizaynlar/30.jpg")

            words = yoz.split(' ')
            max_uzunlik = 500
            qatorlar = []
            oldingi = ""
            for word in words:
                test_qator = oldingi + word + " "   
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_qator, font= ImageFont.truetype( "fonts/salom.ttf",  50 ))[2:]
                if width <= max_uzunlik:
                    oldingi = test_qator
                else:
                    qatorlar.append(oldingi)
                    oldingi = word + " "
            qatorlar.append(oldingi)


            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype( "fonts/salom.ttf",  90 )
            font1 = ImageFont.truetype("fonts/salom.ttf", 50 )
            font2 = ImageFont.truetype("fonts/salom.ttf", 50)
            font3 = ImageFont.truetype("fonts/salom.ttf", 100 )
            font4 = ImageFont.truetype("fonts/salom.ttf", 50 )

            ytext = 350
            eni, boyi = rasm.size
            for chiziq in qatorlar:
                chiziq = chiziq.strip()
                text_uzunlik = chiz.textbbox((0, 0), chiziq, font=font1)[2]
                x_text = (eni - text_uzunlik + 200 ) // 2
                chiz.text((x_text, ytext), chiziq, fill="#08080A", font=font1)
                ytext +=50


            uzun = chiz.textbbox((0,0), text1, font=font)[2]
            uzun1 = chiz.textbbox((0,0), yoz1, font=font2)[2]
            uzun2 = chiz.textbbox((0,0), kelin, font=font3)[2]
            uzun3 = chiz.textbbox((0,0), text2, font=font3)[2]
            uzun5= chiz.textbbox((0,0), text4, font=font2)[2]
            xtext = (eni - uzun + 400)//2
            xtext1 = (eni - uzun1)//2
            xtext2 = (eni - uzun2-180)//2
            xtext3 = (eni - uzun2+240)//2
            xtext4 = (eni - uzun3-70)//2
            xtext5 = (eni - uzun5+50)//2
            chiz.text((xtext, 150), text1 , fill="#796544", font=font)
            chiz.text((xtext1, 620), yoz1 , fill="#E1B973", font=font2)
            chiz.text((xtext2, 530), kuyov, fill="#796544", font=font3)
            chiz.text((xtext3, 660), kelin, fill="#796544", font=font3)
            chiz.text((xtext4, 800), text2, fill="#E1B973", font=font3)
            chiz.text((xtext5, 1100), text4, fill="#08080A", font=font1)
            rasm.save("yozuvli2.png")
            await update.message.reply_photo(photo=open("yozuvli2.png", "rb"), parse_mode='HTML')
        else :
            await update.message.reply_text('Iltimos  botdan foydalanishdan oldin qo`llanmani ko`rib chiqing!!! /yordam ni bosing.  ')
    except Exception as err:
        await update.message.reply_text('Text hato yozilgan /yordam ni bosing va qo`llanmani korib chiqing')
async def yordam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    video = open('yordam.mp4', 'rb')
    yozuv = "Iltimos videoni to`liq ko`ring"
    await update.message.reply_video(video=video, caption=yozuv)
async def rek(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('obuna.txt', 'r') as f:
        text = f.read()
        tes = text.split()
        sel = set(tes)
    for sat in (sel):
        son = int(sat)
    with open('rek.txt', 'r') as q:
        rasmtext = q.read()
    with open('post1.jpg', 'rb') as photo:
        await context.bot.send_photo(son, photo=photo, caption=rasmtext)

async def Dizaynlar1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    for i, photo_path in enumerate(photo_paths):
        # Inline keyboard yaratish (1 ta tugma har bir rasm uchun)
        keyboard = [
            [InlineKeyboardButton(f" {i+1}-Dizayn", callback_data=f'salom{i+1}')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Rasm yuborish
        with open(photo_path, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id,
                                         photo=photo_file,
                                         caption=f' {i+1}-Dizayn',
                                         reply_markup=reply_markup)
async def Dizaynlar2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    for i, photo_path1 in enumerate(photo_path2):
        # Inline keyboard yaratish (1 ta tugma har bir rasm uchun)
        keyboard = [
            [InlineKeyboardButton(f" {i+1}-Dizayn", callback_data=f'turoq{i+1}')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Rasm yuborish
        with open(photo_path1, 'rb') as photo_file:
            await context.bot.send_photo(chat_id=chat_id,
                                         photo=photo_file,
                                         caption=f' {i+1}-Dizayn',
                                         reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data

    if callback_data.startswith('salom'):
        button_number = int(callback_data.lstrip('salom'))
        await query.answer()
        await context.bot.send_message(chat_id=query.message.chat_id,
                                      text=f"__________<Dizayn-{button_number}>__________ \nHurmatlidan keyin chiqadigan ism<Davronbek>\nTo`y bo`ladigan sana<19-dekabr>\nKelin va kuyov ismi<Baxtiyor va  Odina>\nManzil<Kosonsoy shahri>")
    elif query.data =='boshlash':
        await Dizaynlar1(update, context)
    elif query.data =='boshlash1':
        await Dizaynlar2(update, context)
    elif callback_data.startswith('turoq'):
        button_number = int(callback_data.lstrip('turoq'))
        await query.answer()
        await context.bot.send_message(chat_id=query.message.chat_id,
                                      text=f"__________<Design-{button_number}>__________ \nHurmatlidan keyin chiqadigan ism<Davronbek>\nTo`y bo`ladigan sana<19 | 09 | 2024>\nKelin va kuyov ismi<Baxtiyor  Odina>\nManzil<Kosonsoy shahri>")

app = ApplicationBuilder().token("1952748542:AAFXU2eglpwEaMbig4GOZhZ2vtew6g9i9nA").build()
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("start", salom))
app.add_handler(CommandHandler("restart", salom))
app.add_handler(CommandHandler("yordam", yordam))
app.add_handler(CommandHandler("reklama2002", rek))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, rasmga))

app.run_polling()
