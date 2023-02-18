from flask import Flask, render_template, request

app = Flask(__name__, template_folder='C:/Users/KABIR YADAV/Desktop/VSCODE_PROGRAMS/HUNTAI/templates')

def check_water_potability(pH, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes):
    status = ""
    if not (6.5 <= pH <= 8.5):
        status += "pH is not in the range of 6.5 to 8.5. "
    if turbidity > 5:
        status += "Turbidity is greater than 5 NTU. "
    if hardness > 500:
        status += "Hardness is greater than 500 ppm. "
    if solids > 1000:
        status += "Solids are greater than 1000 ppm. "
    if chloramines > 4:
        status += "Chloramines are greater than 4 ppm. "
    if sulfate > 250:
        status += "Sulfate is greater than 250 ppm. "
    if conductivity > 800:
        status += "Conductivity is greater than 800 ppm. "
    if organic_carbon > 10:
        status += "Organic carbon is greater than 10 ppm. "
    if trihalomethanes > 80:
        status += "Trihalomethanes are greater than 80 ppm. "
    if status == "":
        return "Potable", None
    else:
        return "Not Potable", status




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/water_quality')
def water_quality_form():
    return render_template('water_quality_form.html')

@app.route('/check_water_quality', methods=['POST'])

def check_water_quality():
    pH = float(request.form['ph'])
    turbidity = float(request.form['turbidity'])
    hardness = float(request.form['Hardness'])
    solids = float(request.form['Solids'])
    chloramines = float(request.form['Chloramines'])
    sulfate = float(request.form['Sulfate'])
    conductivity = float(request.form['Conductivity'])
    organic_carbon = float(request.form['organic carbon'])
    trihalomethanes = float(request.form['Trihalomethanes'])
    result, status = check_water_potability(pH, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes)
    return render_template('water_quality_result.html', result=result, status=status)

    # Calling the  function to check the water quality
    #result = check_water_potability(ph, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes)

    # Return the result to the user
    #return render_template('water_quality_result.html', result=result)

