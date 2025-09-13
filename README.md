# 🍽️ Reverse Recipe AI

A web-based AI application that predicts cuisine type from ingredients and allows users to submit and explore recipes. Built with a full-stack architecture and designed for intuitive user experience.

---

## 📁 Project Structure

REVERSE_RECIPE_AI/ 
├── backend/
│ ├── app.py # Main Flask application 
│ ├── requirements.txt # Python dependencies 
│ ├── README.md # Backend-specific documentation 
│ ├── .gitignore # Git ignore rules 
│ ├── .gitattributes # Git LFS tracking 
│ ├── data/ 
│ │ ├── cuisine_updated.csv.zip # Compressed dataset 
│ │ └── pycache/ # Python cache
│ ├── static/ 
│ │ ├── images/ # UI assets 
│ │ └── style.css # Styling 
│ ├── templates/ 
│ │ ├── index.html # Homepage 
│ │ ├── about.html # About page
│ │ ├── blogs.html # Blog listing 
│ │ ├── blog_detail.html # Blog details 
│ │ └── submit_recipe.html # Recipe submission form 
│ └── utils/ 
│ ├── init.py # Utility package init 
│ ├── load_data.py # Data loading logic 
│ └── pycache/ # Compiled Python files






---

## 🚀 Features

- Predict cuisine type from ingredients using ML
- Submit and browse recipes via a clean UI
- Responsive design with HTML/CSS templates
- Modular backend with organized utilities and data handling

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/Chinickchoudhary/reverse_recipe_ai.git
cd reverse_recipe_ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r backend/requirements.txt

# Run the app
python backend/app.py

## 📦 Dataset Access

Due to GitHub's file size limits, the dataset is hosted externally.

🔗 [Download cuisine_updated.csv.zip]([https://drive.google.com/your-shareable-link](https://drive.google.com/file/d/1Ni5_82YrgQm17viG4OarlKsYZHDHqkN3/view?usp=sharing)

> After downloading, unzip and place it in:
> `backend/data/cuisine_updated.csv.zip`


