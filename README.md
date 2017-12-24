"# PicartoAlertBoxApp" 

A Desktop app that lets you make your own alert boxes for picarto followers and subscribers.

# Pre-Alpha Version

The file testMain.py prints new followers and subscribers on the comand line.

To use this you must have the following things installed:
* Python 2.7.11
* pygame (the python module)
* Requests (the python module)

First go to https://docs.picarto.tv/api/ and authorize the Picarto.TV API Documentation to see your public and private data.

After that go back to https://docs.picarto.tv/api/ and make a query of whatever you want, like \categories, where it says curl should be something like this:

```
curl -X GET --header 'Accept: application/json' --header 'Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAAAA' 'https://api.picarto.tv/v1/categories'
```

Then go to model\tools, open jsonManager.py as a text file and in the 4th line add your bearer inside the "" put whatever is after bearer, "AAAAAAAAAAAAAAAAAAAAAAAA" in the example. The line should look like this:

```
Bearer = "AAAAAAAAAAAAAAAAAAAAAAAA"
```

Then just run testMain.py with the command: (```py -2 testMain.py```) because we are using python 2 here, and it should work.
