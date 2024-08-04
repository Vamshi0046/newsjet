from django.shortcuts import render
import datetime
import requests
def news(request):
    if request.method == 'POST':
        Day=datetime.date.today()
        Year = datetime.date.today().year
        # print('year:',Year)
        Today=Day.strftime("%d")
        m=datetime.datetime.now()
        Month=m.strftime("%m")
        n = request.POST.get('news_type')
        url = f"https://newsapi.org/v2/everything?q={n}&from={Year}-{int(Month)-1}-{Today}&sortBy=publishedAt&apiKey=d16f9163c3474ad79ebf3ec9a90d3811"
        r = requests.get(url)
        news = r.json()
        # print("news:-->",news)
        articles = news['articles']
        for article in articles:
            article['image_url'] = article.get('urlToImage', '') 
        return render(request, 'htmlfiles/news.html', {'articles': articles})
    return render(request, 'htmlfiles/news.html')