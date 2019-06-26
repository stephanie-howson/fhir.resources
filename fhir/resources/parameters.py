#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2019-06-25.
#  2019, SMART Health IT.


from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """
    
    resource_type = "Parameters"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.parameter = None
        """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(Parameters, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True, None, False),
        ])
        return js


from . import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.
    
    A parameter passed to or received from the operation.
    """
    
    resource_type = "ParametersParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name from the definition.
        Type `str`. """
        
        self.valueBase64Binary = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueBoolean = None
        """ If parameter is a data type.
        Type `bool`. """
        
        self.valueCanonical = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueCode = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """
        
        self.valueId = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueInstant = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueMarkdown = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueOid = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valuePositiveInt = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueString = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUnsignedInt = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueUri = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueUrl = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueUuid = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ If parameter is a data type.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ If parameter is a data type.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDistance = None
        """ If parameter is a data type.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ If parameter is a data type.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ If parameter is a data type.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueTiming = None
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ If parameter is a data type.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ If parameter is a data type.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ If parameter is a data type.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ If parameter is a data type.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueParameterDefinition = None
        """ If parameter is a data type.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ If parameter is a data type.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ If parameter is a data type.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUsageContext = None
        """ If parameter is a data type.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ If parameter is a data type.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.part = None
        """ Named part of a multi-part parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(ParametersParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCanonical", "valueCanonical", str, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("valueUrl", "valueUrl", str, False, "value", False),
            ("valueUuid", "valueUuid", str, False, "value", False),
            ("valueAddress", "valueAddress", address.Address, False, "value", False),
            ("valueAge", "valueAge", age.Age, False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("valueCount", "valueCount", count.Count, False, "value", False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("valueMoney", "valueMoney", money.Money, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("part", "part", ParametersParameter, True, None, False),
        ])
        return js


from . import fhirdate
from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import count
from . import distance
from . import duration
from . import humanname
from . import identifier
from . import money
from . import period
from . import quantity
from . import range
from . import ratio
from . import fhirreference
from . import sampleddata
from . import signature
from . import timing
from . import contactdetail
from . import contributor
from . import datarequirement
from . import expression
from . import parameterdefinition
from . import relatedartifact
from . import triggerdefinition
from . import usagecontext
from . import dosage
