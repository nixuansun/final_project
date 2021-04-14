<div align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNlDe4ZXrWpa4vFKWNbxL-5f7BHCThyatBtK2gHrAq2IkpQKGq&s" width = "100" height = "100">
</div>

# IEOR 4501: Tools for Analytics Project - Squirrel Tracker 
## Project Description
Users can keep track of all the known squirrels and plans to start with Central Park. 
It's an web application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data.
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
7. View the general sightings statistics:
   - Locate at: ```/sightings/stats```
## Group Information
- Project Group 34
- UNIs: [ss6125, ]
