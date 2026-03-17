#!/usr/bin/env python3
"""
Telegram AI Assistant Bot using OpenAI API with Webhook
This bot responds to user messages using OpenAI's GPT models
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PORT = int(os.getenv('PORT', 8000))

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Store conversation history for context
user_conversations = {}

# Create FastAPI app
app = FastAPI()

# Create Telegram application
application = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user_id = update.effective_user.id
    user_conversations[user_id] = []
    
    welcome_message = """
🤖 မြန်မာ AI Assistant Bot သို့ ကြိုးဆိုကပါသည်!

ကျနော် OpenAI ၏ GPT AI ကို အသုံးပြုပြီး သင့်ရဲ့ မေးခွန်းများကို ဖြေကြားပေးပါ့မယ်။

အသုံးပြုနိုင်သော Command များ:
/start - Bot ကို စတင်ခြင်း
/clear - စကားပြောင်းလဲမှု မှတ်တမ်းကို ရှင်းလင်းခြင်း
/help - အကူအညီ ရယူခြင်း

ဘာမျိုး မေးခွန်းမျိုး မေးမြန်းနိုင်ပါတယ်။ ကျနော်ကို စာသားပို့ပေးပါ! 📝
"""
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
📚 အကူအညီ

ဤ Bot သည် OpenAI ၏ GPT AI ကို အသုံးပြုပြီး သင့်ရဲ့ မေးခွန်းများကို ဖြေကြားပေးပါသည်။

အသုံးပြုနိုင်သော Command များ:
• /start - Bot ကို စတင်ခြင်း
• /clear - စကားပြောင်းလဲမှု မှတ်တမ်းကို ရှင်းလင်းခြင်း
• /help - ဤ အကူအညီ စာမျက်နှာကို ပြသခြင်း

💡 အကြံပြုချက်များ:
- သင် မေးခွန်းမျိုး မေးမြန်းနိုင်ပါတယ်
- အဖြေများ ပိုမိုအသေးစိတ် ရယူလိုပါက ပြန်လည် မေးမြန်းနိုင်ပါတယ်
- /clear ကို အသုံးပြုပြီး စကားပြောင်းလဲမှု မှတ်တမ်းကို ရှင်းလင်းနိုင်ပါတယ်

ကျနော်ကို စာသားပို့ပေးပါ! 📝
"""
    await update.message.reply_text(help_text)

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Clear conversation history for the user."""
    user_id = update.effective_user.id
    user_conversations[user_id] = []
    await update.message.reply_text("✅ စကားပြောင်းလဲမှု မှတ်တမ်းကို ရှင်းလင်းပြီးပါပြီ။ နောက်ထပ် မေးခွန်းများ မေးမြန်းနိုင်ပါတယ်။")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and respond with OpenAI API."""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Initialize conversation history if not exists
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    
    # Show typing indicator
    await update.message.chat.send_action("typing")
    
    try:
        # Add user message to history
        user_conversations[user_id].append({
            "role": "user",
            "content": user_message
        })
        
        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=user_conversations[user_id],
            max_tokens=2048,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # Add AI response to history
        user_conversations[user_id].append({
            "role": "assistant",
            "content": ai_response
        })
        
        # Send response back to user
        # Telegram has a 4096 character limit per message
        if len(ai_response) > 4096:
            # Split message into chunks
            for i in range(0, len(ai_response), 4096):
                await update.message.reply_text(ai_response[i:i+4096])
        else:
            await update.message.reply_text(ai_response)
            
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        error_message = f"❌ အဆင်မပြေပါ။ အမှားအယွင်း ရှိပါသည်:\n{str(e)[:200]}"
        await update.message.reply_text(error_message)
        
        # Remove the failed message from history
        if user_conversations[user_id]:
            user_conversations[user_id].pop()

@app.post(f"/webhook/{TELEGRAM_BOT_TOKEN}")
async def webhook(request: Request):
    """Handle incoming webhook updates from Telegram."""
    try:
        update_data = await request.json()
        update = Update.de_json(update_data, application.bot)
        await application.process_update(update)
        return JSONResponse({"ok": True})
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return JSONResponse({"ok": False, "error": str(e)}, status_code=500)

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}

async def setup_webhook():
    """Setup webhook for Telegram."""
    try:
        webhook_url = f"https://telegram-bot-r41n.onrender.com/webhook/{TELEGRAM_BOT_TOKEN}"
        await application.bot.set_webhook(url=webhook_url)
        logger.info(f"Webhook set to: {webhook_url}")
    except Exception as e:
        logger.error(f"Error setting webhook: {e}")

@app.on_event("startup")
async def startup():
    """Initialize the application on startup."""
    global application
    
    if not TELEGRAM_BOT_TOKEN or not OPENAI_API_KEY:
        logger.error("Missing required environment variables!")
        logger.error(f"TELEGRAM_BOT_TOKEN: {bool(TELEGRAM_BOT_TOKEN)}")
        logger.error(f"OPENAI_API_KEY: {bool(OPENAI_API_KEY)}")
        return
    
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Initialize application
    await application.initialize()
    
    # Setup webhook
    await setup_webhook()
    
    logger.info("Bot is ready!")

@app.on_event("shutdown")
async def shutdown():
    """Cleanup on shutdown."""
    if application:
        await application.stop()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
