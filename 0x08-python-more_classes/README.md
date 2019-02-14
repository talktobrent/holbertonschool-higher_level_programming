<h1>0x08. Python - More Classes and Objects</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
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
<li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
<li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
<li>What is a class attribute</li>
<li>What is the difference between a object attribute and a class attribute</li>
<li>What is a class method</li>
<li>What is a static method</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Simple rectangle
  </h3>
  <p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>
<ul>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>0-rectangle.py</code></p>
  <h3>
    1. Real definition of a rectangle
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>1-rectangle.py</code></p>
  <h3>
    2. Area and Perimeter
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>2-rectangle.py</code></p>
  <h3>
    3. String representation
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>Object address can be different</strong></p>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>3-rectangle.py</code></p>
  <h3>
    4. Eval is magic
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)</li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>4-rectangle.py</code></p>
  <h3>
    5. Detect instance deletion
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>5-rectangle.py</code></p>
  <h3>
    6. How many instances
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>6-rectangle.py</code></p>
  <h3>
    7. Change representation
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>6-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:
<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>7-rectangle.py</code></p>
  <h3>
    8. Compare rectangles
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>7-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:
<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area
<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>8-rectangle.py</code></p>
  <h3>
    9. A square is a rectangle
  </h3>
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>8-rectangle.py</code>)</p>
<ul>
<li>Private instance attribute: <code>width</code>:
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:
<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area
<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code></li>
<li>You are not allowed to import any module</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>9-rectangle.py</code></p>
  <h3>
    10. Class and instance attributes
  </h3>
  <p>Write a blog post describing how object and class attributes work.</p>
<ul>
<li>What&rsquo;s a class attribute</li>
<li>What&rsquo;s an instance attribute</li>
<li>What are all the ways to create them and what is the Pythonic way of doing it</li>
<li>What are the differences between class and instance attributes</li>
<li>What are the advantages and drawbacks of each of them</li>
<li>How does Python deal with the object and class attributes using the <code>__dict__</code></li>
</ul>
<p>Your posts should have examples and at least one picture, at the top. 
Publish your blog post on Medium or LinkedIn, and share it at least on Twitter and LinkedIn.</p>
  <h3>
    11. N queens
  </h3>
<small>Chess grandmaster Judit Polgár, the strongest female chess player of all time</small>
<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>
<ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem
<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don&rsquo;t have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>
<p>Read: Queen, Backtracking</p>
        <p>File: <code>101-nqueens.py</code></p>
