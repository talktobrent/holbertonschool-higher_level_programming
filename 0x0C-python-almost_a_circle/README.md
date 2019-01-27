<h1>0x0C. Python - Almost a circle</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. If it&#39;s not tested it doesn&#39;t work
  </h3>
  <p>All your files, classes and methods must be unit tested and be PEP 8 validated. </p>
<p><em>Note that this is just an example. The number of tests you create can be different from the above example.</em></p>
        <p>File: <code>tests/</code></p>
  <h3>
    1. Base class
  </h3>
  <p>Write the first class <code>Base</code>:</p>
<p>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python module</p>
<p>Create a file named <code>models/base.py</code>:</p>
<ul>
<li>Class <code>Base</code>:
<ul>
<li>private class attribute <code>__nb_objects = 0</code></li>
<li>class constructor: <code>def __init__(self, id=None):</code>:
<ul>
<li>if <code>id</code> is not <code>None</code>, assign the public instance attribute <code>id</code> to this argument value</li>
<li>otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
</ul></li>
</ul></li>
</ul>
<p>This class will be the &ldquo;base&rdquo; of all other classes in this project. The goal of it is to manage <code>id</code> attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)</p>
        <p>File: <code>models/base.py, models/__init__.py</code></p>
  <h3>
    2. First Rectangle
  </h3>
  <p>Write the class <code>Rectangle</code> that inherits from <code>Base</code>:</p>
<ul>
<li>In the file <code>models/rectangle.py</code></li>
<li>Class <code>Rectangle</code> inherits from <code>Base</code></li>
<li>Private instance attributes, each with its own public getter and setter:
<ul>
<li><code>__width</code> -&gt; <code>width</code></li>
<li><code>__height</code> -&gt; <code>height</code></li>
<li><code>__x</code> -&gt; <code>x</code></li>
<li><code>__y</code> -&gt; <code>y</code></li>
</ul></li>
<li>Class constructor: <code>def __init__(self, width, height, x=0, y=0, id=None)</code>:
<ul>
<li>Call the super class with <code>id</code> - this super call with use the logic of the <code>__init__</code> of the <code>Base</code> class</li>
<li>Assign each argument <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> to the right attribute</li>
</ul></li>
</ul>
<p>Why private attributes with getter/setter? Why not directly public attribute?</p>
<p>Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can &ldquo;trust&rdquo; these attributes.</p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    3. Validate attributes
  </h3>
  <p>Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded):</p>
<ul>
<li>If the input is not an integer, raise the <code>TypeError</code> exception with the message: <code>&lt;name of the attribute&gt; must be an integer</code>. Example: <code>width must be an integer</code></li>
<li>If <code>width</code> or <code>height</code> is under or equals 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt; 0</code>. Example: <code>width must be &gt; 0</code></li>
<li>If <code>x</code> or <code>y</code> is under 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt;= 0</code>. Example: <code>x must be &gt;= 0</code></li>
</ul>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    4. Area first
  </h3>
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def area(self):</code> that returns the area value of the <code>Rectangle</code> instance.</p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    5. Display #0
  </h3>
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def display(self):</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don&rsquo;t need to handle <code>x</code> and <code>y</code> here.</p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    6. __str__
  </h3>
  <p>Update the class <code>Rectangle</code> by overriding the <code>__str__</code> method so that it returns <code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;width&gt;/&lt;height&gt;</code></p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    7. Display #1
  </h3>
  <p>Update the class <code>Rectangle</code> by improving the public method <code>def display(self):</code> to print in stdout the <code>Rectangle</code> instance with the character <code>#</code> by taking care of <code>x</code> and <code>y</code></p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    8. Update #0
  </h3>
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args):</code> that assigns an argument to each attribute:</p>
<ul>
<li>1st argument should be the <code>id</code> attribute</li>
<li>2nd argument should be the <code>width</code> attribute</li>
<li>3rd argument should be the <code>height</code> attribute</li>
<li>4th argument should be the <code>x</code> attribute</li>
<li>5th argument should be the <code>y</code> attribute</li>
</ul>
<p>This type of argument is called a &ldquo;no-keyword argument&rdquo; - Argument order is super important.</p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    9. Update #1
  </h3>
  <p>Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args):</code> by changing the prototype to <code>update(self, *args, **kwargs)</code> that assigns a key/value argument to attributes:</p>
<ul>
<li><code>**kwargs</code> is a double pointer to a dictionary: key/value</li>
<li><code>**kwargs</code> must be skipped if <code>*args</code> exists and is not empty</li>
<li>Each key in this dictionary represents an attribute to the instance</li>
</ul>
<p>This type of argument is called a &ldquo;key-worded argument&rdquo;. Argument order is not important.</p>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    10. And now, the Square!
  </h3>
  <p>Write the class <code>Square</code> that inherits from <code>Rectangle</code>:</p>
