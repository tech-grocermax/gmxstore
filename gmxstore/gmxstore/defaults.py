
MESSAGE = "Grocermax Play Store"

# Fully read every request to ensure the nginx and uwsgi play nice
FORCE_READ_REQUESTS = True
CONTENT_TYPE = "application/json"
APK_PATH = "/home/ubuntu/gmxstore/gmxstore/gmxstore/static/apk"
PACKAGE_DETAILS = {
    "CrateManagement": {
        "id": "1",
        "name": "Crate Management",
        "package": "com.rgretail.cratemanagement.activity",
        "version_code": "2",
        "icon": "crate.png"
    },
    "CSAllocation": {
        "id": "2",
        "name": "CS Allocation",
        "package": "com.rgretail.grocermaxnewapp",
        "version_code": "2",
        "icon": "csallocation.png"
    },
    "CDI": {
        "id": "3",
        "name": "Cross Dock Indent",
        "package": "com.rgretail.crossdockindent",
        "version_code": "1",
        "icon": "csallocation.png"
    },
    "FTP_Support": {
        "id": "4",
        "name": "FTP Support",
        "package": "com.rgretail.ftpuchasesupportapp",
        "version_code": "1",
        "icon": "csallocation.png"
    },
    "FT_Purchase": {
        "id": "5",
        "name": "FT Purchase",
        "package": "com.rgretail.grocermaxcrate",
        "version_code": "1",
        "icon": "csallocation.png"
    },
    "PAI": {
        "id": "6",
        "name": "Put Away Indent",
        "package": "com.rgretail.putawaypicklist",
        "version_code": "1",
        "icon": "csallocation.png"
    },
    "PickList": {
        "id": "7",
        "name": "Pick List",
        "package": "com.rgretail.picklist",
        "version_code": "4",
        "icon": "csallocation.png"
    },
    "WareHouse_Operation": {
        "id": "8",
        "name": "Warehouse Operation",
        "package": "com.rgretail.warehouseoperation",
        "version_code": "2",
        "icon": "csallocation.png"
    },
    "Core_Operation": {
        "id": "9",
        "name": "Core Operation App",
        "package": "com.rgretail.coreoperationapp",
        "version_code": "1",
        "icon": "coreoperations.png"
    },
    "GRN": {
        "id": "10",
        "name": "GRN App",
        "package": "com.rgretail.grn",
        "version_code": "4",
        "icon": "grn.png"
    },
    "IA_App": {
        "id": "11",
        "name": "IA App",
        "package": "com.rgretail.iaapp",
        "version_code": "4",
        "icon": "iaa.png"
    },
}

# Default logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(hostname)s | %(asctime)s | %(levelname)s | %(name)s | %(message)s"
        }
    },
    "filters": {
        "add_hostname": {
            "()": "timber.filters.HostnameAddingFilter"
        }
    },
    "handlers": {
        "file_handler": {
            "class": "logging.handlers.WatchedFileHandler",
            "formatter": "simple",
            "filename": "/var/log/gmxstore/gmxstore.log",
            "filters": ["add_hostname"]
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["file_handler"]
    },
}
