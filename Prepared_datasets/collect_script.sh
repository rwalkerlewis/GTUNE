#!/bin/bash

# Define the URL of the webpage
URL="http://geophysics.eas.gatech.edu/people/lbarama/SRL_GTUNE_Repository/GTUNE/Prepared_datasets/"

# Use wget to download the HTML content of the page
wget -q -O - $URL |

# Parse the HTML content to find all links (href attributes)
grep -o '<a href=['"'"'"][^"'"'"']*['"'"'"]' |

# Extract the URLs from the href attributes
grep -o 'http[s]*://[^"]*' |

# Download each file linked on the page
while read -r line; do
    wget "$line"
done