<ul>
<li>In the file <code>models/square.py</code></li>
<li>Class <code>Square</code> inherits from <code>Rectangle</code></li>
<li>Class constructor: <code>def __init__(self, size, x=0, y=0, id=None):</code>:
<ul>
<li>Call the super class with <code>id</code>, <code>x</code>, <code>y</code>, <code>width</code> and <code>height</code> - this super call will use the logic of the <code>__init__</code> of the <code>Rectangle</code> class. The <code>width</code> and <code>height</code> must be assigned to the value of <code>size</code></li>
<li>You must not create new attributes for this class, use all attributes of <code>Rectangle</code> - As reminder: a Square is a Rectangle with the same width and height</li>
<li>All <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> validation must inherit from <code>Rectangle</code> - same behavior in case of wrong data</li>
</ul></li>
<li>The overloading <code>__str__</code> method should return <code>[Square] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;size&gt;</code> - in our case, <code>width</code> or <code>height</code></li>
</ul>
<p>As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.</p>
        <p>File: <code>models/square.py</code></p>
  <h3>
    11. Square size
  </h3>
  <p>Update the class <code>Square</code> by adding the public getter and setter <code>size</code></p>
<ul>
<li>The setter should assign (in this order) the <code>width</code> and the <code>height</code> - with the same value</li>
<li>The setter should have the same value validation as the <code>Rectangle</code> for <code>width</code> and <code>height</code> - No need to change the exception error message (It should be the one from <code>width</code>)</li>
</ul>
        <p>File: <code>models/square.py</code></p>
  <h3>
    12. Square update
  </h3>
  <p>Update the class <code>Square</code> by adding the public method <code>def update(self, *args, **kwargs)</code> that assigns attributes:</p>
<ul>
<li><code>*args</code> is the list of arguments - no-keyworded arguments
<ul>
<li>1st argument should be the <code>id</code> attribute</li>
<li>2nd argument should be the <code>size</code> attribute</li>
<li>3rd argument should be the <code>x</code> attribute</li>
<li>4th argument should be the <code>y</code> attribute</li>
</ul></li>
<li><code>**kwargs</code> is a double pointer to a dictionary: key/value (keyworded arguments)</li>
<li><code>**kwargs</code> must be skipped if *args exists and is not empty</li>
<li>Each key in this dictionary represents an attribute to the instance</li>
</ul>
        <p>File: <code>models/square.py</code></p>
  <h3>
    13. Rectangle instance to dictionary representation
  </h3>
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def to_dictionary(self):</code> that returns the dictionary representation of a <code>Rectangle</code>:</p>
<p>This dictionary must contain:</p>
<ul>
<li><code>id</code></li>
<li><code>width</code></li>
<li><code>height</code></li>
<li><code>x</code></li>
<li><code>y</code></li>
</ul>
        <p>File: <code>models/rectangle.py</code></p>
  <h3>
    14. Square instance to dictionary representation
  </h3>
  <p>Update the class <code>Square</code> by adding the public method <code>def to_dictionary(self):</code> that returns the dictionary representation of a <code>Square</code>:</p>
<p>This dictionary must contain:</p>
<ul>
<li><code>id</code></li>
<li><code>size</code></li>
<li><code>x</code></li>
<li><code>y</code></li>
</ul>
        <p>File: <code>models/square.py</code></p>
  <h3>
    15. Dictionary to JSON string
  </h3>
  <p>JSON is one of the standard formats for sharing data representation.</p>
<p>Update the class <code>Base</code> by adding the static method <code>def to_json_string(list_dictionaries):</code> that returns the JSON string representation of <code>list_dictionaries</code>:</p>
<ul>
<li><code>list_dictionaries</code> is a list of dictionaries</li>
<li>If <code>list_dictionaries</code> is <code>None</code> or empty, return the string: <code>&quot;[]&quot;</code></li>
<li>Otherwise, return the JSON string representation of <code>list_dictionaries</code></li>
</ul>
        <p>File: <code>models/base.py</code></p>
  <h3>
    16. JSON string to file
  </h3>
  <p>Update the class <code>Base</code> by adding the class method <code>def save_to_file(cls, list_objs):</code> that writes the JSON string representation of <code>list_objs</code> to a file:</p>
<ul>
<li><code>list_objs</code> is a list of instances who inherits of <code>Base</code> - example: list of <code>Rectangle</code> or list of <code>Square</code> instances</li>
<li>If <code>list_objs</code> is <code>None</code>, save an empty list</li>
<li>The filename must be: <code>&lt;Class name&gt;.json</code> - example: <code>Rectangle.json</code></li>
<li>You must use the static method <code>to_json_string</code> (created before)</li>
<li>You must overwrite the file if it already exists</li>
</ul>
        <p>File: <code>models/base.py</code></p>
  <h3>
    17. JSON string to dictionary
  </h3>
  <p>Update the class <code>Base</code> by adding the static method <code>def from_json_string(json_string):</code> that returns the list of the JSON string representation <code>json_string</code>:</p>
