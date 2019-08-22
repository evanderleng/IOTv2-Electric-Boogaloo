Python Gungnir
==================================

|alpha| |pypi| |versions| 

# Overview of project

Our project, takes images using the camera every predefined seconds, feeds it into a cloud bucket and performs image recognition on it. It has been preconfigured to identify faces and highlight them. Currently it is performing the function of security camera, thus when it recognises a person, it will email the owner and issue a verbal warning to the visitor.It has been attached to servos to allow movement of the camera however this application is infinitely dynamic, allowing it to be used for a variety of other purposes such as as being able to be configured for Optical character recognition and other artificial intelligence purposes.


Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud AutoML API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud AutoML API.:  https://cloud.google.com/automl
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 2.7

Deprecated Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Python == 2.7. Python 2.7 support will be removed on January 1, 2020.

## Installation

To implement the google cloud functions, the libraries need to be installed on the Raspberry Pi. 
Install Google Cloud Storage (https://pypi.org/project/google-cloud-storage/)

```bash
sudo pip install google-cloud-storage
```
Install Google Cloud Vision (https://pypi.org/project/google-cloud-vision/)
```bash
sudo  install google-cloud-vision
```

Install Pillow (https://pypi.org/project/Pillow/2.2.1)
```bash
sudo  pip install Pillow
```
To implement MySQL database, the MySQL libraries need to be installed. If you are using the ST0324 IoT Raspbian image, you might encounter an error as the libraries have already been pre-installed. If you are using a fresh image, you would need to run the commands below to install the MySQL libraries.

```bash
sudo pip install mysql-connector-python
sudo pip install mysql-connector
```
Finally, install the pubsub libararies needed to send mqtt data

```bash
sudo pip install google-cloud-pubsub
```

## Authentication

If you want to run all programs, you will need a billing-enabled GCP project, and a service account with access to the APIs.
```bash
export PROJECT_ID=<project-id> GOOGLE_APPLICATION_CREDENTIALS=</path/to/creds.json>
```
## Hardware
- 1x Raspberry pi
- 1x Raspberry pi camera
- 1x Breadboard
- 2x SG90 servo
- 2x AA battery packs
- 1x Light-Dependant Resistor
- 1x Light-emitting diode
- 1x Speaker
- 1x AUX Cable
- 1x Portable Charger

## Authors

* **Davis Zheng** - *Initial work* - [Nonsour/Nonsouris](https://github.com/nonsour)


## Acknowledgments

* Thanks to Ms Dora Chua for her guidance


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
