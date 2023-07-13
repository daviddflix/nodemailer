from typing import Final
from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TOKEN: Final = '6185446761:AAGXE98znTx0dEKkRdoA-Zxum2VPOXTSHhI'
BOT_USERNAME: Final = '@QCryptos_bot'


async def invitation_link(context):
          chat_id = -1001869959989
          invite = await context.bot.create_chat_invite_link(chat_id=chat_id, name='AI Alpha Link Invitation',
          member_limit=1)

          return invite.invite_link



async def send_email(link_to_chat):
       
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'daviddflix@gmail.com'
        sender_password = 'jchmimzuurlmpndh'
        recipient_email = 'david-972010@hotmail.com'
        subject = 'AI Alpha Invitation Link'

        emailBody = f'''
                    <h1>Welcome to AI Alpha</h1>
                    <p style="margin: 0;">We are happy you have decided to try our product</p>
                    <p style="margin: 0 0 2rem 0;">To start interacting with AI Alpha Bot click on the next Button</p>
                    <a href={link_to_chat} style="padding: 8px 20px; margin-top: 1.5rem; background-color: #fcd535; border: none; border-radius: 5px; font-weight: 600; text-decoration: none; color: #282828; font-style:Sans-serif;">Access Link</a>
                    '''
        body = emailBody

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'html'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        try:
            server.login(sender_email, sender_password)
           

            server.send_message(message)
            print("Email sent successfully")

        except Exception as e:
            print("error found", str(e))

        finally:
            server.quit()

# command to get invitation link and send email.
async def sender_command(update, context):
    link = await invitation_link(context)
    print('invitation > ', link)
    await send_email(link)
   
    await update.message.reply_text('Hello, This is Alpha an IA Bot that can help you with any question you may have about Cryptocurrencies!')


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # app.add_handler(CommandHandler('start', start_command))

    # Log all errors
    app.add_error_handler(error)

    print('Bot is running...')
    app.run_polling(poll_interval=5)