Section 1\
Overview of project {#section-1-overview-of-project .ListParagraph}
===================

Where we have uploaded our tutorial {#where-we-have-uploaded-our-tutorial .Header2dora1}
-----------------------------------

Paste the link here of your Youtube and tutorial document here

What is the application about? {#what-is-the-application-about .Header2dora1}
------------------------------

Our project, takes images using the camera every predefined seconds,
feeds it into a cloud bucket and performs image recognition on it. It
has been preconfigured to identify faces and highlight them. Currently
it is performing the function of security camera, thus when it
recognises a person, it will email the owner and issue a verbal warning
to the visitor.It has been attached to servos to allow movement of the
camera however this application is infinitely dynamic, allowing it to be
used for a variety of other purposes such as as being able to be
configured for Optical character recognition and other artificial
intelligence purposes.

How does the final RPI set-up looks like? {#how-does-the-final-rpi-set-up-looks-like .Header2dora1}
-----------------------------------------

[]{#_Hlk11435148 .anchor}The following images shows how the completed
circuit should look and a fritzing diagram for reference when setting up
the hardware.

![](media/image1.png){width="6.770138888888889in"
height="5.077083333333333in"}

Connect the LDR
---------------

  -----------------------------------------------------------------------------------------------------------------
         Task
  ------ ----------------------------------------------------------------------------------------------------------
  a)     Add the LDR to the breadboard as shown
         
         -   One end of the LDR should be connected to **Pin 1** of the MCP3008 ADC and the 10k ohms **resistor**
         
         -   The other end of the LDR should be connected to **GND**
         
         ![](media/image2.png){width="6.100092957130359in" height="3.1458333333333335in"}
  -----------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------
         Task
  ------ ------------------------------------------------------------------------------------
  a)     Follow the wiring display down below to properly connect the servos to the arduino
         
         ![](media/image3.png){width="6.770138888888889in" height="6.499305555555556in"}
  -------------------------------------------------------------------------------------------

How does the web or mobile application look like? {#how-does-the-web-or-mobile-application-look-like .Header2dora1}
-------------------------------------------------

[]{#_Hlk11435154 .anchor}The following images are screenshots of how the
web application should look if setup was done correctly. All the
screenshots are of index.html.

System architecture of our system {#system-architecture-of-our-system .Header2dora1}
---------------------------------

Provide a hand-drawn or computer-drawn system architecture diagram
please. Example given below.

![](media/image4.png){width="6.766666666666667in"
height="3.7416666666666667in"}

Evidence that we have met basic requirements {#evidence-that-we-have-met-basic-requirements .Header2dora1}
--------------------------------------------

Provide bullet list to describe how your group has met basic
requirements

  --------------------------------------------------------------------------------------------------------------------------------
  Requirement                               Evidence
  ----------------------------------------- --------------------------------------------------------------------------------------
  Used three sensors                        Used Camera, and light detector as sensors, led and servos as actuator

  Used MQTT                                 Our MQTT endpoint --&gt; Google cloud platform
                                            
                                            Example of data sent through MQTT : Blob of images, light value : 0.8

  Stored data in cloud                      Stored People detected data in Google Cloud

  Used cloud service                        Used Google Cloud Platform with AppEngine, IOTCore, Storage and Vision

  Provide real-time sensor value / status   Show historical values of whether theres any body visible and detected by the camera

  Provide historical sensor value/ status   Show historical values of whether theres any body visible and detected by the camera

  Control actuator                          Control Servos through the WebApp
  --------------------------------------------------------------------------------------------------------------------------------

Bonus features on top of basic requirements {#bonus-features-on-top-of-basic-requirements .Header2dora1}
-------------------------------------------

Provide bullet list of the bonus features you have added on top of basic
requirements

a)  Image Recognition

b)  SSL Email system

c)  Audio Alert System

d)  Outline Faces

e)  Store to Google Cloud

f)  Independent Power

    A.  Quick-start guide (Readme first) {#quick-start-guide-readme-first .Header2dora1}
        --------------------------------

[]{#_Hlk11435242 .anchor}

The following list is the instruction to set up the web application.

1)  First connect the hardware using the fritzing diagram located in
    Section B as a guide

2)  Git Clone the Repository from git hub

3)  Pip install Requirements.txt to install all the packages required

4)  Run Main.py for all the functions

