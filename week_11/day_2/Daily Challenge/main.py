from flask import Flask, render_template_string

# https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-to-convert-markdown-text-to-html

import markdown

app = Flask(__name__)


@app.route('/lesson')
def lesson():
    with open('./lesson1/in-this-chapter.md', 'r') as f:
        chapter_text = f.read()
        html = markdown.markdown(chapter_text)
    return html


@app.route('/exercises')
def exercises():
    with open('./lesson1/exercises.md') as f:
        exercises_text = f.read()
        html = markdown.markdown(exercises_text)
    return html


if __name__ == '__main__':
    app.run(debug=True)


