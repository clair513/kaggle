# Navigation Guidelines:

  <p class="lead"><i class="fa fa-tag w3-spin"></i> To launch application, set up an environment using any external packages like <a href="https://pypi.org/project/virtualenv/" target="_blank">virtualenv</a> or <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file" target="_blank">anaconda</a> distribution, with the provided <kbd>artivatic.yml</kbd> file. Kindly follow instructions provided in resource link. Project has been completed within Anaconda environment.</p>

  <hr class="my-4">

  <p class="lead"><i class="fa fa-tag w3-spin"></i>Application execution has been tested on a Windows, as well as Linux platform so please feel free to proceed as per availability. All these guidelines are a copy of <strong>readme.md</strong> file available in primary folder, for convenience.</p>

  <hr class="my-4">

  <p class="lead"><i class="fa fa-tag w3-spin"></i>On a Windows platform, open <strong>Command Prompt</strong> and run <kbd>set FLASK_APP = app.py</kbd> but for Linux platform kindly replace on Terminal with <kbd>export FLASK_APP = app.py</kbd>. Next to be executed is  <kbd>flask db init</kbd>, followed by <kbd>flask db migrate</kbd>. Then finally run <kbd>flask db upgrade</kbd>, followed by <kbd>python app.py</kbd>.</p>

  <hr class="my-4">

  <p class="lead"><i class="fa fa-tag w3-spin"></i>If not proceeding with previously provided dataset containing 60k records, please ensure to manually rename uploaded dataset with <kbd>.csv</kbd> extension. Uploaded file can be found in <kbd>~/artivatic/data/training_datasets</kbd> folder, named as <kbd>new_dataset</kbd>, which would require addition of file extension. Currently application has renaming glitch which hasn't been sorted as of now.</p>
