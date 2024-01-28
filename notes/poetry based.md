To structure a project with multiple scripts and a developing package using Poetry, you can follow a modular approach. Here's a suggested structure:

1. *Create a New Poetry Project:*
   Start by creating a new Poetry project in your desired root directory. This will be the root of your project.

   bash
   poetry new your_project_name
   

   This will create the basic structure for a Poetry project.

2. *Separate Package Development:*
   Inside the project, create a directory for your package, let's call it `your_package`. Place the actual source code of your package inside this directory. Ensure that your package has a `pyproject.toml` file with the necessary metadata for building the package.


   your_project_name/
   ├── pyproject.toml
   ├── your_package/
   │   ├── __init__.py
   │   └── your_module.py
   └── your_project_name/
       └── __init__.py
   

3. *Develop Scripts:*
   Create another directory for your scripts, such as `scripts`. Each script can be in its own file within this directory.

   
   your_project_name/
   ├── pyproject.toml
   ├── your_package/
   │   ├── __init__.py
   │   └── your_module.py
   ├── scripts/
   │   └── script1.py
   │   └── script2.py
   └── your_project_name/
       └── __init__.py
   

4. *Handle Package Dependencies:*
   In the `pyproject.toml` file at the root level, add your package as a dependency. Ensure you use a relative path for local development.

   toml
   [tool.poetry.dependencies]
   python = "^3.8"
   your-package-name = { path = "your_package" }
   

   This setup allows you to make changes to your package code and test it locally within your project.

5. *Install Package for Development:*
   During development, install the package in editable mode:

   bash
   poetry install
   

   This will create a virtual environment and install your package in editable mode, allowing you to make changes to your package and see the effects without reinstalling it.

6. *Scripts in Development:*
   Your scripts in the `scripts` directory can then import and use the functionalities provided by your package.

7. *Distribution:*
   When you are ready to distribute your package, you can publish it to a package repository (e.g., PyPI) using the `poetry publish` command. This makes it pip installable.

   bash
   poetry publish --build
   

8. *Deploy Scripts:*
   Deploy your scripts to the desired location. You can use packaging tools like `pyinstaller` or `cx_Freeze` to create standalone executables if needed.

   bash
   pyinstaller script1.py
   

By following this structure, you can maintain a clean separation between your package development and script development. Additionally, your package remains installable both in local development and on servers using either Poetry or pip.

---

Yes, if your package requires additional files such as configuration JSON files, you can include them in the package and make sure they are accessible to your package code. Here's how you can handle it:

1. *Organize Files:*
   Place your configuration JSON files and any other necessary files within your package directory. For example:

   
   your_package/
   ├── __init__.py
   ├── your_module.py
   ├── config/
   │   ├── config1.json
   │   └── config2.json
   └── other_files/
       └── file1.txt
   

2. *Accessing Files in Package Code:*
   In your package code (`your_module.py` or other files), you can access these files using relative paths or package-relative paths.

   python
   import os

   config_path = os.path.join(os.path.dirname(__file__), 'config', 'config1.json')
   with open(config_path, 'r') as file:
       config_data = json.load(file)
   

   This allows your package code to access the configuration files and other necessary files when the package is installed.

3. *Including Files in Distribution:*
   Update your `pyproject.toml` file to include these files in the distribution. You can use the `package.include` section for this purpose.

   toml
   [tool.poetry]
   # ... other configuration ...

   [tool.poetry.package]
   include = ["your_package/config/*.json", "your_package/other_files/*.txt"]
   

   This ensures that these files are included when your package is built and distributed.

4. *Installation and Access in Scripts:*
   When your package is installed using Poetry or pip, these files will be included in the installed package. In your scripts, you can access these files using the appropriate paths relative to your package.

5. *Development Environment:*
   During development, when you use `poetry install` in editable mode, your package and its files will be available for testing within your project.

By following these steps, you can include additional files in your package and ensure that they are accessible both during development and when the package is installed on other systems.

---

Yes, the `poetry publish --build` command creates distribution packages, and it typically includes both source distributions (`.tar.gz` files) and wheel distributions (`.whl` files). These distribution packages contain the necessary files for your Python package to be installed by other users.

The wheel distribution format is a binary distribution format that is more efficient for installation compared to source distributions. It is a common practice to publish both source distributions and wheel distributions to accommodate a broader range of user environments.

When you run `poetry publish --build`, Poetry creates these distribution packages in the `dist` directory within your project. The directory structure might look like this:


your_project_name/
├── dist/
│   ├── your_package_name-1.0.0-py3-none-any.whl
│   └── your_package_name-1.0.0.tar.gz


Here, `your_package_name-1.0.0` represents the version number of your package. The `.whl` file is the wheel distribution, and the `.tar.gz` file is the source distribution.

The wheel distribution contains a binary distribution of your package, including compiled code, if applicable, along with any required files such as JSON configuration files or other package data. When users install your package using `pip install`, `pip` will choose the appropriate distribution format based on the user's environment.

In summary, `poetry publish --build` creates both source and wheel distribution packages, and these packages include the necessary files for your Python package to be installed by other users.

