from flask import Flask, request, render_template
import pickle
import sklearn


app = Flask(__name__)
with open('svm_rbf_model.pkl','rb') as f:
    model=pickle.load(f)
    print('\nSVM model load successfully\n')



@app.route("/")
def home():
    print("\nHome page loaded\n")
    return render_template("home.html")



@app.route("/predict", methods = ["GET", "POST"])
def predict():
    
    if request.method == "POST":
        print("\nWater Data successfuly posted\n")    
        ph_value = float(request.form["pvalue"])
        organic = float(request.form["Organic"])
        trihalo_value = float(request.form["tri"])
        turbid_value = float(request.form["turb"])
        solid_value = float(request.form["Solid"])
        chloro_value = float(request.form["choloro"])
        conduct_value = float(request.form["conduct"])
        sulfate_value = float(request.form["sulfate"])
        hardness_value = float(request.form["Hardness"])
        
        print("\nModel prediction started....\n")
        prediction=model.predict([[
            ph_value,
            hardness_value,
            solid_value,
            chloro_value,
            sulfate_value,
            conduct_value,
            organic,
            trihalo_value,
            turbid_value
        ]])
        print("Prediction completed")
        if prediction>0.5:
            print("\nWater is purified\n")
            return render_template('purified.html')
        else:
            print('\nWater is not purified\n')
            return render_template('not_purified.html')
    return render_template("home.html")




if __name__ == "__main__":
    print("\nApplication runinng.....\n")
    app.run(debug=True)
    