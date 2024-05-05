import pandas as pd
from flask import Flask, request,render_template
app=Flask(__name__)
data=pd.read_csv('Cleaned_data.csv')

@app.route('/')
def index():
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

if __name__=="__main__":
    app.run(debug=True,port=5001)