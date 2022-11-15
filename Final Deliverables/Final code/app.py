from flask import Flask, render_template, request                     
app = Flask(__name__,template_folder="templates")          
                                                          
@app.route("/")
def hello():
    return render_template('index0.html') 

if __name__ == "__main__":
     app.run(debug=True ,port=8080,use_reloader=False) 
@app.route('/register', methods=['POST'])
def register():
   query = request.form.get('query1')
   selected = request.form.get('query')
   if (not query or not selected):
       return 'failure'
   processed_text = query.upper()
   return render_template('sucess.html')