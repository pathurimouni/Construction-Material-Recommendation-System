# Construction-Material-Recommendation-System
🔹 STEP 1: Install Python (if not already installed)
Download Python from: https://www.python.org/downloads/

During installation, check the box "Add Python to PATH"

🔹 STEP 2: Download the Project
👉 Option A: Clone via Git
Open Command Prompt and run:
git clone https://github.com/Arunrajmuthkapally/ConstructionMaterialRecommendationSystem.Github.io.git

👉 Option B: Download as ZIP
Go to the GitHub repo
Click on Code → Download ZIP
Extract it to a folder

🔹 STEP 3: Open the Project Folder
Navigate to the project folder using Command Prompt or Terminal:
cd path\to\ConstructionMaterialRecommendationSystem.Github.io
(Replace path\to\ with the actual location of your folder)

🔹 STEP 4: Install Required Libraries
Run this in Command Prompt (inside the project folder):
pip install pandas scikit-learn
These are the ML libraries used in the project.

🔹 STEP 5: Train the Model (if needed)
If the file material_model.pkl doesn't exist, run:
python train_recommendation_model.py
✅ This will create a trained model based on the dataset material_recommendation_dataset.csv.

🔹 STEP 6: Run the Recommendation System
Now run the main app script:
python recommendation_app.py

 🔹 STEP 7:If streamlit is not installed:
Install it using pip:
pip install streamlit
Then run again:
streamlit run recommendation_app.py

✅ This will ask for inputs like:

Project type

Material type

Quality level

Then it will recommend a construction material based on your input.
