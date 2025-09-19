import os
import json
from typing import List, Dict, Any

def generate_portfolio_narrative(artist_name: str, posts: List[Dict], products: List[Dict]) -> str:
    """
    Generate a basic portfolio narrative as fallback.
    """
    if not posts and not products:
        return f"Welcome to {artist_name}'s creative space. This collection is just beginning to take shape."
    
    total_works = len(posts) + len(products)
    posts_count = len(posts)
    products_count = len(products)
    
    return f"Welcome to {artist_name}'s artistic journey, a collection that weaves together {total_works} unique pieces into a compelling narrative of creativity and expression. This collection includes {posts_count} community-shared works that showcase the artist's creative process, alongside {products_count} carefully crafted pieces available for acquisition. Together, these works form a cohesive narrative that invites viewers to explore {artist_name}'s unique perspective and artistic voice."


def generate_enhanced_portfolio_narrative(artist_name: str, posts: List[Dict], products: List[Dict], user_location: str = None) -> str:
    """
    Generate an AI-powered portfolio narrative using Google Gemini API.
    Analyzes all artwork and creates a compelling story connecting the works.
    """
    
    if not posts and not products:
        return f"Welcome to {artist_name}'s creative space. This collection is just beginning to take shape."
    
    try:
        # Import Gemini here to avoid import errors if not available
        import google.generativeai as genai
        from config import GEMINI_API_KEY
        
        # Check if Gemini is available and configured
        api_key = GEMINI_API_KEY
        if not genai or not api_key or api_key == "your_gemini_api_key_here":
            return generate_portfolio_narrative(artist_name, posts, products)
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            generation_config={
                'temperature': 0.7,
                'top_p': 0.9,
                'max_output_tokens': 500,
            }
        )
        
        # Prepare comprehensive data for AI analysis
        all_works = []
        
        # Process posts
        for post in posts:
            work_data = {
                'type': 'community_post',
                'title': post.get('post_title', ''),
                'description': post.get('post_description', ''),
                'created_at': post.get('created_at', ''),
                'media_url': post.get('media_url', '')
            }
            all_works.append(work_data)
        
        # Process products
        for product in products:
            work_data = {
                'type': 'marketplace_product',
                'title': product.get('title', ''),
                'description': product.get('description', ''),
                'price': product.get('price', ''),
                'created_at': product.get('created_at', ''),
                'img_url': product.get('img_url', '')
            }
            all_works.append(work_data)
        
        # Create AI prompt
        location_context = f" from {user_location}" if user_location else ""
        works_summary = f"Total works: {len(all_works)} (Posts: {len(posts)}, Products: {len(products)})"
        
        prompt = f"""
You are an expert art curator and storyteller. Analyze this artist's portfolio and create a compelling "About This Collection" narrative that connects their works into a cohesive artistic story.

ARTIST: {artist_name}{location_context}
{works_summary}

ARTWORKS TO ANALYZE:
{json.dumps(all_works, indent=2)}

Create a narrative that:
1. Welcomes visitors to the artist's creative journey
2. Identifies key themes, styles, and artistic evolution
3. Connects the works into a meaningful story
4. Highlights the balance between community posts and marketplace products
5. Invites viewers to explore the collection
6. Uses engaging, professional language suitable for an art marketplace
7. Keeps it concise but compelling (2-3 paragraphs max)

Focus on the artistic themes, creative evolution, and the story these works tell together. Make it feel personal and inspiring.
"""
        
        # Generate AI response
        response = model.generate_content(prompt)
        narrative = response.text.strip()
        
        # Fallback if AI response is empty or too short
        if not narrative or len(narrative) < 50:
            return generate_portfolio_narrative(artist_name, posts, products)
        
        return narrative
        
    except Exception as e:
        # If AI fails, return basic narrative
        print(f"AI portfolio narrative generation failed: {e}")
        return generate_portfolio_narrative(artist_name, posts, products)

