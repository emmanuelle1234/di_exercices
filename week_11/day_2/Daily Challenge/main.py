from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/lesson')
def lesson():
    template = '''
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Lesson 1</title>
    </head>
    <body>
        {{markdown}}
    </body>
    </html>
        '''
    with open('./lesson1/in-this-chapter.md') as f:
        chapter_text = f.read()
    html = render_template_string(template, markdown=chapter_text)
    return html


@app.route('/exercises')
def exercises():
    template = '''
       <html>
       <head>
           <meta charset="UTF-8">
           <title>Exercises</title>
       </head>
       <body>
           {{markdown}}
       </body>
       </html>
           '''
    with open('./lesson1/exercises.md') as f:
        exercises_text = f.read()
    html = render_template_string(template, markdown=exercises_text)
    return html


if __name__ == '__main__':
    app.run(debug=True)


