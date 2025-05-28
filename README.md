# Telegram Dual Bot System

## 💡 Description
This project includes two Telegram bots:
- **User Bot**: For registration, profile, channel verification, and showing servers.
- **Admin Bot**: For activating users via `/activate user_id`.

## ⚙️ Setup Instructions

### 1. Add your secrets
Go to your GitHub repo → Settings → Secrets and Variables → Actions, and add:

- `BOT1_TOKEN`
- `BOT2_TOKEN`
- `CHANNEL_USERNAME`
- `ADMIN_ID`

### 2. Deploy to GitHub
Push this code to a new GitHub repo.

### 3. Automatic Execution
Bots will run every 4 hours, or you can trigger manually via GitHub Actions.

— Yassine MDV. Dev