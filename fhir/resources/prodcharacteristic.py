#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2019-06-25.
#  2019, SMART Health IT.


from . import backboneelement

class ProdCharacteristic(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    
    resource_type = "ProdCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.height = None
        """ Where applicable, the height can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.width = None
        """ Where applicable, the width can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.depth = None
        """ Where applicable, the depth can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.weight = None
        """ Where applicable, the weight can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.nominalVolume = None
        """ Where applicable, the nominal volume can be specified using a
        numerical value and its unit of measurement The unit of measurement
        shall be specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.externalDiameter = None
        """ Where applicable, the external diameter can be specified using a
        numerical value and its unit of measurement The unit of measurement
        shall be specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.shape = None
        """ Where applicable, the shape can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        Type `str`. """
        
        self.color = None
        """ Where applicable, the color can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        List of `str` items. """
        
        self.imprint = None
        """ Where applicable, the imprint can be specified as text.
        List of `str` items. """
        
        self.image = None
        """ Where applicable, the image can be provided The format of the image
        attachment shall be specified by regional implementations.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.scoring = None
        """ Where applicable, the scoring can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProdCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("height", "height", quantity.Quantity, False, None, False),
            ("width", "width", quantity.Quantity, False, None, False),
            ("depth", "depth", quantity.Quantity, False, None, False),
            ("weight", "weight", quantity.Quantity, False, None, False),
            ("nominalVolume", "nominalVolume", quantity.Quantity, False, None, False),
            ("externalDiameter", "externalDiameter", quantity.Quantity, False, None, False),
            ("shape", "shape", str, False, None, False),
            ("color", "color", str, True, None, False),
            ("imprint", "imprint", str, True, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import quantity
from . import attachment
from . import codeableconcept
