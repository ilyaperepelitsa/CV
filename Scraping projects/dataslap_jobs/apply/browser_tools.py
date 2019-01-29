import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.expected_conditions import staleness_of

import time

from contextlib import contextmanager

import fpdf
import pandas as pd
import os

dir_name = os.path.dirname(os.path.realpath(__file__))
# dir_name = os.path.dirname(os.path.realpath("__file__"))
path_to_chromedriver = os.path.join(dir_name, "chromedriver")

def init_driver():
    driver = webdriver.Chrome(executable_path=path_to_chromedriver)
    driver.wait = WebDriverWait(driver, 5)
    return driver

def open_a_job(driver, url):
    driver.get(url)
    wait_for_page_load(driver)
    driver.execute_script(jscode_functions)


@contextmanager
def wait_for_page_load(driver, timeout=5):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(EC.staleness_of(old_page))


jscode_functions = """
    function HighlightText(bodyText, searchTerm){

    highlightStartTag = "<font style='font-weight:bold; font-size: 1.875em; background-color: #c500ed; color: black'>";
    highlightEndTag = "</font>";


  var newText = "";
  var i = -1;
  var lcSearchTerm = searchTerm.toLowerCase();
  var lcBodyText = bodyText.toLowerCase();

  while (bodyText.length > 0) {
    i = lcBodyText.indexOf(lcSearchTerm, i+1);
    if (i < 0) {
      newText += bodyText;
      bodyText = "";
    } else {

      if (bodyText.lastIndexOf(">", i) >= bodyText.lastIndexOf("<", i)) {

        if (lcBodyText.lastIndexOf("/script>", i) >= lcBodyText.lastIndexOf("<script", i)) {
          newText += bodyText.substring(0, i) + highlightStartTag + bodyText.substr(i, searchTerm.length) + highlightEndTag;
          bodyText = bodyText.substr(i + searchTerm.length);
          lcBodyText = bodyText.toLowerCase();
          i = -1;
        }
      }
    }
  }

  return newText;
}


function highlight(searchPhrase, treatAsPhrase,element)
{
  if (treatAsPhrase) {
    searchArray = [searchPhrase];
  } else {
    searchArray = searchPhrase.split(" ");
  }

  //var Text = document.getElementById(element).innerHTML;
  var Text = document.getElementsByTagName(element)[0].innerHTML;

  for (var i = 0; i < searchArray.length; i++) {
    Text = HighlightText(Text, searchArray[i]);
  }

  document.getElementsByTagName(element)[0].innerHTML = Text;
  return true;
}

//handle as phrase (1) or search for every single word (0)


var bodyExists =  document.getElementsByTagName('body')[0];

if (typeof(bodyExists) != 'undefined' && bodyExists != null)
{
highlight('python ggplot pandas selenium matplotlib numpy sklear scikit scikit-learn ggplot dplyr p5.js p5js p5 sql urban policy scrapy java js javascript d3 tableau github Javascript',0,'body');
highlight('urban policy',1,'body');
highlight('machine learning',1,'body');
highlight('data visualization',1,'body');
}



"""

# driver = init_driver()
# # print("pew")
# # driver.get("https://google.com")
# # driver.find_element_by_tag_name("html")
# open_a_job(driver, "https://www.amazon.com")
# driver.quit()