<ul>
<li><code>json_string</code> is a string representing a list of dictionaries</li>
<li>If <code>json_string</code> is <code>None</code> or empty, return an empty list</li>
<li>Otherwise, return the list represented by <code>json_string</code></li>
</ul>
        <p>File: <code>models/base.py</code></p>
  <h3>
    18. Dictionary to Instance
  </h3>
  <p>Update the class <code>Base</code> by adding the class method <code>def create(cls, **dictionary):</code> that returns an instance with all attributes already set:</p>
<ul>
<li><code>**dictionary</code> is a double pointer to a dictionary</li>
<li>To use the <code>update</code> method to assign all attributes, you must create a &ldquo;dummy&rdquo; instance before: 
<ul>
<li>Create a <code>Rectangle</code> or <code>Square</code> instance with &ldquo;dummy&rdquo; mandatory attributes (width, height, size, etc.)</li>
<li>Call <code>update</code> instance method to this &ldquo;dummy&rdquo; instance to apply your real values</li>
</ul></li>
<li>You must use the method <code>def update(self, *args, **kwargs)</code></li>
<li><code>**dictionary</code> must be used as <code>**kwargs</code> of the method <code>update</code></li>
<li>You are not allowed to use <code>eval</code></li>
</ul>
        <p>File: <code>models/base.py</code></p>
  <h3>
    19. File to instances
  </h3>
  <p>Update the class <code>Base</code> by adding the class method <code>def load_from_file(cls):</code> that returns a list of instances:</p>
<ul>
<li>The filename must be: <code>&lt;Class name&gt;.json</code> - example: <code>Rectangle.json</code></li>
<li>If the file doesn&rsquo;t exist, return an empty list</li>
<li>Otherwise, return a list of instances - the type of these instances depends on <code>cls</code> (current class using this method)</li>
<li>You must use the <code>from_json_string</code> and <code>create</code> methods (implemented previously) </li>
</ul>
        <p>File: <code>models/base.py</code></p>
  <h3>
    20. JSON ok, but CSV?
  </h3>
  <p>Update the class <code>Base</code> by adding the class methods <code>def save_to_file_csv(cls, list_objs):</code> and <code>def load_from_file_csv(cls):</code> that serializes and deserializes in CSV:</p>
<ul>
<li>The filename must be: <code>&lt;Class name&gt;.csv</code> - example: <code>Rectangle.csv</code></li>
<li>Has the same behavior as the JSON serialization/deserialization</li>
<li>Format of the CSV:
<ul>
<li>Rectangle: <code>&lt;id&gt;,&lt;width&gt;,&lt;height&gt;,&lt;x&gt;,&lt;y&gt;</code></li>
<li>Square: <code>&lt;id&gt;,&lt;size&gt;,&lt;x&gt;,&lt;y&gt;</code></li>
</ul></li>
</ul>
        <p>File: <code>models/</code></p>
  <h3>
    21. Let&#39;s draw it
  </h3>
  <p>Update the class <code>Base</code> by adding the static method <code>def draw(list_rectangles, list_squares):</code> that opens a window and draws all the <code>Rectangles</code> and <code>Squares</code>:</p>
<ul>
<li>You must use the Turtle graphics module</li>
<li>To install it: <code>sudo apt-get install python3-tk</code></li>
<li>To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: <code>config.ssh.forward_x11 = true</code></li>
<li>No constraints for color, shape etc&hellip; be creative!</li>
</ul>
<p>Please find here Cohort 3 - San Francisco&rsquo;s Andrew Birnberg&rsquo;s tips to make Turtle working with Vagrant</p>
<ul>
<li>Uncommented line in <code>/etc/ssh/ssh_config</code> that said <code>#    ForwardX11 no</code> and change <code>no</code> to <code>yes</code>. </li>
<li>Then added line <code>config.ssh.forward_agent = true</code> to my Vagrantfile in addition to <code>config.ssh.forward_x11 = true</code>. </li>
<li>Halted my vm with <code>vagrant halt</code> and started it back up with <code>vagrant up --provision</code> then <code>vagrant ssh</code>. </li>
<li>If you get an error that looks like <code>/usr/bin/xauth:  timeout in locking authority file /home/vagrant/.Xauthority</code>, then enter <code>rm .Xauthority</code> (you may have to <code>sudo</code>). </li>
<li>Logout and restart the vm with <code>vagrant up --provision</code>. </li>
<li>Test with <code>xeyes</code>. If Xquartz is installed on the Mac OS it should open in an Xquartz window.</li>
</ul>
        <p>File: <code>models/base.py</code></p>
