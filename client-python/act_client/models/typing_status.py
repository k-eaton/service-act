# coding: utf-8

"""
    Allele Calling Service

    The Allele Calling  service provides an API for converting raw sequence data to GFE and HLA allele calls.

    OpenAPI spec version: 0.0.4
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TypingStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'str',
        'novel_features': 'list[Feature]'
    }

    attribute_map = {
        'status': 'status',
        'novel_features': 'novel_features'
    }

    def __init__(self, status=None, novel_features=None):
        """
        TypingStatus - a model defined in Swagger
        """

        self._status = None
        self._novel_features = None

        if status is not None:
          self.status = status
        if novel_features is not None:
          self.novel_features = novel_features

    @property
    def status(self):
        """
        Gets the status of this TypingStatus.

        :return: The status of this TypingStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TypingStatus.

        :param status: The status of this TypingStatus.
        :type: str
        """

        self._status = status

    @property
    def novel_features(self):
        """
        Gets the novel_features of this TypingStatus.

        :return: The novel_features of this TypingStatus.
        :rtype: list[Feature]
        """
        return self._novel_features

    @novel_features.setter
    def novel_features(self, novel_features):
        """
        Sets the novel_features of this TypingStatus.

        :param novel_features: The novel_features of this TypingStatus.
        :type: list[Feature]
        """

        self._novel_features = novel_features

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TypingStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
