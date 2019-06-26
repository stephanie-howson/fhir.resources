#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/Meta) on 2019-06-25.
#  2019, SMART Health IT.


from . import element

class Meta(element.Element):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    
    resource_type = "Meta"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.versionId = None
        """ Version specific identifier.
        Type `str`. """
        
        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.source = None
        """ Identifies where the resource comes from.
        Type `str`. """
        
        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `str` items. """
        
        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.tag = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(Meta, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("versionId", "versionId", str, False, None, False),
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("source", "source", str, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
        ])
        return js


from . import fhirdate
from . import coding
