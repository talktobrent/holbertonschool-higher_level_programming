<h1>0x05. Python - Exceptions</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What&rsquo;s the difference between errors and exceptions</li>
<li>What are exceptions and how to use them</li>
<li>When do we need to use exceptions</li>
<li>How to correctly handle an exception</li>
<li>What&rsquo;s the purpose of catching exceptions</li>
<li>How to raise a builtin exception</li>
<li>When do we need to implement a clean-up action after an exception</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Safe list printing
  </h3>
  <p>Write a function that prints <code>x</code> elements of a list.</p>
<ul>
<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>
        <p>File: <code>0-safe_print_list.py</code></p>
  <h3>
    1. Safe printing of an integers list
  </h3>
  <p>Write a function that prints an integer with <code>&quot;{:d}&quot;.format()</code>.</p>
<ul>
<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>
        <p>File: <code>1-safe_print_integer.py</code></p>
  <h3>
    2. Print and count integers
  </h3>
  <p>Write a function that prints the first <code>x</code> elements of a list and only integers.</p>
<ul>
<li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).</li>
<li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
<li><code>x</code> can be bigger than the length of <code>my_list</code> - if it&rsquo;s the case, an exception will occurred </li>
<li>Returns the real number of integers printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print an integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>
        <p>File: <code>2-safe_print_list_integers.py</code></p>
  <h3>
    3. Integers division with debug
  </h3>
  <p>Write a function that divides 2 integers and prints the result.</p>
<ul>
<li>Prototype: <code>def safe_print_division(a, b):</code></li>
<li>You can assume that <code>a</code> and <code>b</code> are integers</li>
<li>The result of the division should print on the <code>finally:</code> section preceded by <code>Inside result:</code></li>
<li>Returns the value of the division, otherwise: <code>None</code></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You have to use <code>&quot;{}&quot;.format()</code> to print the result</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>3-safe_print_division.py</code></p>
  <h3>
    4. Divide a list
  </h3>
  <p>Write a function that divides element by element 2 lists.</p>
<ul>
<li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
<li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
<li><code>list_length</code> can be bigger than the length of both lists</li>
<li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
<li>If 2 elements can&rsquo;t be divided, the division result should be equal to <code>0</code></li>
<li>If an element is not an integer or float:
<ul>
<li>print: <code>wrong type</code></li>
</ul></li>
<li>If the division can&rsquo;t be done (<code>/0</code>):
<ul>
<li>print: <code>division by 0</code></li>
</ul></li>
<li>If <code>my_list_1</code> or <code>my_list_2</code> is too short
<ul>
<li>print: <code>out of range</code></li>
</ul></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>4-list_division.py</code></p>
  <h3>
    5. Raise exception
  </h3>
  <p>Write a function that raises a type exception.</p>
<ul>
<li>Prototype: <code>def raise_exception():</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>5-raise_exception.py</code></p>
  <h3>
    6. Raise a message
  </h3>
  <p>Write a function that raises a name exception with a message.</p>
<ul>
<li>Prototype: <code>def raise_exception_msg(message=&quot;&quot;):</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>6-raise_exception_msg.py</code></p>
  <h3>
    7. Safe integer print with error message
  </h3>
  <p>Write a function that prints an integer.</p>
<ul>
<li>Prototype: <code>def safe_print_integer_err(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code> and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print as integer</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>
        <p>File: <code>100-safe_print_integer_err.py</code></p>
  <h3>
    8. Safe function
  </h3>
  <p>Write a function that executes a function safely.  </p>
<ul>
<li>Prototype: <code>def safe_function(fct, *args):</code></li>
<li>You can assume <code>fct</code> will be always a pointer to a function</li>
<li>Returns the result of the function,</li>
<li>Otherwise, returns <code>None</code> if something happens during the function and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
</ul>
        <p>File: <code>101-safe_function.py</code></p>
  <h3>
    9. ByteCode -&gt; Python #4
  </h3>
  <p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>
<ul>
</ul>
        <p>File: <code>102-magic_calculation.py</code></p>
  <h3>
    10. CPython #2: PyFloatObject
  </h3>
  <p>Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
Python lists:</p>
<ul>
<li>Prototype: <code>void print_python_list(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid <code>PyListObject</code>, print an error message (see example)</li>
</ul>
<p>Python bytes:</p>
<ul>
<li>Prototype: <code>void print_python_bytes(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Line &ldquo;first X bytes&rdquo;: print a maximum of 10 bytes</li>
<li>If <code>p</code> is not a valid <code>PyBytesObject</code>, print an error message (see example)</li>
</ul>
<p>Python float:</p>
<ul>
<li>Prototype: <code>void print_python_float(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid <code>PyFloatObject</code>, print an error message (see example)</li>
<li>Read <code>/usr/include/python3.4/floatobject.h</code></li>
</ul>
<p>About:</p>
<ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c</code></li>
<li>You are not allowed to use the following macros/functions:
<ul>
<li><code>Py_SIZE</code></li>
<li><code>Py_TYPE</code></li>
<li><code>PyList_Size</code></li>
<li><code>PyList_GetItem</code></li>
<li><code>PyBytes_AS_STRING</code></li>
<li><code>PyBytes_GET_SIZE</code></li>
<li><code>PyBytes_AsString</code></li>
<li><code>PyFloat_AS_DOUBLE</code></li>
<li><code>PySequence_GetItem</code></li>
<li><code>PySequence_Fast_GET_SIZE</code></li>
<li><code>PySequence_Fast_GET_ITEM</code></li>
<li><code>PySequence_ITEM</code></li>
<li><code>PySequence_Fast_ITEMS</code></li>
</ul></li>
</ul>
<p><strong>NOTE</strong>:</p>
<ul>
<li>The python script will be launched using the <code>-u</code> option (Force <code>stdout</code> to be unbuffered).</li>
<li>It is <strong>strongly</strong> advised to either use <code>setbuf(stdout, NULL);</code> or <code>fflush(stdout)</code> in your C functions IF you choose to use <code>printf</code>. The reason to that is that Python<code>s</code>print<code>and libC</code>s <code>printf</code> don&rsquo;t share the same buffer, and the output can appear disordered.</li>
</ul>
        <p>File: <code>103-python.c</code></p>
