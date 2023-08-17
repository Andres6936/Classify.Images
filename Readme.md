### Project with Tensorflow

This project uses Tensorflow to classify images in format webp that were scraped 
from of ECommerce. The scraper download the images of site, but these images 
have meaningless numbers as file name, so the idea is to use Tensorflow to classify
and sort these images into directories for later use.

The process currently has three stages, the first is the scrapper, the seconds is the
classification of these images and the third stage is move these images to the
corresponding directory to give in the order imposed in the second stage.

### Deleting webp repeat with hash function

After the process of downloading of the images by the scrapper, it is convenient to 
eliminate the images that are repeated, leaving only one imagen and eliminating the
remaining repeated images, for this process the hashes of the images download are
calculated and nay hash with more than one coincidence is eliminated until leaving
only one image, avoiding repetition.


### Using SQLite for save information in intermediate process



### How to Start

1. Clone the repository for the project to your local machine.
2. Navigate to the directory for the project in your terminal. 
3. Install the packages that are required for the project by running the following command:

`pipenv install`

This will install the packages that are listed in the Pipfile and Pipfile.lock files.

4. To activate the virtual environment for the project, run the following command:

`pipenv shell`

This will change your shell environment to use the packages that are installed in the project's virtual environment.

5. Once you are in the virtual environment, you can start working on the project. You can install additional packages, run Python scripts, and use any other tools that you need for the project.
6. To exit the virtual environment, run the following command:

`exit`

This will return you to your normal shell environment.

### How to Start the service

The command for start the service:

`uvicorn App:app --reload`
