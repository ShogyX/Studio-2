from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        input_text = request.form['input_text']
        analysis_result = analyze_text(input_text)
        #Returns a json doc with information to the client side
        return jsonify({'result': analysis_result})

def search_special_int_caps(text):
    results = {
        "special_characters": 0,
        "integers": 0,
        "capitalized_letters": 0
    }
    
    special_characters = re.findall(r'[^a-zA-Z0-9\s]', text)
    integers = re.findall(r'\d', text)
    capitalized_letters = re.findall(r'[A-Z]', text)
    
    if special_characters:
        results["special_characters"] = special_characters
    if integers:
        results["integers"] = integers
    if capitalized_letters:
        results["capitalized_letters"] = capitalized_letters
    
    return results



def analyze_text(text):
    #not integrated yet
    special_char = search_special_int_caps(text)



    return {'Length': len(text), 'First Character': text[0] if text else ''}

if __name__ == '__main__':
    app.run(debug=True)

