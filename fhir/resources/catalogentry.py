#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-06-25.
#  2019, SMART Health IT.


from . import domainresource

class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.
    
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    
    resource_type = "CatalogEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier of the catalog entry.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Displayable name assigned to the catalog entry.
        Type `str`. """
        
        self.type = None
        """ ActivityDefinition | PlanDefinition | SpecimenDefinition |
        ObservationDefinition | DeviceDefinition | Organization |
        Practitioner | PractitionerRole | HealthcareService |
        MedicationKnowledge | Medication | Substance | Location.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.effectivePeriod = None
        """ When this catalog entry is expected to be active.
        Type `Period` (represented as `dict` in JSON). """
        
        self.orderable = None
        """ Is orderable.
        Type `bool`. """
        
        self.referencedItem = None
        """ Item attached to this entry of the catalog.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relatedEntry = None
        """ Another entry of the catalog related to this one.
        List of `CatalogEntryRelatedEntry` items (represented as `dict` in JSON). """
        
        self.updatedBy = None
        """ Last updater of this catalog entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
        """ Notes and comments about this catalog entry.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.billingCode = None
        """ Billing code in the context of this catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.billingSummary = None
        """ Billing summary in the context of this catalog entry.
        Type `str`. """
        
        self.scheduleSummary = None
        """ Schedule summary for the catalog entry.
        Type `str`. """
        
        self.limitationSummary = None
        """ Summary of limitations for the catalog entry.
        Type `str`. """
        
        self.regulatorySummary = None
        """ Regulatory  summary for the catalog entry.
        Type `str`. """
        
        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("status", "status", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("updatedBy", "updatedBy", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("billingCode", "billingCode", codeableconcept.CodeableConcept, True, None, False),
            ("billingSummary", "billingSummary", str, False, None, False),
            ("scheduleSummary", "scheduleSummary", str, False, None, False),
            ("limitationSummary", "limitationSummary", str, False, None, False),
            ("regulatorySummary", "regulatorySummary", str, False, None, False),
        ])
        return js


from . import backboneelement

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ Another entry of the catalog related to this one.
    
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    
    resource_type = "CatalogEntryRelatedEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relationship = None
        """ triggers | is-replaced-by | excludes | includes.
        Type `str`. """
        
        self.target = None
        """ The reference to the related entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("relationship", "relationship", str, False, None, True),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import identifier
from . import period
from . import fhirreference
from . import annotation
from . import codeableconcept
