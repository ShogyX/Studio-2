from flask import Flask, render_template, request, jsonify
#imports functions from the local AnalysisFunctions script
from AnalysisFunctions import search_special_int_caps

#Initialize the app with Flask
app = Flask(__name__)

#Tell the App where out base HTML is located and run it.
@app.route('/')
def index():
    return render_template('index.html')


#This function accepts the password and calls all our analysis function to evaluate the password.
def analyze_password(password):

    #Simple String Manipulation/reading to provide som filler output
    extra_variables = {
        'Length': len(password),
        'First Character': password[0] if password else '',
        'Second Character': password[1] if len(password) > 1 else '',
        'Last Character': password[-1] if password else ''
        }
    
    #This unpacks all dicts and combines them into one big dict to be passed to the client side.
    analysis_results = {**extra_variables, **search_special_int_caps(password)}

    #This return will be passed to the Analyze() function and fruther to the client side.
    return analysis_results


#Recieve the password password from the HTML form and pass it back to the Analyze_Password function before returning the results.
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        password = request.form['input_text']
        analysis_result = analyze_password(password)
        #Returns a json doc with information to the client side
        return jsonify({'result': analysis_result})




#Actually run the app, run with host=0.0.0.0 if you want the app to be visible on local network. 
#(this is needed if you want to port forward and allow external access to the site), default port it 5000
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True. host="0.0.0.0")