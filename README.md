# Simple Flask Landing Page

A clean, modern landing page built with Flask that displays links to your other projects.

## Features

- 🎨 Modern, responsive design
- 🔗 Easy to customize links
- 🚀 Simple Flask backend
- 📱 Mobile-friendly
- ⚡ Fast and lightweight

## Quick Start

1. **Install Flask:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   python3 app.py
   ```

3. **Open your browser:**
   Go to `http://localhost:5001`

## Customization

Edit `app.py` to change the links:

```python
LINKS = [
    {
        'name': 'Your Project Name',
        'url': 'https://yourproject.com',
        'description': 'What this project is about'
    },
    # Add more links...
]
```

## Deployment

This app can be deployed to:
- Heroku
- PythonAnywhere
- DigitalOcean
- Any Python hosting service

Just make sure to install the requirements and run the app!
