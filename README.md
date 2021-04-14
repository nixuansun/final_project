<div align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNlDe4ZXrWpa4vFKWNbxL-5f7BHCThyatBtK2gHrAq2IkpQKGq&s" width = "100" height = "100">
</div>

# IEOR 4501: Tools for Analytics Project - Squirrel Tracker 
## Project Description
In this web application, users can import the [2018 Central Park Squirrel Census data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) and view the squirrel data on it. In addition, users can add a new squirrel sighting or update an existing squirrel sighting. 

1. Import command:
```
$ python manage.py import_squirrel_data /path/to/file.csv
```
2. Export command:
```
$ python manage.py export_squirrel_data /path/to/file.csv
```
3. View the location of squirrel sightings on a map:
   - Locate at: ```/map```
4. View the list of all squirrel sightings:
   - Locate at: ```/sightings```
5. Update a particular squirrel sighting:
   - Locate at: ```/sightings/<unique-squirrel-id>```
6. Add a new squirrel sighting:
   - Locate at: ```/sightings/add```



## Group Information
- Project Group 34
- UNIs: [ss6125, ns3535]


## Links 
- Deployed Link: 
- [To view map]
- [To view all squirrel sightings]
- [To add a new squirrel sighting]
- [To view general sightings statistics]
