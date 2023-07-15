# Helmets
Visualizing the price and ratings of bike helmets

# Intro
As a cyclist myself, I found myself looking for an upgrade from the skateboarding helmet I was wearing. Virginia Tech had a website on which they displayed the results of impact tests they performed. 
However, looking at the first few entries, I was startled at the prices. I looked through the data and found an affordable, well-rated helmet but the large price range made me wonder about the spread of price and quality in bike helmets. The original website with the data can be found here: https://www.helmet.beam.vt.edu/bicycle-helmet-ratings.html#!

# Process
I scraped the information using BeautifulSoup and put it into a pandas database, then displayed it using matplotlib.

# Results
The scatterplot shows there is somewhat of a relationship between concussion risk (the lower, the better) and helmet price. We can see that the cheapest helmets are pretty high in concussion risk, but also that the most expensive helmet did not get the best rating. We can also see some vertical lines at common price points of 100, 200, 250 and 300 dollars.

![helmet scatter](https://github.com/djboek42/helmets/assets/78880986/964139de-41d1-4019-863d-e3628db75f82)

In the boxplot, we can see the spread of the helmet prices grouped by rating. This is a rating out of 5 stars, based on the concussion risk previously shown. We see there are no 2-star helmets more expensive than $100. But, a cheaper helmet does not mean it is necessarily a bad helmet. Though the median price of a 5-star helmet is considerably higher than that of the lower-rated helmets, the spread is pretty big so for as little as $50, you can already get a highly rated helmet.

![helmet boxplot](https://github.com/djboek42/helmets/assets/78880986/7a7abd25-4f6d-490d-bdf1-05b93e9cd57a)

# Future considerations
- The tests included road, urban, mountain bike and multisport helmets. Road helmets seem most expensive at first glance, but it would be good to visualize types on the scatter plot (different colors or shapes for different types) to get a clearer view of the spread.
- There is a large spread in 5-star helmet prices. I could further investigate what causes this spread. Helmet weight could be a feature to include since a lighter-weight helmet leads to less neck fatigue on long rides. It would be interesting to see if lower helmet weight correlates with a higher price.
