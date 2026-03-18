#!/usr/bin/env python3
"""
Telegram AI Assistant Bot using Google Gemini API with Polling
This bot responds to user messages using Google's Gemini AI model
"""

import os
import logging
import sys
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Import Gemini library
try:
    import google.generativeai as genai
    logger.info("✅ google.generativeai library imported successfully")
except ImportError:
    logger.error("❌ google.generativeai library not found. Please install it.")
    sys.exit(1)

# Configure Gemini API
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    logger.info("✅ Gemini API configured successfully")
else:
    logger.error("❌ GEMINI_API_KEY not found in environment variables")
    sys.exit(1)

# Store conversation history for context
user_conversations = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user_id = update.effective_user.id
    user_conversations[user_id] = []
    
    welcome_message = """
🤖 မြန်မာ AI Assistant Bot သို့ ကြိုးဆိုကပါသည်!

ကျနော် Google Gemini AI ကို အသုံးပြုပြီး သင့်ရဲ့ မေးခွန်းများကို ဖြေကြားပေးပါ့မယ်။

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

ဤ Bot သည် Google Gemini AI ကို အသုံးပြုပြီး သင့်ရဲ့ မေးခွန်းများကို ဖြေကြားပေးပါသည်။

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
    """Handle incoming messages and respond with Gemini AI."""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Initialize conversation history if not exists
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    
    # Show typing indicator
    await update.message.chat.send_action("typing")
    
    try:
        # Create model instance
        model = genai.GenerativeModel('gemini-pro')
        
        # Prepare conversation history for context
        history = []
        for msg in user_conversations[user_id]:
            history.append(msg)
        
        # Start chat with history
        chat = model.start_chat(history=history)
        
        # Get response from Gemini with retry logic
        max_retries = 3
        retry_count = 0
        response = None
        
        while retry_count < max_retries:
            try:
                response = chat.send_message(user_message)
                break
            except Exception as e:
                retry_count += 1
                if retry_count < max_retries:
                    logger.warning(f"Retry {retry_count}/{max_retries}: {str(e)}")
                    time.sleep(2)  # Wait before retrying
                else:
                    raise
        
        if response is None:
            raise Exception("Failed to get response from Gemini API after retries")
        
        ai_response = response.text
        
        # Store conversation in history
        user_conversations[user_id].append({
            "role": "user",
            "parts": [user_message]
        })
        user_conversations[user_id].append({
            "role": "model",
            "parts": [ai_response]
        })
        
        # Send response back to user
        # Telegram has a 4096 character limit per message
        if len(ai_response) > 4096:
            # Split message into chunks
            for i in range(0, len(ai_response), 4096):
                await update.message.reply_text(ai_response[i:i+4096])
        else:
            await update.message.reply_text(ai_response)
        
        logger.info(f"✅ Successfully responded to user {user_id}")
            
    except Exception as e:
        logger.error(f"❌ Error processing message: {e}", exc_info=True)
        error_message = f"❌ အဆင်မပြေပါ။ အမှားအယွင်း ရှိပါသည်:\n{str(e)[:200]}"
        await update.message.reply_text(error_message)

def main() -> None:
    """Start the bot."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ Missing TELEGRAM_BOT_TOKEN environment variable!")
        sys.exit(1)
    
    if not GEMINI_API_KEY:
        logger.error("❌ Missing GEMINI_API_KEY environment variable!")
        sys.exit(1)
    
    logger.info("=" * 60)
    logger.info("✅ Starting Telegram AI Bot with Gemini API...")
    logger.info(f"Bot Token: {TELEGRAM_BOT_TOKEN[:20]}...")
    logger.info(f"Gemini API Key: {GEMINI_API_KEY[:20]}...")
    logger.info("=" * 60)
    
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    logger.info("✅ Bot is running with polling mode...")
    logger.info("Waiting for messages...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
