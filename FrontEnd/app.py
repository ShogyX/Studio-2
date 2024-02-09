from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Process the input_text as needed
        return render_template('result.html', input_text=input_text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
