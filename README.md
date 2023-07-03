<h1>TripAdvisor Istanbul Restaurant Scraper</h1>

<p>This is a web scraping project that extracts restaurant data from the TripAdvisor website for Istanbul and stores it in a MySQL database. The project is implemented using Scrapy, a powerful web scraping framework in Python.</p>

<h2>Requirements</h2>

<p>To run this project, you need to have the following dependencies installed:</p>

<ul>
  <li>Python 3.x</li>
  <li>Scrapy</li>
  <li>mysql-connector-python</li>
</ul>

<h2>Project Structure</h2>

<p>The repository has the following structure:</p>

<ul>
  <li><code>istanbul.py</code>: Scrapy spider that defines the crawling behavior and data extraction logic.</li>
  <li><code>items.py</code>: Item class that represents the structure of the scraped data.</li>
  <li><code>pipelines.py</code>: Pipeline class responsible for processing and storing the scraped data in a MySQL database.</li>
  <li><code>settings.py</code>: A configuration file for the Scrapy project, allowing to customize the behavior of the project by modifying various settings.</li>
</ul>

<p>Make sure to update the database connection details in the <code>pipelines.py</code> file by providing the appropriate values for <code>host</code>, <code>user</code>, and <code>password</code> variables.</p>

<p>To run the spider, navigate to the project directory in the terminal and execute the following command:</p>

<pre>
<code>scrapy crawl istanbul</code>
</pre>

<p>The spider will start scraping restaurant data from TripAdvisor and store it in the MySQL database.</p>
