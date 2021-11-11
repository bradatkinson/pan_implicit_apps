# pan_implicit_apps

A script for finding app dependencies for a given App-ID

## Built With
 
[Palo Alto Networks PAN-OS SDK for Python](https://github.com/PaloAltoNetworks/pan-os-python)

## Deployment

All files within the folder should be deployed in the same directory for proper file execution.

## Prerequisites

Update `config.py` file with correct values before operating.

```
# CONNECTIVITY CONFIGURATIONS

paloalto = {
    'username': '<USERNAME>',
    'password': '<PASSWORD>',
    'key': '<API_KEY>',
    'fw_ip': '<FIREWALL_IP>
    }
```

## Operating

From the CLI, change directory into the folder containing the files.  The following command will execute the script:

```bash
python pan_implicit_apps.py -a active-directory-base
```

For help:
```bash
python pan_implicit_apps.py -h
usage: pan_implicit_apps.py [-h] -a

To get implicit applications

optional arguments:
  -h, --help   show this help message and exit
  -a , --app   The app to check
```

## Changelog

See the [CHANGELOG](CHANGELOG) file for details

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
