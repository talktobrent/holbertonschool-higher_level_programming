<h1>0x06. Python - Classes and Objects</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>What is OOP</li>
<li>&ldquo;first-class everything&rdquo;</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is <code>self</code></li>
<li>What is a method</li>
<li>What is the special <code>__init__</code> method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. My first square
  </h3>
  <p>Write an empty class <code>Square</code> that defines a square:</p>
<ul>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>0-square.py</code></p>
  <h3>
    1. Square with size
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with <code>size</code> (no type/value verification)</li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>Why?</strong></p>
<p><em>Why <code>size</code> is private attribute?</em></p>
<p>The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. 
One way to have the control is to keep it privately. 
You will see in next tasks how to get, update and validate the size value.</p>
        <p>File: <code>1-square.py</code></p>
  <h3>
    2. Size validation
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>
<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>2-square.py</code></p>
  <h3>
    3. Area of a square
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>
<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>3-square.py</code></p>
  <h3>
    4. Access and update private attribute
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code>:
<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:
<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>Why?</strong></p>
<p><em>Why a getter and setter?</em></p>
<p>Reminder: <code>size</code> is a private attribute. We did that to make sure we control the type and value. 
Getter and setter methods are not 100% Python, but more OOP. 
With them, you will be able to validate the assignation of a private attribute and also define how this one will be available from outside (get the attribute value) - by copy? by assignation, etc.
Also, adding type/value validation in the setter will centralize the logic, you will do it in only one place.</p>
        <p>File: <code>4-square.py</code></p>
  <h3>
    5. Printing a square
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code>:
<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:
<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:
<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>5-square.py</code></p>
  <h3>
    6. Coordinates of a square
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code>:
<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:
<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:
<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:
<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:
<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space - <strong>Don&rsquo;t fill lines by spaces</strong> when <code>position[1] &gt; 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>6-square.py</code></p>
  <h3>
    7. Singly linked list
  </h3>
  <p>Write a class <code>Node</code> that defines a node of a singly linked list by: </p>
<ul>
<li>Private instance attribute: <code>data</code>:
<ul>
<li>property <code>def data(self):</code> to retrieve it</li>
<li>property setter <code>def data(self, value):</code> to set it:
<ul>
<li><code>data</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>data must be an integer</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>next_node</code>:
<ul>
<li>property <code>def next_node(self):</code> to retrieve it</li>
<li>property setter <code>def next_node(self, value):</code> to set it:
<ul>
<li><code>next_node</code> can be <code>None</code> or must be a <code>Node</code>, otherwise raise a <code>TypeError</code> exception with the message <code>next_node must be a Node object</code></li>
</ul></li>
</ul></li>
<li>Instantiation with <code>data</code> and <code>next_node</code>: <code>def __init__(self, data, next_node=None):</code></li>
</ul>
<p>And, write a class <code>SinglyLinkedList</code> that defines a singly linked list by: </p>
<ul>
<li>Private instance attribute: <code>head</code> (no setter or getter)</li>
<li>Simple instantiation: <code>def __init__(self):</code></li>
<li>Should be printable:
<ul>
<li>print the entire list in stdout</li>
<li>one node number by line</li>
</ul></li>
<li>Public instance method: <code>def sorted_insert(self, value):</code> that inserts a new <code>Node</code> into the correct sorted position in the list (increasing order)</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>100-singly_linked_list.py</code></p>
  <h3>
    8. Print Square instance
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>6-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code>:
<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:
<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:
<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:
<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integer</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:
<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space</li>
</ul></li>
<li>Printing a <code>Square</code> instance should have the same behavior as <code>my_print()</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>101-square.py</code></p>
  <h3>
    9. Compare 2 squares
  </h3>
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>
<ul>
<li>Private instance attribute: <code>size</code>:
<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:
<ul>
<li><code>size</code> must be a number (float or integer), otherwise raise a <code>TypeError</code> exception with the message <code>size must be a number</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li><code>Square</code> instance can answer to comparators: <code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code> and <code>&lt;=</code> based on the square area</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>102-square.py</code></p>
  <h3>
    10. ByteCode -&gt; Python #5
  </h3>
  <p>Write the Python class <code>MagicClass</code> that does exactly the same as the following Python bytecode:</p>
<ul>
<li>Tip: Python bytecode</li>
</ul>
        <p>File: <code>103-magic_class.py</code></p>
