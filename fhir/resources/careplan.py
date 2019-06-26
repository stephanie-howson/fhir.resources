#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2019-06-25.
#  2019, SMART Health IT.


from . import domainresource

class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.
    
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    
    resource_type = "CarePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.basedOn = None
        """ Fulfills CarePlan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        """ CarePlan replaced by this CarePlan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced CarePlan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | completed | entered-in-error |
        cancelled | unknown.
        Type `str`. """
        
        self.intent = None
        """ proposal | plan | order | option.
        Type `str`. """
        
        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Human-friendly name for the care plan.
        Type `str`. """
        
        self.description = None
        """ Summary of nature of plan.
        Type `str`. """
        
        self.subject = None
        """ Who the care plan is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ The Encounter during which this CarePlan was created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.created = None
        """ Date record was first recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ Who is the designated responsible party.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contributor = None
        """ Who provided the content of the care plan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ Who's involved in plan?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.addressesCode = None
        """ Health issues this plan addresses.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.addressesReference = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Information considered as part of plan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.goal = None
        """ Desired outcome of plan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the plan.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(CarePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("title", "title", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("careTeam", "careTeam", fhirreference.FHIRReference, True, None, False),
            ("addressesCode", "addressesCode", codeableconcept.CodeableConcept, True, None, False),
            ("addressesReference", "addressesReference", fhirreference.FHIRReference, True, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


from . import backboneelement

class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.
    
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    
    resource_type = "CarePlanActivity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcomeCodeableConcept = None
        """ Results of the activity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ Appointment, Encounter, Procedure, etc..
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.progress = None
        """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.detail = None
        """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """
        
        super(CarePlanActivity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("outcomeCodeableConcept", "outcomeCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("progress", "progress", annotation.Annotation, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
        ])
        return js


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.
    
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    
    resource_type = "CarePlanActivityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.kind = None
        """ Kind of resource.
        Type `str`. """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why activity should be done or why activity was prohibited.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why activity is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled | stopped | unknown | entered-in-error.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doNotPerform = None
        """ If true, activity is prohibiting action.
        Type `bool`. """
        
        self.scheduledTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.scheduledPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledString = None
        """ When activity is to occur.
        Type `str`. """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reportedBoolean = None
        """ Reported rather than primary record.
        Type `bool`. """
        
        self.reportedReference = None
        """ Reported rather than primary record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        """ What is to be administered/supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dailyAmount = None
        """ How to consume/day?.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Extra info describing activity to perform.
        Type `str`. """
        
        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("kind", "kind", str, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("reportedBoolean", "reportedBoolean", bool, False, "reported", False),
            ("reportedReference", "reportedReference", fhirreference.FHIRReference, False, "reported", False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("dailyAmount", "dailyAmount", quantity.Quantity, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


from . import identifier
from . import fhirreference
from . import codeableconcept
from . import period
from . import fhirdate
from . import annotation
from . import timing
from . import quantity
