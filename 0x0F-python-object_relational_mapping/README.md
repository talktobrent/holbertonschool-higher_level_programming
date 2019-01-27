<h1>0x0F. Python - Object-relational mapping</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Get all states
  </h3>
  <p>Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>: </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>0-select_states.py</code></p>
  <h3>
    1. Filter states
  </h3>
  <p>Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>: </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>1-filter_states.py</code></p>
  <h3>
    2. Filter states by user input
  </h3>
  <p>Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.</p>
<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use <code>format</code> to create the SQL query with the user input</li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>2-my_filter_states.py</code></p>
  <h3>
    3. SQL Injection...
  </h3>
  <p>Wait, do you remember the previous task? Did you test <code>&quot;Arizona&#39;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &#39;&quot;</code> as an input?</p>
<p>What? Empty?</p>
<p>Yes, it&rsquo;s an SQL injection to delete all records of a table&hellip;</p>
<p>Once again, write a script that takes in arguments and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!</p>
<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (safe from MySQL injection)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>3-my_safe_filter_states.py</code></p>
  <h3>
    4. Cities by states
  </h3>
  <p>Write a script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>4-cities_by_state.py</code></p>
  <h3>
    5. All cities by state
  </h3>
  <p>Write a script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code> </p>
<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name</code> (SQL injection free!)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>5-filter_cities.py</code></p>
  <h3>
    6. First state model
  </h3>
<p>Write a python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>:</p>
<ul>
<li><code>State</code> class:
<ul>
<li>inherits from <code>Base</code>  Tips</li>
<li>links to the MySQL table <code>states</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string with maximum 128 characters and can&rsquo;t be null</li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li><strong>WARNING:</strong> all classes who inherit from <code>Base</code> <strong>must</strong> be imported before calling <code>Base.metadata.create_all(engine)</code></li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>model_state.py</code></p>
  <h3>
    7. All states via SQLAlchemy
  </h3>
  <p>Write a script that lists all <code>State</code> objects from the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>7-model_state_fetch_all.py</code></p>
  <h3>
    8. First state
  </h3>
  <p>Write a script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>The state you display must be the first in <code>states.id</code></li>
<li>You are not allowed to fetch all states from the database before displaying the result</li>
<li>The results must be displayed as they are in the example below</li>
<li>If the table <code>states</code> is empty, print <code>Nothing</code> followed by a new line</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>8-model_state_fetch_first.py</code></p>
  <h3>
    9. Contains `a`
  </h3>
  <p>Write a script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>9-model_state_filter_a.py</code></p>
  <h3>
    10. Get a state
  </h3>
  <p>Write a script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name to search</code> (SQL injection free)</li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You can assume you have one record with the state name to search</li>
<li>Results must display the <code>states.id</code></li>
<li>If no state has the name you searched for, display <code>Not found</code></li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>10-model_state_my_get.py</code></p>
  <h3>
    11. Add a new state
  </h3>
  <p>Write a script that adds the <code>State</code> object &ldquo;Louisiana&rdquo; to the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Print the new <code>states.id</code> after creation</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>11-model_state_insert.py</code></p>
  <h3>
    12. Update a state
  </h3>
  <p>Write a script that changes the name of a <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Change the name of the <code>State</code> where <code>id = 2</code> to <code>New Mexico</code></li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>12-model_state_update_id_2.py</code></p>
  <h3>
    13. Delete states
  </h3>
  <p>Write a script that deletes all <code>State</code> objects with a name containing the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>13-model_state_delete_a.py</code></p>
  <h3>
    14. Cities in state
  </h3>
  <p>Write a Python file similar to <code>model_state.py</code> named <code>model_city.py</code> that contains the class definition of a <code>City</code>.</p>
<ul>
<li><code>City</code> class:
<ul>
<li>inherits from <code>Base</code> (imported from <code>model_state</code>)</li>
<li>links to the MySQL table <code>cities</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string of 128 characters and can&rsquo;t be null</li>
<li>class attribute <code>state_id</code> that represents a column of an integer, can&rsquo;t be null and is a foreign key to <code>states.id</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul>
<p>Next, write a script <code>14-model_city_fetch_by_state.py</code> that prints all <code>City</code> objects from the database <code>hbtn_0e_14_usa</code>: </p>
<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be display as they are in the example below (<code>&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;</code>)</li>
<li>Your code should not be executed when imported</li>
</ul>
<p><strong>No test cases needed</strong></p>
        <p>File: <code>model_city.py, 14-model_city_fetch_by_state.py</code></p>
