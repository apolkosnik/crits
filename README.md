# Welcome to CRITs

![Image](https://github.com/crits/crits/raw/master/extras/www/new_images/crits_logo.png)

## What Is CRITs?

CRITs is a web-based tool which combines an analytic engine with a cyber threat database that not only serves as a repository for attack data and malware, but also provides analysts with a powerful platform for conducting malware analyses, correlating malware, and for targeting data. These analyses and correlations can also be saved and exploited within CRITs. CRITs employs a simple but very useful hierarchy to structure cyber threat information. This structure gives analysts the power to 'pivot' on metadata to discover previously unknown related content.

Visit our [website](https://crits.github.io) for more information, documentation, and links to community content such as our mailing lists and IRC channel.

# Installation

CRITs has been modernized to work with Python 3.10+ and Django 4.2+ LTS. The system supports modern 64-bit architectures including Ubuntu 22.04+, RHEL8+, and other contemporary Linux distributions. Installation is also supported on macOS and can be deployed using Docker for containerized environments.

**System Requirements:**
- Python 3.10 or higher
- Django 4.2+ LTS
- MongoEngine 0.27+
- MongoDB 6.0+
- 64-bit architecture recommended

**Modernization Summary:**
This CRITs installation has been updated from legacy versions:
- **Python**: 2.7 → 3.10+
- **Django**: 1.x → 4.2.23 LTS
- **MongoEngine**: 0.8 → 0.29.1
- **MongoDB**: Updated to 6.0+ compatibility

## Docker Installation (Recommended)

The easiest way to get started with modernized CRITs is using Docker:

```bash
# Build the CRITs container
docker build -t crits-modernized .

# Run CRITs with MongoDB
docker run -d -p 8080:8080 --name crits-app crits-modernized
```

The Docker container includes:
- Ubuntu 22.04 LTS base
- Python 3.10+ runtime
- Django 4.2+ framework
- MongoEngine 0.27+ ODM
- MongoDB 6.0 database
- All dependencies pre-installed

## Quick install using bootstrap

CRITs comes with a bootstrap script which will help you:

* Install all of the dependencies (requires Python 3.10+).
* Configure CRITs for database connectivity and your first admin user.
* Get MongoDB running with default settings.
* Use Django's runserver to quickly get you up and running with the CRITs interface.

**Prerequisites:** Ensure you have Python 3.10+, pip3, and MongoDB installed.

Just run the following:

```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Run the bootstrap script
sh script/bootstrap
```

Once you've run bootstrap once, do not use it again to get the runserver going, you'll be going through the install process again. Instead use the server script:

```bash
# Start the development server
python3 manage.py runserver 0.0.0.0:8080
```

## Production CRITs install

If you are looking for a more permanent and performant CRITs installation or just interested in tweaking things, read more about setting up CRITs for [production](https://github.com/crits/crits/wiki/Production-grade-CRITs-install).

## What's next?

We recommend adding services to your CRITs install. Services extend the features and functionality of the core project allowing you to enhance CRITs based on your needs. You can find more information about how to do this [here](https://github.com/crits/crits/wiki/Adding-services-to-CRITs).

**Thanks for using CRITs!**
