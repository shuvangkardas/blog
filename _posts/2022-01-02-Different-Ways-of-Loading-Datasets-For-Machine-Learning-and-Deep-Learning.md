I began my Ph.D. journey on 2021. At that time I started learning ML. So, initially, I practiced different ML models on the internet and through different tutorials. I always got confused about the ways different tutorials demonstrated how to load the dataset. Because I was not sure which way is good for my case. Then, I documented the dataset loading mechanism that different tutorials followed. I found that most of the tutorials follow only 2/3 types of mechanisms. 

Here I will write a few techniques for loading CSV datasets into your machine learning and deep learning model.
## Method1: Load data using basic python module
The first method I will discuss is a little lengthy and has two steps.
-   Download or load the raw data into RAM
-   Convert the data into a standard format such as list, Numpy array.

**Open File into RAM**
```python
#Method 1: Open File from Remote URL
from urllib.request import urlopen
path = "path_of_the_data"
rawdata= urlopen(path) #loads the raw data from url into ram

#Method 2: Open File from Local 
rawdata= open(filename, 'rt') #r=read mode | t=txt mode
```
**Convert Data Into Numpy array**
```python
#Method 1 : Convert numpy array using loadtxt() method
data_np = np.loadtxt(rawdata, delimiter=',') # returns numpy array

#Method 2: Convert numpy array using csv and numpy
import csv
csvObj = csv.reader(rawdata, delimiter=',', quoting=csv.QUOTE_NONE)
listObj = list(csvObj)             # convert csv object into list
data_np= np.array(listObj)         #convert list object into numpy array
data_np = data_np.astype('float')  #convert string array into float
```
## Method 2: Load data using Pandas
The second method is using the Pandas module which is very straightforward. It has a csv_read() method which takes both URL and local path and returns the output as pandas dataframe.
```python
import pandas as pd
df1 = pd.read_csv(remote_url) #read data from remote url
df2 = pd.read_csv(local_path) #read data from local path
df3 = pd.read_csv('local_path',header=None)  #headers=none for there is not header in my dataset
# return the numpy representation of the dataframe
np_data= df1.values
```
## Method 3: Load data from google drive
While working in Google Colab, it is convenient to load data from google drive. Suppose here is the structure of your google drive folder and you uploaded the dataset into the `dataset_folder`

My Drive   
|—folder_1  
|—dataset_folder

To access the dataset from `dataset_folder` we have to write the following code.
```python
from google.colab import drive
import os
# Mounting my Google drive
drive.mount('/content/drive')
#Setting google drive folder path. 
os.chdir(r"/content/drive/My Drive/dataset_folder")
```


Another important point you need to remember all the time while working with ML. Sometimes you download the dataset and feed that from the local directory. When you pass our model to someone, it kind of breaks the code. If the dataset is available online, don’t download it into your drive and load it. Because it will break your code in the future. So it is good practice to load the dataset directly from the URL and process it after that.

---
Shuvangkar Das,Potsdam, New York