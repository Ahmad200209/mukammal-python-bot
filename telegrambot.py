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
] 
async def salom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    userid = update.message.from_user.id
    chat_id = update.effective_message.chat_id
    
    user = update.effective_user
    res = str(chat_id)
    with open('obuna.txt', 'a') as f:
        f.write(" {}".format(res))
    user = await context.bot.get_chat_member(chat_id='@Qadr_dizayn' ,user_id=userid)
    userstatus = user.status 
    boshlash = [[InlineKeyboardButton("Boshlash", callback_data='boshlash')]]
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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
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
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/4.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/5.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 70 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 90)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 60 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/6.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  110 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 110)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/7.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/8.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/9.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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
                width, _ = ImageDraw.Draw(Image.new('RGB', (0, 0))).textbbox((0, 0), test_line, font=ImageFont.truetype(" fonts/ariston_normal.ttf", 40))[2:]
                if width <= max_width:
                    current_line = test_line
                else:
                    qatorlar.append(current_line)
                    current_line = word + " "
            qatorlar.append(current_line)


            rasm = Image.open(" Dizaynlar/10.jpg")
            chiz = ImageDraw.Draw(rasm)
            font = ImageFont.truetype(" fonts/ariston_normal.ttf",  90 )
            font1 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )
            font2 = ImageFont.truetype(" fonts/ariston_normal.ttf", 100)
            font3 = ImageFont.truetype(" fonts/ariston_normal.ttf", 80 )

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

        else :
            await update.message.reply_text('Iltimos  botdan foydalanishdan oldin qo`llanmani ko`rib chiqing!!! /yordam ni bosing.  ')
    except Exception as err:
        await update.message.reply_text('Text hato yozilgan /yordam ni bosing va qo`llanmani korib chiqing')
async def yordam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hurmatli foydalanuvchi bu botdan foydalanishda e`tiborli bo`ling yuborilgan videoni to`liq ko`ring")
async def rek(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('obuna.txt', 'r') as f:
        text = f.read()
        tes = text.split()
        sel = set(tes)
    for sat in (sel):
        son = int(sat)
    with open('rek/rek.txt', 'r') as q:
        rasmtext = q.read()
    with open('rek/post1.jpg', 'rb') as photo:
        await context.bot.send_photo(son, photo=photo, caption=rasmtext)

async def dizaynlar1(update: Update, context: ContextTypes.DEFAULT_TYPE):
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


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data

    if callback_data.startswith('salom'):
        button_number = int(callback_data.lstrip('salom'))
        await query.answer()
        await context.bot.send_message(chat_id=query.message.chat_id,
                                      text=f"__________<Dizayn-{button_number}>__________ \nHurmatlidan keyin chiqadigan ism<Davronbek>\nTo`y bo`ladigan sana<19-dekabr>\nKelin va kuyov ismi<Baxtiyor va Odina>\nManzil<Kosonsoy shahri>")
    elif query.data =='boshlash':
        await dizaynlar1(update, context)


app = ApplicationBuilder().token("1952748542:AAH3EVIa0wGZg1tcuw3w_qs8aCFjH6r14gA").build()
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("start", salom))
app.add_handler(CommandHandler("restart", salom))
app.add_handler(CommandHandler("yordam", yordam))
app.add_handler(CommandHandler("reklama2002", rek))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, rasmga))

app.run_polling()
