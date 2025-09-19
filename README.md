# Clyst - Art Marketplace & Community Platform

Clyst is a comprehensive web application that serves as both a social platform for artists to share their work and a marketplace for selling artwork. Built with Flask and featuring AI-powered content generation, natural language search, and multilingual support.

## 🌟 Features

### Core Functionality
- **Community Feed**: Artists can share their artwork with the community through posts
- **Marketplace**: Buy and sell artwork with integrated pricing and product management
- **User Authentication**: Secure registration, login, and profile management
- **Image Management**: Support for both URL-based and file upload images
- **Search & Discovery**: Natural language search with price filtering capabilities

### AI-Powered Features
- **Content Generation**: AI-powered title and description suggestions for posts and products
- **Multilingual Support**: Automatic translation of content into multiple languages
- **SEO Optimization**: AI-generated SEO phrases for better discoverability
- **Image Analysis**: AI analyzes uploaded images to generate contextual content

### Advanced Search
- **Natural Language Processing**: Search using phrases like "minimalist monochrome abstracts under ₹5k"
- **Price Filtering**: Support for price ranges, minimum/maximum price constraints
- **Keyword Extraction**: Intelligent keyword parsing from search queries
- **Multi-field Search**: Search across titles, descriptions, and artist names

### User Experience
- **Responsive Design**: Mobile-first design with adaptive layouts
- **Accessibility**: Text-to-speech functionality for content
- **Modern UI**: Clean, Instagram-inspired interface with smooth animations
- **Real-time Features**: Dynamic content updates and interactive elements

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0**: Web framework
- **SQLAlchemy 2.0.38**: ORM for database operations
- **Flask-Login 0.6.3**: User authentication and session management
- **Flask-SQLAlchemy 3.1.1**: Flask integration with SQLAlchemy
- **Werkzeug 3.0.1**: WSGI toolkit with password hashing

### Frontend
- **HTML5/CSS3**: Modern web standards
- **JavaScript (ES6+)**: Interactive functionality
- **Font Awesome 6.0.0**: Icon library
- **Responsive CSS Grid/Flexbox**: Layout system

### AI Integration
- **Google Gemini API**: AI content generation and translation
- **Natural Language Processing**: Custom search query parser
- **Image Analysis**: AI-powered image understanding

### Database
- **SQLite**: Lightweight database for development
- **Database Migrations**: Automatic table creation and management

## 📁 Project Structure

```
ClystProto/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── natural_search.py     # Natural language search parser
├── ai.py                 # AI integration module
├── requirements.txt      # Python dependencies
├── models/
│   └── dbs.py           # Database models (commented out)
├── templates/           # HTML templates
│   ├── index.html       # Community feed
│   ├── products.html    # Marketplace
│   ├── add_posts.html   # Create post form
│   ├── add_products.html # Add product form
│   ├── profile.html     # User profile
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   └── product_buy.html # Product purchase page
├── static/
│   ├── css/
│   │   └── styles.css   # Global styles
│   └── uploads/         # User uploaded files
│       ├── posts/       # Post images
│       └── products/    # Product images
└── instance/
    └── clyst.db        # SQLite database
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ClystProto
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Edit `config.py` to set your API keys:
   ```python
   GEMINI_API_KEY = "your_gemini_api_key_here"
   FLASK_SECRET_KEY = "your_secret_key_here"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 🔧 Configuration

### API Keys Setup
1. **Google Gemini API**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to `config.py`

2. **Flask Secret Key**:
   - Generate a secure secret key for session management
   - Update `FLASK_SECRET_KEY` in `config.py`

### Database Configuration
- The application uses SQLite by default
- Database file is created automatically in the `instance/` directory
- Tables are created on first run

## 📱 Usage Guide

### For Artists

1. **Registration & Profile**
   - Create an account with email, name, phone, and location
   - Access your profile to manage posts and products

2. **Creating Posts**
   - Share artwork with the community
   - Upload images or provide image URLs
   - Use AI to generate engaging titles and descriptions
   - Translate content into multiple languages

3. **Selling Products**
   - Add products to the marketplace
   - Set prices and detailed descriptions
   - Use AI suggestions for better product listings
   - Manage your product inventory

