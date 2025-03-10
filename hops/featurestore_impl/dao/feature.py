from hops import constants

class Feature(object):
    """
    Represents an individual feature in the feature store, either in a feature group or in a training dataset
    """

    def __init__(self, feature_json):
        """
        Initialize the feature from JSON payload

        Args:
            :feature_json: JSON data about the feature returned from Hopsworks REST API
        """
        self.name = feature_json[constants.REST_CONFIG.JSON_FEATURE_NAME]
        self.type = feature_json[constants.REST_CONFIG.JSON_FEATURE_TYPE]
        self.description = feature_json[constants.REST_CONFIG.JSON_FEATURE_DESCRIPTION]
        self.primary = feature_json[constants.REST_CONFIG.JSON_FEATURE_PRIMARY]
        self.partition = feature_json[constants.REST_CONFIG.JSON_FEATURE_PARTITION]