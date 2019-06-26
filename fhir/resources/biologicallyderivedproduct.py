#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct) on 2019-06-25.
#  2019, SMART Health IT.


from . import domainresource

class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.
    
    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    
    resource_type = "BiologicallyDerivedProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.productCategory = None
        """ organ | tissue | fluid | cells | biologicalAgent.
        Type `str`. """
        
        self.productCode = None
        """ What this biologically derived product is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ available | unavailable.
        Type `str`. """
        
        self.request = None
        """ Procedure request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The amount of this biologically derived product.
        Type `int`. """
        
        self.parent = None
        """ BiologicallyDerivedProduct parent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.collection = None
        """ How this product was collected.
        Type `BiologicallyDerivedProductCollection` (represented as `dict` in JSON). """
        
        self.processing = None
        """ Any processing of the product during collection.
        List of `BiologicallyDerivedProductProcessing` items (represented as `dict` in JSON). """
        
        self.manipulation = None
        """ Any manipulation of product post-collection.
        Type `BiologicallyDerivedProductManipulation` (represented as `dict` in JSON). """
        
        self.storage = None
        """ Product storage.
        List of `BiologicallyDerivedProductStorage` items (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("productCode", "productCode", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
        ])
        return js


from . import backboneelement

class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """
    
    resource_type = "BiologicallyDerivedProductCollection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collector = None
        """ Individual performing collection.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who is product from.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.collectedDateTime = None
        """ Time of product collection.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        """ Time of product collection.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
        ])
        return js


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.
    
    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """
    
    resource_type = "BiologicallyDerivedProductProcessing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of of processing.
        Type `str`. """
        
        self.procedure = None
        """ Procesing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additive = None
        """ Substance added during processing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timeDateTime = None
        """ Time of processing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        """ Time of processing.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("additive", "additive", fhirreference.FHIRReference, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.
    
    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """
    
    resource_type = "BiologicallyDerivedProductManipulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of manipulation.
        Type `str`. """
        
        self.timeDateTime = None
        """ Time of manipulation.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        """ Time of manipulation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductManipulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """
    
    resource_type = "BiologicallyDerivedProductStorage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of storage.
        Type `str`. """
        
        self.temperature = None
        """ Storage temperature.
        Type `float`. """
        
        self.scale = None
        """ farenheit | celsius | kelvin.
        Type `str`. """
        
        self.duration = None
        """ Storage timeperiod.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductStorage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("temperature", "temperature", float, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("duration", "duration", period.Period, False, None, False),
        ])
        return js


from . import identifier
from . import codeableconcept
from . import fhirreference
from . import fhirdate
from . import period
