# coding: utf-8

"""
    Allele Calling Service

    The Allele Calling  service provides an API for converting raw sequence data to GFE and HLA allele calls.

    OpenAPI spec version: 0.0.3
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FeatureCall(object):
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
        'alleles': 'list[str]',
        'features_searched': 'list[str]',
        'matched': 'list[Typing]',
        'act_version': 'str',
        'gfe_version': 'str',
        'gfedb_version': 'str'
    }

    attribute_map = {
        'alleles': 'alleles',
        'features_searched': 'features_searched',
        'matched': 'matched',
        'act_version': 'act_version',
        'gfe_version': 'gfe_version',
        'gfedb_version': 'gfedb_version'
    }

    def __init__(self, alleles=None, features_searched=None, matched=None, act_version=None, gfe_version=None, gfedb_version=None):
        """
        FeatureCall - a model defined in Swagger
        """

        self._alleles = None
        self._features_searched = None
        self._matched = None
        self._act_version = None
        self._gfe_version = None
        self._gfedb_version = None

        if alleles is not None:
          self.alleles = alleles
        if features_searched is not None:
          self.features_searched = features_searched
        if matched is not None:
          self.matched = matched
        if act_version is not None:
          self.act_version = act_version
        if gfe_version is not None:
          self.gfe_version = gfe_version
        if gfedb_version is not None:
          self.gfedb_version = gfedb_version

    @property
    def alleles(self):
        """
        Gets the alleles of this FeatureCall.

        :return: The alleles of this FeatureCall.
        :rtype: list[str]
        """
        return self._alleles

    @alleles.setter
    def alleles(self, alleles):
        """
        Sets the alleles of this FeatureCall.

        :param alleles: The alleles of this FeatureCall.
        :type: list[str]
        """

        self._alleles = alleles

    @property
    def features_searched(self):
        """
        Gets the features_searched of this FeatureCall.

        :return: The features_searched of this FeatureCall.
        :rtype: list[str]
        """
        return self._features_searched

    @features_searched.setter
    def features_searched(self, features_searched):
        """
        Sets the features_searched of this FeatureCall.

        :param features_searched: The features_searched of this FeatureCall.
        :type: list[str]
        """

        self._features_searched = features_searched

    @property
    def matched(self):
        """
        Gets the matched of this FeatureCall.

        :return: The matched of this FeatureCall.
        :rtype: list[Typing]
        """
        return self._matched

    @matched.setter
    def matched(self, matched):
        """
        Sets the matched of this FeatureCall.

        :param matched: The matched of this FeatureCall.
        :type: list[Typing]
        """

        self._matched = matched

    @property
    def act_version(self):
        """
        Gets the act_version of this FeatureCall.

        :return: The act_version of this FeatureCall.
        :rtype: str
        """
        return self._act_version

    @act_version.setter
    def act_version(self, act_version):
        """
        Sets the act_version of this FeatureCall.

        :param act_version: The act_version of this FeatureCall.
        :type: str
        """

        self._act_version = act_version

    @property
    def gfe_version(self):
        """
        Gets the gfe_version of this FeatureCall.

        :return: The gfe_version of this FeatureCall.
        :rtype: str
        """
        return self._gfe_version

    @gfe_version.setter
    def gfe_version(self, gfe_version):
        """
        Sets the gfe_version of this FeatureCall.

        :param gfe_version: The gfe_version of this FeatureCall.
        :type: str
        """

        self._gfe_version = gfe_version

    @property
    def gfedb_version(self):
        """
        Gets the gfedb_version of this FeatureCall.

        :return: The gfedb_version of this FeatureCall.
        :rtype: str
        """
        return self._gfedb_version

    @gfedb_version.setter
    def gfedb_version(self, gfedb_version):
        """
        Sets the gfedb_version of this FeatureCall.

        :param gfedb_version: The gfedb_version of this FeatureCall.
        :type: str
        """

        self._gfedb_version = gfedb_version

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
        if not isinstance(other, FeatureCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
