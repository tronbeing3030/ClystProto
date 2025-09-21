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

## 🌐 Free Deployment Options

### Option 1: Railway (Recommended - Easiest)

**Why Railway?**
- ✅ Free tier: $5 credit monthly (enough for small apps)
- ✅ Automatic deployments from GitHub
- ✅ Built-in database support
- ✅ File storage included
- ✅ Custom domains
- ✅ Environment variables support

**Steps:**
1. Push your code to GitHub
2. Go to [Railway.app](https://railway.app)
3. Sign up with GitHub
4. Click "New Project" → "Deploy from GitHub repo"
5. Select your Clyst repository
6. Add environment variables in Railway dashboard:
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `FLASK_SECRET_KEY`: Your secure secret key
   - `FLASK_ENV`: production
7. Railway will automatically deploy your app

**Railway Configuration:**
- Your app will be available at: `https://your-app-name.railway.app`
- Database: SQLite (included)
- File storage: Local filesystem (included)

### Option 2: Render (Free Tier)

**Why Render?**
- ✅ Free tier: 750 hours/month
- ✅ Automatic deployments
- ✅ PostgreSQL database (free tier)
- ✅ File storage via external service
- ✅ Custom domains

**Steps:**
1. Push code to GitHub
2. Go to [Render.com](https://render.com)
3. Sign up and connect GitHub
4. Create "New Web Service"
5. Connect your repository
6. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3
7. Add environment variables in Render dashboard
8. Deploy

**Note**: For file storage on Render, you'll need to use external storage (see File Storage section below).

### Option 3: Heroku (Free Alternative - Fly.io)

**Why Fly.io?**
- ✅ Free tier: 3 shared-cpu VMs
- ✅ Global deployment
- ✅ Built-in database
- ✅ File storage support
- ✅ Custom domains

**Steps:**
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `fly auth login`
3. Initialize: `fly launch`
4. Deploy: `fly deploy`
5. Set secrets: `fly secrets set GEMINI_API_KEY=your_key FLASK_SECRET_KEY=your_secret`

### Option 4: PythonAnywhere (Beginner Friendly)

**Why PythonAnywhere?**
- ✅ Free tier: 1 web app
- ✅ Easy setup
- ✅ Built-in file storage
- ✅ SQLite support
- ✅ Custom domains (paid)

**Steps:**
1. Sign up at [PythonAnywhere.com](https://pythonanywhere.com)
2. Upload your code via Git or file upload
3. Create a new web app
4. Configure WSGI file
5. Set environment variables in web app settings
6. Reload your web app

## 🗄️ Database Configuration

### For Production (Recommended)
Update your `app.py` to use environment-based database configuration:

```python
# Add this to app.py after line 53
import os

# Database configuration
if os.getenv('FLASK_ENV') == 'production':
    # Use PostgreSQL for production (Railway, Render)
    DATABASE_URL = os.getenv('DATABASE_URL')
    if DATABASE_URL:
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace('postgres://', 'postgresql://')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clyst.db'
else:
    # Use SQLite for development
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clyst.db'
```

## 📁 File Storage Solutions

### Option 1: Cloudinary (Free Tier)
- ✅ 25GB storage
- ✅ Image transformations
- ✅ CDN included
- ✅ Easy integration

**Setup:**
1. Sign up at [Cloudinary.com](https://cloudinary.com)
2. Get your cloud name, API key, and API secret
3. Install: `pip install cloudinary`
4. Add to your `.env`:
```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### Option 2: AWS S3 (Free Tier)
- ✅ 5GB storage
- ✅ 20,000 GET requests
- ✅ 2,000 PUT requests

### Option 3: Local Storage (Railway/PythonAnywhere)
- ✅ No additional setup
- ✅ Files stored on server
- ⚠️ Files lost on redeployment

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
4. Select your Clyst repository
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

## 🔧 Production Optimizations

### 1. Update app.py for Production
Add this to the end of your `app.py`:

```python
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run the app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### 2. Add Production Requirements
Update your `requirements.txt`:
```
gunicorn>=21.2.0
```

### 3. Create Procfile (for Heroku-style platforms)
Create a `Procfile`:
```
web: gunicorn app:app
```

## 🎯 Recommended Deployment Stack

**For Best Free Experience:**
1. **Hosting**: Railway (easiest setup)
2. **Database**: SQLite (included) or PostgreSQL (Railway free tier)
3. **File Storage**: Cloudinary (free tier)
4. **Domain**: Railway subdomain (free) or custom domain

## 🆘 Troubleshooting

### Common Issues:

1. **App won't start**: Check environment variables are set
2. **Database errors**: Ensure database tables are created
3. **File upload issues**: Check file storage configuration
4. **AI features not working**: Verify GEMINI_API_KEY is set

### Debug Commands:
```bash
# Check if app runs locally
python app.py

# Test environment variables
python -c "import os; print(os.getenv('GEMINI_API_KEY'))"
```

## 📞 Support

If you encounter issues:
1. Check the platform's documentation
2. Verify all environment variables are set
3. Check the deployment logs
4. Test locally first

---

**Your Clyst art marketplace will be live and fully functional with all AI features working!** 🎨✨
