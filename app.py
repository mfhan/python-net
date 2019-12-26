from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'MF Han',
        'title': 'Blog Intro',
        'content': 'Let me introduce myself! I am learning Flask',
        'date_posted': 'Dec 22, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Guest Blog Post',
        'content': 'Yo, I am a guest poster',
        'date_posted': 'Dec 26, 2019'
    }
]


@app.route('/')
# def hello():
#     return '<h1>Hello, Blog Readers!</h1>'
@app.route('/home')
def home():
        # initially: return '<h1>Hello, Blog Readers!</h1>'
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    # initially: return '<h1>About this repo</h1>'
    # then: return render_template('about.html')
    return render_template('about.html', title="About this project")


if __name__ == '__main__':
    app.run(debug=True)
