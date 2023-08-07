
![AirBnB clone](https://github.com/l11EG4/AirBnB_clone/assets/79404170/499889ce-bc50-4369-828b-07838d6733fd.png)

<h1 align="center"> AirBnB Clone Project README</h1>

  <h2>Project Name: AirBnB_clone</h2>

   <h2>Team Members:</h2>
    <ul>
        <li>Laila Tabourit</li>
        <li>Zakaria Berahmi</li>
    </ul>

  <h2>Project Description:</h2>
    <p>Welcome to the AirBnB clone project! This project is the first step towards building a full web application: the AirBnB clone. The goal of this step is to create a command interpreter to manage AirBnB objects and lay the foundation for future development. By completing this step, you will be able to put in place a parent class (BaseModel) for initializing, serializing, and deserializing instances. You'll also create various classes such as User, State, City, and Place, which will inherit from BaseModel. Additionally, you'll implement a simple flow of serialization/deserialization for instances, dictionaries, JSON strings, and files. Finally, you'll develop the first abstracted storage engine of the project, the File storage, and create unit tests to validate all classes and the storage engine.</p>

   <h2>Command Interpreter Description:</h2>
    <p>The command interpreter in this project is similar to a shell but limited to managing the objects of the AirBnB project. With the command interpreter, you can perform the following actions:</p>
    <ol>
        <li>Create a new object (e.g., a new User or a new Place).</li>
        <li>Retrieve an object from a file, a database, etc.</li>
        <li>Perform operations on objects (e.g., count, compute stats, etc.).</li>
        <li>Update attributes of an object.</li>
        <li>Destroy an object.</li>
    </ol>

   <h2>How to Start the Command Interpreter:</h2>
    <p>To start the command interpreter, follow these steps:</p>
    <ol>
        <li>Clone the repository: <code>$ git clone https://github.com/yourusername/AirBnB_clone.git</code></li>
        <li>Change directory to the project folder: <code>$ cd AirBnB_clone</code></li>
        <li>Run the command interpreter: <code>$ ./console.py</code></li>
    </ol>

  <h2>How to Use the Command Interpreter:</h2>
    <p>Once the command interpreter is running, you can start interacting with it. The prompt will be displayed as follows:</p>
    <pre><code>(hbnb) </code></pre>
    <p>You can now enter commands to manage the AirBnB objects. The available commands include:</p>
    <ul>
        <li><code>create</code>: Create a new instance of an object (e.g., <code>create User</code>).</li>
        <li><code>show</code>: Display information about a specific object (e.g., <code>show User 1234-5678-9012</code>).</li>
        <li><code>all</code>: Display information about all objects or all instances of a specific class (e.g., <code>all</code> or <code>all User</code>).</li>
        <li><code>update</code>: Update attributes of an object (e.g., <code>update User 1234-5678-9012 email "example@example.com"</code>).</li>
        <li><code>destroy</code>: Destroy an object (e.g., <code>destroy User 1234-5678-9012</code>).</li>
        <li><code>quit</code>: Exit the command interpreter.</li>
    </ul>

  <h2>Resources:</h2>
    <ul>
        <li><a href="https://docs.python.org/3/library/cmd.html">cmd module</a></li>
        <li><a href="https://pymotw.com/3/cmd/">cmd module in-depth</a></li>
        <li><a href="https://packaging.python.org/guides/distributing-packages-using-setuptools/">Packages concept page</a></li>
        <li><a href="https://docs.python.org/3/library/uuid.html">uuid module</a></li>
        <li><a href="https://docs.python.org/3/library/datetime.html">datetime</a></li>
        <li><a href="https://docs.python.org/3/library/unittest.html">unittest module</a></li>
        <li><a href="https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments">args/kwargs</a></li>
        <li><a href="https://www.pythonsheets.com/notes/python-tests.html">Python test cheatsheet</a></li>
        <li><a href="https://en.wikipedia.org/wiki/Cmd.exe">cmd module wiki page</a></li>
        <li><a href="https://docs.python.org/3/library/unittest.html">Python unittest</a></li>
    </ul>

  <p>We wish you the best of luck with the AirBnB clone project! If you have any questions or need assistance, feel free to reach out to the team members mentioned above. Happy coding! 🚀</p>
<h2>License</h2>
  <p>&copy; 2023 Laila Tabourit & Zakaria Berahmi</p>
  <p>This repository is open-source and licensed under the <a href="LICENSE">MIT License</a>. Feel free to use,
        modify, and distribute the code examples and explanations for educational or personal use. However, please refer
        to the License file for more details on the permissions and restrictions.</p>
