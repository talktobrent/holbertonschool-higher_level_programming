<h1>0x15. Javascript - Web JQuery</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to select HTML elements in Javascript</li>
<li>How to select HTML elements with jQuery</li>
<li>What are differences between <code>ID</code>, <code>class</code> and <code>tag name</code> selectors</li>
<li>How to modify an HTML element style</li>
<li>How to get and update an HTML element content</li>
<li>How to modify the DOM</li>
<li>How to make a <code>GET</code> request with jQuery Ajax</li>
<li>How to make a <code>POST</code> request with jQuery Ajax</li>
<li>How to listen/bind to DOM events</li>
<li>How to listen/bind to user events</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. No jQuery
  </h3>
  <p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p>
<ul>
<li>You must use <code>document.querySelector</code> to select the HTML tag</li>
<li>You can&rsquo;t use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>0-script.js</code></p>
  <h3>
    1. With jQuery
  </h3>
  <p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p>
<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>1-script.js</code></p>
  <h3>
    2. Click and turn red
  </h3>
  <p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p>
<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>2-script.js</code></p>
  <h3>
    3. Add `.red` class
  </h3>
  <p>Write a Javascript script that adds the class <code>red</code> to the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p>
<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>3-script.js</code></p>
  <h3>
    4. Toggle classes
  </h3>
  <p>Write a Javascript script that toggles the class of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#toggle_header</code>:</p>
<ul>
<li>The <code>HEADER</code> tag must always have one class: <code>red</code> or <code>green</code>, never both in the same time, never empty.</li>
<li>If the current class is <code>red</code>, when the user click on <code>DIV#toggle_header</code>, the class must be updated to <code>green</code> ; and the reverse.</li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>4-script.js</code></p>
  <h3>
    5. List of elements
  </h3>
  <p>Write a Javascript script that adds a <code>LI</code> element to a list when the user clicks on the tag <code>DIV#add_item</code>:</p>
<ul>
<li>The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code></li>
<li>The new element must be added to <code>UL.my_list</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>5-script.js</code></p>
  <h3>
    6. Change the text
  </h3>
  <p>Write a Javascript script that updates the text of the HTML tag <code>HEADER</code> to &ldquo;New Header!!!&rdquo; when the user clicks on <code>DIV#update_header</code></p>
<ul>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>6-script.js</code></p>
  <h3>
    7. Star wars character
  </h3>
  <p>Write a Javascript script that fetches and replaces the <code>name</code> of this URL: <code>https://swapi.co/api/people/5/?format=json</code></p>
<ul>
<li>The name must be displayed in the HTML tag <code>DIV#character</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>7-script.js</code></p>
  <h3>
    8. Star Wars movies
  </h3>
  <p>Write a Javascript script that fetches and lists all movies <code>title</code> by using this URL: <code>https://swapi.co/api/films/?format=json</code></p>
<ul>
<li>All movie titles must be list in the HTML tag <code>UL#list_movies</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>8-script.js</code></p>
  <h3>
    9. Wind speed
  </h3>
  <p>Write a Javascript script that fetches and prints how to say &ldquo;Hello&rdquo; depending of the language: (here in French) <code>https://fourtonfish.com/hellosalut/?lang=fr</code></p>
<ul>
<li>The translation of &ldquo;Hello&rdquo; must be display in the HTML tag <code>DIV#hello</code></li>
<li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API
You script must be work when it imported from the <code>HEAD</code> tag</li>
</ul>
<p>Please test with this HTML file in your browser:</p>
        <p>File: <code>9-script.js</code></p>
