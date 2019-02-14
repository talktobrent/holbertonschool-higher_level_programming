<h1>0x07. Python - Test-driven development</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What&rsquo;s an interactive test</li>
<li>Why tests are important</li>
<li>How to write Docstrings to create tests</li>
<li>How to write documentation for each module and function</li>
<li>What are the basic option flags to create tests</li>
<li>How to find edge cases</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Integers addition
  </h3>
  <p>Write a function that adds 2 integers.</p>
<ul>
<li>Prototype: <code>def add_integer(a, b=98):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>0-add_integer.py, tests/0-add_integer.txt</code></p>
  <h3>
    1. Divide a matrix
  </h3>
  <p>Write a function that divides all elements of a matrix.</p>
<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&rsquo;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>
<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>
        <p>File: <code>2-matrix_divided.py, tests/2-matrix_divided.txt</code></p>
  <h3>
    2. Say my name
  </h3>
  <p>Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>
<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>
<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>
        <p>File: <code>3-say_my_name.py, tests/3-say_my_name.txt</code></p>
  <h3>
    3. Print square
  </h3>
  <p>Write a function that prints a square with the character <code>#</code>.</p>
<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>4-print_square.py, tests/4-print_square.txt</code></p>
  <h3>
    4. Text indentation
  </h3>
  <p>Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>
<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>5-text_indentation.py, tests/5-text_indentation.txt</code></p>
  <h3>
    5. Max integer - Unittest
  </h3>
  <p>Since the beginning you have been creating &ldquo;Interactive tests&rdquo;. For this exercise, you will add Unittests.</p>
<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>
<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the unittest module </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
<li>All tests you make must be passable by the function below</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>
        <p>File: <code>tests/6-max_integer_test.py</code></p>
  <h3>
    6. Matrix multiplication
  </h3>
  <p>Write a function that multiplies 2 matrices:</p>
<ul>
<li><p>Read: Matrix multiplication - only Matrix product (two matrices)</p></li>
<li><p>Prototype: <code>def matrix_mul(m_a, m_b):</code></p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be validated with these requirements in this order</p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be an list of lists of integers or floats:</p>
<ul>
<li>if <code>m_a</code> or <code>m_b</code> is not a list: raise a <code>TypeError</code> exception with the message <code>m_a must be a list</code> or <code>m_b must be a list</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a list of lists: raise a <code>TypeError</code> exception with the message <code>m_a must be a list of lists</code> or <code>m_b must be a list of lists</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is empty (it means: <code>= []</code> or <code>= [[]]</code>): raise a <code>ValueError</code> exception with the message <code>m_a can&#39;t be empty</code> or <code>m_b can&#39;t be empty</code></li>
<li>if one element of those list of lists is not an integer or a float: raise a <code>TypeError</code> exception with the message <code>m_a should contain only integers or floats</code> or <code>m_b should contain only integers or floats</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a rectangle (all &lsquo;rows&rsquo; should be of the same size): raise a <code>TypeError</code> exception with the message <code>each row of m_a must should be of the same size</code> or <code>each row of m_b must should be of the same size</code></li>
</ul></li>
<li><p>If <code>m_a</code> and <code>m_b</code> can&rsquo;t be multiplied: raise a <code>ValueError</code> exception with the message <code>m_a and m_b can&#39;t be multiplied</code></p></li>
<li><p>You are not allowed to import any module</p></li>
</ul>
        <p>File: <code>100-matrix_mul.py, tests/100-matrix_mul.txt</code></p>
  <h3>
    7. Lazy matrix multiplication
  </h3>
  <p>Write a function that multiplies 2 matrices by using the module NumPy</p>
<p>To install it: <code>pip3 install numpy</code></p>
<ul>
<li>Prototype: <code>def lazy_matrix_mul(m_a, m_b):</code></li>
<li>Test cases should be the same as <code>100-matrix_mul</code> but with new exception type/message</li>
</ul>
        <p>File: <code>101-lazy_matrix_mul.py, tests/101-lazy_matrix_mul.txt</code></p>
  <h3>
    8. CPython #3: Python Strings
  </h3>
<p>Create a function that prints Python strings.</p>
<ul>
<li>Prototype: <code>void print_python_string(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid string, print an error message (see example)</li>
<li>Read: Unicode HOWTO</li>
</ul>
<p>About:</p>
<ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c</code></li>
</ul>
        <p>File: <code>102-python.c</code></p>
