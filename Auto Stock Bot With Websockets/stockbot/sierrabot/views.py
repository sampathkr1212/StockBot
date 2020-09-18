from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "SierraAlgoBot",
        "stocklist": [
            "Q.AAPL",
            "Q.TSLA",
            "Q.MSFT",
            "Q.GOOG",
            "Q.AMZN",
            "Q.INTC",
            "Q.FB",
            "Q.JNJ",
            "Q.JPM",
            "Q.BAC",
            "Q.WMT",
            "AM.AAPL",
        ],
        "stocknames": [
            "AAPL",
            "TSLA",
            "MSFT",
            "GOOG",
            "AMZN",
            "INTC",
            "FB",
            "JNJ",
            "JPM",
            "BAC",
            "WMT",
        ],
    }
    return render(request, "sierrabot/index.html", context)

