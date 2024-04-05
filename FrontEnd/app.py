from flask import Flask, render_template, request, jsonify
#imports functions from the local AnalysisFunctions script
from AnalysisFunctions import RunFullAnalysis

#Initialize the app with Flask
app = Flask(__name__)

#Tell the App where out base HTML is located and run it.
@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('index.html')

#Recieve the password password from the HTML form and pass it back to the Analyze_Password function before returning the results.
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        password = request.form['input_text']
        try:
            analysis_result = RunFullAnalysis(password)
        except:
            analysis_result = {}
        #Returns a json doc with information to the client side
        return jsonify({'result': analysis_result})


#Actually run the app, run with host=0.0.0.0 if you want the app to be visible on local network. 
#this is needed if you want to port forward and allow external access to the site, default port it 5000
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
