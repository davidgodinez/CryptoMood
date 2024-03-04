# CryptoMood
Using sentiment analysis from Twitter and Reddit to figure out which cryoto currencies to buy. 


### CryptoMood Initial Version Steps

1. **Twitter**
   - [x] Access the Twitter API.
   - [x] Get tweets by filtering with crypto-related hashtags.
   - [x] Handle API rate limits and implement pagination.
   - [x] Preprocess tweets to remove noise (URLs, mentions, etc.).

2. **Reddit**
   - [x] Access the Reddit API.
   - [x] Get posts from crypto-focused subreddits.
   - [ ] Handle API rate limits and implement pagination.
   - [ ] Preprocess posts to improve sentiment analysis accuracy.

3. **Sentiment Analysis**
   - [x] Use the TextBlob sentiment analysis tool.
   - [x] Analyze sentiment of tweets and posts.
   - [ ] Aggregate sentiment scores for each cryptocurrency.

4. **Data Visualization**
   - [x] Create interactive dashboards with Plotly/Dash.
   - [ ] Display sentiment trends over time.
   - [ ] Visualize sentiment distribution among different cryptocurrencies.

5. **Access Binance API**
   - [x] Fetch current prices of top 10 cryptocurrencies identified by sentiment analysis.
   - [ ] Compare sentiment analysis results with historical price data.

### Additional Enhancements

- [ ] Implement robust error handling for API interactions.
- [ ] Consider data privacy and ethical aspects when presenting user-generated content.
- [ ] Plan for scalability and transitioning from a notebook to a more user-friendly application.
- [ ] Explore incorporating additional data sources like news articles in future versions.
- [ ] Investigate custom machine learning models tailored to cryptocurrency discussions.


## Progress as of 3/3/2024

- I was able to get a basic trading bot going in the TradingBot folder. This uses the markers from Binance to determine if a certain crypto is a buy or sell. I was also able to visualize the markers using mpfiance. 