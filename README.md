## Python plotting course

<https://ualberta-rcg.github.io/python-plotting>

### Installing dependencies

To install the dependencies, run the following at the command line:

```
pip install jupyter matplotlib plotly pandas numpy cufflinks
```

Or in a Jupyter notebook:

```
!pip install matplotlib plotly pandas numpy cufflinks
```

### Getting the notebooks

To get the notebooks that make up this course, you can either use them in
Google Colab, or download them to your own computer.

#### Opening notebooks on Colab:

* Go to File->Open notebook
* Select "Github" tab
  * Organization: ualberta-rcg (important: press enter)
  * Repository: ualberta-rcg/python-plotting
  * Choose the notebook you want

#### Getting notebooks on your computer:

Either use git to clone the repository at Github:

```
git clone https://github.com/ualberta-rcg/python-plotting.git
```

... or click here to download from your browser: <https://github.com/ualberta-rcg/python-plotting/archive/master.zip>

... or run the following in a Jupyter notebook:

```
# Downloads and extracts to python-plotting-master directory
# Warning (overwrites notebooks if they exist)
import os, urllib.request, zipfile
def get_notebooks():
  url = 'https://github.com/ualberta-rcg/python-plotting/archive/master.zip'
  zip_file = 'python-plotting.zip'
  if os.path.exists(zip_file): return
  urllib.request.urlretrieve(url, zip_file)
  with zipfile.ZipFile(zip_file) as zip_ref:
    zip_ref.extractall()

get_notebooks()
```
