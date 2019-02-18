<h1>0x13. Javascript - Objects, Scopes and Closures</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create an object in Javascript</li>
<li>What <code>this</code> means</li>
<li>What <code>undefined</code> means </li>
<li>Why the variable type and scope is important</li>
<li>What is a closure</li>
<li>What is a prototype</li>
<li>How to inherit an object from another</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Rectangle #0
  </h3>
  <p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class </li>
</ul>
        <p>File: <code>0-rectangle.js</code></p>
  <h3>
    1. Rectangle #1
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
</ul>
        <p>File: <code>1-rectangle.js</code></p>
  <h3>
    2. Rectangle #2
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
</ul>
        <p>File: <code>2-rectangle.js</code></p>
  <h3>
    3. Rectangle #3
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
</ul>
        <p>File: <code>3-rectangle.js</code></p>
  <h3>
    4. Rectangle #4
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
<li>Create an instance method called <code>rotate()</code> that exchanges the <code>width</code> and the <code>height</code> of the rectangle</li>
<li>Create an instance method called <code>double()</code> that multiples the <code>width</code> and the <code>height</code> of the rectangle by 2</li>
</ul>
        <p>File: <code>4-rectangle.js</code></p>
  <h3>
    5. Square #0
  </h3>
  <p>Write a class <code>Square</code> that defines a square and inherits from <code>Rectangle</code> of <code>4-rectangle.js</code>:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>The constructor must take 1 argument: <code>size</code></li>
<li>The constructor of <code>Rectangle</code> must be called (by using <code>super()</code>)</li>
</ul>
        <p>File: <code>5-square.js</code></p>
  <h3>
    6. Square #1
  </h3>
  <p>Write a class <code>Square</code> that defines a square and inherits from <code>Square</code> of <code>5-square.js</code>:</p>
<ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>Create an instance method called <code>charPrint(c)</code> that prints the rectangle using the character <code>c</code>
<ul>
<li>If <code>c</code> is <code>undefined</code>, use the character <code>X</code></li>
</ul></li>
</ul>
        <p>File: <code>6-square.js</code></p>
  <h3>
    7. Occurrences
  </h3>
  <p>Write a function that returns the number of occurrences in a list:</p>
<ul>
<li>Prototype: <code>exports.nbOccurences = function (list, searchElement)</code></li>
</ul>
        <p>File: <code>7-occurrences.js</code></p>
  <h3>
    8. Esrever
  </h3>
  <p>Write a function that returns the reversed version of a list:</p>
<ul>
<li>Prototype: <code>exports.esrever = function (list)</code></li>
<li>You are not allow to use the built-in method <code>reverse</code></li>
</ul>
        <p>File: <code>8-esrever.js</code></p>
  <h3>
    9. Log me
  </h3>
  <p>Write a function that prints the number of arguments already printed and the new argument value. (see example below)</p>
<ul>
<li>Prototype: <code>exports.logMe = function (item)</code></li>
<li>Output format: <code>&lt;number arguments already printed&gt;: &lt;current argument value&gt;</code></li>
</ul>
        <p>File: <code>9-logme.js</code></p>
  <h3>
    10. Number conversion
  </h3>
  <p>Write a function that converts a number from base 10 to another base passed as argument:</p>
<ul>
<li>Prototype: <code>exports.converter = function (base)</code></li>
<li>You are not allowed to import any file</li>
<li>You are not allowed to declare any new variable (<code>var</code>, <code>let</code>, etc..)</li>
</ul>
        <p>File: <code>10-converter.js</code></p>
