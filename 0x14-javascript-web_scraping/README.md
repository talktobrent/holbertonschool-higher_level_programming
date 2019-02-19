<h1>0x14. Javascript - Web scraping</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Readme
  </h3>
  <p>Write a script that reads and prints the content of a file.</p>
<ul>
<li>The first argument is the file path</li>
<li>The content of the file must be read in <code>utf-8</code></li>
<li>If an error occurred during the reading, print the error object</li>
</ul>
        <p>File: <code>0-readme.js</code></p>
  <h3>
    1. Write me
  </h3>
  <p>Write a script that writes a string to a file.</p>
<ul>
<li>The first argument is the file path</li>
<li>The second argument is the string to write</li>
<li>The content of the file must be written in <code>utf-8</code></li>
<li>If an error occurred during while writing, print the error object</li>
</ul>
        <p>File: <code>1-writeme.js</code></p>
  <h3>
    2. Status code
  </h3>
  <p>Write a script that display the status code of a <code>GET</code> request.</p>
<ul>
<li>The first argument is the URL to request (<code>GET</code>)</li>
<li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>2-statuscode.js</code></p>
  <h3>
    3. Star wars movie title
  </h3>
  <p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p>
<ul>
<li>The first argument is the episode number</li>
<li>You must use the Star wars API with the endpoint <code>http://swapi.co/api/films/:id</code></li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>3-starwars_title.js</code></p>
  <h3>
    4. Star wars Wedge Antilles
  </h3>
  <p>Write a script that prints the number of movies where the character &ldquo;Wedge Antilles&rdquo; is present.</p>
<ul>
<li>The first argument is the API URL of the Star wars API: <code>http://swapi.co/api/films/</code></li>
<li>Wedge Antilles is character ID <code>18</code></li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>4-starwars_count.js</code></p>
  <h3>
    5. Loripsum
  </h3>
  <p>Write a script that gets the contents of a webpage and stores it in a file.</p>
<ul>
<li>The first argument is the URL to request</li>
<li>The second argument the file path to store the body response</li>
<li>The file must be UTF-8 encoded</li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>5-request_store.js</code></p>
  <h3>
    6. How many completed?
  </h3>
  <p>Write a script that computes the number of tasks completed by user id.</p>
<ul>
<li>The first argument is the API URL: <code>https://jsonplaceholder.typicode.com/todos</code></li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>6-completed_tasks.js</code></p>
  <h3>
    7. Who was playing in this movie?
  </h3>
  <p>Write a script that prints all characters of a Star Wars movie:</p>
<ul>
<li>The first argument is the Movie ID - example: <code>3</code> = &ldquo;Return of the Jedi&rdquo; </li>
<li>Display one character name by line</li>
<li>You must use the Star wars API</li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>100-starwars_characters.js</code></p>
  <h3>
    8. Right order
  </h3>
  <p>Write a script that prints all characters of a Star Wars movie:</p>
<ul>
<li>The first argument is the Movie ID - example: <code>3</code> = &ldquo;Return of the Jedi&rdquo; </li>
<li>Display one character name by line <strong>in the same order of the list &ldquo;characters&rdquo; in the <code>/films/</code> response</strong></li>
<li>You must use the Star wars API</li>
<li>You must use the module <code>request</code></li>
</ul>
        <p>File: <code>101-starwars_characters.js</code></p>
  <h3>
    9. Twitter Auth
  </h3>
  <p>Write a Javascript script that takes in 3 strings and sends a search request to the Twitter API</p>
<ul>
<li>Use the Twitter API search endpoint</li>
<li>Use the Application-only authentication flow to do a search request </li>
<li>Create an Twitter application here</li>
<li>The first argument must be the Consumer Key (API Key)</li>
<li>The second argument must be the Consumer Secret (API Secret)</li>
<li>The third argument must be the search string</li>
<li>Display only 5 results in the following format: <code>[&lt;Tweet ID&gt;] &lt;Tweet text&gt; by &lt;Tweet owner name&gt;</code> (see example below)</li>
<li>Only these modules are allowed: <code>request</code>, <code>base-64</code> and <code>utf8</code></li>
<li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
</ul>
        <p>File: <code>102-search_twitter.js</code></p>
