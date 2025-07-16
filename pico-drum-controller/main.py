from ota import OTAUpdater
from secrets import secrets

ota_updater = OTAUpdater(secrets['ssid'], secrets['password'], secrets['url'], secrets['filename'])

ota_updater.download_and_install_update_if_available()

#did it work?
