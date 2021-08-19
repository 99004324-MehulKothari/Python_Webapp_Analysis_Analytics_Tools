"""
This program is to develop a simple web application
"""
from logging import debug
from flask import Flask, app,redirect,url_for,render_template,request
import pyodbc
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pygal
from pygal.style import Style

SERVER = 'sql-car.database.windows.net'
DATABASE = 'car_details'
USERNAME = 'azure-car'
PASSWORD = '{India#123}'
DRIVER= '{ODBC Driver 17 for SQL Server}'
app=Flask(__name__)
ANALYSIS_DROP1=0
ANALYSIS_DROP2=0
ANALYTICS_DROP=0
ANALYTICS_YEAR=0



@app.route('/',methods=['GET', 'POST'])
def index():
    """
    This function is used to create the index page of our app with 2 buttons analysis and analytics
    """
    if request.method == 'POST':
        if request.form['action1'] == 'Analysis':
            return redirect(url_for('analysis'))
        else:
            return redirect(url_for('analytics'))
    return render_template('index.html')

@app.route('/analysis',methods=['GET', 'POST'])
def analysis():
    """
    This function is used to create an analysis page with
    3 buttons ,2 for selecting the company and a submit button
    """
    if request.method == 'POST':
        if request.form['action4'] == 'Submit' and \
        request.form['action2'] != "Choose..." and \
        request.form['action3'] != "Choose...":
            global ANALYSIS_DROP1,ANALYSIS_DROP2
            ANALYSIS_DROP1=request.form['action2']
            ANALYSIS_DROP2=request.form['action3']
            return redirect(url_for('analysis_results'))
        else:
            pass # unknown
    return render_template('analysis.html')

@app.route('/analytics',methods=['GET', 'POST'])
def analytics():
    """
    This function is used to create an analysis page with 3 buttons
    - selecting the company,enter a year and a submit button
    """
    if request.method == 'POST':
        if request.form['action7'] == 'Submit' and \
            request.form['action5'] != "Choose..." and \
            request.form['action6'] !=None and \
            request.form['action6'].isdigit() and \
            int(request.form['action6'])>=2000 and \
            int(request.form['action6'])<=2100 :
            global ANALYTICS_DROP,ANALYTICS_YEAR
            ANALYTICS_DROP= request.form['action5']
            ANALYTICS_YEAR=request.form['action6']
            return redirect(url_for('analytics_results'))
    elif request.method == 'GET':
        return render_template('analytics.html')
    return render_template('analytics.html')

@app.route('/analysis_results')
def analysis_results():
    """
    This function is used to provide the results for
    analysis between 2 companies in the form of a graph
    """
    with pyodbc.connect('DRIVER='+DRIVER+
        ';SERVER=tcp:'+SERVER+';PORT=1433;DATABASE='+DATABASE+
        ';UID='+USERNAME+';PWD='+ PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from "+ANALYSIS_DROP1+" ORDER BY year")
            row = cursor.fetchone()
            year_row=[]
            car_mauf_row=[]
            while row:
                year_row.append((row[0]))
                car_mauf_row.append((row[2]))
                row = cursor.fetchone()
            data={"Year":year_row,"Cars_Manufactured "+ANALYSIS_DROP1+" (in millions)":car_mauf_row}
            df=pd.DataFrame(data)
    with pyodbc.connect('DRIVER='+DRIVER+';SERVER=tcp:'+SERVER+
            ';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from "+ANALYSIS_DROP2+" ORDER BY year")
            row = cursor.fetchone()
            year_row=[]
            car_mauf_row=[]
            while row:
                year_row.append((row[0]))
                car_mauf_row.append((row[2]))
                row = cursor.fetchone()
            data1={"Year":year_row,"Cars_Manufactured "+ANALYSIS_DROP2+
            " (in millions)":car_mauf_row}
            df1=pd.DataFrame(data1)
    df['Cars_Manufactured '+ANALYSIS_DROP2+' (in millions)']= \
    df1['Cars_Manufactured '+ANALYSIS_DROP2+' (in millions)']
    custom_style = Style(
        background='#FFE5B4',
    )
    line_chart = pygal.Line(x_title="Year",y_title="Cars_Manufactured(in millions)" \
        ,legend_at_bottom=True,style=custom_style)
    line_chart.title =str(ANALYSIS_DROP1).capitalize() +' Vs '+str(ANALYSIS_DROP2).capitalize()
    line_chart.x_labels = df['Year']
    for x in df.columns[1:3]:
        line_chart.add(x,df[x].values)
    return line_chart.render_response()

@app.route('/analytics_results',methods=['GET', 'POST'])
def analytics_results():
    """
    This function is used to provide analytics results based on the company and the year provided
    """
    with pyodbc.connect('DRIVER='+DRIVER+';SERVER=tcp:'+SERVER+
        ';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from "+ANALYTICS_DROP+" ORDER BY year")
            row = cursor.fetchone()
            year_row=[]
            car_mauf_row=[]
            while row:
                year_row.append((row[0]))
                car_mauf_row.append((row[2]))
                row = cursor.fetchone()
            data={"Year":year_row,"Cars_Manufactured "+ANALYTICS_DROP+" (in millions)":car_mauf_row}
            df_val=pd.DataFrame(data)
            x_val=df_val.iloc[:,:1].values
            y_val=df_val.iloc[:,-1].values
            x_train, x_test, y_train, y_test = \
                train_test_split(x_val,y_val, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(x_train, y_train)
            x_test=y_test+0+x_test
            predicted_val=str(round((float(regressor.predict([[ANALYTICS_YEAR]]))),2))
            return render_template('final_result.html' \
                ,first_header=predicted_val,p1=ANALYTICS_DROP,p2=ANALYTICS_YEAR)
if __name__ == '__main__':
    app.run(debug=True)
