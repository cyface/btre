Udemy Django Dev to Deployment Class Project
--------------------------------------------

URL To Class: https://www.udemy.com/python-django-dev-to-deployment

This is my interpretation of what he builds in this class.

I chose to use Class-Based Generic Views, and the Django Forms module in my implementation.

I checked in the media directory, which normally you wouldn't do - but I didn't want to re-upload the data every time I moved between machines.

This project requires Python 3 - I used Python 3.7 and PyCharm.

I created Template Tags for the Listing Tile and Realtor tile to avoid having that HTML in multiple places throughout the app.

I renamed the 'btre' module to 'project', which is a standard I've seen elsewhere that makes it easier to find things across projects.

Docker Configuration
--------------------
Once you have Docker installed in your environment, you can get this going with Docker by running `./cicd/docker-compose/update.sh`

The first time you run, you will then need to run `./cicd/docker-compose/init.sh` to load sample data.

The MEDIA_ROOT is set as a volume, so once you've run this, you won't be able to re-load the starting media files.

If you want to delete all the images and such: `docker-compose down` (from the root of this project.)