### For Buyers

1. **Browsing & Discovery**
   - Explore the community feed for inspiration
   - Browse the marketplace for products
   - Use natural language search (e.g., "abstract paintings under 5000")

2. **Search Features**
   - Search by keywords, artist names, or descriptions
   - Filter by price ranges
   - Use phrases like "landscape oil painting below 7500"

3. **Product Interaction**
   - View detailed product information
   - Contact artists through their profiles
   - Use text-to-speech for accessibility

## 🔍 Search Capabilities

The application features an advanced natural language search system that understands:

### Price Queries
- `"under ₹5k"` - Maximum price filter
- `"above 2000"` - Minimum price filter
- `"between 1000 and 5000"` - Price range filter
- `"rs 1200"` - Exact price search

### Style & Content Queries
- `"minimalist monochrome abstracts"` - Style-based search
- `"blue portrait"` - Color and subject search
- `"landscape oil painting"` - Medium and subject search

### Combined Queries
- `"minimalist monochrome abstracts under ₹5k"` - Style + price
- `"blue portrait < 2000"` - Color + subject + price

## 🤖 AI Features

### Content Generation
- **Title Suggestions**: AI generates engaging titles based on artwork
- **Description Writing**: Contextual descriptions highlighting artistic elements
- **Style Adaptation**: Different suggestions for posts vs. products

### Translation Support
- **Multi-language**: Support for 15+ languages including Indian languages
- **SEO Optimization**: Translated content includes SEO phrases
- **Cultural Adaptation**: Translations consider cultural context

### Supported Languages
- English, Hindi, Bengali, Tamil, Telugu, Marathi
- Gujarati, Kannada, Malayalam, Punjabi, Urdu
- Spanish, French, German, Chinese, Japanese

## 🎨 User Interface

### Design Philosophy
- **Clean & Modern**: Instagram-inspired interface
- **Mobile-First**: Responsive design for all devices
- **Accessibility**: Text-to-speech and keyboard navigation
- **Performance**: Optimized loading and smooth animations

### Key UI Components
- **Navigation**: Sticky header with search functionality
- **Cards**: Consistent card-based layout for posts and products
- **Forms**: Intuitive forms with real-time validation
- **Modals**: Smooth overlay interactions
- **Grid Layouts**: Responsive grid systems

## 🔒 Security Features

- **Password Hashing**: Secure password storage using Werkzeug
- **Session Management**: Flask-Login for secure sessions
- **File Upload Security**: Secure filename handling and type validation
- **Input Validation**: Server-side validation for all inputs
- **CSRF Protection**: Built-in CSRF protection with Flask

## 📊 Database Schema

### Users Table
- `id`: Primary key
- `name`: User's display name
- `email`: Unique email address
- `password_hash`: Hashed password
- `phone`: Contact number
- `location`: User's location
- `created_at`: Account creation date

### Posts Table
- `post_id`: Primary key
- `artist_id`: Foreign key to users
- `post_title`: Post title
- `description`: Post description
- `media_url`: Image URL or path
- `created_at`: Post creation date

### Products Table
- `product_id`: Primary key
- `artist_id`: Foreign key to users
- `title`: Product name
- `description`: Product description
- `price`: Product price (decimal)
- `img_url`: Product image URL or path
- `created_at`: Product creation date

## 🚀 Deployment

### Production Considerations
1. **Environment Variables**: Use environment variables for sensitive data
2. **Database**: Consider PostgreSQL for production
3. **File Storage**: Use cloud storage for uploaded files
4. **HTTPS**: Enable SSL/TLS for secure communication
5. **Caching**: Implement Redis for session storage
6. **Load Balancing**: Use Gunicorn or similar WSGI server

### Environment Setup
```bash
export FLASK_ENV=production
export GEMINI_API_KEY=your_production_key
export FLASK_SECRET_KEY=your_production_secret
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Review the code comments for implementation details

## 🔮 Future Enhancements

- **Payment Integration**: Stripe/PayPal integration for transactions
- **Advanced AI**: More sophisticated content generation
- **Social Features**: Comments, likes, and following system
- **Mobile App**: Native mobile application


---

**Clyst** - Where Art Meets Community and Commerce
