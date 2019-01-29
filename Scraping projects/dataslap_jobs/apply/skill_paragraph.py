from dataslap_jobs.models import *
from datetime import datetime,tzinfo,timedelta
from pytz import timezone
# from sqlalchemy import Column


init_skill_paragraphs = {
"gis" : """I have experience creating both printed and online maps.
    One of my most complicated printed map projects was a heatmap of walking distance
    to NYC subway from apartments listed on Zillow. I scraped data myself and
    attempted to find relationship between walking distance to subway stops and rent (I found
    little evidence when controlled for subway stop as a proxy of "neighborhood").
    Less sophisticated cases involve making a Census API pipeline that pulls data
    and converts it to the format suitable for choropleth maps. I used that to
    provide insight into neighborhoods surrounding potential sites for affordable
    housing projects and to provide insights into access to fresh produce, both
    for low income populations either on census tract or county level (using QGIS
    and ArcGIS). Some of the more impressive online maps that I generated in
    Carto produce insights into NYC street pavement quality, traffic collisions
    and public pay phones using CARTO.""",
"scraping" : """I started learning Python solely for the purposes of
    scraping financial data for Machine Learning projects in R. I have completed
    projects that involve scraping such sources as SEC, FERC, Zillow, Instagram,
    Craiglslist, Yelp and others. Recently I finished development of a micro-service
    scraping platform that utilizes Docker as an arcitecture, runs a proxy server,
    a Cron scheduler and a JavaScript rendering service. I oversee my production-grade
    news aggregator and a job aggregator based on this infrastructure for further
    use in my Machine Learning projects. Some of my projects were made to benefit
    some larger communities and are open source. I recently published a Scrapy
    project on Github that enables downloading more than 500 art books that
    Metropolitan Museum of Art shared on their website. It would be a great plesure
    to utilize my scraping skills in your organization.
    """,
"data_science" : """I discovered my interest in Machine Learning when I was
    writing angry LaTeX-knitted econometrics homework papers where I argued
    that choosing regression variables that have little predictive value based
    purely "on theory" is unscientific. I used to rely heavily on R in such projects as
    analysis of energy efficiency subsidies for NYC Department of
    Design and Construction, text analysis of Presidential
    debates of 2016 and subsequently - Congressional committee hearing
    transcripts and in engineering pipelines to convert Census API data into
    maps that tell a story about neighborhoods where affordable housing projects
    are built in NYC. The most recent commitment to switch to Python for data
    science work involved analysis of a 2GB tax assessment dataset to reveal
    county specialization in certain agriculture industries. Another part of
    this project involved combining state data on farmers markets and Census
    data to reveal counties where economically vulnerable population has limited
    access to affordable fresh produce.""",
"database" : """My practical exposure to databases started relatively
    recently. Despite reading a book on MySQL and a W3 SQL tutorial a few years
    ago I only started actively using databases two years ago. I started my exposure
    by setting up PostgreSQL to store parsed text of Congressional hearings on my
    private CentOS server. Later I switched to SQLite using Python sqlalchemy
    library to store tabular output of scrapers. I generated close to 10 narrow
    tables to save the logs of an Instagram bot and since then I've been using
    sqlalchemy in all pipelines of my scrapy projects. One of the most recent
    implementations was the use in a news aggregator that accumulated ~1.5GB of
    ~300 thousand articles in a test phase of the first news source in the pipeline.
    Current version writes to an RDS PostgreSQL instance on AWS and utilizes some
    custom psql data types like arrays and time stamps. My current databases are
    Third Normal Form, the biggest database consisting of 17 tables.""",
"machine_learning" : """Like most people fascinated by Machine Learning field, I
    started with a book called 'Intro to Statistical Learning'. After working
    through code a few times I started writing my own functions that mimicked
    best_score and best_estimator attributes in sklearn. I utilized some of that
    code to find the incorrectly extracted paragraphs using a 95 percent
    accurate KNN classifier. Having later switched to Python and sklearn I worked
    throught the code of a few Packt and O'Reiley books in order to practice
    the basic concepts. Currently I'm working on designing Sci-kit Learn pipelines
    to perform highly granular preprocessing on a mass scale for Randomized
    Search Cross Validation.""",
"finance" : """My first exposure to Financial analysis started when I
    was working as a hostile acquisitions lawyer at the family Private Equity
    fund that focused on distressed real estate and equity investments. While I
    was getting my Finance degree I was consulting the CFO of the fund and helped
    managing post-acquisition analysis when I visited during summer breaks. My
    interest in the wide range of finance topics (from Real Estate to Derrivatives
    and Mergers and Acquisitions) led me to explore Venture Capital Finance and
    co-found Bentley VC and PE club on campus which I helped grow as VP of
    Administration. Most recently I applied my Finance skills at Lambda Prime
    in financial analysis and market research of Public Cyber Security companies
    and startups in that area. After a successful summer in the Venture Capital
    side of the company I transitioned to the Hedge Fund side of the company performing
    research and providing strategy recommendations on the Public companies of
    interest to the founder and Senior Executives of the fund.
    """,
"python" : """For the past three years I heavily relied on Python in
    various data aggregation projects ranging from governmental data (SEC, FERC,
    Congress Hearings) to market/social data (Zillow Rentals and Craigslist Casual
    Encounters) and less traditional projects like an Instagram bot. I pushed myself
    to learn sqlalchemy package which resulted in projects of the past year
    to rely on SQLite and PostgreSQL data storage in up to 17 tables per project. I used my
    capstone project  as an oportunity to switch from R to Python pandas library by analyzing
    NYS tax assessment and US Census data. I provided insights on agricultural
    land by summarizing over 6 million entries on land lots - having exposure
    to such data helped me switch my data wrangling pipelines (along with feature
    engineering and data mining) from R to Python and practice most widely used
    grouping and summarizing methods (i.e. pivoting) and design custom transformations.
    """,
"data_visualization" : """I like using graphs to learn about strange and obscure things
   and to spread my fascination with them. Explicit example is plotting the
   cumulative words of Presidential debates of 2016 to see how much candidates
   talk about themselves or mention sensitive topics (words "nuclear" or "war"). Another one is
   accidentally stumbling upon an army of bots that followed me on Instagram in response to
   my bot - something that I wouldn’t have noticed with regular statistical tools since I was
   interested in how effective my follow-like-unfollow strategy was rather than exploring
   the industry. Currently I am focusing on mastering matplotlib for professional work (D3.js - next) and
   Processing (including p5.js) for my personal projects. I have achieved some heights
   in ggplot like custom themes or boxplot sorting (by mean/median) but my goal is to switch
   to more advanced or scientific tools - I consider them superior in “spreading fascination”.
    """}

# for i in init_skill_paragraphs.items():
#     print(i[0])



for paragraph_item in init_skill_paragraphs.items():
    post_entry(entry = {"skill_id" :
                    inst_to_dict(
                    session_test.query(Skill_focus_entry).\
                    filter(Skill_focus_entry.skill_label == paragraph_item[0]).\
                    one())["skill_id"],
                        "skill_paragraph_text" : paragraph_item[1],
                        "skill_paragraph_added" : datetime.now(timezone('US/Eastern'))},
                    session = session_test,
                    item = Skill_paragraph_entry,
                    item_column = Skill_paragraph_entry.skill_paragraph_text,
                    query_string = paragraph_item[1])
