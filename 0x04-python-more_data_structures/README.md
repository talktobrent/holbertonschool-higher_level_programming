<h1>0x04. Python - More Data Structures: Set, Dictionary</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>What are set and how to use them</li>
<li>What are the most common methods of set and how to use them</li>
<li>When to use sets versus lists</li>
<li>How to iterate into a set</li>
<li>What are dictionary and how to use them</li>
<li>When to use dictionaries versus lists or sets</li>
<li>What is a key in a dictionary</li>
<li>How to iterate into a dictionary</li>
<li>What is a lambda function</li>
<li>What is map, reduce and map functions</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Squared simple
  </h3>
  <p>Write a function that computes the square value of all integers of a matrix.</p>
<ul>
<li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:
<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You are allowed to use regular loops, <code>map</code>, etc.</li>
</ul>
        <p>File: <code>0-square_matrix_simple.py</code></p>
  <h3>
    1. Search and replace
  </h3>
  <p>Write a function that replaces all occurrences of an element by another in a new list.</p>
<ul>
<li>Prototype: <code>def search_replace(my_list, search, replace):</code></li>
<li><code>my_list</code> is the initial list</li>
<li><code>search</code> is the element to replace in the list</li>
<li><code>replace</code> is the new element</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>1-search_replace.py</code></p>
  <h3>
    2. Unique addition
  </h3>
  <p>Write a function that adds all unique integers in a list (only once for each integer).</p>
<ul>
<li>Prototype: <code>def uniq_add(my_list=[]):</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>2-uniq_add.py</code></p>
  <h3>
    3. Present in both
  </h3>
  <p>Write a function that returns a set of common elements in two sets.</p>
<ul>
<li>Prototype: <code>def common_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>3-common_elements.py</code></p>
  <h3>
    4. Only differents
  </h3>
  <p>Write a function that returns a set of all elements present in only one set.</p>
<ul>
<li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>4-only_diff_elements.py</code></p>
  <h3>
    5. Number of keys
  </h3>
  <p>Write a function that returns the number of keys in a dictionary.</p>
<ul>
<li>Prototype: <code>def number_keys(a_dictionary):</code></li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>5-number_keys.py</code></p>
  <h3>
    6. Print sorted dictionary
  </h3>
  <p>Write a function that prints a dictionary by ordered keys.</p>
<ul>
<li>Prototype: <code>def print_sorted_dictionary(a_dictionary):</code></li>
<li>You can assume that all keys are strings</li>
<li>Keys should be sorted by alphabetic order</li>
<li>Only sort keys of the first level (don&rsquo;t sort keys of a dictionary inside the main dictionary)</li>
<li>Dictionary values can have any type</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>6-print_sorted_dictionary.py</code></p>
  <h3>
    7. Update dictionary
  </h3>
  <p>Write a function that replaces or adds key/value in a dictionary.</p>
<ul>
<li>Prototype: <code>def update_dictionary(a_dictionary, key, value):</code></li>
<li><code>key</code> argument will be always a string</li>
<li><code>value</code> argument will be any type</li>
<li>If a key exists in the dictionary, the value will be replaced</li>
<li>If a key doesn&rsquo;t exist in the dictionary, it will be created</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>7-update_dictionary.py</code></p>
  <h3>
    8. Simple delete by key
  </h3>
  <p>Write a function that deletes a key in a dictionary.</p>
<ul>
<li>Prototype: <code>def simple_delete(a_dictionary, key=&quot;&quot;):</code></li>
<li><code>key</code> argument will be always a string</li>
<li>If a key doesn&rsquo;t exist, the dictionary won&rsquo;t change</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>8-simple_delete.py</code></p>
  <h3>
    9. Multiply by 2
  </h3>
  <p>Write a function that returns a new dictionary with all values multiplied by 2</p>
