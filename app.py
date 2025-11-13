from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Sample links - you can customize these
LINKS = [
    {
        'name': 'My Portfolio',
        'url': 'https://yourportfolio.com',
        'description': 'Check out my work and projects'
    },
    {
        'name': 'GitHub',
        'url': 'https://github.com/Nicklugo',
        'description': 'View my code repositories'
    },
    {
        'name': 'LinkedIn',
        'url': 'https://linkedin.com/in/yourprofile',
        'description': 'Connect with me professionally'
    },
    {
        'name': 'Substack',
        'url': 'https://humaneexperience.substack.com/',
        'description': 'Read my latest thoughts'
    },
    {
        'name': 'Contact',
        'url': 'mailto:your@email.com',
        'description': 'Get in touch with me'
    }
]

@app.route('/')
def home():
    return render_template('index.html', links=LINKS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
