#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 on 2019-06-25.
#  2019, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".
        
        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        if "Element" == resource_type:
            from . import element
            return element.Element(jsondict)
        if "BackboneElement" == resource_type:
            from . import backboneelement
            return backboneelement.BackboneElement(jsondict)
        if "Address" == resource_type:
            from . import address
            return address.Address(jsondict)
        if "Age" == resource_type:
            from . import age
            return age.Age(jsondict)
        if "Annotation" == resource_type:
            from . import annotation
            return annotation.Annotation(jsondict)
        if "Attachment" == resource_type:
            from . import attachment
            return attachment.Attachment(jsondict)
        if "CodeableConcept" == resource_type:
            from . import codeableconcept
            return codeableconcept.CodeableConcept(jsondict)
        if "Coding" == resource_type:
            from . import coding
            return coding.Coding(jsondict)
        if "ContactDetail" == resource_type:
            from . import contactdetail
            return contactdetail.ContactDetail(jsondict)
        if "ContactPoint" == resource_type:
            from . import contactpoint
            return contactpoint.ContactPoint(jsondict)
        if "Contributor" == resource_type:
            from . import contributor
            return contributor.Contributor(jsondict)
        if "Count" == resource_type:
            from . import count
            return count.Count(jsondict)
        if "DataRequirement" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirement(jsondict)
        if "DataRequirementCodeFilter" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementCodeFilter(jsondict)
        if "DataRequirementDateFilter" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementDateFilter(jsondict)
        if "DataRequirementSort" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementSort(jsondict)
        if "Distance" == resource_type:
            from . import distance
            return distance.Distance(jsondict)
        if "Dosage" == resource_type:
            from . import dosage
            return dosage.Dosage(jsondict)
        if "DosageDoseAndRate" == resource_type:
            from . import dosage
            return dosage.DosageDoseAndRate(jsondict)
        if "Duration" == resource_type:
            from . import duration
            return duration.Duration(jsondict)
        if "ElementDefinition" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinition(jsondict)
        if "ElementDefinitionSlicing" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicing(jsondict)
        if "ElementDefinitionSlicingDiscriminator" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicingDiscriminator(jsondict)
        if "ElementDefinitionBase" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBase(jsondict)
        if "ElementDefinitionType" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionType(jsondict)
        if "ElementDefinitionExample" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionExample(jsondict)
        if "ElementDefinitionConstraint" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionConstraint(jsondict)
        if "ElementDefinitionBinding" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBinding(jsondict)
        if "ElementDefinitionMapping" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionMapping(jsondict)
        if "Expression" == resource_type:
            from . import expression
            return expression.Expression(jsondict)
        if "Extension" == resource_type:
            from . import extension
            return extension.Extension(jsondict)
        if "HumanName" == resource_type:
            from . import humanname
            return humanname.HumanName(jsondict)
        if "Identifier" == resource_type:
            from . import identifier
            return identifier.Identifier(jsondict)
        if "MarketingStatus" == resource_type:
            from . import marketingstatus
            return marketingstatus.MarketingStatus(jsondict)
        if "Meta" == resource_type:
            from . import meta
            return meta.Meta(jsondict)
        if "Money" == resource_type:
            from . import money
            return money.Money(jsondict)
        if "Narrative" == resource_type:
            from . import narrative
            return narrative.Narrative(jsondict)
        if "ParameterDefinition" == resource_type:
            from . import parameterdefinition
            return parameterdefinition.ParameterDefinition(jsondict)
        if "Period" == resource_type:
            from . import period
            return period.Period(jsondict)
        if "Population" == resource_type:
            from . import population
            return population.Population(jsondict)
        if "ProdCharacteristic" == resource_type:
            from . import prodcharacteristic
            return prodcharacteristic.ProdCharacteristic(jsondict)
        if "ProductShelfLife" == resource_type:
            from . import productshelflife
            return productshelflife.ProductShelfLife(jsondict)
        if "Quantity" == resource_type:
            from . import quantity
            return quantity.Quantity(jsondict)
        if "Range" == resource_type:
            from . import range
            return range.Range(jsondict)
        if "Ratio" == resource_type:
            from . import ratio
            return ratio.Ratio(jsondict)
        if "Reference" == resource_type:
            from . import reference
            return reference.Reference(jsondict)
        if "RelatedArtifact" == resource_type:
            from . import relatedartifact
            return relatedartifact.RelatedArtifact(jsondict)
        if "SampledData" == resource_type:
            from . import sampleddata
            return sampleddata.SampledData(jsondict)
        if "Signature" == resource_type:
            from . import signature
            return signature.Signature(jsondict)
        if "SubstanceAmount" == resource_type:
            from . import substanceamount
            return substanceamount.SubstanceAmount(jsondict)
        if "SubstanceAmountReferenceRange" == resource_type:
            from . import substanceamount
            return substanceamount.SubstanceAmountReferenceRange(jsondict)
        if "Timing" == resource_type:
            from . import timing
            return timing.Timing(jsondict)
        if "TimingRepeat" == resource_type:
            from . import timing
            return timing.TimingRepeat(jsondict)
        if "TriggerDefinition" == resource_type:
            from . import triggerdefinition
            return triggerdefinition.TriggerDefinition(jsondict)
        if "UsageContext" == resource_type:
            from . import usagecontext
            return usagecontext.UsageContext(jsondict)
        if "Quantity" == resource_type:
            from . import quantity
            return quantity.Quantity(jsondict)
        if "Resource" == resource_type:
            from . import resource
            return resource.Resource(jsondict)
        if "Account" == resource_type:
            from . import account
            return account.Account(jsondict)
        if "AccountCoverage" == resource_type:
            from . import account
            return account.AccountCoverage(jsondict)
        if "AccountGuarantor" == resource_type:
            from . import account
            return account.AccountGuarantor(jsondict)
        if "ActivityDefinition" == resource_type:
            from . import activitydefinition
            return activitydefinition.ActivityDefinition(jsondict)
        if "ActivityDefinitionParticipant" == resource_type:
            from . import activitydefinition
            return activitydefinition.ActivityDefinitionParticipant(jsondict)
        if "ActivityDefinitionDynamicValue" == resource_type:
            from . import activitydefinition
            return activitydefinition.ActivityDefinitionDynamicValue(jsondict)
        if "AdverseEvent" == resource_type:
            from . import adverseevent
            return adverseevent.AdverseEvent(jsondict)
        if "AdverseEventSuspectEntity" == resource_type:
            from . import adverseevent
            return adverseevent.AdverseEventSuspectEntity(jsondict)
        if "AdverseEventSuspectEntityCausality" == resource_type:
            from . import adverseevent
            return adverseevent.AdverseEventSuspectEntityCausality(jsondict)
        if "AllergyIntolerance" == resource_type:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict)
        if "AllergyIntoleranceReaction" == resource_type:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntoleranceReaction(jsondict)
        if "Appointment" == resource_type:
            from . import appointment
            return appointment.Appointment(jsondict)
        if "AppointmentParticipant" == resource_type:
            from . import appointment
            return appointment.AppointmentParticipant(jsondict)
        if "AppointmentResponse" == resource_type:
            from . import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict)
        if "AuditEvent" == resource_type:
            from . import auditevent
            return auditevent.AuditEvent(jsondict)
        if "AuditEventAgent" == resource_type:
            from . import auditevent
            return auditevent.AuditEventAgent(jsondict)
        if "AuditEventAgentNetwork" == resource_type:
            from . import auditevent
            return auditevent.AuditEventAgentNetwork(jsondict)
        if "AuditEventSource" == resource_type:
            from . import auditevent
            return auditevent.AuditEventSource(jsondict)
        if "AuditEventEntity" == resource_type:
            from . import auditevent
            return auditevent.AuditEventEntity(jsondict)
        if "AuditEventEntityDetail" == resource_type:
            from . import auditevent
            return auditevent.AuditEventEntityDetail(jsondict)
        if "Basic" == resource_type:
            from . import basic
            return basic.Basic(jsondict)
        if "Binary" == resource_type:
            from . import binary
            return binary.Binary(jsondict)
        if "BiologicallyDerivedProduct" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProduct(jsondict)
        if "BiologicallyDerivedProductCollection" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductCollection(jsondict)
        if "BiologicallyDerivedProductProcessing" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductProcessing(jsondict)
        if "BiologicallyDerivedProductManipulation" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductManipulation(jsondict)
        if "BiologicallyDerivedProductStorage" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductStorage(jsondict)
        if "BodyStructure" == resource_type:
            from . import bodystructure
            return bodystructure.BodyStructure(jsondict)
        if "Bundle" == resource_type:
            from . import bundle
            return bundle.Bundle(jsondict)
        if "BundleLink" == resource_type:
            from . import bundle
            return bundle.BundleLink(jsondict)
        if "BundleEntry" == resource_type:
            from . import bundle
            return bundle.BundleEntry(jsondict)
        if "BundleEntrySearch" == resource_type:
            from . import bundle
            return bundle.BundleEntrySearch(jsondict)
        if "BundleEntryRequest" == resource_type:
            from . import bundle
            return bundle.BundleEntryRequest(jsondict)
        if "BundleEntryResponse" == resource_type:
            from . import bundle
            return bundle.BundleEntryResponse(jsondict)
        if "CapabilityStatement" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatement(jsondict)
        if "CapabilityStatementSoftware" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementSoftware(jsondict)
        if "CapabilityStatementImplementation" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementImplementation(jsondict)
        if "CapabilityStatementRest" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRest(jsondict)
        if "CapabilityStatementRestSecurity" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestSecurity(jsondict)
        if "CapabilityStatementRestResource" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResource(jsondict)
        if "CapabilityStatementRestResourceInteraction" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceInteraction(jsondict)
        if "CapabilityStatementRestResourceSearchParam" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceSearchParam(jsondict)
        if "CapabilityStatementRestResourceOperation" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceOperation(jsondict)
        if "CapabilityStatementRestInteraction" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestInteraction(jsondict)
        if "CapabilityStatementMessaging" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessaging(jsondict)
        if "CapabilityStatementMessagingEndpoint" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingEndpoint(jsondict)
        if "CapabilityStatementMessagingSupportedMessage" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingSupportedMessage(jsondict)
        if "CapabilityStatementDocument" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementDocument(jsondict)
        if "CarePlan" == resource_type:
            from . import careplan
            return careplan.CarePlan(jsondict)
        if "CarePlanActivity" == resource_type:
            from . import careplan
            return careplan.CarePlanActivity(jsondict)
        if "CarePlanActivityDetail" == resource_type:
            from . import careplan
            return careplan.CarePlanActivityDetail(jsondict)
        if "CareTeam" == resource_type:
            from . import careteam
            return careteam.CareTeam(jsondict)
        if "CareTeamParticipant" == resource_type:
            from . import careteam
            return careteam.CareTeamParticipant(jsondict)
        if "CatalogEntry" == resource_type:
            from . import catalogentry
            return catalogentry.CatalogEntry(jsondict)
        if "CatalogEntryRelatedEntry" == resource_type:
            from . import catalogentry
            return catalogentry.CatalogEntryRelatedEntry(jsondict)
        if "ChargeItem" == resource_type:
            from . import chargeitem
            return chargeitem.ChargeItem(jsondict)
        if "ChargeItemPerformer" == resource_type:
            from . import chargeitem
            return chargeitem.ChargeItemPerformer(jsondict)
        if "ChargeItemDefinition" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinition(jsondict)
        if "ChargeItemDefinitionApplicability" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionApplicability(jsondict)
        if "ChargeItemDefinitionPropertyGroup" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionPropertyGroup(jsondict)
        if "ChargeItemDefinitionPropertyGroupPriceComponent" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionPropertyGroupPriceComponent(jsondict)
        if "Claim" == resource_type:
            from . import claim
            return claim.Claim(jsondict)
        if "ClaimRelated" == resource_type:
            from . import claim
            return claim.ClaimRelated(jsondict)
        if "ClaimPayee" == resource_type:
            from . import claim
            return claim.ClaimPayee(jsondict)
        if "ClaimCareTeam" == resource_type:
            from . import claim
            return claim.ClaimCareTeam(jsondict)
        if "ClaimSupportingInfo" == resource_type:
            from . import claim
            return claim.ClaimSupportingInfo(jsondict)
        if "ClaimDiagnosis" == resource_type:
            from . import claim
            return claim.ClaimDiagnosis(jsondict)
        if "ClaimProcedure" == resource_type:
            from . import claim
            return claim.ClaimProcedure(jsondict)
        if "ClaimInsurance" == resource_type:
            from . import claim
            return claim.ClaimInsurance(jsondict)
        if "ClaimAccident" == resource_type:
            from . import claim
            return claim.ClaimAccident(jsondict)
        if "ClaimItem" == resource_type:
            from . import claim
            return claim.ClaimItem(jsondict)
        if "ClaimItemDetail" == resource_type:
            from . import claim
            return claim.ClaimItemDetail(jsondict)
        if "ClaimItemDetailSubDetail" == resource_type:
            from . import claim
            return claim.ClaimItemDetailSubDetail(jsondict)
        if "ClaimResponse" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "ClaimResponseItem" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItem(jsondict)
        if "ClaimResponseItemAdjudication" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItemAdjudication(jsondict)
        if "ClaimResponseItemDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetail(jsondict)
        if "ClaimResponseItemDetailSubDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict)
        if "ClaimResponseAddItem" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItem(jsondict)
        if "ClaimResponseAddItemDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetail(jsondict)
        if "ClaimResponseAddItemDetailSubDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetailSubDetail(jsondict)
        if "ClaimResponseTotal" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseTotal(jsondict)
        if "ClaimResponsePayment" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponsePayment(jsondict)
        if "ClaimResponseProcessNote" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseProcessNote(jsondict)
        if "ClaimResponseInsurance" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseInsurance(jsondict)
        if "ClaimResponseError" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseError(jsondict)
        if "ClinicalImpression" == resource_type:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict)
        if "ClinicalImpressionFinding" == resource_type:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionFinding(jsondict)
        if "ClinicalProfile" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfile(jsondict)
        if "ClinicalProfileLab" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLab(jsondict)
        if "ClinicalProfileLabScalarDistribution" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistribution(jsondict)
        if "ClinicalProfileLabScalarDistributionDecile" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionDecile(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedLabs" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedLabs(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedLabsEntry" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedLabsEntry(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedDiagnoses" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedDiagnoses(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedMedications" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedMedications(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedProcedures" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedProcedures(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedPhenotypes" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedPhenotypes(jsondict)
        if "ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry(jsondict)
        if "ClinicalProfileMedication" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileMedication(jsondict)
        if "ClinicalProfileMedicationDosage" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileMedicationDosage(jsondict)
        if "ClinicalProfileDiagnosis" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileDiagnosis(jsondict)
        if "ClinicalProfileProcedure" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileProcedure(jsondict)
        if "ClinicalProfileHpo" == resource_type:
            from . import clinicalprofile
            return clinicalprofile.ClinicalProfileHpo(jsondict)
        if "CodeSystem" == resource_type:
            from . import codesystem
            return codesystem.CodeSystem(jsondict)
        if "CodeSystemFilter" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemFilter(jsondict)
        if "CodeSystemProperty" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemProperty(jsondict)
        if "CodeSystemConcept" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemConcept(jsondict)
        if "CodeSystemConceptDesignation" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemConceptDesignation(jsondict)
        if "CodeSystemConceptProperty" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemConceptProperty(jsondict)
        if "Communication" == resource_type:
            from . import communication
            return communication.Communication(jsondict)
        if "CommunicationPayload" == resource_type:
            from . import communication
            return communication.CommunicationPayload(jsondict)
        if "CommunicationRequest" == resource_type:
            from . import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict)
        if "CommunicationRequestPayload" == resource_type:
            from . import communicationrequest
            return communicationrequest.CommunicationRequestPayload(jsondict)
        if "CompartmentDefinition" == resource_type:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinition(jsondict)
        if "CompartmentDefinitionResource" == resource_type:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinitionResource(jsondict)
        if "Composition" == resource_type:
            from . import composition
            return composition.Composition(jsondict)
        if "CompositionAttester" == resource_type:
            from . import composition
            return composition.CompositionAttester(jsondict)
        if "CompositionRelatesTo" == resource_type:
            from . import composition
            return composition.CompositionRelatesTo(jsondict)
        if "CompositionEvent" == resource_type:
            from . import composition
            return composition.CompositionEvent(jsondict)
        if "CompositionSection" == resource_type:
            from . import composition
            return composition.CompositionSection(jsondict)
        if "ConceptMap" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMap(jsondict)
        if "ConceptMapGroup" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroup(jsondict)
        if "ConceptMapGroupElement" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElement(jsondict)
        if "ConceptMapGroupElementTarget" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElementTarget(jsondict)
        if "ConceptMapGroupElementTargetDependsOn" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElementTargetDependsOn(jsondict)
        if "ConceptMapGroupUnmapped" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupUnmapped(jsondict)
        if "Condition" == resource_type:
            from . import condition
            return condition.Condition(jsondict)
        if "ConditionStage" == resource_type:
            from . import condition
            return condition.ConditionStage(jsondict)
        if "ConditionEvidence" == resource_type:
            from . import condition
            return condition.ConditionEvidence(jsondict)
        if "Consent" == resource_type:
            from . import consent
            return consent.Consent(jsondict)
        if "ConsentPolicy" == resource_type:
            from . import consent
            return consent.ConsentPolicy(jsondict)
        if "ConsentVerification" == resource_type:
            from . import consent
            return consent.ConsentVerification(jsondict)
        if "ConsentProvision" == resource_type:
            from . import consent
            return consent.ConsentProvision(jsondict)
        if "ConsentProvisionActor" == resource_type:
            from . import consent
            return consent.ConsentProvisionActor(jsondict)
        if "ConsentProvisionData" == resource_type:
            from . import consent
            return consent.ConsentProvisionData(jsondict)
        if "Contract" == resource_type:
            from . import contract
            return contract.Contract(jsondict)
        if "ContractContentDefinition" == resource_type:
            from . import contract
            return contract.ContractContentDefinition(jsondict)
        if "ContractTerm" == resource_type:
            from . import contract
            return contract.ContractTerm(jsondict)
        if "ContractTermSecurityLabel" == resource_type:
            from . import contract
            return contract.ContractTermSecurityLabel(jsondict)
        if "ContractTermOffer" == resource_type:
            from . import contract
            return contract.ContractTermOffer(jsondict)
        if "ContractTermOfferParty" == resource_type:
            from . import contract
            return contract.ContractTermOfferParty(jsondict)
        if "ContractTermOfferAnswer" == resource_type:
            from . import contract
            return contract.ContractTermOfferAnswer(jsondict)
        if "ContractTermAsset" == resource_type:
            from . import contract
            return contract.ContractTermAsset(jsondict)
        if "ContractTermAssetContext" == resource_type:
            from . import contract
            return contract.ContractTermAssetContext(jsondict)
        if "ContractTermAssetValuedItem" == resource_type:
            from . import contract
            return contract.ContractTermAssetValuedItem(jsondict)
        if "ContractTermAction" == resource_type:
            from . import contract
            return contract.ContractTermAction(jsondict)
        if "ContractTermActionSubject" == resource_type:
            from . import contract
            return contract.ContractTermActionSubject(jsondict)
        if "ContractSigner" == resource_type:
            from . import contract
            return contract.ContractSigner(jsondict)
        if "ContractFriendly" == resource_type:
            from . import contract
            return contract.ContractFriendly(jsondict)
        if "ContractLegal" == resource_type:
            from . import contract
            return contract.ContractLegal(jsondict)
        if "ContractRule" == resource_type:
            from . import contract
            return contract.ContractRule(jsondict)
        if "Coverage" == resource_type:
            from . import coverage
            return coverage.Coverage(jsondict)
        if "CoverageClass" == resource_type:
            from . import coverage
            return coverage.CoverageClass(jsondict)
        if "CoverageCostToBeneficiary" == resource_type:
            from . import coverage
            return coverage.CoverageCostToBeneficiary(jsondict)
        if "CoverageCostToBeneficiaryException" == resource_type:
            from . import coverage
            return coverage.CoverageCostToBeneficiaryException(jsondict)
        if "CoverageEligibilityRequest" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequest(jsondict)
        if "CoverageEligibilityRequestSupportingInfo" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo(jsondict)
        if "CoverageEligibilityRequestInsurance" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestInsurance(jsondict)
        if "CoverageEligibilityRequestItem" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestItem(jsondict)
        if "CoverageEligibilityRequestItemDiagnosis" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis(jsondict)
        if "CoverageEligibilityResponse" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponse(jsondict)
        if "CoverageEligibilityResponseInsurance" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsurance(jsondict)
        if "CoverageEligibilityResponseInsuranceItem" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem(jsondict)
        if "CoverageEligibilityResponseInsuranceItemBenefit" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit(jsondict)
        if "CoverageEligibilityResponseError" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseError(jsondict)
        if "DetectedIssue" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssue(jsondict)
        if "DetectedIssueEvidence" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssueEvidence(jsondict)
        if "DetectedIssueMitigation" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssueMitigation(jsondict)
        if "Device" == resource_type:
            from . import device
            return device.Device(jsondict)
        if "DeviceUdiCarrier" == resource_type:
            from . import device
            return device.DeviceUdiCarrier(jsondict)
        if "DeviceDeviceName" == resource_type:
            from . import device
            return device.DeviceDeviceName(jsondict)
        if "DeviceSpecialization" == resource_type:
            from . import device
            return device.DeviceSpecialization(jsondict)
        if "DeviceVersion" == resource_type:
            from . import device
            return device.DeviceVersion(jsondict)
        if "DeviceProperty" == resource_type:
            from . import device
            return device.DeviceProperty(jsondict)
        if "DeviceDefinition" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinition(jsondict)
        if "DeviceDefinitionUdiDeviceIdentifier" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionUdiDeviceIdentifier(jsondict)
        if "DeviceDefinitionDeviceName" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionDeviceName(jsondict)
        if "DeviceDefinitionSpecialization" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionSpecialization(jsondict)
        if "DeviceDefinitionCapability" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionCapability(jsondict)
        if "DeviceDefinitionProperty" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionProperty(jsondict)
        if "DeviceDefinitionMaterial" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionMaterial(jsondict)
        if "DeviceMetric" == resource_type:
            from . import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "DeviceMetricCalibration" == resource_type:
            from . import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict)
        if "DeviceRequest" == resource_type:
            from . import devicerequest
            return devicerequest.DeviceRequest(jsondict)
        if "DeviceRequestParameter" == resource_type:
            from . import devicerequest
            return devicerequest.DeviceRequestParameter(jsondict)
        if "DeviceUseStatement" == resource_type:
            from . import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "DiagnosticReport" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "DiagnosticReportMedia" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportMedia(jsondict)
        if "DocumentManifest" == resource_type:
            from . import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "DocumentManifestRelated" == resource_type:
            from . import documentmanifest
            return documentmanifest.DocumentManifestRelated(jsondict)
        if "DocumentReference" == resource_type:
            from . import documentreference
            return documentreference.DocumentReference(jsondict)
        if "DocumentReferenceRelatesTo" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "DocumentReferenceContent" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceContent(jsondict)
        if "DocumentReferenceContext" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceContext(jsondict)
        if "DomainResource" == resource_type:
            from . import domainresource
            return domainresource.DomainResource(jsondict)
        if "EffectEvidenceSynthesis" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesis(jsondict)
        if "EffectEvidenceSynthesisSampleSize" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisSampleSize(jsondict)
        if "EffectEvidenceSynthesisResultsByExposure" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisResultsByExposure(jsondict)
        if "EffectEvidenceSynthesisEffectEstimate" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimate(jsondict)
        if "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(jsondict)
        if "EffectEvidenceSynthesisCertainty" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisCertainty(jsondict)
        if "EffectEvidenceSynthesisCertaintyCertaintySubcomponent" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisCertaintyCertaintySubcomponent(jsondict)
        if "Encounter" == resource_type:
            from . import encounter
            return encounter.Encounter(jsondict)
        if "EncounterStatusHistory" == resource_type:
            from . import encounter
            return encounter.EncounterStatusHistory(jsondict)
        if "EncounterClassHistory" == resource_type:
            from . import encounter
            return encounter.EncounterClassHistory(jsondict)
        if "EncounterParticipant" == resource_type:
            from . import encounter
            return encounter.EncounterParticipant(jsondict)
        if "EncounterDiagnosis" == resource_type:
            from . import encounter
            return encounter.EncounterDiagnosis(jsondict)
        if "EncounterHospitalization" == resource_type:
            from . import encounter
            return encounter.EncounterHospitalization(jsondict)
        if "EncounterLocation" == resource_type:
            from . import encounter
            return encounter.EncounterLocation(jsondict)
        if "Endpoint" == resource_type:
            from . import endpoint
            return endpoint.Endpoint(jsondict)
        if "EnrollmentRequest" == resource_type:
            from . import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict)
        if "EnrollmentResponse" == resource_type:
            from . import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict)
        if "EpisodeOfCare" == resource_type:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict)
        if "EpisodeOfCareStatusHistory" == resource_type:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareStatusHistory(jsondict)
        if "EpisodeOfCareDiagnosis" == resource_type:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareDiagnosis(jsondict)
        if "EventDefinition" == resource_type:
            from . import eventdefinition
            return eventdefinition.EventDefinition(jsondict)
        if "Evidence" == resource_type:
            from . import evidence
            return evidence.Evidence(jsondict)
        if "EvidenceVariable" == resource_type:
            from . import evidencevariable
            return evidencevariable.EvidenceVariable(jsondict)
        if "EvidenceVariableCharacteristic" == resource_type:
            from . import evidencevariable
            return evidencevariable.EvidenceVariableCharacteristic(jsondict)
        if "ExampleScenario" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenario(jsondict)
        if "ExampleScenarioActor" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioActor(jsondict)
        if "ExampleScenarioInstance" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstance(jsondict)
        if "ExampleScenarioInstanceVersion" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstanceVersion(jsondict)
        if "ExampleScenarioInstanceContainedInstance" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstanceContainedInstance(jsondict)
        if "ExampleScenarioProcess" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcess(jsondict)
        if "ExampleScenarioProcessStep" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStep(jsondict)
        if "ExampleScenarioProcessStepOperation" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStepOperation(jsondict)
        if "ExampleScenarioProcessStepAlternative" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStepAlternative(jsondict)
        if "ExplanationOfBenefit" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict)
        if "ExplanationOfBenefitRelated" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitRelated(jsondict)
        if "ExplanationOfBenefitPayee" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayee(jsondict)
        if "ExplanationOfBenefitCareTeam" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitCareTeam(jsondict)
        if "ExplanationOfBenefitSupportingInfo" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitSupportingInfo(jsondict)
        if "ExplanationOfBenefitDiagnosis" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitDiagnosis(jsondict)
        if "ExplanationOfBenefitProcedure" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitProcedure(jsondict)
        if "ExplanationOfBenefitInsurance" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitInsurance(jsondict)
        if "ExplanationOfBenefitAccident" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAccident(jsondict)
        if "ExplanationOfBenefitItem" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItem(jsondict)
        if "ExplanationOfBenefitItemAdjudication" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemAdjudication(jsondict)
        if "ExplanationOfBenefitItemDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetail(jsondict)
        if "ExplanationOfBenefitItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail(jsondict)
        if "ExplanationOfBenefitAddItem" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItem(jsondict)
        if "ExplanationOfBenefitAddItemDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetail(jsondict)
        if "ExplanationOfBenefitAddItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail(jsondict)
        if "ExplanationOfBenefitTotal" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitTotal(jsondict)
        if "ExplanationOfBenefitPayment" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayment(jsondict)
        if "ExplanationOfBenefitProcessNote" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitProcessNote(jsondict)
        if "ExplanationOfBenefitBenefitBalance" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalance(jsondict)
        if "ExplanationOfBenefitBenefitBalanceFinancial" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial(jsondict)
        if "FamilyMemberHistory" == resource_type:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict)
        if "FamilyMemberHistoryCondition" == resource_type:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryCondition(jsondict)
        if "FamilyMemberHistoryProcedure" == resource_type:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryProcedure(jsondict)
        if "Flag" == resource_type:
            from . import flag
            return flag.Flag(jsondict)
        if "Goal" == resource_type:
            from . import goal
            return goal.Goal(jsondict)
        if "GoalTarget" == resource_type:
            from . import goal
            return goal.GoalTarget(jsondict)
        if "GraphDefinition" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinition(jsondict)
        if "GraphDefinitionLink" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLink(jsondict)
        if "GraphDefinitionLinkTarget" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLinkTarget(jsondict)
        if "GraphDefinitionLinkTargetCompartment" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLinkTargetCompartment(jsondict)
        if "Group" == resource_type:
            from . import group
            return group.Group(jsondict)
        if "GroupCharacteristic" == resource_type:
            from . import group
            return group.GroupCharacteristic(jsondict)
        if "GroupMember" == resource_type:
            from . import group
            return group.GroupMember(jsondict)
        if "GuidanceResponse" == resource_type:
            from . import guidanceresponse
            return guidanceresponse.GuidanceResponse(jsondict)
        if "HealthcareService" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareService(jsondict)
        if "HealthcareServiceEligibility" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceEligibility(jsondict)
        if "HealthcareServiceAvailableTime" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceAvailableTime(jsondict)
        if "HealthcareServiceNotAvailable" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict)
        if "ImagingStudy" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "ImagingStudySeries" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict)
        if "ImagingStudySeriesPerformer" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesPerformer(jsondict)
        if "ImagingStudySeriesInstance" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict)
        if "Immunization" == resource_type:
            from . import immunization
            return immunization.Immunization(jsondict)
        if "ImmunizationPerformer" == resource_type:
            from . import immunization
            return immunization.ImmunizationPerformer(jsondict)
        if "ImmunizationEducation" == resource_type:
            from . import immunization
            return immunization.ImmunizationEducation(jsondict)
        if "ImmunizationReaction" == resource_type:
            from . import immunization
            return immunization.ImmunizationReaction(jsondict)
        if "ImmunizationProtocolApplied" == resource_type:
            from . import immunization
            return immunization.ImmunizationProtocolApplied(jsondict)
        if "ImmunizationEvaluation" == resource_type:
            from . import immunizationevaluation
            return immunizationevaluation.ImmunizationEvaluation(jsondict)
        if "ImmunizationRecommendation" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendation" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(jsondict)
        if "ImplementationGuide" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuide(jsondict)
        if "ImplementationGuideDependsOn" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDependsOn(jsondict)
        if "ImplementationGuideGlobal" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideGlobal(jsondict)
        if "ImplementationGuideDefinition" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinition(jsondict)
        if "ImplementationGuideDefinitionGrouping" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionGrouping(jsondict)
        if "ImplementationGuideDefinitionResource" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionResource(jsondict)
        if "ImplementationGuideDefinitionPage" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionPage(jsondict)
        if "ImplementationGuideDefinitionParameter" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionParameter(jsondict)
        if "ImplementationGuideDefinitionTemplate" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionTemplate(jsondict)
        if "ImplementationGuideManifest" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifest(jsondict)
        if "ImplementationGuideManifestResource" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifestResource(jsondict)
        if "ImplementationGuideManifestPage" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifestPage(jsondict)
        if "InsurancePlan" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlan(jsondict)
        if "InsurancePlanContact" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanContact(jsondict)
        if "InsurancePlanCoverage" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverage(jsondict)
        if "InsurancePlanCoverageBenefit" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverageBenefit(jsondict)
        if "InsurancePlanCoverageBenefitLimit" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverageBenefitLimit(jsondict)
        if "InsurancePlanPlan" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlan(jsondict)
        if "InsurancePlanPlanGeneralCost" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanGeneralCost(jsondict)
        if "InsurancePlanPlanSpecificCost" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCost(jsondict)
        if "InsurancePlanPlanSpecificCostBenefit" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCostBenefit(jsondict)
        if "InsurancePlanPlanSpecificCostBenefitCost" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCostBenefitCost(jsondict)
        if "Invoice" == resource_type:
            from . import invoice
            return invoice.Invoice(jsondict)
        if "InvoiceParticipant" == resource_type:
            from . import invoice
            return invoice.InvoiceParticipant(jsondict)
        if "InvoiceLineItem" == resource_type:
            from . import invoice
            return invoice.InvoiceLineItem(jsondict)
        if "InvoiceLineItemPriceComponent" == resource_type:
            from . import invoice
            return invoice.InvoiceLineItemPriceComponent(jsondict)
        if "Library" == resource_type:
            from . import library
            return library.Library(jsondict)
        if "Linkage" == resource_type:
            from . import linkage
            return linkage.Linkage(jsondict)
        if "LinkageItem" == resource_type:
            from . import linkage
            return linkage.LinkageItem(jsondict)
        if "List" == resource_type:
            from . import list
            return list.List(jsondict)
        if "ListEntry" == resource_type:
            from . import list
            return list.ListEntry(jsondict)
        if "Location" == resource_type:
            from . import location
            return location.Location(jsondict)
        if "LocationPosition" == resource_type:
            from . import location
            return location.LocationPosition(jsondict)
        if "LocationHoursOfOperation" == resource_type:
            from . import location
            return location.LocationHoursOfOperation(jsondict)
        if "Measure" == resource_type:
            from . import measure
            return measure.Measure(jsondict)
        if "MeasureGroup" == resource_type:
            from . import measure
            return measure.MeasureGroup(jsondict)
        if "MeasureGroupPopulation" == resource_type:
            from . import measure
            return measure.MeasureGroupPopulation(jsondict)
        if "MeasureGroupStratifier" == resource_type:
            from . import measure
            return measure.MeasureGroupStratifier(jsondict)
        if "MeasureGroupStratifierComponent" == resource_type:
            from . import measure
            return measure.MeasureGroupStratifierComponent(jsondict)
        if "MeasureSupplementalData" == resource_type:
            from . import measure
            return measure.MeasureSupplementalData(jsondict)
        if "MeasureReport" == resource_type:
            from . import measurereport
            return measurereport.MeasureReport(jsondict)
        if "MeasureReportGroup" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroup(jsondict)
        if "MeasureReportGroupPopulation" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupPopulation(jsondict)
        if "MeasureReportGroupStratifier" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifier(jsondict)
        if "MeasureReportGroupStratifierStratum" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratum(jsondict)
        if "MeasureReportGroupStratifierStratumComponent" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratumComponent(jsondict)
        if "MeasureReportGroupStratifierStratumPopulation" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratumPopulation(jsondict)
        if "Media" == resource_type:
            from . import media
            return media.Media(jsondict)
        if "Medication" == resource_type:
            from . import medication
            return medication.Medication(jsondict)
        if "MedicationIngredient" == resource_type:
            from . import medication
            return medication.MedicationIngredient(jsondict)
        if "MedicationBatch" == resource_type:
            from . import medication
            return medication.MedicationBatch(jsondict)
        if "MedicationAdministration" == resource_type:
            from . import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict)
        if "MedicationAdministrationPerformer" == resource_type:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationPerformer(jsondict)
        if "MedicationAdministrationDosage" == resource_type:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationDosage(jsondict)
        if "MedicationDispense" == resource_type:
            from . import medicationdispense
            return medicationdispense.MedicationDispense(jsondict)
        if "MedicationDispensePerformer" == resource_type:
            from . import medicationdispense
            return medicationdispense.MedicationDispensePerformer(jsondict)
        if "MedicationDispenseSubstitution" == resource_type:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseSubstitution(jsondict)
        if "MedicationKnowledge" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledge(jsondict)
        if "MedicationKnowledgeRelatedMedicationKnowledge" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge(jsondict)
        if "MedicationKnowledgeMonograph" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMonograph(jsondict)
        if "MedicationKnowledgeIngredient" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeIngredient(jsondict)
        if "MedicationKnowledgeCost" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeCost(jsondict)
        if "MedicationKnowledgeMonitoringProgram" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMonitoringProgram(jsondict)
        if "MedicationKnowledgeAdministrationGuidelines" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelines(jsondict)
        if "MedicationKnowledgeAdministrationGuidelinesDosage" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesDosage(jsondict)
        if "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(jsondict)
        if "MedicationKnowledgeMedicineClassification" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMedicineClassification(jsondict)
        if "MedicationKnowledgePackaging" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgePackaging(jsondict)
        if "MedicationKnowledgeDrugCharacteristic" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeDrugCharacteristic(jsondict)
        if "MedicationKnowledgeRegulatory" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatory(jsondict)
        if "MedicationKnowledgeRegulatorySubstitution" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatorySubstitution(jsondict)
        if "MedicationKnowledgeRegulatorySchedule" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatorySchedule(jsondict)
        if "MedicationKnowledgeRegulatoryMaxDispense" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense(jsondict)
        if "MedicationKnowledgeKinetics" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeKinetics(jsondict)
        if "MedicationRequest" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequest(jsondict)
        if "MedicationRequestDispenseRequest" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequest(jsondict)
        if "MedicationRequestDispenseRequestInitialFill" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequestInitialFill(jsondict)
        if "MedicationRequestSubstitution" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestSubstitution(jsondict)
        if "MedicationStatement" == resource_type:
            from . import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
        if "MedicinalProduct" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProduct(jsondict)
        if "MedicinalProductContact" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductContact(jsondict)
        if "MedicinalProductName" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductName(jsondict)
        if "MedicinalProductNameNamePart" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductNameNamePart(jsondict)
        if "MedicinalProductNameCountryLanguage" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductNameCountryLanguage(jsondict)
        if "MedicinalProductManufacturingBusinessOperation" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductManufacturingBusinessOperation(jsondict)
        if "MedicinalProductSpecialDesignation" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductSpecialDesignation(jsondict)
        if "MedicinalProductAuthorization" == resource_type:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorization(jsondict)
        if "MedicinalProductAuthorizationJurisdictionalAuthorization" == resource_type:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorizationJurisdictionalAuthorization(jsondict)
        if "MedicinalProductAuthorizationProcedure" == resource_type:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorizationProcedure(jsondict)
        if "MedicinalProductContraindication" == resource_type:
            from . import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindication(jsondict)
        if "MedicinalProductContraindicationOtherTherapy" == resource_type:
            from . import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindicationOtherTherapy(jsondict)
        if "MedicinalProductIndication" == resource_type:
            from . import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndication(jsondict)
        if "MedicinalProductIndicationOtherTherapy" == resource_type:
            from . import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndicationOtherTherapy(jsondict)
        if "MedicinalProductIngredient" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredient(jsondict)
        if "MedicinalProductIngredientSpecifiedSubstance" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstance(jsondict)
        if "MedicinalProductIngredientSpecifiedSubstanceStrength" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrength(jsondict)
        if "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(jsondict)
        if "MedicinalProductIngredientSubstance" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSubstance(jsondict)
        if "MedicinalProductInteraction" == resource_type:
            from . import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteraction(jsondict)
        if "MedicinalProductInteractionInteractant" == resource_type:
            from . import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteractionInteractant(jsondict)
        if "MedicinalProductManufactured" == resource_type:
            from . import medicinalproductmanufactured
            return medicinalproductmanufactured.MedicinalProductManufactured(jsondict)
        if "MedicinalProductPackaged" == resource_type:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackaged(jsondict)
        if "MedicinalProductPackagedBatchIdentifier" == resource_type:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackagedBatchIdentifier(jsondict)
        if "MedicinalProductPackagedPackageItem" == resource_type:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackagedPackageItem(jsondict)
        if "MedicinalProductPharmaceutical" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(jsondict)
        if "MedicinalProductPharmaceuticalCharacteristics" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalCharacteristics(jsondict)
        if "MedicinalProductPharmaceuticalRouteOfAdministration" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministration(jsondict)
        if "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(jsondict)
        if "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(jsondict)
        if "MedicinalProductUndesirableEffect" == resource_type:
            from . import medicinalproductundesirableeffect
            return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(jsondict)
        if "MessageDefinition" == resource_type:
            from . import messagedefinition
            return messagedefinition.MessageDefinition(jsondict)
        if "MessageDefinitionFocus" == resource_type:
            from . import messagedefinition
            return messagedefinition.MessageDefinitionFocus(jsondict)
        if "MessageDefinitionAllowedResponse" == resource_type:
            from . import messagedefinition
            return messagedefinition.MessageDefinitionAllowedResponse(jsondict)
        if "MessageHeader" == resource_type:
            from . import messageheader
            return messageheader.MessageHeader(jsondict)
        if "MessageHeaderDestination" == resource_type:
            from . import messageheader
            return messageheader.MessageHeaderDestination(jsondict)
        if "MessageHeaderSource" == resource_type:
            from . import messageheader
            return messageheader.MessageHeaderSource(jsondict)
        if "MessageHeaderResponse" == resource_type:
            from . import messageheader
            return messageheader.MessageHeaderResponse(jsondict)
        if "MolecularSequence" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequence(jsondict)
        if "MolecularSequenceReferenceSeq" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceReferenceSeq(jsondict)
        if "MolecularSequenceVariant" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceVariant(jsondict)
        if "MolecularSequenceQuality" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceQuality(jsondict)
        if "MolecularSequenceQualityRoc" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceQualityRoc(jsondict)
        if "MolecularSequenceRepository" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceRepository(jsondict)
        if "MolecularSequenceStructureVariant" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariant(jsondict)
        if "MolecularSequenceStructureVariantOuter" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariantOuter(jsondict)
        if "MolecularSequenceStructureVariantInner" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariantInner(jsondict)
        if "NamingSystem" == resource_type:
            from . import namingsystem
            return namingsystem.NamingSystem(jsondict)
        if "NamingSystemUniqueId" == resource_type:
            from . import namingsystem
            return namingsystem.NamingSystemUniqueId(jsondict)
        if "NutritionOrder" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrder(jsondict)
        if "NutritionOrderOralDiet" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDiet(jsondict)
        if "NutritionOrderOralDietNutrient" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietNutrient(jsondict)
        if "NutritionOrderOralDietTexture" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietTexture(jsondict)
        if "NutritionOrderSupplement" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderSupplement(jsondict)
        if "NutritionOrderEnteralFormula" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormula(jsondict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormulaAdministration(jsondict)
        if "Observation" == resource_type:
            from . import observation
            return observation.Observation(jsondict)
        if "ObservationReferenceRange" == resource_type:
            from . import observation
            return observation.ObservationReferenceRange(jsondict)
        if "ObservationComponent" == resource_type:
            from . import observation
            return observation.ObservationComponent(jsondict)
        if "ObservationDefinition" == resource_type:
            from . import observationdefinition
            return observationdefinition.ObservationDefinition(jsondict)
        if "ObservationDefinitionQuantitativeDetails" == resource_type:
            from . import observationdefinition
            return observationdefinition.ObservationDefinitionQuantitativeDetails(jsondict)
        if "ObservationDefinitionQualifiedInterval" == resource_type:
            from . import observationdefinition
            return observationdefinition.ObservationDefinitionQualifiedInterval(jsondict)
        if "OperationDefinition" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinition(jsondict)
        if "OperationDefinitionParameter" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameter(jsondict)
        if "OperationDefinitionParameterBinding" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterBinding(jsondict)
        if "OperationDefinitionParameterReferencedFrom" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterReferencedFrom(jsondict)
        if "OperationDefinitionOverload" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionOverload(jsondict)
        if "OperationOutcome" == resource_type:
            from . import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "OperationOutcomeIssue" == resource_type:
            from . import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict)
        if "Organization" == resource_type:
            from . import organization
            return organization.Organization(jsondict)
        if "OrganizationContact" == resource_type:
            from . import organization
            return organization.OrganizationContact(jsondict)
        if "OrganizationAffiliation" == resource_type:
            from . import organizationaffiliation
            return organizationaffiliation.OrganizationAffiliation(jsondict)
        if "Parameters" == resource_type:
            from . import parameters
            return parameters.Parameters(jsondict)
        if "ParametersParameter" == resource_type:
            from . import parameters
            return parameters.ParametersParameter(jsondict)
        if "Patient" == resource_type:
            from . import patient
            return patient.Patient(jsondict)
        if "PatientContact" == resource_type:
            from . import patient
            return patient.PatientContact(jsondict)
        if "PatientCommunication" == resource_type:
            from . import patient
            return patient.PatientCommunication(jsondict)
        if "PatientLink" == resource_type:
            from . import patient
            return patient.PatientLink(jsondict)
        if "PaymentNotice" == resource_type:
            from . import paymentnotice
            return paymentnotice.PaymentNotice(jsondict)
        if "PaymentReconciliation" == resource_type:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict)
        if "PaymentReconciliationDetail" == resource_type:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationDetail(jsondict)
        if "PaymentReconciliationProcessNote" == resource_type:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationProcessNote(jsondict)
        if "Person" == resource_type:
            from . import person
            return person.Person(jsondict)
        if "PersonLink" == resource_type:
            from . import person
            return person.PersonLink(jsondict)
        if "PlanDefinition" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinition(jsondict)
        if "PlanDefinitionGoal" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionGoal(jsondict)
        if "PlanDefinitionGoalTarget" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionGoalTarget(jsondict)
        if "PlanDefinitionAction" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionAction(jsondict)
        if "PlanDefinitionActionCondition" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionCondition(jsondict)
        if "PlanDefinitionActionRelatedAction" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionRelatedAction(jsondict)
        if "PlanDefinitionActionParticipant" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionParticipant(jsondict)
        if "PlanDefinitionActionDynamicValue" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionDynamicValue(jsondict)
        if "Practitioner" == resource_type:
            from . import practitioner
            return practitioner.Practitioner(jsondict)
        if "PractitionerQualification" == resource_type:
            from . import practitioner
            return practitioner.PractitionerQualification(jsondict)
        if "PractitionerRole" == resource_type:
            from . import practitionerrole
            return practitionerrole.PractitionerRole(jsondict)
        if "PractitionerRoleAvailableTime" == resource_type:
            from . import practitionerrole
            return practitionerrole.PractitionerRoleAvailableTime(jsondict)
        if "PractitionerRoleNotAvailable" == resource_type:
            from . import practitionerrole
            return practitionerrole.PractitionerRoleNotAvailable(jsondict)
        if "Procedure" == resource_type:
            from . import procedure
            return procedure.Procedure(jsondict)
        if "ProcedurePerformer" == resource_type:
            from . import procedure
            return procedure.ProcedurePerformer(jsondict)
        if "ProcedureFocalDevice" == resource_type:
            from . import procedure
            return procedure.ProcedureFocalDevice(jsondict)
        if "Provenance" == resource_type:
            from . import provenance
            return provenance.Provenance(jsondict)
        if "ProvenanceAgent" == resource_type:
            from . import provenance
            return provenance.ProvenanceAgent(jsondict)
        if "ProvenanceEntity" == resource_type:
            from . import provenance
            return provenance.ProvenanceEntity(jsondict)
        if "Questionnaire" == resource_type:
            from . import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "QuestionnaireItem" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItem(jsondict)
        if "QuestionnaireItemEnableWhen" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemEnableWhen(jsondict)
        if "QuestionnaireItemAnswerOption" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemAnswerOption(jsondict)
        if "QuestionnaireItemInitial" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemInitial(jsondict)
        if "QuestionnaireResponse" == resource_type:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponse(jsondict)
        if "QuestionnaireResponseItem" == resource_type:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItem(jsondict)
        if "QuestionnaireResponseItemAnswer" == resource_type:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItemAnswer(jsondict)
        if "RelatedPerson" == resource_type:
            from . import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "RelatedPersonCommunication" == resource_type:
            from . import relatedperson
            return relatedperson.RelatedPersonCommunication(jsondict)
        if "RequestGroup" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroup(jsondict)
        if "RequestGroupAction" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroupAction(jsondict)
        if "RequestGroupActionCondition" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroupActionCondition(jsondict)
        if "RequestGroupActionRelatedAction" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroupActionRelatedAction(jsondict)
        if "ResearchDefinition" == resource_type:
            from . import researchdefinition
            return researchdefinition.ResearchDefinition(jsondict)
        if "ResearchElementDefinition" == resource_type:
            from . import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinition(jsondict)
        if "ResearchElementDefinitionCharacteristic" == resource_type:
            from . import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinitionCharacteristic(jsondict)
        if "ResearchStudy" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudy(jsondict)
        if "ResearchStudyArm" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudyArm(jsondict)
        if "ResearchStudyObjective" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudyObjective(jsondict)
        if "ResearchSubject" == resource_type:
            from . import researchsubject
            return researchsubject.ResearchSubject(jsondict)
        if "RiskAssessment" == resource_type:
            from . import riskassessment
            return riskassessment.RiskAssessment(jsondict)
        if "RiskAssessmentPrediction" == resource_type:
            from . import riskassessment
            return riskassessment.RiskAssessmentPrediction(jsondict)
        if "RiskEvidenceSynthesis" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesis(jsondict)
        if "RiskEvidenceSynthesisSampleSize" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisSampleSize(jsondict)
        if "RiskEvidenceSynthesisRiskEstimate" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimate(jsondict)
        if "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(jsondict)
        if "RiskEvidenceSynthesisCertainty" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisCertainty(jsondict)
        if "RiskEvidenceSynthesisCertaintyCertaintySubcomponent" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisCertaintyCertaintySubcomponent(jsondict)
        if "Schedule" == resource_type:
            from . import schedule
            return schedule.Schedule(jsondict)
        if "SearchParameter" == resource_type:
            from . import searchparameter
            return searchparameter.SearchParameter(jsondict)
        if "SearchParameterComponent" == resource_type:
            from . import searchparameter
            return searchparameter.SearchParameterComponent(jsondict)
        if "ServiceRequest" == resource_type:
            from . import servicerequest
            return servicerequest.ServiceRequest(jsondict)
        if "Slot" == resource_type:
            from . import slot
            return slot.Slot(jsondict)
        if "Specimen" == resource_type:
            from . import specimen
            return specimen.Specimen(jsondict)
        if "SpecimenCollection" == resource_type:
            from . import specimen
            return specimen.SpecimenCollection(jsondict)
        if "SpecimenProcessing" == resource_type:
            from . import specimen
            return specimen.SpecimenProcessing(jsondict)
        if "SpecimenContainer" == resource_type:
            from . import specimen
            return specimen.SpecimenContainer(jsondict)
        if "SpecimenDefinition" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinition(jsondict)
        if "SpecimenDefinitionTypeTested" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTested(jsondict)
        if "SpecimenDefinitionTypeTestedContainer" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedContainer(jsondict)
        if "SpecimenDefinitionTypeTestedContainerAdditive" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive(jsondict)
        if "SpecimenDefinitionTypeTestedHandling" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedHandling(jsondict)
        if "StructureDefinition" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
        if "StructureDefinitionMapping" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionMapping(jsondict)
        if "StructureDefinitionContext" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionContext(jsondict)
        if "StructureDefinitionSnapshot" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionSnapshot(jsondict)
        if "StructureDefinitionDifferential" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionDifferential(jsondict)
        if "StructureMap" == resource_type:
            from . import structuremap
            return structuremap.StructureMap(jsondict)
        if "StructureMapStructure" == resource_type:
            from . import structuremap
            return structuremap.StructureMapStructure(jsondict)
        if "StructureMapGroup" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroup(jsondict)
        if "StructureMapGroupInput" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupInput(jsondict)
        if "StructureMapGroupRule" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRule(jsondict)
        if "StructureMapGroupRuleSource" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleSource(jsondict)
        if "StructureMapGroupRuleTarget" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTarget(jsondict)
        if "StructureMapGroupRuleTargetParameter" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTargetParameter(jsondict)
        if "StructureMapGroupRuleDependent" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleDependent(jsondict)
        if "Subscription" == resource_type:
            from . import subscription
            return subscription.Subscription(jsondict)
        if "SubscriptionChannel" == resource_type:
            from . import subscription
            return subscription.SubscriptionChannel(jsondict)
        if "Substance" == resource_type:
            from . import substance
            return substance.Substance(jsondict)
        if "SubstanceInstance" == resource_type:
            from . import substance
            return substance.SubstanceInstance(jsondict)
        if "SubstanceIngredient" == resource_type:
            from . import substance
            return substance.SubstanceIngredient(jsondict)
        if "SubstanceDefinition" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinition(jsondict)
        if "SubstanceDefinitionMoiety" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionMoiety(jsondict)
        if "SubstanceDefinitionProperty" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionProperty(jsondict)
        if "SubstanceDefinitionStructure" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionStructure(jsondict)
        if "SubstanceDefinitionStructureIsotope" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionStructureIsotope(jsondict)
        if "SubstanceDefinitionStructureIsotopeMolecularWeight" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionStructureIsotopeMolecularWeight(jsondict)
        if "SubstanceDefinitionStructureRepresentation" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionStructureRepresentation(jsondict)
        if "SubstanceDefinitionstr" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionstr(jsondict)
        if "SubstanceDefinitionName" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionName(jsondict)
        if "SubstanceDefinitionNameOfficial" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionNameOfficial(jsondict)
        if "SubstanceDefinitionRelationship" == resource_type:
            from . import substancedefinition
            return substancedefinition.SubstanceDefinitionRelationship(jsondict)
        if "SubstanceNucleicAcid" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcid(jsondict)
        if "SubstanceNucleicAcidSubunit" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunit(jsondict)
        if "SubstanceNucleicAcidSubunitLinkage" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunitLinkage(jsondict)
        if "SubstanceNucleicAcidSubunitSugar" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunitSugar(jsondict)
        if "SubstancePolymer" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymer(jsondict)
        if "SubstancePolymerMonomerSet" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerMonomerSet(jsondict)
        if "SubstancePolymerMonomerSetStartingMaterial" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerMonomerSetStartingMaterial(jsondict)
        if "SubstancePolymerRepeat" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeat(jsondict)
        if "SubstancePolymerRepeatRepeatUnit" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnit(jsondict)
        if "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(jsondict)
        if "SubstancePolymerRepeatRepeatUnitStructuralRepresentation" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnitStructuralRepresentation(jsondict)
        if "SubstanceProtein" == resource_type:
            from . import substanceprotein
            return substanceprotein.SubstanceProtein(jsondict)
        if "SubstanceProteinSubunit" == resource_type:
            from . import substanceprotein
            return substanceprotein.SubstanceProteinSubunit(jsondict)
        if "SubstanceReferenceInformation" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformation(jsondict)
        if "SubstanceReferenceInformationGene" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationGene(jsondict)
        if "SubstanceReferenceInformationGeneElement" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationGeneElement(jsondict)
        if "SubstanceReferenceInformationClassification" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationClassification(jsondict)
        if "SubstanceReferenceInformationTarget" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationTarget(jsondict)
        if "SubstanceSourceMaterial" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterial(jsondict)
        if "SubstanceSourceMaterialFractionDescription" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialFractionDescription(jsondict)
        if "SubstanceSourceMaterialOrganism" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganism(jsondict)
        if "SubstanceSourceMaterialOrganismAuthor" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismAuthor(jsondict)
        if "SubstanceSourceMaterialOrganismHybrid" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismHybrid(jsondict)
        if "SubstanceSourceMaterialOrganismOrganismGeneral" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismOrganismGeneral(jsondict)
        if "SubstanceSourceMaterialPartDescription" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialPartDescription(jsondict)
        if "SupplyDelivery" == resource_type:
            from . import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict)
        if "SupplyDeliverySuppliedItem" == resource_type:
            from . import supplydelivery
            return supplydelivery.SupplyDeliverySuppliedItem(jsondict)
        if "SupplyRequest" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequest(jsondict)
        if "SupplyRequestParameter" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequestParameter(jsondict)
        if "Task" == resource_type:
            from . import task
            return task.Task(jsondict)
        if "TaskRestriction" == resource_type:
            from . import task
            return task.TaskRestriction(jsondict)
        if "TaskInput" == resource_type:
            from . import task
            return task.TaskInput(jsondict)
        if "TaskOutput" == resource_type:
            from . import task
            return task.TaskOutput(jsondict)
        if "TerminologyCapabilities" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilities(jsondict)
        if "TerminologyCapabilitiesSoftware" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesSoftware(jsondict)
        if "TerminologyCapabilitiesImplementation" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesImplementation(jsondict)
        if "TerminologyCapabilitiesCodeSystem" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystem(jsondict)
        if "TerminologyCapabilitiesCodeSystemVersion" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion(jsondict)
        if "TerminologyCapabilitiesCodeSystemVersionFilter" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter(jsondict)
        if "TerminologyCapabilitiesExpansion" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesExpansion(jsondict)
        if "TerminologyCapabilitiesExpansionParameter" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesExpansionParameter(jsondict)
        if "TerminologyCapabilitiesValidateCode" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesValidateCode(jsondict)
        if "TerminologyCapabilitiesTranslation" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesTranslation(jsondict)
        if "TerminologyCapabilitiesClosure" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesClosure(jsondict)
        if "TestReport" == resource_type:
            from . import testreport
            return testreport.TestReport(jsondict)
        if "TestReportParticipant" == resource_type:
            from . import testreport
            return testreport.TestReportParticipant(jsondict)
        if "TestReportSetup" == resource_type:
            from . import testreport
            return testreport.TestReportSetup(jsondict)
        if "TestReportSetupAction" == resource_type:
            from . import testreport
            return testreport.TestReportSetupAction(jsondict)
        if "TestReportSetupActionOperation" == resource_type:
            from . import testreport
            return testreport.TestReportSetupActionOperation(jsondict)
        if "TestReportSetupActionAssert" == resource_type:
            from . import testreport
            return testreport.TestReportSetupActionAssert(jsondict)
        if "TestReportTest" == resource_type:
            from . import testreport
            return testreport.TestReportTest(jsondict)
        if "TestReportTestAction" == resource_type:
            from . import testreport
            return testreport.TestReportTestAction(jsondict)
        if "TestReportTeardown" == resource_type:
            from . import testreport
            return testreport.TestReportTeardown(jsondict)
        if "TestReportTeardownAction" == resource_type:
            from . import testreport
            return testreport.TestReportTeardownAction(jsondict)
        if "TestScript" == resource_type:
            from . import testscript
            return testscript.TestScript(jsondict)
        if "TestScriptOrigin" == resource_type:
            from . import testscript
            return testscript.TestScriptOrigin(jsondict)
        if "TestScriptDestination" == resource_type:
            from . import testscript
            return testscript.TestScriptDestination(jsondict)
        if "TestScriptMetadata" == resource_type:
            from . import testscript
            return testscript.TestScriptMetadata(jsondict)
        if "TestScriptMetadataLink" == resource_type:
            from . import testscript
            return testscript.TestScriptMetadataLink(jsondict)
        if "TestScriptMetadataCapability" == resource_type:
            from . import testscript
            return testscript.TestScriptMetadataCapability(jsondict)
        if "TestScriptFixture" == resource_type:
            from . import testscript
            return testscript.TestScriptFixture(jsondict)
        if "TestScriptVariable" == resource_type:
            from . import testscript
            return testscript.TestScriptVariable(jsondict)
        if "TestScriptSetup" == resource_type:
            from . import testscript
            return testscript.TestScriptSetup(jsondict)
        if "TestScriptSetupAction" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupAction(jsondict)
        if "TestScriptSetupActionOperation" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionOperation(jsondict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionOperationRequestHeader(jsondict)
        if "TestScriptSetupActionAssert" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssert(jsondict)
        if "TestScriptTest" == resource_type:
            from . import testscript
            return testscript.TestScriptTest(jsondict)
        if "TestScriptTestAction" == resource_type:
            from . import testscript
            return testscript.TestScriptTestAction(jsondict)
        if "TestScriptTeardown" == resource_type:
            from . import testscript
            return testscript.TestScriptTeardown(jsondict)
        if "TestScriptTeardownAction" == resource_type:
            from . import testscript
            return testscript.TestScriptTeardownAction(jsondict)
        if "ValueSet" == resource_type:
            from . import valueset
            return valueset.ValueSet(jsondict)
        if "ValueSetCompose" == resource_type:
            from . import valueset
            return valueset.ValueSetCompose(jsondict)
        if "ValueSetComposeInclude" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeInclude(jsondict)
        if "ValueSetComposeIncludeConcept" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeIncludeConcept(jsondict)
        if "ValueSetComposeIncludeConceptDesignation" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeIncludeConceptDesignation(jsondict)
        if "ValueSetComposeIncludeFilter" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeIncludeFilter(jsondict)
        if "ValueSetExpansion" == resource_type:
            from . import valueset
            return valueset.ValueSetExpansion(jsondict)
        if "ValueSetExpansionParameter" == resource_type:
            from . import valueset
            return valueset.ValueSetExpansionParameter(jsondict)
        if "ValueSetExpansionContains" == resource_type:
            from . import valueset
            return valueset.ValueSetExpansionContains(jsondict)
        if "VerificationResult" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResult(jsondict)
        if "VerificationResultPrimarySource" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResultPrimarySource(jsondict)
        if "VerificationResultAttestation" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResultAttestation(jsondict)
        if "VerificationResultValidator" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResultValidator(jsondict)
        if "VisionPrescription" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "VisionPrescriptionLensSpecification" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescriptionLensSpecification(jsondict)
        if "VisionPrescriptionLensSpecificationPrism" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescriptionLensSpecificationPrism(jsondict)
        if "MetadataResource" == resource_type:
            from . import metadataresource
            return metadataresource.MetadataResource(jsondict)
        from . import element
        return element.Element(jsondict)
