# NAND Prediction Flask App

## 📌 Overview
This is a simple web application built using Flask that demonstrates a trained **neural network model** to predict the output of a **NAND gate** based on user input. The model has been trained using TensorFlow/Keras and requires scaled inputs for accurate predictions.

The application consists of:
- A **Flask web server** to handle user input and predictions.
- A **pre-trained Keras model (`nand.keras`)** to make predictions.
- A **scaler (`scaler.pkl`)** used to normalize inputs.
- A **HTML frontend (`index.html`)** to interact with the user.

---

## ⚙️ How It Works
1. The user enters two numerical inputs (representing the NAND gate inputs: 0 or 1).
2. The inputs are preprocessed and scaled using the saved `scaler.pkl`.
3. The scaled values are fed into the pre-trained **NAND neural network model**.
4. The model returns a prediction (either **0** or **1**), which is displayed to the user.

---

## 🚀 Installation & Setup
### **Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **pip**
- **Flask**
- **TensorFlow/Keras**
- **NumPy**
- **Pickle**

### **Steps to Set Up**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/nand-flask-app.git
   cd nand-flask-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open a browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## 🎯 Usage
- Open the web application.
- Enter two numerical inputs (0 or 1) in the provided form.
- Click **Predict** to get the NAND output.
- The result will be displayed on the webpage.

---

## 📁 File Structure
```
/project-folder
│── app.py           # Main Flask application
│── nand.keras       # Pre-trained Keras model
│── scaler.pkl       # Pre-trained scaler for input normalization
│── templates/
│   └── index.html   # Web interface for user input
│── static/          # (If needed for CSS, JS, images)
│── requirements.txt # List of dependencies
```

---

## 🛠️ Technologies Used
- **Flask** (Python web framework)
- **TensorFlow/Keras** (Machine Learning Model)
- **NumPy** (Numerical operations)
- **Pickle** (For saving and loading the scaler)
- **HTML + Jinja2** (For web rendering)

---

## ❌ Troubleshooting
- **TemplateNotFound: index.html**
  - Ensure `index.html` is inside the `templates/` folder.
- **ModuleNotFoundError: No module named 'flask'**
  - Run `pip install flask` to install Flask.
- **Model or Scaler Not Found Error**
  - Ensure `nand.keras` and `scaler.pkl` exist in the project directory.

---

## 👥 Contributors
- **Your Name** - Developer
- Contributions are welcome! Feel free to fork and submit pull requests.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

Any questions? ask asgervb@gmail.com

Happy Coding! 🚀

