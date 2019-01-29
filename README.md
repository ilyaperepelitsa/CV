# CV
Ilya Perepelitsa


## Description

A few collected highlights of my work in python, JS and Carto are collected
here.
Some of the projects are pure code, some come with an html that one can open in
chrome. All relevant points will be presented in the general overview

## General info

*


## Contents
Bulk of my work deals with scraping - I love getting to visualizations and ML
but in so many cases you're just swamped with data collection and Data
Engineering matters (spinning databases, dealing with schemas etc.)
There is loads of scrapy (mostly) code as well as some sqlalchemy in there
### Scraping projects
* Dataslap jobs - a job aggregator that I plan to launch as a service for slow
gathering of Glassdoor jobs and putting together tools for job applications on a
scale (cover letter generator, submission scripts, maybe even resume generator
that, similar to cover letter generator, makes ones based on the match of
relevant skills and job description). More advanced features are coming after I
finish with my React.js adventures.
* FERC_DOC_TRAIL - a contract job that I did for these wonderful people:
[VzPI](https://github.com/VzPI) - a set of tools for monitoring pipeline
construction in the U.S. It's a part of the repository, can be found here:
[FERC DOC part](https://github.com/VzPI/FERC_DOC_TRAIL)
* snew - news (yep, puns) aggregator. Started with a few sources, shouldn't
really be discussing them. Two sources at the moment, work in progress
* Met Book downloader - Metropolitan museum published some books for free. This
is a community tool project for downloading them. Published
[here](https://github.com/ilyaperepelitsa/met_book_downloader), got some support
from people for it.
* Intercept - Intercept had a dump of documents with some semi-confidential
stuff. Please take your own risk on what PDFs are evil and what you download.

### kaggle
Most recently I've only had a chance of playing with sklearn on some job
application test assignments so I pushed myself to start submitting some basic
stuff on kaggle. Below - AMNES housing dataset and MNIST (keras and TF).
* AMNES - scored top 36% (the last version I could find). Bayesian Ridge worked
in this case but there's more room for improvement - I was testing raw
hyperparameter approach with no feature engineering. It's gonna be the next
step. Generally I like L1 and L2 regressions a lot - one of the most naturally
interpretable parameter output to explain and visualize.
* MNIST - scored top 25% (initial 22%) with 99.4% accuracy. The model that
worked is a combo of Imagenet and Inception models working in parallel, very
small replicas (number of inception layers in particular). Started with TF,
replicated the same models in Keras and moved on to parodies of reliable
academic models with the intention of "being able to construct any convolutional
architecture". Attached - all the files of tested architectures with some
hyperparameters preserved in the json file. Some later models were lost (they're
)on my iMac in Vladivostok) - the folder wasn't "githubbable" - I was saving all
the logs and weights in order to be able to restart the training by pickling
them and not do it from scratch.
Some of the more advanced code might be missing. The furthest I got to with
keras is pickling the model weights, writing logs, model saving weights only if
there is improvement in test accuracy/loss. I tried playing with outputting
convolutional weights as well but something went wrong and instead of a weights
array I got a vector of pixels from convolutional layers (which is very odd but
I couldn't find how to fix it at the time). Planning to check that in more
advanced kaggle competitions when I get to the CV NN book.

* Common learning - I started putting together some basic sklearn custom
transformers. I want to pick it up later and make them work properly with
pipelines so that I can test various "automatic feature engineering" pipeline
steps i.e. figure out a datetime thing to pull out of data, pick some variables
and count with grouping by year/month/day of the week to test wether they can be
used as features automatically and focus on some more interesting features.


### Python graphs init
* Python graphs - I started putting together some boilerplate for graphs.
Initiated a boxplot graph function that accepts arguments to determine how to
order boxes - some usual i.e. by median, mean and some more interesting - by
interquartile range. Also some color palette code that gets imported. I want to
grow the basic graphs part of the library as well as explore some of the more
unusual pyplot visualizations like table graphs etc.


### P5.js projects
* Instagram bot - available at [this
link](https://ilyaperepelitsa.github.io/graph/). I made a Selenium-based
instagram bot that followed thousands of people and liked a bunch of their
photos, got 82 clean "follow-backs" and visualized it in a processing graph.
Initially wanted to run some ML and write a proper bot but ran out of time and
resources.


### GIS Projects
* Traffic accidents map - a Carto map with some simple jquery (I would probably
use React now) that filters the input data and outputs only that filtered data
on the map and calculates some basic stats (count of people killed and injured).
I had some leaflet.js experiments for my final project but I'm too embarassed to
share it.
