## workhours

plot a pretty distribution of working hours over a week

### get the code

    git clone https://github.com/philshem/workhours
    cd workhours/
    pip install -r requirements.txt

### edit the config data

open the file `config.py` with your favorite editor and change the number of hours of work on each day, as well as the color

'''
data = [{'day': 0, 'hours' : 4, 'color' : 'b'},
		{'day': 1, 'hours' : 4, 'color' : 'lime'},
		{'day': 2, 'hours' : 6, 'color' : 'g'},
		{'day': 3, 'hours' : 4, 'color' : 'lime'},
		{'day': 4, 'hours' : 2, 'color' : 'r'},
		]
'''

### run the code

    python3 workhours

### save your nice picture

![example output image](https://raw.githubusercontent.com/philshem/workhours/master/example.png)

