<h1>0x12. Javascript - Warm up</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to run a Javascript script</li>
<li>How to create variables and constants</li>
<li>What are differences between <code>var</code>, <code>const</code> and <code>let</code></li>
<li>What are all the data types available in Javascript</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use <code>while</code> and <code>for</code> loops</li>
<li>How to use <code>break</code> and <code>continue</code> statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any <code>return</code> statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. First constant, first print
  </h3>
  <p>Write a script that prints &ldquo;Javascript is amazing&rdquo;:</p>
<ul>
<li>You must create a constant variable called <code>myVar</code> with the value &ldquo;Javascript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>0-javascript_is_amazing.js</code></p>
  <h3>
    1. 3 languages
  </h3>
  <p>Write a script that prints 3 lines:</p>
<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;Javascript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>1-multi_languages.js</code></p>
  <h3>
    2. Arguments
  </h3>
  <p>Write a script that prints a message depending of the number of arguments passed:</p>
<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>If only one argument is passed to the script, print &ldquo;Argument found&rdquo;</li>
<li>Otherwise, print &ldquo;Arguments found&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
<p>Reference: process.argv</p>
        <p>File: <code>2-arguments.js</code></p>
  <h3>
    3. Value of my argument
  </h3>
  <p>Write a script that prints the first argument passed to it:</p>
<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>length</code></li>
</ul>
        <p>File: <code>3-value_argument.js</code></p>
  <h3>
    4. Create a sentence
  </h3>
  <p>Write a script that prints two arguments passed to it, in the following format: &ldquo;<first argument> is <second argument>&rdquo;</p>
<ul>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>4-concat.js</code></p>
  <h3>
    5. An Integer
  </h3>
  <p>Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:</p>
<ul>
<li>If the argument can&rsquo;t be converted to an integer, print &ldquo;Not a number&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>try/catch</code></li>
</ul>
        <p>File: <code>5-to_integer.js</code></p>
  <h3>
    6. Loop to languages
  </h3>
  <p>Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>
<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;Javascript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use any <code>if/else</code> statement</li>
<li>You can use only one <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>
        <p>File: <code>6-multi_languages_loop.js</code></p>
  <h3>
    7. I love C
  </h3>
  <p>Write a script that prints <code>x</code> times &ldquo;C is fun&rdquo;</p>
<ul>
<li>Where <code>x</code> is the first argument of the script</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing number of occurrences&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You can use only two <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>
        <p>File: <code>7-multi_c.js</code></p>
  <h3>
    8. Square
  </h3>
  <p>Write a script that prints a square</p>
<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing size&rdquo;</li>
<li>You must use the character <code>X</code> to print the square</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>
        <p>File: <code>8-square.js</code></p>
  <h3>
    9. Add
  </h3>
  <p>Write a script that prints the addition of 2 integers</p>
<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: <code>function add(a, b)</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>9-add.js</code></p>
  <h3>
    10. Factorial
  </h3>
  <p>Write a script that computes and prints a factorial</p>
<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of <code>NaN</code> is <code>1</code></li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>10-factorial.js</code></p>
  <h3>
    11. Second biggest!
  </h3>
  <p>Write a script that searches the second biggest integer in the list of arguments.</p>
<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print <code>0</code></li>
<li>If the number of arguments is 1, print <code>0</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>11-second_biggest.js</code></p>
  <h3>
    12. Object
  </h3>
  <p>Update this script to replace the value <code>12</code> with <code>89</code>:</p>
<ul>
<li>You are not allowed to use <code>var</code></li>
</ul>
        <p>File: <code>12-object.js</code></p>
  <h3>
    13. Add file
  </h3>
  <p>Write a function that returns the addition of 2 integers.</p>
<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be <code>add</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>
<p>Tip from Jared</p>
        <p>File: <code>13-add.js</code></p>
