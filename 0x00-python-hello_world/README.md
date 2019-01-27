<h1>0x00. Python - Hello, World</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>Who created Python</li>
<li>Who is Guido van Rossum</li>
<li>Where does the name &lsquo;Python&rsquo; come from</li>
<li>What is the Zen of Python</li>
<li>How to use the Python interpreter</li>
<li>How to print text and variables using <code>print</code></li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Holberton Python coding style and how to check your code with <code>PEP 8</code></li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Run Python file
  </h3>
  <p>Write a Shell script that runs a Python script.</p>
<p>The Python file name will be saved in the environment variable <code>$PYFILE</code></p>
        <p>File: <code>0-run</code></p>
  <h3>
    1. Run inline
  </h3>
  <p>Write a Shell script that runs Python code.</p>
<p>The Python code will be saved in the environment variable <code>$PYCODE</code></p>
        <p>File: <code>1-run_inline</code></p>
  <h3>
    2. Hello, print
  </h3>
  <p>Write a Python script that prints exactly <code>&quot;Programming is like building a multilingual puzzle</code>, followed by a new line.</p>
<ul>
<li>Use the function <code>print</code></li>
</ul>
        <p>File: <code>2-print.py</code></p>
  <h3>
    3. Print integer
  </h3>
  <p>Complete this source code in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.</p>
<ul>
<li>You can find the source code here</li>
<li>The output of the script should be:
<ul>
<li>the number, followed by <code>Battery street</code>,</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast the variable <code>number</code> into a string</li>
<li>Your code must be 3 lines long</li>
<li>You have to use the new print numbers tips</li>
</ul>
        <p>File: <code>3-print_number.py</code></p>
  <h3>
    4. Print float
  </h3>
  <p>Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.</p>
<ul>
<li>You can find the source code here</li>
<li>The output of the program should be:
<ul>
<li><code>Float:</code>, followed by the float with only 2 digits</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast <code>number</code> to string</li>
<li>You have to use the new print formatting tips</li>
</ul>
        <p>File: <code>4-print_float.py</code></p>
  <h3>
    5. Print string
  </h3>
  <p>Complete this source code in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.</p>
<ul>
<li>You can find the source code here</li>
<li>The output of the program should be:
<ul>
<li>3 times the value of <code>str</code></li>
<li>followed by a new line</li>
<li>followed by the 9 first characters of <code>str</code></li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to use any loops or conditional statement</li>
<li>Your program should be maximum 5 lines long</li>
</ul>
        <p>File: <code>5-print_string.py</code></p>
  <h3>
    6. Play with strings
  </h3>
  <p>Complete this source code to print <code>Welcome to Holberton School!</code></p>
<ul>
<li>You can find the source code here</li>
<li>You are not allowed to use any loops or conditional statements.</li>
<li>You have to use the variables <code>str1</code> and <code>str2</code> in your new line of code</li>
<li>Your program should be exactly 5 lines long</li>
</ul>
        <p>File: <code>6-concat.py</code></p>
  <h3>
    7. Copy - Cut - Paste
  </h3>
  <p>Complete this source code</p>
<ul>
<li>You can find the source code here</li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 8 lines long</li>
<li><code>word_first_3</code> should contain the first 3 letters of the variable <code>word</code></li>
<li><code>word_last_2</code> should contain the last 2 letters of the variable <code>word</code></li>
<li><code>middle_word</code> should contain the value of the variable <code>word</code> without the first and last letters</li>
</ul>
        <p>File: <code>7-edges.py</code></p>
  <h3>
    8. Create a new sentence
  </h3>
  <p>Complete this source code to print <code>object-oriented programming with Python</code>, followed by a new line.</p>
<ul>
<li>You can find the source code here</li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 5 lines long</li>
<li>You are not allowed to create new variables</li>
<li>You are not allowed to use string literals</li>
</ul>
        <p>File: <code>8-concat_edges.py</code></p>
  <h3>
    9. Easter Egg
  </h3>
  <p>Write a Python script that prints &ldquo;The Zen of Python&rdquo;, by TimPeters, followed by a new line.</p>
<ul>
<li>Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py</code>)</li>
</ul>
        <p>File: <code>9-easter_egg.py</code></p>
  <h3>
    10. Linked list cycle
  </h3>
  <p><strong>Technical interview preparation</strong>: </p>
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
<li>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution&rsquo;s runtime fast enough, does your solution require extra memory usage / mallocs, etc.</li>
</ul>
<p>Write a function in C that checks if a singly linked list has a cycle in it.</p>
<ul>
<li>Prototype: <code>int check_cycle(listint_t *list);</code></li>
<li>Return: <code>0</code> if there is no cycle, <code>1</code> if there is a cycle</li>
</ul>
<p>Requirements:</p>
<ul>
<li>Only these functions are allowed: <code>write</code>, <code>printf</code>, <code>putchar</code>, <code>puts</code>, <code>malloc</code>, <code>free</code></li>
</ul>
        <p>File: <code>10-check_cycle.c, lists.h</code></p>
