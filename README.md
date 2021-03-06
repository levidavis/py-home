# py-home

This is a fork of [Cameron Gray's](https://github.com/camerongray1515/) [Home-Automation-Hub](https://github.com/home-automation-hub/home-automation-hub/), which (hopefully) i will be keeping up-to-date.

## Getting Started

### Requirements
- Ubuntu 18.04 or above
- Docker installed, [docs are here](https://docs.docker.com/get-docker/)
- Baisc Knowledge of: Docker, Linux and Python

### Basic install

Commands may differ between machines, im using Ubuntu Server 18.04 LTS.

First we need to download the files and go into the directory

```
git clone https://github.com/levidavis/py-home.git
cd py-home/
```
Now we need to use the 'Make' command to make our docker image, you dont have to run it as root but personally i needed to to allowed docker commands

```
sudo make
```
once the docker image is made we run the docker multi-container in what i like to call "Test Mode" it basically shows us a log of what is happening just in case there is any problems
```
sudo docker-compose up
```
if there is no problem running the docker then we can go and close it using Ctrl + C
```
Ctrl + C
```
now we need to get the docker containter running in the background using this command:
```
sudo dokcer-compose up -d
```
lets visit the hub now!
```
Goto: http://{IP ADDRESS}:8080/
```
Done! , What's next? i would suggest looking at the [Modules Section](README.md#-Modules)

### Customized Install
Commands may differ between machines, im using Ubuntu Server 18.04 LTS.

First we need to download the files and go into the directory

```
git clone https://github.com/levidavis/py-home.git
cd py-home/
```
Now lets customize!

##### Change Web Port
All we need to do is change the docker-compose file!
```
nano docker-compose.yml
```
and go down line 20 and edit this (Default port is 8080):
```
 -{PORT YOU WANT}:80
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
