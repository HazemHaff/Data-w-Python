#A variety of data providers make data available via Application Programming Interfaces (APIs), 
#that makes it easy to access such data via Python.
#There are also a number of datasets available online in various formats.
#An online available example is the UC Irvine Machine Learning Library.
#Here, we read one of its datasets into Pandas directly via the URL.

#UCI Cars data set - url location
data_url ='http://archive.ics.uci.edu/ml/machine -learning-databases/autos/imports-85.data'

df=pd.read_csv (data_url, header=None)