5)  Run pub.py to publish data from the light sensor to the IOT Topic

Section 2\
Hardware requirements  {#section-2-hardware-requirements .ListParagraph}
======================

Hardware checklist {#hardware-checklist .ListParagraph .Header2dora1}
------------------

### Light-Dependant Resistor (LDR)

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  []{#_Toc478835715 .anchor}   Task
  ---------------------------- --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  a)                           -   Light-Dependant Resistor (LDR) are light sensitive resistors which change resistance based on how much light they are exposed to.   **LDR**
                                                                                                                                                                       
                               -   The more light a LDR receives, the less resistant it becomes, i.e. lets more current flow                                           ![](media/image5.jpg){width="1.5133748906386701in" height="0.9696959755030621in"}
                                                                                                                                                                       
                               -   When it’s in the dark, the resistance is very high                                                                                  
                                                                                                                                                                       
                               -   The resistance of an LDR may typically have the following resistances:                                                              
                                                                                                                                                                       
                                   -   Daylight = 5000Ω                                                                                                                
                                                                                                                                                                       
                                   -   Dark = 20000000Ω                                                                                                                
                                                                                                                                                                       
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### SG90 Servo Motor

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Task
  ------ ------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  a)     -   Servo motors (or servos) are self-contained electric devices that rotate or push parts of a machine with great precision.   ![](media/image6.png){width="1.7770833333333333in" height="1.1854166666666666in"}
                                                                                                                                         
         -   The heart of a servo is a small direct current (DC) motor, similar to what you might find in an inexpensive toy.            
                                                                                                                                         
         -   These motors run on electricity from a battery and spin at high RPM (rotations per minute) but put out very low torque      
                                                                                                                                         
         -   The specifications of the motor are the following:                                                                          
                                                                                                                                         
             -   Speed = 0.32 oz                                                                                                         
                                                                                                                                         
             -   Torque = 4.8V: 25.0 oz-in (1.80 kg-cm)                                                                                  
                                                                                                                                         
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Section 3\
Configuration {#section-3-configuration .ListParagraph}
=============

Enable camera with raspi-config
-------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  No.    Task
  ------ -------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  a)     -   Open the Raspberry Pi Configuration Tool from the main menu:                                         ![](media/image7.png){width="2.7192005686789154in" height="2.6770833333333335in"}
                                                                                                                  

  a)     -   Ensure the camera software is enabled. If it's not enabled, enable it and reboot your Pi to begin.   ![](media/image8.png){width="3.0979779090113735in" height="2.6930555555555555in"}
                                                                                                                  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Configure Gmail Account {#configure-gmail-account .Header2dora1}
-----------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Task
  ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  a)     Go to https://www.google.com/gmail/ and log in with your credentials

  a)     If you don’t have one, you can create a gmail account for free easily following this guide (<https://support.google.com/mail/answer/56256?hl=en>).
         
         Follow the instructions to apply for the account so that you can access the Google APIs.
         
         You can block sign-in attempts from some apps or devices that are less secure. Apps that are less secure don't use modern security standards, such as OAuth. Using apps and devices that don’t use modern security standards increases the risk of accounts being compromised. Blocking these apps and devices helps keep your users and data safe.

  a)     Sign in to your Google Admin console. <https://myaccount.google.com/>

  a)     From the Admin console Home page, go to Security and then Basic settings.
         
         To see Security on the Home page, you might have to click More controls at the bottom.

  a)     Scroll down until you see the tab on the left saying less secure app access

  a)     Press the button and allow less secure app access
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Configure Google Cloud {#configure-google-cloud .Header2dora1}
-----------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Task
  ------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  a)     Go to https://console.cloud.google.com and log in with your credentials

  a)     If you don’t have one, you can create a gmail account for free easily following this guide (<https://support.google.com/mail/answer/56256?hl=en>).
         
         Follow the instructions to apply for the account so that you can access the Google APIs.

  a)     You will see this Dashboard

  a)     Click on the project selection and click new project

  a)     You will be faced with this selection next, name your project what you wishbut keep track of your project ID for later

  a)     After Creation, head to the drop down bar and set up your billing account as it will be needed to enable the additional features. You can follow the billing guide here (https://cloud.google.com/billing/docs/)

  a)     Click Link a billing account and create a billing account

  a)     Select Singapore, after which fill up contact and credit card details
         
         ![](media/image18.png){width="2.3493055555555555in" height="3.609027777777778in"}
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Configure Google Bucket {#configure-google-bucket .Header2dora1}
-----------------------

  ---------------------------------------------------------------------------------------------------------------------------------
         Task
  ------ --------------------------------------------------------------------------------------------------------------------------
  a)     In your terminal window, create a Cloud Storage bucket, where \[YOUR\_BUCKET\_NAME\] represents the name of your bucket:
         
         gsutil mb gs://\[YOUR\_BUCKET\_NAME\]

  a)     To view uploaded images in the Bookshelf app, set the bucket's default access control list (ACL) to public-read:
         
         gsutil defacl set public-read gs://\[YOUR\_BUCKET\_NAME\].
  ---------------------------------------------------------------------------------------------------------------------------------

