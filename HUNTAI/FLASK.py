import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__,static_folder = 'C:/Users/akshu/Documents/Aqua Check/HUNTAI/static' ,template_folder='C:/Users/akshu/Documents/Aqua Check/HUNTAI/templates')

with open("AquaCheckModel.pkl",'rb') as f:
    model = pickle.load(f)



def check_water_potability(pH, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes):
    dick = {}
    status = ""
    uses = ""
    pure=""
    listy = ['pH', 'turbidity', 'hardness', 'solids', 'chloramines', 'sulfate', 'conductivity', 'organic_carbon', 'trihalomethanes']
    inputs = np.array([pH, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes])
    inputs=inputs.reshape(1,-1)
    y=model.predict(inputs)
    if (pH <= 7):
        status += "pH is not in the good range.\n"
        dick.update({"pH_low": abs(((pH-7)/7)*100)})
    if (pH >= 7.074755):
        status += "pH is not in the good range.\n"
        dick.update({"pH_high": abs(((pH-7)/7)*100)})
    if turbidity > 3.968328:
        status += "Turbidity is greater than 3.9 NTU.\n"
        dick.update({"turbidity": (((turbidity-5)/5)*100)})
    if hardness > 195.800744:
        status += "Hardness is greater than 195.8 ppm.\n"
        dick.update({"hardness": (((hardness-500)/500)*100)})
    if solids > 22383.991018:
        status += "Solids are greater than 22383.9 ppm.\n"
        dick.update({"solids": (((solids-1000)/1000)*100)})
    if chloramines > 7.169338:
        status += "Chloramines are greater than 7.1 ppm.\n"
        dick.update({"chloramines": (((chloramines-4)/4)*100)})
    if sulfate > 332.844122:
        status += "Sulfate is greater than 332.8 ppm.\n"
        dick.update({"sulfate": (((sulfate-250)/250)*100)})
    if conductivity > 425.383800:
        status += "Conductivity is greater than 425.3 ppm.\n"
        dick.update({"conductivity": (((conductivity-1800)/1800)*100)})
    if organic_carbon > 14.16083:
        status += "Organic carbon is greater than 14.1 ppm.\n"
        dick.update({"organic_carbon": (((organic_carbon-10)/10)*100)})
    if trihalomethanes > 66.533513:
        status += "Trihalomethanes are greater than 66.5 ppm.\n"
        dick.update({"trihalomethanes": (((trihalomethanes-80)/80)*100)})
    else:
        status +=""
        dick.update({"Water is purely Potable.\n\nNo need of doing such practices to make water Potable": 0})
    max_key = max(dick, key=dick.get)

    if max_key == 'pH_low':
        uses += "Adding soda ash or sodium carbonate can help increase the pH.\n\n"
        uses += "Water with high or low pH can be used for non-potable purposes such as irrigation or industrial processes. For example, acidic water can be used to clean metal surfaces."
    if max_key == 'ph_high':
        uses += "Adding hydrochloric acid or sulfuric acid can help reduce the pH.\n\n"
        uses += "Water with high or low pH can be used for non-potable purposes such as irrigation or industrial processes. For example, acidic water can be used to clean metal surfaces."
    if max_key == 'turbidity':
        uses += "Filtration using activated carbon or alum can help remove turbidity.\n\n"
        uses += "Water with high turbidity can be used for non-potable purposes such as construction, dust control, or washing vehicles. It can also be used for industrial processes that do not require clear water."
    if max_key == 'hardness':
        uses += "Adding a water softener, such as sodium chloride or potassium chloride, can help reduce hardness.\n\n"
        uses += "Hard water can be used for non-potable purposes such as irrigation, industrial processes, or cooling systems. It can also be used for household cleaning tasks like washing clothes or dishes."
    if max_key == 'solids':
        uses += "Reverse osmosis, ion exchange, or distillation can help remove solids.\n\n"
        uses += "Water with elevated levels of dissolved solids can be used for non-potable purposes such as irrigation or industrial processes. It can also be used for livestock watering or aquaculture."
    if max_key == 'chloramines':
        uses += "Activated carbon filtration can help remove chloramines.\n\n"
        uses += "Water with high levels of chloramines can be used for non-potable purposes such as industrial cooling, wastewater treatment, or swimming pool water."
    if max_key == 'sulfate':
        uses += "Reverse osmosis or distillation can help remove sulfate.\n\n"
        uses += "Water with elevated sulfate levels can be used for non-potable purposes such as irrigation or livestock watering. It can also be used for industrial processes such as mining or pulp and paper production."
    if max_key == 'conductivity':
        uses += "Reverse osmosis, deionization, or distillation can help reduce conductivity.\n\n"
        uses += "Water with high conductivity can be used for non-potable purposes such as industrial processes or cooling systems. It can also be used for agricultural irrigation in certain crops."
    if max_key == 'organic_carbon':
        uses += "Activated carbon filtration can help remove organic carbon.\n\n"
        uses += "Water with elevated organic carbon levels can be used for non-potable purposes such as irrigation or industrial processes. It can also be used for aquaculture or hydroponic systems."
    if max_key == 'trihalomethanes':
        uses += "Aeration or activated carbon filtration can help remove trihalomethanes.\n\n"
        uses += "Water with high levels of trihalomethanes can be used for non-potable purposes such as industrial cooling or firefighting."
    else :
        max_key == 'Water is purely Potable.\n\nNo need of doing such practices to make water Potable.'
        pure += 'Water is purely Potable.\n\nNo need of doing such practices to make water Potable.'

    if y[0] == 1:
        return "Potable", None, pure
    else:
        return "Not Potable", status, uses




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
    result, status, uses = check_water_potability(pH, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes)
    #print(uses)
    return render_template('water_quality_result.html', result=result, status=status, uses=uses)

    # Calling the  function to check the water quality
    #result = check_water_potability(ph, turbidity, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes)

    # Return the result to the user
    #return render_template('water_quality_result.html', result=result)

if __name__ == '__main__':
    pass
