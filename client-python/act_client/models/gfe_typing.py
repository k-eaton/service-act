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


class GfeTyping(object):
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
        'gfe': 'str',
        'features_shared': 'int',
        'shares': 'list[Feature]'
    }

    attribute_map = {
        'gfe': 'gfe',
        'features_shared': 'features_shared',
        'shares': 'shares'
    }

    def __init__(self, gfe=None, features_shared=None, shares=None):
        """
        GfeTyping - a model defined in Swagger
        """

        self._gfe = None
        self._features_shared = None
        self._shares = None

        if gfe is not None:
          self.gfe = gfe
        if features_shared is not None:
          self.features_shared = features_shared
        if shares is not None:
          self.shares = shares

    @property
    def gfe(self):
        """
        Gets the gfe of this GfeTyping.

        :return: The gfe of this GfeTyping.
        :rtype: str
        """
        return self._gfe

    @gfe.setter
    def gfe(self, gfe):
        """
        Sets the gfe of this GfeTyping.

        :param gfe: The gfe of this GfeTyping.
        :type: str
        """

        self._gfe = gfe

    @property
    def features_shared(self):
        """
        Gets the features_shared of this GfeTyping.

        :return: The features_shared of this GfeTyping.
        :rtype: int
        """
        return self._features_shared

    @features_shared.setter
    def features_shared(self, features_shared):
        """
        Sets the features_shared of this GfeTyping.

        :param features_shared: The features_shared of this GfeTyping.
        :type: int
        """

        self._features_shared = features_shared

    @property
    def shares(self):
        """
        Gets the shares of this GfeTyping.

        :return: The shares of this GfeTyping.
        :rtype: list[Feature]
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """
        Sets the shares of this GfeTyping.

        :param shares: The shares of this GfeTyping.
        :type: list[Feature]
        """

        self._shares = shares

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
        if not isinstance(other, GfeTyping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
