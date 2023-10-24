# Wiki - A Wikipedia-like Encyclopedia

## Description
"Wiki" is a web application that emulates the format and functionality of Wikipedia, allowing users to create and edit articles in a user-friendly and Markdown-based interface. It was developed as part of the CS50's Web Programming with Python and JavaScript course offered by Harvard University with this [task](https://cs50.harvard.edu/web/2020/projects/1/wiki/).

## Features
<ul>
<li>
User-friendly and familiar Wikipedia-style interface.
</li>
<li>
Create new articles using Markdown syntax.
</li>
<li>
Edit existing articles.
</li>
<li>
Search for articles.
</li>
<li>
Random page feature to explore content.
</li>
<li>
View and navigate articles by title.
</li>
</ul>

## Deployment
The "Wiki" application is deployed on Heroku and can be accessed at [Heroku Wiki](https://encyclopedia-zodiac-signs-b527c512364f.herokuapp.com/wiki/).

## How to Use
**To create a new article**, click on the "Create" link and use Markdown syntax to write the article's content.
**To edit an existing article**, click on the "Edit" link and make your changes using the Markdown editor.
**To search for articles**, use the search bar at the top of the page.
**To explore random content**, click the "Random Page" link.

## Contributions
"Wiki" is designed to be an open platform for anyone to contribute their favorite TV series, movies, books, or other content in Markdown syntax. To add a new entry, follow these guidelines:
<ul>
<li>
Click on the "Create" link to create a new article.
</li>
<li>
Use Markdown syntax to format your content. Include a title, description, and any additional details.
</li>
<li>
Save your changes to publish the article.
</li>
<li>
Please ensure that your contributions are respectful, relevant, and adhere to any community guidelines or rules in place.
</li>
</ul>

## Tha Django Application

Files and Directories modified from the original Django packadge:
<ul>
<li>
encyclopedia (my web application)
<ul>
    <li>
    templates (including the CSS content) : I used the Bootstrap CSS and JavaScript for the layout of the web pages.
    </li>
    <li>
    urls.py : I included all the paths to specific templates, including the name of enties in some url format.
    </li>
    <li>
    util.py : includes functions that helped retrieving or getting data from md files, such as get_entry, save_entry, list_entries and list_entries_by_type
    </li>
    <li>
    views.py : includes the logic behind the web applications and covers any possible user-error case, so that the app doesn't crash
    </li>
</ul>
</li>
<li>
entries : md files containing the Markdown content of the pages
</li>
<li>
wiki
<ul>
    <li>
    urls.py : included the wiki path for this web application
    </li>
</ul>
</li>
</ul>




