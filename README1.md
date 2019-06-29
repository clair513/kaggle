# Navigation Guidelines:


  Batch/shell file not prepared so to launch this *Flask application*, set up an environment using any external packages like [virtualenv](https://pypi.org/project/virtualenv/) or [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) distribution, with provided **artivatic.yml** file. Kindly follow instructions provided in resource link. Project has been completed within Anaconda environment.

  ------------------------------------------------------------------------------------------------------------------------------

  Application execution has been tested on *Windows* as well as *Linux* platform so feel free to proceed as per availability. All these guidelines are a copy of **README.md** file available in primary folder, for convenience. *Serialization* is available via **API Testing** in navigation.

  -------------------------------------------------------------------------------------------------------------------------------

  On *Windows* platform, open *Command Prompt* and run `set FLASK_APP = app.py` but for *Linux* platform, kindly replace command on *Terminal* with `export FLASK_APP = app.py`. Next to be executed is  `flask db init`, followed by `flask db migrate`. Then finally run `flask db upgrade`, followed by `python app.py`.

  --------------------------------------------------------------------------------------------------------------------------------

  If not proceeding with previously provided dataset containing 60k records, please ensure to manually rename uploaded dataset with `.csv` extension. Uploaded file can be found in `~/artivatic/data/training_datasets` folder, named as **new_dataset**, which would require addition of file extension. Currently application has auto-renaming glitch which hasn't been sorted as of now.
