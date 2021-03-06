# RuPaul's Data Race: Rupository
A series of analyses on data from the best reality competition on television, RuPaul's Drag Race

I've recently added a dataset taken from wikipedia and converted to CSV format. The dataset contains the "results" for each queen in each episode, but currently does not include queens' names. More datasets will come in the future. If you'd like a dataset with the names, or minor changes, let me know, and I'm happy to provide.

For now, this repository will include updated statistics as I calculate them, but in the future, it will include more datasets for others to use and enjoy, along with a nicer website to display my findings. I hope you'll shante and stay to learn more!

*Note: This data does not include data from All Stars Seasons due to differences in judging*

*Additional Note: I am in no way affiliated with RuPaul's Drag Race, or World of Wonder. I'm merely a fan who loves math, data, and drag.*


Some updates on what I've learned so far: 
=================

How one episode affects the results of the next:
-------
![alt text](https://raw.githubusercontent.com/rupaulsdatarace/rupository/master/alluvialforrpdrresults.png)

Here's a nifty alluvial graph I made with rawgraphs.io to represent the relationship between one episode and the next episode's results. On the left-hand side of the graph is the result from the first episode, and on the right is the result from the second episode. As an example, you can see that a large percentage of queens who are high in the 2nd episode were safe in the previous episode. If you're like me and you like numbers, see the chart below, and following discussion.

|      | WIN   | HIGH | SAFE | LOW   | BTM2  | ELIM  |
|------|-------|------|------|-------|-------|-------|
|**WIN**  | 6.5%  | 25%  | 40%  | 11%   | 10%   | 6.5%  |
|**HIGH**| 15%   | 26%  | 28%  | 11%   | 14%   | 6.5%  |
|**SAFE**| 13%   | 21%  | 31%  | 11.5% | 12%   | 11%   |
|**LOW**| 12.5% | 26%  | 25%  | 9%    | 14.5% | 13.5% |
|**BTM2**| 17%   | 12%  | 23%  | 8%    | 12%   | 27%   |

Above is a table displaying the percentage of queens who had a result in an episode (vertical axis), and then had another result in the following episode (horizontal axis). So, as an example, 13% of queens who were safe in one episode went on to win the next episode. 
Some highlights from this table:
  + The percentage of queens who won two episodes in a row is significantly less than the percentage of queens who won an episode after any other result. And in fact, it appears that queens are just as likely to be eliminated the next episode as they are to win.
  + The percentage of queens who won an episode immediately after being in the bottom 2 is higher than the percentage for any other group on the table. That said, the same could be said for being eliminated immediately after being in the bottom 2. 
  + The percentage of queens who are low in one episode and go on to be high the next episode is the same as the percentage of queens who are high two episodes in a row.
  + The percentage of queens who are high in one episode and go home the next episode is the same as the percentage of queens who win and go home the next episode, so it appears that being high, even if they don't win, grants queens some benefits when it comes to elimination.
  
Percentage of Surviving Queens Based on Number of Prior Lip Sync For Your Life (LSFYL):
-----

| Prior LSFYL | % Survival |
|-------------|------------|
| 0           | 59%        |
| 1           | 49%        |
| 2           | 24%        |
| 3           | 0%         |

Basically, this table displays the percentage of queens who have survived LSFYL based on how many times the queens had previously LSFYL in that season. So, as you can see, almost 60% of queens will survive their first LSFYL, but none have survived a 4th.

*You're probably wondering about Kameron Michaels' survival of what was technically her 4th lipsync in episode 12 of season 10. I don't count this as a LSFYL because all of the queens participated, and there was no "bottom 2" of the episode.*

Percentage of Surviving Queens Based on Number of Prior Main Challenge Wins:
-----
 ![alt text](https://raw.githubusercontent.com/rupaulsdatarace/rupository/master/mcLSFYLSurvival.png)

| MC Wins | % Survival |
|---------|------------|
| 0       | 44%        |
| 1       | 57.5%      |
| 2       | 70%        |
| 3       | 100%       |

This table (and graph) display the percentage of queens who have survived a LSFYL based on how many times the queens had previously won a main challenge in that season. The table shows that even one MC win increases the chances of survival significantly.

Mini Challenges
-----

Ah, mini-challenges. Do they give the winner(s) an advantage? Do they hinder winners? I hope to do more analysis on this, but so far, I've found that **16%** of winners of mini-challenges have won the main challenge in the same episode, while **10%** have been eliminated in the same episode, so it would appear that winning has some benefit. There have been 110 mini-challenges, and 69 mini-challenge winners. The queen with the most wins is Detox, from Season 5, with 5 wins. It should be noted that earlier seasons appear to have a larger number of mini-challenges, thus queens in later seasons have less opportunity to win multiple mcs.

| # of Minichallenge Wins | # of Queens |
|-------------------------|-------------|
| 1                       | 43          |
| 2                       | 16          |
| 3                       | 6           |
| 4                       | 3           |
| 5                       | 1           |


On Double Saves/Double Eliminations
-----

There have been a total of 6 double saves in the 10 seasons of RPDR, suggesting that on any given season, the chance of a double save is a toss up. In that time, there have only been 2 double eliminations, both fairly early in the season (Season 5, ep 4 of 13, and Season 8, ep 2 of 10). In the case of double saves, 1 was due to a queen having to leave because of an injury (Eureka, Season 9, ep 5 of 13), and 1 was due to a queen being disqualified (Willam, Season 4, ep 8 of 14). 

Additional Stats on Double Outcomes:
- 5/6 double saves occurred in the 7-9 episode of the season (S9, injury, is the exception)
- 9/12 (75%) of queens who were saved in doubles had at least 1 win of the season prior to the double save
- 4/4 (100%) of queens who were eliminated in doubles had 0 wins of the season
- 50% of queens who were saved in doubles survived to the finale of the season (excl S9)
- Queens saved in doubles survived an average of 78% of the rest of the episodes of the season (excl S9)

On Snatch Game
-----

Snatch Game is iconic. It's the challenge fans wait for every season. There has been much speculation regarding how Snatch Game results affect the rest of the season. So naturally, I made a dataset, and am spilling some Tea.

- 41% of queens who survive Snatch Game will make it to the finale. This is simply because of where Snatch Game falls in the season.
- 54% of queens who win or are high for Snatch game will go on to be in the finale, compared with 49% of queens who win at least one episode, and 33.5% of queens who will win or be high for at least one episode.
- 28% of queens who survive Snatch Game and are low or LSFYL during the Snatch game episode will make it to the finale, compared with 33% of queens who LSFYL at least once, and 32.5% of queens who LSFYL or were low at least once.
- 37% of queens who are safe in the Snatch Game episode will be in the finale.
- (Unrelated) 25% of all queens who enter the show will make it to the finale

So, it does appear that doing well at Snatch Game has benefits, doing poorly has consequences, and being safe does very little. I could do a comparison of Season winners and results, but frankly, there are only 80 queens who have done Snatch Game, so dividing the dataset further would be a _choice_.

On First Episode Wins
-----

There have only been 10 first episodes. Drawing conclusions on that little data is silly, but this is a github account about analytics for a reality competition for drag queens, so I'm gonna go with it.

- 70% of queens who won the first episode of their season made it to the finale of the show. Note that this does not hold for the last 2 seasons
- 40% of queens who won the first episode won their season
- 40% of queens who won their season were safe in the first episode
- 0% of queens who LSFYL and survived in the first episode made it to the finale
- 50% of queens who were eliminated in the 2nd episode of the season were safe in the first
- 40% of queens who LSFYL and survived in the first episode were eliminated in the 2nd episode
