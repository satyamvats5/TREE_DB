### TREE DB

## Steps To Use:-

i) Clone the Repository <br>
ii) Go inside the Repo.<br>
iii) TO RUN TESTS<br>
    &nbsp; &nbsp; &nbsp;&nbsp;Build and run docker image with following commands<br>
    &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;iii.i) ``` docker build -t assign -f Dockerfile.test . ``` <br>
    &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;iii.ii) ```docker run -it assign```

iV) TO RUN Appllication:-<br>
    &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;iv.i) ```docker build -t assign .```<br>
    &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;iv.ii)```docker run -it -p 5000:5000 assign```<br>
  #### NOTE :- It will run the application in port 5000 inside container and we have expose the same 5000 port inside the container to 5000 on our host machine.


  
 
 
  ### Config Options available on flask app using CMD
  We can pass command line params while running application
  Options available :- <br>
  &nbsp; &nbsp; &nbsp;&nbsp;i)   ```-h or --host``` can be used as ```python app.py -h localhost``` or ```python app.py --host=localhost```<br>
  &nbsp; &nbsp; &nbsp;&nbsp;ii)  ```-p or --port``` can be used as ```python app.py -h localhost -p 5002``` or ```python app.py --port=5002```<br>
  &nbsp; &nbsp; &nbsp;&nbsp;iii) ```-d``` can be used to activate debug mode ```python app.py -d```<br>
  
  ### NOTE:- If any option will not be provided default one will be taken.
  
### Available APIs<br>
  A swagger documentation has been created for the API.<br>
  &nbsp; &nbsp; &nbsp;&nbsp;=> For accesing swagger docs :- ```GET htttp://host_name:port_number/```<br>
  &nbsp; &nbsp; &nbsp;&nbsp;=> For Fetching data :- ```GET http://host_name:port_number/api/v1/query``` With possible filters of country(list of strings) and device(list of strings).<br>
  &nbsp; &nbsp; &nbsp;&nbsp;=> For Inserting data:- ```POST http://host_name:port_number/aip/v1/insert``` with payload containing a country(string), a device(string), webreq(int) and timespent(int) values.<br>

