import json
import xml.etree.ElementTree as ET
from datetime import datetime
import requests

def download_json_file(url, output_file):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, 'w') as file:
            json.dump(response.json(), file, indent=4)
        return response.json()
    else:
        raise Exception(f"Failed to download JSON file. Status code: {response.status_code}")

def generate_rss_feed(json_data, output_file):
    # Sort the JSON data based on the 'discovered' field in descending order
    sorted_data = sorted(json_data, key=lambda x: datetime.strptime(x['discovered'], '%Y-%m-%d %H:%M:%S.%f'), reverse=True)

    # Create the RSS root element
    rss = ET.Element('rss', {'version': '2.0'})
    channel = ET.SubElement(rss, 'channel')

    # Set the channel elements
    ET.SubElement(channel, 'title').text = 'RansomWatch'
    ET.SubElement(channel, 'link').text = 'https://ransomwatch.telemetry.ltd/#/recentposts'
    ET.SubElement(channel, 'description').text = 'Latest ransomware posts'

    # Iterate over the sorted JSON data and create items
    for item in sorted_data:
        post_title = item['post_title']
        group_name = item['group_name']
        discovered = datetime.strptime(item['discovered'], '%Y-%m-%d %H:%M:%S.%f')

        # Create an item element for each post
        item_element = ET.SubElement(channel, 'item')
        ET.SubElement(item_element, 'title').text = post_title
        ET.SubElement(item_element, 'description').text = f'Group: {group_name}'
        ET.SubElement(item_element, 'pubDate').text = discovered.strftime('%a, %d %b %Y %H:%M:%S +0000')
        ET.SubElement(item_element, 'guid').text = f'{post_title}_{discovered}'

    # Generate the RSS feed XML
    tree = ET.ElementTree(rss)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Usage example
json_url = 'https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json'
json_output_file = 'posts.json'
rss_output_file = 'feed.xml'

try:
    json_data = download_json_file(json_url, json_output_file)
    generate_rss_feed(json_data, rss_output_file)
    print("JSON file downloaded and RSS feed generated successfully.")
except Exception as e:
    print(f"Error: {str(e)}")
