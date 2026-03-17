# Telegram AI Assistant Bot (Google Gemini)

ဤ project သည် Google Gemini AI ကို အသုံးပြုပြီး Telegram တွင် အလုပ်လုပ်သော AI Assistant Bot တစ်ခု ဖြစ်ပါသည်။

## အင်္ဂါရပ်များ (Features)

✅ Google Gemini AI ကို အသုံးပြုသော အဆင်သင့်ဖြေကြားမှု
✅ စကားပြောင်းလဲမှု မှတ်တမ်း (Conversation History) ထိန်းသိမ်းခြင်း
✅ အခမဲ့ Hosting ပေါ်တွင် 24/7 အလုပ်လုပ်နိုင်ခြင်း
✅ မြန်မာဘာသာ ပံ့ပိုးခြင်း
✅ လုံခြုံသော API Key ကိုင်တွယ်မှု

## လိုအပ်သည့် အချက်များ

- Python 3.8 သို့မဟုတ် အထက်
- Telegram Bot Token (BotFather မှ)
- Google Gemini API Key (Google AI Studio မှ)
- GitHub Account (Render နဲ့ ချိတ်ဆက်ရန်)
- Render Account (အခမဲ့ Hosting အတွက်)

## အစ စတင်ခြင်း (Local Setup)

### 1. Repository Clone လုပ်ခြင်း

```bash
git clone <your-repo-url>
cd telegram_ai_bot
```

### 2. Python Environment ဖန်တီးခြင်း

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# သို့မဟုတ်
venv\Scripts\activate  # Windows
```

### 3. Dependencies Install လုပ်ခြင်း

```bash
pip install -r requirements.txt
```

### 4. Environment Variables သတ်မှတ်ခြင်း

`.env.example` ကို `.env` အဖြစ် ကူးပြီး သင့်ရဲ့ API Keys တွေ ထည့်သွင်းပါ-

```bash
cp .env.example .env
```

`.env` ဖိုင်ကို အသုံးပြုသူ၏ text editor ဖြင့် ဖွင့်ပြီး အောက်ပါအတိုင်း ပြင်ဆင်ပါ-

```
TELEGRAM_BOT_TOKEN=8666586423:AAFa0fitN_pY0opWG5si8YMomQbQqbUOOgw
GEMINI_API_KEY=AIzaSyBlNBaBINYqNHV4H7bBvmFEie2dnZAcKEA
```

### 5. Bot ကို Local တွင် စမ်းသပ်ခြင်း

```bash
python bot.py
```

Bot သည် အလုပ်လုပ်နေပါလိမ့်မည်။ Telegram တွင် သင့်ရဲ့ Bot ကို ရှာဖွေပြီး `/start` command ကို ပေးပို့ကြည့်ပါ။

## Render တွင် Deploy လုပ်ခြင်း (အခမဲ့ Hosting)

### 1. GitHub ပေါ် Upload လုပ်ခြင်း

သင့်ရဲ့ project ကို GitHub ပေါ် push လုပ်ပါ-

```bash
git add .
git commit -m "Initial commit: Telegram AI Bot"
git push origin main
```

### 2. Render Account ဖန်တီးခြင်း

[Render.com](https://render.com) သို့ သွားပြီး GitHub Account နဲ့ Sign Up လုပ်ပါ။

### 3. New Web Service ဖန်တီးခြင်း

1. Dashboard တွင် **"New +"** ကို နှိပ်ပါ
2. **"Web Service"** ကို ရွေးပါ
3. သင့်ရဲ့ GitHub Repository ကို ရွေးပါ
4. အောက်ပါ အချက်အလက်များ ထည့်သွင်းပါ-

   - **Name**: `telegram-ai-bot` (သို့မဟုတ် အခြား နာမည်)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: `Free` (အခမဲ့)

### 4. Environment Variables သတ်မှတ်ခြင်း

Render Dashboard တွင်-

1. **Environment** tab သို့ သွားပါ
2. အောက်ပါ variables တွေ ထည့်သွင်းပါ-

```
TELEGRAM_BOT_TOKEN=8666586423:AAFa0fitN_pY0opWG5si8YMomQbQqbUOOgw
GEMINI_API_KEY=AIzaSyBlNBaBINYqNHV4H7bBvmFEie2dnZAcKEA
```

### 5. Deploy လုပ်ခြင်း

**"Create Web Service"** ကို နှိပ်ပါ။ Render သည် အလိုအလျှောက် deploy လုပ်ပါလိမ့်မည်။

## အသုံးပြုနိုင်သော Commands

| Command | ရှင်းလင်းချက် |
|---------|------------|
| `/start` | Bot ကို စတင်ခြင်း နှင့် ကြိုဆိုချက် ပြသခြင်း |
| `/help` | အကူအညီ စာမျက်နှာ ပြသခြင်း |
| `/clear` | စကားပြောင်းလဲမှု မှတ်တမ်းကို ရှင်းလင်းခြင်း |

## အသုံးပြုပုံ

1. Telegram တွင် သင့်ရဲ့ Bot ကို ရှာဖွေပါ
2. `/start` command ကို ပေးပို့ပါ
3. မေးခွန်းများ သို့မဟုတ် စာသားများ ပို့ပေးပါ
4. Bot သည် Google Gemini AI ကို အသုံးပြုပြီး အဖြေ ပြန်ပေးပါလိမ့်မည်

## အဆင်မပြေရင် Troubleshooting

### Bot အလုပ်မလုပ်ပါက

1. **Telegram Bot Token ကို စစ်ဆေးပါ**: BotFather မှ ရယူသော token သည် မှန်ကန်သည်ကို အတည်ပြုပါ
2. **Gemini API Key ကို စစ်ဆေးပါ**: Google AI Studio မှ ရယူသော key သည် မှန်ကန်သည်ကို အတည်ပြုပါ
3. **Internet Connection ကို စစ်ဆေးပါ**: Bot သည် internet connection လိုအပ်ပါသည်
4. **Logs ကို ကြည့်ပါ**: Render Dashboard တွင် logs ကို ကြည့်ပြီး error messages ကို ရှာဖွေပါ

### Render တွင် Deploy မအောင်မြင်ပါက

1. **requirements.txt ကို စစ်ဆေးပါ**: Dependencies အားလုံး ကျေးဇူးတင်ပါသည်ကို အတည်ပြုပါ
2. **Procfile ကို စစ်ဆေးပါ**: Procfile သည် မှန်ကန်သည်ကို အတည်ပြုပါ
3. **GitHub ကို Push လုပ်ပါ**: Render သည် အလိုအလျှောက် deploy လုပ်ပါလိမ့်မည်

## လုံခြုံရေး အကြံပြုချက်များ

⚠️ **အရေးကြီး**: သင့်ရဲ့ API Keys တွေကို GitHub ပေါ် မထည့်သွင်းပါနှင့်။ အမြဲတမ်း Environment Variables ကို အသုံးပြုပါ။

## ကျေးဇူးတင်ပါတယ်!

ဤ project ကို အသုံးပြုရန် ကျေးဇူးတင်ပါတယ်။ မည်သည့် အကြံပြုချက် သို့မဟုတ် bug reports ရှိပါက GitHub Issues တွင် ဖန်တီးပါ။

## License

MIT License - အသုံးပြုရန် အခမဲ့ဖြစ်ပါသည်။
