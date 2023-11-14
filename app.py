from flask import Flask, render_template, request, flash
from predict import predict_price

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"




@app.route('/predict-price', methods=['GET', 'POST'])
def basic():
	
	prediction=0
	if request.method == 'POST':
		state = request.form['state']
		nombre_de_chambre = int(request.form['nombre_de_chambre'])
		surface_living = float(request.form['surface_living'])
		if(state is not None and nombre_de_chambre>0 and surface_living>0 ) :
			prediction = predict_price(state, nombre_de_chambre, surface_living)
	
	
	return render_template('index.html', prediction=prediction)