Configure Google Features {#configure-google-features .Header2dora1}
-------------------------

  ---------------------------------------------------------------------------------------------------------------------------------
         Task
  ------ --------------------------------------------------------------------------------------------------------------------------
  a)     In your terminal window, create a Cloud Storage bucket, where \[YOUR\_BUCKET\_NAME\] represents the name of your bucket:
         
         gsutil mb gs://\[YOUR\_BUCKET\_NAME\]

  a)     To view uploaded images in the Bookshelf app, set the bucket's default access control list (ACL) to public-read:
         
         gsutil defacl set public-read gs://\[YOUR\_BUCKET\_NAME\].
  ---------------------------------------------------------------------------------------------------------------------------------

Section 4\
Software Requirements {#section-4-software-requirements .ListParagraph}
=====================

Software checklist {#software-checklist .Header2dora1}
------------------

Below is a list of libraries that I have imported and used for each of
the python script.

  ---------------------------------------------------------------------------------------------------------------------------------
  **main.py**                              **Faces\_detection.py**     **publish.py**                         **receive.py**
  ---------------------------------------- --------------------------- -------------------------------------- ---------------------
  1.  base64                               1.  PIL :Image, ImageDraw   1.  receive :receive\_messages         1.  mysql.connector
                                                                                                              
  2.  json                                                             2.  publish: publish\_messages         
                                                                                                              
  3.  os                                                               3.  google.oauth2 : service\_account   
                                                                                                              
  4.  smtplib                                                          4.  gpiozero : MCP3008                 
                                                                                                              
  5.  time                                                             5.  time :sleep                        
                                                                                                              
  6.  sys                                                              6.  RPi.GPIO : GPIO                    
                                                                                                              
  7.  random:randrange                                                                                        
                                                                                                              
  8.  pygame:mixer                                                                                            
                                                                                                              
  9.  google.cloud: pubsub\_v1                                                                                
                                                                                                              
  10. google.cloud: storage                                                                                   
                                                                                                              
  11. google.cloud:vision                                                                                     
                                                                                                              
  12. time:sleep                                                                                              
                                                                                                              
  13. datetime : datetime                                                                                     
                                                                                                              
  14. picamera: PiCamera                                                                                      
                                                                                                              
  15. google.cloud.vision: types                                                                              
                                                                                                              
  16. face\_detection:highlight\_faces                                                                        
                                                                                                              
  17. PIL: Image, ImageDraw                                                                                   
                                                                                                              
  18. email.mime.text:MIMEText                                                                                
                                                                                                              
  19. email.mime.image: MIMEImage                                                                             
                                                                                                              
  20. email.mime.multipart:MIMEMultipart                                                                      
                                                                                                              
  ---------------------------------------------------------------------------------------------------------------------------------

Section 5\
Software SetUp {#section-5-software-setup .ListParagraph}
==============

Software setup instructions {#software-setup-instructions .Header2dora1}
---------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  No.   Task
  ----- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1)    []{#_Hlk11435266 .anchor}To implement the google cloud functions, the libraries need to be installed on the Raspberry Pi.
        
        Install Google Cloud Storage (https://pypi.org/project/google-cloud-storage/)
        
        sudo pip install google-cloud-storage
        
        Install Google Cloud Vision (https://pypi.org/project/google-cloud-vision/)
        
        sudo install google-cloud-vision
        
        Install Pillow (https://pypi.org/project/Pillow/2.2.1)
        
        sudo pip install Pillow

  2)    []{#_Hlk11435274 .anchor}To implement the Pi Camera, the camera has to be enable inside the raspberry pi configuration. Open the Raspberry Pi Configuration Tool from the main menu: ![](media/image7.png){width="2.7192005686789154in" height="2.6770833333333335in"}
        
        -   Ensure the camera software is enabled. If it's not enabled, enable it and reboot your Pi to begin.
        
            ![](media/image8.png){width="3.0979779090113735in" height="2.6930555555555555in"}
        

  4)    []{#_Hlk11435295 .anchor}To implement MySQL database, the MySQL libraries need to be installed. If you are using the ST0324 IoT Raspbian image, you might encounter an error as the libraries have already been pre-installed. If you are using a fresh image, you would need to run the commands below to install the MySQL libraries.
        
        sudo pip install mysql-connector-python
        
        sudo pip install mysql-connector
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Section 6\
Source codes {#section-6-source-codes .ListParagraph}
============

Bootstrap {#bootstrap .Header2dora1}
---------

1.  []{#_Hlk11435340 .anchor}After you have git cloned the repository,
    change directory into WebApp

2.  Run the command export
    GOOGLE\_APPLICATION\_CREDENTIALS="../credentials/credentials\_davis.json"
    to export the credentials necessary to access google applications

3.  Run the command gcloud app deploy to deploy the app to the app
    engine

![](media/image20.png){width="6.770138888888889in"
height="2.0993055555555555in"}

1.  []{#_Hlk11435347 .anchor}For this web application, We will be using
    a free bootstrap template called Paper Dashboard 2 that has already
    been downloaded. It is also available here at
    (https://www.creative-tim.com/product/paper-dashboard-2)

2.  The asset and css folders have been already copied into the static
    folder ![](media/image21.png){width="6.525565398075241in"
    height="2.1668547681539807in"}

index.html {#index.html .Header2dora1}
----------

Create a *index.html* file in the template folder with the following
code below

&lt;!DOCTYPE html&gt;

&lt;html lang="en"&gt;

&lt;head&gt;

&lt;meta charset="utf-8" /&gt;

&lt;link rel="apple-touch-icon" sizes="76x76"
href="../static/img/apple-icon.png"&gt;

&lt;link rel="icon" type="image/png"
href="../static/img/favicon.png"&gt;

&lt;meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /&gt;

&lt;title&gt;

Paper Dashboard 2 by Creative Tim

&lt;/title&gt;

&lt;meta content='width=device-width, initial-scale=1.0,
maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport'
/&gt;

&lt;!-- Fonts and icons --&gt;

&lt;link
href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200"
rel="stylesheet" /&gt;

&lt;link
href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css"
rel="stylesheet"&gt;

&lt;!-- CSS Files --&gt;

&lt;link href="../static/css/bootstrap.min.css" rel="stylesheet" /&gt;

&lt;link href="../static/css/paper-dashboard.css?v=2.0.0"
rel="stylesheet" /&gt;

&lt;!-- CSS Just for demo purpose, don't include it in your project
--&gt;

&lt;link href="../static/demo/demo.css" rel="stylesheet" /&gt;

&lt;/head&gt;

&lt;body class=""&gt;

&lt;div class="wrapper "&gt;

&lt;div class="sidebar" data-color="white"
data-active-color="danger"&gt;

&lt;!--

Tip 1: You can change the color of the sidebar using: data-color="blue |
green | orange | red | yellow"

--&gt;

&lt;div class="logo"&gt;

&lt;img src="../static/img/sp.png"&gt;

&lt;/div&gt;

&lt;div class="sidebar-wrapper"&gt;

&lt;ul class="nav"&gt;

&lt;li class="active "&gt;

&lt;a href="./index.html"&gt;

&lt;i class="nc-icon nc-bank"&gt;&lt;/i&gt;

&lt;p&gt;Index&lt;/p&gt;

&lt;/a&gt;

&lt;/li&gt;

&lt;/ul&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;div class="main-panel"&gt;

&lt;!-- Navbar --&gt;

&lt;nav class="navbar navbar-expand-lg navbar-absolute fixed-top
navbar-transparent"&gt;

&lt;div class="container-fluid"&gt;

&lt;div class="navbar-wrapper"&gt;

&lt;div class="navbar-toggle"&gt;

&lt;button type="button" class="navbar-toggler"&gt;

&lt;span class="navbar-toggler-bar bar1"&gt;&lt;/span&gt;

&lt;span class="navbar-toggler-bar bar2"&gt;&lt;/span&gt;

&lt;span class="navbar-toggler-bar bar3"&gt;&lt;/span&gt;

&lt;/button&gt;

&lt;/div&gt;

&lt;a class="navbar-brand" href="\#pablo"&gt;IOT CA1: Resorts World
Sentosa v1&lt;/a&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/nav&gt;

&lt;!-- End Navbar --&gt;

&lt;!-- &lt;div class="panel-header panel-header-lg"&gt;

&lt;canvas id="bigDashboardChart"&gt;&lt;/canvas&gt;

&lt;/div&gt; --&gt;

&lt;div class="content"&gt;

&lt;div class="row"&gt;

&lt;div class="col-lg-3 col-md-0 col-sm-0"&gt;

&lt;/div&gt;

&lt;div class="col-lg-3 col-md-6 col-sm-6"&gt;

&lt;div class="card card-stats"&gt;

&lt;div class="card-body "&gt;

&lt;div class="row"&gt;

&lt;div class="col-5 col-md-4"&gt;

&lt;div class="icon-big text-center icon-warning"&gt;

&lt;img id="light-bulb" src="../static/img/icons/light-bulb-off.png"&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;div class="col-7 col-md-8"&gt;

&lt;div class="numbers"&gt;

&lt;p class="card-category"&gt;Status of LED&lt;/p&gt;

&lt;p class="card-title" id="lightStatus"&gt;Off&lt;p&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;div class="card-footer "&gt;

&lt;hr&gt;

&lt;div class="stats"&gt;

&lt;button type="button" class="btn btn-outline-primary"
id="toggle"&gt;Toggle Light&lt;/button&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;div class="row"&gt;

&lt;div class="col-md-12"&gt;

&lt;div class="card "&gt;

&lt;div class="row"&gt;

&lt;div class="col-md-6"&gt;

&lt;div class="card-header "&gt;

&lt;h5 class="card-title"&gt;Real Time&lt;/h5&gt;

&lt;/div&gt;

&lt;img id="rt" width="500px"
src="https://storage.cloud.google.com/images1703221/current?authuser=1"/&gt;

&lt;/div&gt;

&lt;div class="col-md-6"&gt;

&lt;div class="card-header "&gt;

&lt;h5 class="card-title"&gt;Analysis&lt;/h5&gt;

&lt;/div&gt;

&lt;img id="an" width="500px"
src="https://storage.cloud.google.com/images1703221/visitor?authuser=1"/&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;div class="row"&gt;

&lt;div class="col-md-12"&gt;

&lt;div class="card "&gt;

&lt;div class="card-header "&gt;

&lt;h5 class="card-title"&gt;Number of people&lt;/h5&gt;

&lt;p class="card-category"&gt;powered by yolo&lt;/p&gt;

&lt;/div&gt;

&lt;div class="card-body "&gt;

&lt;div id="chart\_div" style="width:100%"&gt;&lt;/div&gt;

&lt;div id="table\_div" style="width:100%"&gt;&lt;/div&gt;

&lt;/div&gt;

&lt;div class="card-footer "&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;script type="text/javascript"
src="https://code.jquery.com/jquery-3.2.1.js"&gt;&lt;/script&gt;

&lt;script type="text/javascript"
src="https://www.gstatic.com/charts/loader.js"&gt;&lt;/script&gt;

&lt;script type="text/javascript"&gt;

google.charts.load('current', {'packages':\['corechart','table'\]});

// Set a callback to run when the Google Visualization API is loaded.

google.charts.setOnLoadCallback(googlecharts\_is\_ready);

var chart;

var graphdata;

function reset\_status\_messages(){

\$("\#status").html("")

}

function googlecharts\_is\_ready(){

\$("\#buttonloadchart").show()

\$("\#buttonloadchart").click()

\$("\#status").html("Google charts is ready")

}

function loadChart(){

getData\_and\_drawChart()

}

function getData\_and\_drawChart(){

getNewData()

}

function getNewData(){

\$("\#status").html("Fetching data to plot graph...");

jQuery.ajax({

url: "/api/getdata" ,

type: 'POST',

success: function(ndata, textStatus, xhr){

console.log(ndata.chart\_data.data)

\$("\#status").html("Data fetched! Now plotting graph!");

chartdata = ndata.chart\_data.data

graphdata = createDataTable(chartdata)

drawLineChart(graphdata)

drawDataTable(graphdata)

\$("\#status").html("Graph plotted");

}//end success

});//end ajax

} //end getNewData

function createDataTable(newdata){

graphdata = new google.visualization.DataTable();

graphdata.addColumn('string', 'Time');

graphdata.addColumn('number', 'Light Value');

for (i in newdata) {

datetime = newdata\[i\].datetime\_value;

jsdatetime = new Date(Date.parse(datetime));

jstime = jsdatetime.toLocaleTimeString();

light = newdata\[i\].light;

graphdata.addRows(\[\[jstime,light\]\]);

}//end for

return graphdata

}

function drawDataTable(graphdata){

var table = new
google.visualization.Table(document.getElementById('table\_div'));

table.draw(graphdata, {showRowNumber: true, width: '100%', height:
'100%'});

}//end drawTable

function drawLineChart(graphdata) {

chart = new google.visualization.LineChart(

document.getElementById('chart\_div'));

chart.draw(graphdata, {legend: 'none', vAxis: {baseline: 0},

colors: \['\#A0D100'\]});

return

} //end drawChart

\$(document).ready(function(){

reset\_status\_messages()

setInterval(function () {

loadChart()

}, 3000);

});

&lt;/script&gt;

&lt;script
src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"&gt;&lt;/script&gt;

&lt;script&gt;&lt;!--code for light toggle--&gt;

var imgOne=true;

var URLimgOne="../static/img/icons/light-bulb-off.png";

var URLimgTwo="../static/img/icons/light-bulb-on.png";

function updateImg(){

var currUrl;

if(imgOne){

imgOne=false;

currUrl=URLimgTwo;

}else{

imgOne=true;

currUrl=URLimgOne;

}

document.getElementById("light-bulb").src=currUrl;

}

function toggle(){

\$.ajax({url: "toggle",

success: function(result){

\$("\#lightStatus").html(result);

}

})

}

\$(document).ready(function(){

\$("\#toggle").click(function(){

toggle();

updateImg();

});

});

&lt;/script&gt;

&lt;script&gt;&lt;!--refresh for yolo image--&gt;

window.onload = function() {

var image = document.getElementById("rt");

var image2 = document.getElementById("an");

function updateImage() {

image.src = image.src.split("?")\[0\] + "?" + new Date().getTime();

image2.src = image2.src.split("?")\[0\] + "?" + new Date().getTime();

}

setInterval(updateImage, 5000);

}

&lt;/script&gt;

&lt;script&gt;

document.onkeydown = function(e) {

switch (e.keyCode) {

case 37:

moveL();

break;

case 38:

moveU();

break;

case 39:

moveR();

break;

case 40:

moveD();

break;

}

};

function moveL(){

\$.ajax({url: "moveL",

success: function(result){

}

})

function moveR(){

\$.ajax({url: "moveR",

success: function(result){

}

})

function moveU(){

\$.ajax({url: "moveU",

success: function(result){

}

})

function moveD(){

\$.ajax({url: "moveD",

success: function(result){

}

})

&lt;/script&gt;

&lt;!-- Core JS Files --&gt;

&lt;script src="../static/js/core/jquery.min.js"&gt;&lt;/script&gt;

&lt;script src="../static/js/core/popper.min.js"&gt;&lt;/script&gt;

&lt;script src="../static/js/core/bootstrap.min.js"&gt;&lt;/script&gt;

&lt;script
src="../static/js/plugins/perfect-scrollbar.jquery.min.js"&gt;&lt;/script&gt;

&lt;!-- Google Maps Plugin --&gt;

&lt;script
src="https://maps.googleapis.com/maps/api/js?key=YOUR\_KEY\_HERE"&gt;&lt;/script&gt;

&lt;!-- Chart JS --&gt;

&lt;script src="../static/js/plugins/chartjs.min.js"&gt;&lt;/script&gt;

&lt;!-- Notifications Plugin --&gt;

&lt;script
src="../static/js/plugins/bootstrap-notify.js"&gt;&lt;/script&gt;

&lt;!-- Control Center for Now Ui Dashboard: parallax effects, scripts
for the example pages etc --&gt;

&lt;script src="../static/js/paper-dashboard.min.js?v=2.0.0"
type="text/javascript"&gt;&lt;/script&gt;

&lt;!-- Paper Dashboard DEMO methods, don't include it in your project!
--&gt;

&lt;script src="../static/demo/demo.js"&gt;&lt;/script&gt;

&lt;script&gt;

\$(document).ready(function() {

// Javascript method's body can be found in
assets/assets-for-demo/js/demo.js

demo.initChartsPages();

});

&lt;/script&gt;

&lt;/body&gt;

&lt;/html&gt;

main.py {#main.py .Header2dora1}
-------

[]{#_Hlk11435384 .anchor}To upload the images and perform cloud
functions and recognition as well as other functions that have been
included, the following code has been provided.

import base64

import json

import os

import smtplib

import time, sys

from random import randrange

from pygame import mixer

from google.cloud import pubsub\_v1

from google.cloud import storage

from google.cloud import vision

from time import sleep

from datetime import datetime

from picamera import PiCamera

from google.cloud.vision import types

from face\_detection import highlight\_faces

from PIL import Image, ImageDraw

from email.mime.text import MIMEText

from email.mime.image import MIMEImage

from email.mime.multipart import MIMEMultipart

gmail\_user = 'pentestnil@gmail.com'

gmail\_password = '1qwe\$\#@!'

credential\_path = "../credentials/credentials\_davis.json"

os.environ\['GOOGLE\_APPLICATION\_CREDENTIALS'\] = credential\_path

sent\_from = 'pentestnil@gmail.com'

to = \['t0016029b@gmail.com'\]

From = "pentestnil@gmail.com"

To = "t0016029b@gmail.com"

delay=2

client = vision.ImageAnnotatorClient()

def detect\_face(face\_file, max\_results=4):

"""Uses the Vision API to detect faces in the given file.

Args:

face\_file: A file-like object containing an image with faces.

Returns:

An array of Face objects with information about the picture.

"""

client = vision.ImageAnnotatorClient()

content = face\_file.read()

image = types.Image(content=content)

return client.face\_detection(image=image,
max\_results=max\_results).face\_annotations

def warning(option):

mixer.init()

if option == 1:

sound = mixer.Sound('target.wav')

else:

sound = mixer.Sound('seeyou.wav')

sound.play()

time.sleep(sound.get\_length()+1)

def emailalert():

try:

img\_data = open(full\_path\_post, 'rb').read()

msg = MIMEMultipart()

msg\['Subject'\] = 'Alert!!'

text = MIMEText("Hey, you have a visitor\\n\\n -Davis ")

msg.attach(text)

image = MIMEImage(img\_data, name=os.path.basename(full\_path\_post))

msg.attach(image)

server = smtplib.SMTP\_SSL('smtp.gmail.com', 465)

server.ehlo()

server.login(gmail\_user, gmail\_password)

server.sendmail(From,To, msg.as\_string())

server.close()

print ('Email sent!')

except:

print ('Something went wrong...')

def takePhotoWithPiCam():

camera.capture(full\_path)

sleep(delay)

def faces(input\_filename, output\_filename, max\_results):

with open(input\_filename, 'rb') as image:

faces = detect\_face(image, max\_results)

print('Found {} face{}'.format(

len(faces), '' if len(faces) == 1 else 's'))

print('Writing to file {}'.format(output\_filename))

\# Reset the file pointer, so we can read the file again

image.seek(0)

highlight\_faces(image, faces, output\_filename)

if len(faces) == 1:

print("hi")

emailalert()

warning(randrange(2))

upload\_blob("images1703221",full\_path\_post,"visitor")

raise SystemExit

def upload\_blob(bucket\_name, source\_file\_name,
destination\_blob\_name):

"""Uploads a file to the bucket."""

storage\_client = storage.Client()

bucket = storage\_client.get\_bucket(bucket\_name)

blob = bucket.blob(destination\_blob\_name)

blob.upload\_from\_filename(source\_file\_name)

print('File {} uploaded to {}.'.format(

source\_file\_name,

destination\_blob\_name))

\# Set the filename and bucket name

bucket = 'images1703221' \# replace with your own unique bucket name

with PiCamera() as camera:

while True:

full\_path = ('/home/pi/Desktop/pre.jpg')

full\_path\_post = ('/home/pi/Desktop/post.jpg')

file\_name = (str(datetime.now()) + ' pre.jpg')

takePhotoWithPiCam()

faces(full\_path,full\_path\_post,4)

upload\_blob("images1703221",full\_path,"current")

face\_detection.py {#face_detection.py .Header2dora1}
------------------

[]{#_Hlk11435394 .anchor}Create a python script using the code below
called *face\_detection.py* that will use the image recognition returned
and highlight the people identified in the image and output the image
which will be uploaded online

*from PIL import Image, ImageDraw*

*def highlight\_faces(image, faces, output\_filename):*

*"""Draws a polygon around the faces, then saves to output\_filename.*

*Args:*

*image: a file containing the image with the faces.*

*faces: a list of faces found in the file. This should be in the format*

*returned by the Vision API.*

*output\_filename: the name of the image file to be created, where the*

*faces have polygons drawn around them.*

*"""*

*im = Image.open(image)*

*draw = ImageDraw.Draw(im)*

*\# Sepecify the font-family and the font-size*

*for face in faces:*

*box = \[(vertex.x, vertex.y)*

*for vertex in face.bounding\_poly.vertices\]*

*draw.line(box + \[box\[0\]\], width=5, fill='\#00ff00')*

*\# Place the confidence value/score of the detected faces above the*

*\# detection box in the output image*

*draw.text(((face.bounding\_poly.vertices)\[0\].x,*

*(face.bounding\_poly.vertices)\[0\].y - 30),*

*str(format(face.detection\_confidence, '.3f')) + '%',*

*fill='\#FF0000')*

*im.save(output\_filename)*

publish.py {#publish.py .Header2dora1}
----------

[]{#_Hlk11435407 .anchor}Create a python script called *publish.py*
using the code below. It will retreive the data from the light sensor
and publish via mqtt.

def publish\_messages(project\_id, topic\_name,data):

"""Publishes multiple messages to a Pub/Sub topic."""

\# \[START pubsub\_quickstart\_publisher\]

\# \[START pubsub\_publish\]

from google.cloud import pubsub\_v1

data = str(data)

publisher = pubsub\_v1.PublisherClient()

\# The \`topic\_path\` method creates a fully qualified identifier

\# in the form \`projects/{project\_id}/topics/{topic\_name}\`

topic\_path = publisher.topic\_path(project\_id, topic\_name)

print(topic\_path)

\# Data must be a bytestring

print("data :" + data)

data = data.encode('utf-8')

\# When you publish a message, the client returns a future.

future = publisher.publish(topic\_path, data=data)

print(future.result())

print('Published messages.')

receive.py {#receive.py .Header2dora1}
----------

Create a python script called *retreive.py* using the code below which
allows for subscribing data from mqtt.

def receive\_messages():

"""Receives messages from a pull subscription."""

\# \[START pubsub\_subscriber\_async\_pull\]

\# \[START pubsub\_quickstart\_subscriber\]

import time

from google.cloud import pubsub\_v1

project\_id = "gungnir-249212"

topic\_name = "data"

subscription\_name = "test\_sub"

subscriber = pubsub\_v1.SubscriberClient()

\# The \`subscription\_path\` method creates a fully qualified
identifier

\# in the form
\`projects/{project\_id}/subscriptions/{subscription\_name}\`

subscription\_path = subscriber.subscription\_path(

project\_id, subscription\_name)

def callback(message):

print('Received message: {}'.format(message))

message.ack()

subscriber.subscribe(subscription\_path, callback=callback)

\# The subscriber is non-blocking. We must keep the main thread from

\# exiting to allow it to process messages asynchronously in the
background.

print('Listening for messages on {}'.format(subscription\_path))

while True:

time.sleep(5)

**-- End of CA2 Step-by-step tutorial --**
