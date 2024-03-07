# Report of Monaco 2018 Racing
### Important:
Folder with data should have name "data" and data files should calls like "abbreviations.txt", "end.log", "start.log"

## Usage:
```
python -m app.cli --files path/to/data [--db_name DB_NAME] [--load] [--init] [--asc] [--desc] [--driver DRIVER] {create,drop,init,load}

```

## Examples:

### Command:
```
python -m app.cli --files "path/to/data" print
```
### Printed value:
```
------Printing report------
Driver: Sebastian Vettel Team: FERRARI Result: 64.415 Start: 2018-05-24 12:02:58.917000 End: 2018-05-24 12:04:03.332000 Position: 1
Driver: Valtteri Bottas Team: MERCEDES Result: 72.434 Start: 2018-05-24 12:00:00 End: 2018-05-24 12:01:12.434000 Position: 2
Driver: Stoffel Vandoorne Team: MCLAREN RENAULT Result: 72.463 Start: 2018-05-24 12:18:37.735000 End: 2018-05-24 12:19:50.198000 Position: 3
Driver: Kimi Räikkönen Team: FERRARI Result: 72.639 Start: 2018-05-24 12:03:01.250000 End: 2018-05-24 12:04:13.889000 Position: 4
Driver: Fernando Alonso Team: MCLAREN RENAULT Result: 72.657 Start: 2018-05-24 12:13:04.512000 End: 2018-05-24 12:14:17.169000 Position: 5
Driver: Charles Leclerc Team: SAUBER FERRARI Result: 72.829 Start: 2018-05-24 12:09:41.921000 End: 2018-05-24 12:10:54.750000 Position: 6
Driver: Sergio Perez Team: FORCE INDIA MERCEDES Result: 72.848 Start: 2018-05-24 12:12:01.035000 End: 2018-05-24 12:13:13.883000 Position: 7
Driver: Romain Grosjean Team: HAAS FERRARI Result: 72.93 Start: 2018-05-24 12:05:14.511000 End: 2018-05-24 12:06:27.441000 Position: 8
Driver: Pierre Gasly Team: SCUDERIA TORO ROSSO HONDA Result: 72.941 Start: 2018-05-24 12:07:23.645000 End: 2018-05-24 12:08:36.586000 Position: 9
Driver: Carlos Sainz Team: RENAULT Result: 72.95 Start: 2018-05-24 12:03:15.145000 End: 2018-05-24 12:04:28.095000 Position: 10
Driver: Nico Hulkenberg Team: RENAULT Result: 73.065 Start: 2018-05-24 12:02:49.914000 End: 2018-05-24 12:04:02.979000 Position: 11
Driver: Brendon Hartley Team: SCUDERIA TORO ROSSO HONDA Result: 73.179 Start: 2018-05-24 12:14:51.985000 End: 2018-05-24 12:16:05.164000 Position: 12
Driver: Marcus Ericsson Team: SAUBER FERRARI Result: 73.265 Start: 2018-05-24 12:04:45.513000 End: 2018-05-24 12:05:58.778000 Position: 13
Driver: Lance Stroll Team: WILLIAMS MERCEDES Result: 73.323 Start: 2018-05-24 12:06:13.511000 End: 2018-05-24 12:07:26.834000 Position: 14
Driver: Kevin Magnussen Team: HAAS FERRARI Result: 73.393 Start: 2018-05-24 12:02:51.003000 End: 2018-05-24 12:04:04.396000 Position: 15
---------------------------
Driver: Daniel Ricciardo Team: RED BULL RACING TAG HEUER Result: 167.987 Start: 2018-05-24 12:14:12.054000 End: 2018-05-24 12:11:24.067000 Position: 16
Driver: Sergey Sirotkin Team: WILLIAMS MERCEDES Result: 287.294 Start: 2018-05-24 12:16:11.648000 End: 2018-05-24 12:11:24.354000 Position: 17
Driver: Esteban Ocon Team: FORCE INDIA MERCEDES Result: 346.972 Start: 2018-05-24 12:17:58.810000 End: 2018-05-24 12:12:11.838000 Position: 18
Driver: Lewis Hamilton Team: MERCEDES Result: 407.54 Start: 2018-05-24 12:18:20.125000 End: 2018-05-24 12:11:32.585000 Position: 19
```

### Command:
```
python -m app.cli --files "path/to/data" print  --driver "SVF"
```
### Printed value:
```
------Printing report------
Driver: Sebastian Vettel Team: FERRARI Result: 64.415 Start: 2018-05-24 12:02:58.917000 End: 2018-05-24 12:04:03.332000 Position: 1

```

### Initializing DB Command:
```
python -m app.cli --files "path/to/data" init
```

### Create Tables and Load Data to DB Command:
```
python -m app.cli --files "path/to/data" load
```

### Links Example:
```
app:
http://127.0.0.1:5000/report
http://127.0.0.1:5000/report/?order=desc
http://127.0.0.1:5000/report/drivers/
http://127.0.0.1:5000/report/drivers/?order=desc
http://127.0.0.1:5000/report/drivers?driver_id=VBM

api:
http://127.0.0.1:5000/api/v1/report/?format=json
http://127.0.0.1:5000/api/v1/report/?format=xml
http://127.0.0.1:5000/api/v1/report/drivers/?format=json
http://127.0.0.1:5000/api/v1/report/drivers/?format=xml
http://127.0.0.1:5000/api/v1/report/drivers/about/?driver_id=KRF&format=json
http://127.0.0.1:5000/api/v1/report/drivers/about/?driver_id=KRF&format=xml
```


### Run tests:
```
pytest tests
```