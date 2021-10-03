# Atmospheric_pressure
## How To Run
1. Clone the Repository in your local System

2. Make Sure Python is Installed in your system. Verion > 3.4

3. Go in the Directory ``` cd locus ```

4. Run this Command ``` python Task1.py ```
 
## Explanation Of the function

1.The code Will give the Atmospheric Pressure at 4am for the Past Three Days. 

2. main_execution -> Method 
   This Function Needs A API key and User Input for latitude and longitude for a particular city or place. It will Calculate the Atmospheric Pressure. It Accepts api_key as a parameter. 
   ``` Parameter  
   key : str 
    
   Lattitude: float or int
   Longitude: float or int 
3. get_timestamp -> Method
  It will calculate the Timestamp of a datetime Object and return it. Parameter ``` datetime_object: obj ```


## Logic 
1. Get the Api key.
2. Get Latitude and Longitude as user Input
3. Calculate past 3 day and time from Datetime Library
4. Send this Datetime object to a function to calculate the Timestamp
5. Api Accepts 4 parameter . Latitude,longitude, timestamp, api_key
6. Hit Api 3 times to get the Json containing atmospheric Pressure for Past 3 days.
