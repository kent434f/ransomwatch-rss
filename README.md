# RansomWatch RSS Feed Generator

📰 RSS Link:  [https://ransom.lexter.xyz/feed.xml](https://ransom.lexter.xyz/feed.xml)

This repository contains a Python script, `generate_feed.py`, that generates an Atom XML feed for the latest ransomware attacks, based on data from [joshhighet/ransomwatch](https://github.com/joshhighet/ransomwatch).
As RansomWatch does not currently offer a live RSS feed, this script provides an alternative solution.
The script fetches data from the RansomWatch, processes it to extract relevant information, and generates an RSS feed.
The generated feed is automatically updated every 30 minutes using GitHub Actions.

## Overview

The `generate_feed.py` script performs the following tasks:

1. Fetches ransomware attack data from a JSON file hosted on GitHub.
2. Processes the fetched data to extract relevant information.
3. Generates an Atom XML feed containing the processed data.
4. Saves the generated XML feed to a file named `feed.xml`.

The script is automatically run every 30 minutes using a GitHub Actions workflow defined in `.github/workflows/update_feed.yml`.

## Repository Structure

- `generate_feed.py`: The Python script that generates the ransomware feed.
- `.github/workflows/update_feed.yml`: The GitHub Actions workflow file that automates the feed generation process.
- `feed.xml`: The generated Atom XML feed file containing the ransomware attack data.

## Usage

To use this script in your own project:

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required dependencies.
4. Customize the `JSON_URL` variable in `generate_feed.py` to point to your desired JSON data source.
5. Run the script using `python generate_feed.py`.

The generated `feed.xml` file will be created in the same directory as the script.

## Automation

The repository includes a GitHub Actions workflow that automates the process of generating the ransomware feed and updating the repository every 30 minutes. The workflow is defined in `.github/workflows/update_feed.yml`.

The workflow performs the following steps:

1. Checks out the repository code.
2. Sets up Python.
3. Installs the required dependencies.
4. Runs the `generate_feed.py` script.
5. Commits and pushes the changes to the `feed.xml` file.

## Acknowledgements
- [RansomWatch](https://ransomwatch.telemetry.ltd/) for providing the ransomware attack data
