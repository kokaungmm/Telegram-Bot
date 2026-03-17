# Render တွင် Deploy လုပ်ခြင်းအတွက် အသေးစိတ် လမ်းညွှန်ချက်

ဤ လမ်းညွှန်ချက်သည် သင့်ရဲ့ Telegram AI Bot ကို Render ပေါ်တွင် အခမဲ့ hosting နဲ့ အလုပ်လုပ်စေရန် အသေးစိတ် ရှင်းပြထားပါသည်။

## အဆင့် ၁: GitHub ပေါ် Project Upload လုပ်ခြင်း

### 1.1 GitHub Repository ဖန်တီးခြင်း

1. [GitHub.com](https://github.com) သို့ သွားပါ
2. **"New"** ခလုတ်ကို နှိပ်ပါ
3. Repository အတွက် နာမည်တစ်ခု ပေးပါ (ဥပမာ: `telegram-ai-bot`)
4. **"Create repository"** ကို နှိပ်ပါ

### 1.2 Local Machine မှ GitHub သို့ Push လုပ်ခြင်း

သင့်ရဲ့ computer ပေါ်တွင် terminal/command prompt ကို ဖွင့်ပြီး အောက်ပါ commands တွေကို အလိုအလျှောက် ရိုက်ပါ-

```bash
# Project directory သို့ သွားပါ
cd /home/ubuntu/telegram_ai_bot

# Git initialize လုပ်ပါ
git init

# GitHub repository ကို remote အဖြစ် ထည့်သွင်းပါ
git remote add origin https://github.com/YOUR_USERNAME/telegram-ai-bot.git

# အားလုံး files ကို staging area သို့ ထည့်သွင်းပါ
git add .

# Commit လုပ်ပါ
git commit -m "Initial commit: Telegram AI Bot with Gemini API"

# Main branch သို့ push လုပ်ပါ
git branch -M main
git push -u origin main
```

**မှတ်ချက်**: `YOUR_USERNAME` ကို သင့်ရဲ့ GitHub username နဲ့ အစားထိုးပါ။

## အဆင့် ၂: Render Account ဖန်တီးခြင်း

1. [Render.com](https://render.com) သို့ သွားပါ
2. **"Sign up"** ကို နှိပ်ပါ
3. GitHub Account နဲ့ Sign Up လုပ်ပါ (အလွယ်ဆုံး နည်း)
4. Render သည် သင့်ရဲ့ GitHub account ကို အခွင့်အရေး ပေးရန် တောင်းဆိုပါလိမ့်မည်။ **"Authorize"** ကို နှိပ်ပါ

## အဆင့် ၃: Render တွင် New Service ဖန်တီးခြင်း

### 3.1 Dashboard မှ New Service ဖန်တီးခြင်း

1. Render Dashboard သို့ သွားပါ
2. **"New +"** ခလုတ်ကို နှိပ်ပါ
3. **"Web Service"** ကို ရွေးပါ

### 3.2 GitHub Repository ချိတ်ဆက်ခြင်း

1. **"Connect a repository"** ကို နှိပ်ပါ
2. သင်ဖန်တီးထားသော `telegram-ai-bot` repository ကို ရွေးပါ
3. **"Connect"** ကို နှိပ်ပါ

### 3.3 Service Configuration

အောက်ပါ အချက်အလက်များ ထည့်သွင်းပါ-

| အချက်အလက် | တန်ဖိုး |
|-----------|--------|
| **Name** | `telegram-ai-bot` (သို့မဟုတ် အခြား နာမည်) |
| **Environment** | `Python 3` |
| **Region** | `Singapore` (သို့မဟုတ် သင်နီးစပ်သော region) |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python bot.py` |
| **Instance Type** | `Free` |

## အဆင့် ၄: Environment Variables သတ်မှတ်ခြင်း

### 4.1 Environment Tab သို့ သွားခြင်း

1. Service page တွင် **"Environment"** tab ကို နှိပ်ပါ
2. **"Add Environment Variable"** ကို နှိပ်ပါ

### 4.2 Variables ထည့်သွင်းခြင်း

အောက်ပါ variables တွေကို ထည့်သွင်းပါ-

**Variable 1:**
- **Key**: `TELEGRAM_BOT_TOKEN`
- **Value**: `8666586423:AAFa0fitN_pY0opWG5si8YMomQbQqbUOOgw`

**Variable 2:**
- **Key**: `GEMINI_API_KEY`
- **Value**: `AIzaSyBlNBaBINYqNHV4H7bBvmFEie2dnZAcKEA`

ပြီးတဲ့အခါ **"Save"** ကို နှိပ်ပါ။

## အဆင့် ၅: Deploy လုပ်ခြင်း

1. Service page သို့ ပြန်သွားပါ
2. **"Create Web Service"** ကို နှိပ်ပါ
3. Render သည် အလိုအလျှောက် deploy လုပ်ပါလိမ့်မည်

## အဆင့် ၆: Deploy Status ကြည့်ခြင်း

1. Dashboard တွင် သင့်ရဲ့ service ကို ရွေးပါ
2. **"Logs"** tab ကို နှိပ်ပါ
3. Deploy process ကို ကြည့်ပါ

အောင်မြင်ပါက အောက်ပါ message ကို မြင်ပါလိမ့်မည်-
```
Bot is starting...
```

## အဆင့် ၇: Bot ကို Test လုပ်ခြင်း

1. Telegram တွင် သင့်ရဲ့ Bot ကို ရှာဖွေပါ
2. `/start` command ကို ပေးပို့ပါ
3. Bot သည် ကြိုဆိုချက် ပြန်ပေးပါလိမ့်မည်

## အဆင်မပြေရင် Troubleshooting

### Deploy မအောင်မြင်ပါက

**Error: Build failed**
- `requirements.txt` ကို ကြည့်ပြီး dependencies အားလုံး မှန်ကန်သည်ကို အတည်ပြုပါ
- `Procfile` သည် မှန်ကန်သည်ကို အတည်ပြုပါ

**Error: Application crashed**
- Logs ကို ကြည့်ပြီး error message ကို ရှာဖွေပါ
- Environment variables သည် မှန်ကန်သည်ကို အတည်ပြုပါ

### Bot အလုပ်မလုပ်ပါက

1. **Telegram Bot Token ကို စစ်ဆေးပါ**: Token သည် မှန်ကန်သည်ကို အတည်ပြုပါ
2. **Gemini API Key ကို စစ်ဆေးပါ**: Key သည် မှန်ကန်သည်ကို အတည်ပြုပါ
3. **Logs ကို ကြည့်ပါ**: Render dashboard တွင် logs ကို ကြည့်ပြီး error messages ကို ရှာဖွေပါ

## အခမဲ့ Tier ကန့်သတ်ချက်များ

Render ၏ အခမဲ့ tier တွင် အောက်ပါ ကန့်သတ်ချက်များ ရှိပါသည်-

- **CPU**: အကန့်အသတ် ရှိပါသည်
- **RAM**: 512 MB
- **Disk**: 1 GB
- **Uptime**: အချိန်အကန့်အသတ် ရှိနိုင်ပါသည် (အများအားဖြင့် အလုပ်လုပ်ပါသည်)

အသုံးပြုမှု များပြားလာပါက အခကြေးငွေပေးရသော plan သို့ ပြောင်းလဲနိုင်ပါသည်။

## အပ်ဒေတ်များ ပြုလုပ်ခြင်း

Bot ကို အပ်ဒေတ်လုပ်လိုပါက-

1. Local machine တွင် code ကို ပြင်ဆင်ပါ
2. Git နဲ့ commit နှင့် push လုပ်ပါ
3. Render သည် အလိုအလျှောက် အပ်ဒေတ်လုပ်ပါလိမ့်မည်

```bash
git add .
git commit -m "Update bot features"
git push origin main
```

## ကျေးဇူးတင်ပါတယ်!

သင့်ရဲ့ Telegram AI Bot သည် အခုအခါ Render တွင် အလုပ်လုပ်နေပါလိမ့်မည်။ မည်သည့် အကြံပြုချက် သို့မဟုတ် bug reports ရှိပါက GitHub Issues တွင် ဖန်တီးပါ။
