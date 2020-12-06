# DomInnov

## Prereqs

 - Jeedom up and running
 - python3
 - `git clone git@github.com:mbonnemaison/DomInnov.git`

## Use

cd into the correct directory:

```
cd DomInnov
```

Export and save a data file from Jeedom to wherever you want:

 - in CSV format
 - with comma separators
 - first column timestamp
 - second column 1/0

Run the program:

```
./analysis.py $path/to/your/file.csv
```
