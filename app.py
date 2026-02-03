from flask import Flask, render_template
import worldnewsapi
from worldnewsapi.rest import ApiException

app = Flask(__name__, template_folder='.')

configuration = worldnewsapi.Configuration(
    api_key={'apiKey': "708c8d9b4764432aa992e37c58ed32ae"}
)

client = worldnewsapi.ApiClient(configuration)
api = worldnewsapi.NewsApi(client)

@app.route("/")
def home():
    try:
        response = api.search_news(
            text="technology",
            language="en",
            number=10
        )

        articles = response.news

    except ApiException as e:
        articles = []
        print("API error:", e)

    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
