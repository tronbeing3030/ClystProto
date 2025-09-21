# 🚀 Clyst Art Marketplace - Free Deployment Guide

This guide provides multiple free deployment options for your Clyst art marketplace application with all features working.

## 🔒 Security Setup (REQUIRED FIRST)

### 1. Environment Variables Setup
Create a `.env` file in your project root (this file is already in .gitignore):

```bash
# .env file
GEMINI_API_KEY=your_actual_gemini_api_key_here
FLASK_SECRET_KEY=your_secure_secret_key_here
FLASK_ENV=production
```

### 2. Generate Secure Secret Key
```python
import secrets
print(secrets.token_hex(32))
```
## 🚀 Quick Start Deployment (Railway)

### 1. Prepare Your Code
```bash
# Make sure your code is on GitHub
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### 2. Deploy on Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select the repository
5. Add environment variables:
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `FLASK_SECRET_KEY`: Your secure secret key
   - `FLASK_ENV`: production
6. Railway will automatically build and deploy

### 3. Access Your App
- Your app will be available at: `https://your-app-name.railway.app`
- All features will work including:
  - ✅ User authentication
  - ✅ AI-powered content generation
  - ✅ File uploads
  - ✅ Natural language search
  - ✅ Multilingual support
