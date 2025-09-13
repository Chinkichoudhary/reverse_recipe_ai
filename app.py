from flask import Flask, request, jsonify, render_template
from utils.load_data import load_dataset, search_dish

app = Flask(__name__)
df = load_dataset()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_dishes', methods=['POST'])
def get_dishes():
    data = request.get_json()
    selected_cuisines = data.get('cuisine', [])
    selected_courses = data.get('course', [])
    selected_diets = data.get('diet', [])
    selected_times = data.get('prep_time', [])

    dishes = df.to_dict(orient='records')
    results = []

    for dish in dishes:
        if selected_cuisines and dish.get('cuisine', '').lower() not in [c.lower() for c in selected_cuisines]:
            continue
        if selected_courses and dish.get('course', '').lower() not in [c.lower() for c in selected_courses]:
            continue
        if selected_diets and dish.get('diet', '').lower() not in [d.lower() for d in selected_diets]:
            continue
        if selected_times:
            prep = dish.get('prep_time', '').replace(' min', '').replace('M', '').strip()
            if prep and prep.isdigit() and prep not in selected_times:
                continue
        results.append(dish)

    return jsonify(results)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    dish_name = data.get('dish_name', '')
    diet = data.get('diet', '')
    results = search_dish(df, dish_name, diet)
    return jsonify(results)

@app.route('/dish-names', methods=['GET'])
def dish_names():
    names = df['name'].dropna().unique().tolist()
    return jsonify(names)

@app.route('/blogs')
def blogs():
    blog_posts = [
        {
            "title": "How to Balance Spices",
            "summary": "Learn the art of layering flavors without overpowering your dish.",
            "slug": "spice-balancing"
        },
        {
            "title": "Monsoon Meals: Comfort Foods for Rainy Days",
            "summary": "Explore cozy recipes perfect for the rainy season.",
            "slug": "monsoon-meals"
        },
        {
            "title": "Behind the Biryani: A Cultural Journey",
            "summary": "Discover the rich history and regional variations of India's favorite rice dish.",
            "slug": "biryani-story"
        }
    ]
    return render_template('blogs.html', blogs=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit_recipe():
    if request.method == 'POST':
        name = request.form['name']
        diet = request.form['diet']
        course = request.form['course']
        cuisine = request.form['cuisine']
        prep_time = request.form['prep_time']
        description = request.form['description']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        image = request.files['image']
        # Save logic here...
        return "Recipe submitted successfully!"
    return render_template('submit_recipe.html')

@app.route('/blogs/<slug>')
def blog_detail(slug):
    blog_map = {
        "spice-balancing": {
            "title": "How to Balance Spices",
            "content": """
                <h2>Why Spice Balance Matters</h2>
                <p>Spices are the soul of Indian cooking. But too much of one can overpower the dish...</p>
                <h2>Tips for Perfect Balance</h2>
                <ul>
                  <li>Start with whole spices and toast them lightly</li>
                  <li>Use acidic ingredients like lemon or yogurt to mellow heat</li>
                  <li>Balance pungent spices with sweet ones</li>
                </ul>
                <h2>Final Thought</h2>
                <p>Spice balance is an art — and like all art, it improves with practice.</p>
            """
        },
        "monsoon-meals": {
            "title": "Monsoon Meals",
            "content": "<p>Rainy days call for warm, comforting dishes like khichdi, pakoras, and masala chai...</p>"
        },
        "biryani-story": {
            "title": "Behind the Biryani",
            "content": "<p>Biryani is more than a dish — it's a cultural symbol across India...</p>"
        }
    }

    blog = blog_map.get(slug)
    if not blog:
        return "<h1>Blog not found</h1>", 404

    return render_template("blog_detail.html", blog=blog)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