<ul>
<li>Prototype: <code>def multiply_by_2(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>Returns a new dictionary</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>9-multiply_by_2.py</code></p>
  <h3>
    10. Best score
  </h3>
  <p>Write a function that returns a key with the biggest integer value.</p>
<ul>
<li>Prototype: <code>def best_score(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>If no score found, return <code>None</code></li>
<li>You can assume all students have a different score</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>10-best_score.py</code></p>
  <h3>
    11. Multiply by using map
  </h3>
  <p>Write a function that returns a list with all values multiplied by a number without using any loops.</p>
<ul>
<li>Prototype: <code>def mutiply_list_map(my_list=[], number=0):</code></li>
<li>Returns a new list:
<ul>
<li>Same length as <code>my_list</code></li>
<li>Each value should be multiplied by <code>number</code></li>
</ul></li>
<li>Initial list should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>Your file should be max 3 lines</li>
</ul>
        <p>File: <code>11-mutiply_list_map.py</code></p>
  <h3>
    12. Roman to Integer
  </h3>
  <p><strong>Technical interview preparation</strong>: </p>
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>
<p>Create a function <code>def roman_to_int(roman_string):</code> that converts a Roman numeral to an integer.</p>
<ul>
<li>You can assume the number will be between 1 to 3999.</li>
<li><code>def roman_to_int(roman_string)</code> must return an integer</li>
<li>If the <code>roman_string</code> is not a string or <code>None</code>, return 0</li>
</ul>
        <p>File: <code>12-roman_to_int.py</code></p>
  <h3>
    13. Weighted average!
  </h3>
  <p>Write a function that returns the weighted average of all integers tuple <code>(&lt;score&gt;, &lt;weight&gt;)</code></p>
<ul>
<li>Prototype: <code>def weight_average(my_list=[]):</code></li>
<li>Returns <code>0</code> if the list is empty</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>100-weight_average.py</code></p>
  <h3>
    14. Squared by using map
  </h3>
  <p>Write a function that computes the square value of all integers of a matrix using <code>map</code></p>
<ul>
<li>Prototype: <code>def square_matrix_map(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:
<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>You are not allowed to use <code>for</code> or <code>while</code></li>
<li>Your file should be max 3 lines</li>
</ul>
        <p>File: <code>101-square_matrix_map.py</code></p>
  <h3>
    15. Delete by value
  </h3>
  <p>Write a function that deletes keys with a specific value in a dictionary.</p>
<ul>
<li>Prototype: <code>def complex_delete(a_dictionary, value):</code></li>
<li>If the value doesn&rsquo;t exist, the dictionary won&rsquo;t change</li>
<li>All keys having the searched value have to be deleted</li>
<li>You are not allowed to import any module</li>
</ul>
        <p>File: <code>102-complex_delete.py</code></p>
  <h3>
    16. CPython #1: PyBytesObject
  </h3>
  <p>Create two C functions that print some basic info about Python lists and Python bytes objects.
Python lists:</p>
<ul>
<li>Prototype: <code>void print_python_list(PyObject *p);</code></li>
<li>Format: see example</li>
</ul>
<p>Python bytes:</p>
<ul>
<li>Prototype: <code>void print_python_bytes(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Line &ldquo;first X bytes&rdquo;: print a maximum of 10 bytes</li>
<li>If <code>p</code> is not a valid <code>PyBytesObject</code>, print an error message (see example)</li>
<li>Read <code>/usr/include/python3.4/bytesobject.h</code></li>
</ul>
<p>About:</p>
<ul>
<li>Python version: 3.4</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c</code></li>
<li>You are not allowed to use the following macros/functions:
<ul>
<li><code>Py_SIZE</code></li>
<li><code>Py_TYPE</code></li>
<li><code>PyList_GetItem</code></li>
<li><code>PyBytes_AS_STRING</code></li>
<li><code>PyBytes_GET_SIZE</code></li>
</ul></li>
</ul>
        <p>File: <code>103-python.c</code></p>
