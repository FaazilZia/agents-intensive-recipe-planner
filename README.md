# agents-intensive-recipe-planner
Agents-Intensive Recipe Planner uses multiple AI agents to generate smart, personalized meal plans. It suggests recipes, optimizes ingredients, handles dietary preferences, and creates step-by-step cooking workflows—making meal planning faster, smarter, and fully automated

🚀 Table of Contents

Project Overview

Features

How It Works

Getting Started

Project Structure

Tech Stack

Contributing

License

📖 Project Overview
Manual meal planning and shopping list creation can be a headache. This project automates those steps in a simple, user-friendly way. Enter your meal request, and the agent:

Plans your dinners

Researches recipes

Outputs a clean, categorized shopping list

Lets you manage everything through a simple web page
It's perfect for busy students, home cooks, and anyone wanting to save time and eat better.

✨ Features
Multi-Agent System: Orchestrates Planner, Researcher, and Formatter agents for a seamless workflow.

Automated Recipe & List Generation: Generates search queries, fetches results, and builds your shopping list for you.

Beginner-Friendly Frontend: Copy-paste code for a neat HTML/CSS interface. Just run it in your browser; no coding skills needed!

AI-Ready: Easy to upgrade with Gemini or Google Search API for smarter suggestions or dynamic data.

Fully Self-Contained: No external servers or cloud required for the demo version.


⚙️ How It Works
Enter Prompt: (e.g., “Plan 3 healthy chicken dinners for two people.”)

Planner Agent splits your request into recipe searches.

Researcher Agent fetches dummy recipe ingredients (or connects to Google Search API for actual recipes).

Formatter Agent organizes results into a neat, readable shopping list grouped by category (Produce, Dairy, etc).

See Results: All in your browser — easy copy/paste!

🏁 Getting Started
Quickstart
Clone Repository in Codespaces:

Click Code → Create Codespace on main in GitHub (or clone locally: git clone https://github.com/FaazilZia/agents-intensive-recipe-planner)

Create All Project Files (copy & paste in terminal):

bash
mkdir agents tools
touch main.py requirements.txt .env README.md index.html style.css
touch agents/planner.py agents/researcher.py agents/formatter.py

Paste Provided Code into each file (see /agents and /main.py in this repo).

View Your Frontend:

bash
python3 -m http.server 8000
Open the "Ports" tab and click to view the website on Port 8000.

Run Backend (Terminal):

bash
python main.py
This shows your list in the terminal for now.

Try Out Different Prompts:

Enter meal planning requests in the web interface. (By default this uses sample data—upgrade to connect a real AI/recipe API!)

📁 Project Structure
text
/agents-intensive-recipe-planner
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   └── formatter.py
├── main.py
├── requirements.txt
├── .env
├── README.md
├── index.html
├── style.css
└── tools/
🛠️ Tech Stack
Python 3 (backend logic & agent system)

HTML + CSS + JavaScript (frontend, runs in any browser)

(Optional for bonus) Google Search API, Gemini API, Flask (see advanced guide)

💡 Example Prompts
"Plan 3 Indian vegetarian dinners for my family."

"Make a week of protein-rich lunches for two."

"Find quick, low-calorie recipes with chicken and spinach."

🤝 Contributing
Open to contributions! For bugs or ideas, open issues or submit pull requests.

📄 License
MIT License. Reuse and remix as you like.




