#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2019-06-25.
#  2019, SMART Health IT.


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    
    resource_type = "Procedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.basedOn = None
        """ A request for this procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ The Encounter during which this Procedure was created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the procedure occurred or is occurring.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When the procedure occurred or is occurring.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceString = None
        """ When the procedure occurred or is occurring.
        Type `str`. """
        
        self.occurrenceAge = None
        """ When the procedure occurred or is occurring.
        Type `Age` (represented as `dict` in JSON). """
        
        self.occurrenceRange = None
        """ When the procedure occurred or is occurring.
        Type `Range` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When the procedure occurred or is occurring.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.recorded = None
        """ When the procedure was first captured in the subject's record.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        """ Who recorded the procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reportedBoolean = None
        """ Reported rather than primary record.
        Type `bool`. """
        
        self.reportedReference = None
        """ Reported rather than primary record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ The justification that the procedure was performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complicationDetail = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.focalDevice = None
        """ Manipulated, implanted, or removed device.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.usedReference = None
        """ Items used during procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.usedCode = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", False),
            ("occurrenceAge", "occurrenceAge", age.Age, False, "occurrence", False),
            ("occurrenceRange", "occurrenceRange", range.Range, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("reportedBoolean", "reportedBoolean", bool, False, "reported", False),
            ("reportedReference", "reportedReference", fhirreference.FHIRReference, False, "reported", False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    
    Limited to "real" people rather than equipment.
    """
    
    resource_type = "ProcedurePerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ The reference to the practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.
    
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    
    resource_type = "ProcedureFocalDevice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import identifier
from . import fhirreference
from . import codeableconcept
from . import fhirdate
from . import period
from . import age
from . import range
from . import timing
from . import annotation
