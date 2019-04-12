#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-9a13c5160d (http://hl7.org/fhir/StructureDefinition/ClinicalProfile) on 2019-04-12.
#  2019, SMART Health IT.


from . import domainresource

class ClinicalProfile(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    Clinical Profiles summarize and demonstrate the features of a population.
    """
    
    resource_type = "ClinicalProfile"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cohort = None
        """ The cohort within the population that this profile represents.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the profile was generated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        """ Diagnosis profile entry.
        List of `ClinicalProfileDiagnosis` items (represented as `dict` in JSON). """
        
        self.hpo = None
        """ HPO Profile Entry.
        List of `ClinicalProfileHpo` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the ClinicalProfile.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lab = None
        """ Laboratory profile entry.
        List of `ClinicalProfileLab` items (represented as `dict` in JSON). """
        
        self.medication = None
        """ Medication profile entry.
        List of `ClinicalProfileMedication` items (represented as `dict` in JSON). """
        
        self.population = None
        """ The base population against which this profile was generated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Procedure profile entry.
        List of `ClinicalProfileProcedure` items (represented as `dict` in JSON). """
        
        self.reporter = None
        """ Who is reporting the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ Identifier(s) from where the profile was acquired.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ complete | draft | error.
        Type `str`. """
        
        super(ClinicalProfile, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfile, self).elementProperties()
        js.extend([
            ("cohort", "cohort", fhirreference.FHIRReference, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ClinicalProfileDiagnosis, True, None, False),
            ("hpo", "hpo", ClinicalProfileHpo, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lab", "lab", ClinicalProfileLab, True, None, False),
            ("medication", "medication", ClinicalProfileMedication, True, None, False),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("procedure", "procedure", ClinicalProfileProcedure, True, None, False),
            ("reporter", "reporter", fhirreference.FHIRReference, False, None, True),
            ("source", "source", identifier.Identifier, True, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class ClinicalProfileDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis profile entry.
    """
    
    resource_type = "ClinicalProfileDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Diagnosis code(s).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.correlatedDiagnoses = None
        """ Correlated diagnosies.
        Type `ClinicalProfileMedicationCorrelatedDiagnoses` (represented as `dict` in JSON). """
        
        self.correlatedMedications = None
        """ Correlated medications.
        Type `ClinicalProfileMedicationCorrelatedMedications` (represented as `dict` in JSON). """
        
        self.correlatedPhenotypes = None
        """ Correlated phenotypes.
        Type `ClinicalProfileMedicationCorrelatedPhenotypes` (represented as `dict` in JSON). """
        
        self.correlatedProcedures = None
        """ Correlated procedures.
        Type `ClinicalProfileMedicationCorrelatedProcedures` (represented as `dict` in JSON). """
        
        self.count = None
        """ Number of times listed per patient per hear for each code.
        Type `int`. """
        
        self.fractionOfSubjects = None
        """ Fraction of patients in with this diagnosis.
        Type `float`. """
        
        self.frequencyPerYear = None
        """ Frequency of this diagnosis per patient per year.
        Type `float`. """
        
        super(ClinicalProfileDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileDiagnosis, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileMedicationCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileMedicationCorrelatedMedications, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileMedicationCorrelatedPhenotypes, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileMedicationCorrelatedProcedures, False, None, False),
            ("count", "count", int, False, None, True),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
        ])
        return js


class ClinicalProfileHpo(backboneelement.BackboneElement):
    """ HPO Profile Entry.
    
    Phenotypic description.
    """
    
    resource_type = "ClinicalProfileHpo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ HPO code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.correlatedDiagnoses = None
        """ Correlated diagnosies.
        Type `ClinicalProfileMedicationCorrelatedDiagnoses` (represented as `dict` in JSON). """
        
        self.correlatedMedications = None
        """ Correlated medications.
        Type `ClinicalProfileMedicationCorrelatedMedications` (represented as `dict` in JSON). """
        
        self.correlatedPhenotypes = None
        """ Correlated phenotypes.
        Type `ClinicalProfileMedicationCorrelatedPhenotypes` (represented as `dict` in JSON). """
        
        self.correlatedProcedures = None
        """ Correlated procedures.
        Type `ClinicalProfileMedicationCorrelatedProcedures` (represented as `dict` in JSON). """
        
        self.fractionOfSubjects = None
        """ Fraction of patients with this procedure per year.
        Type `float`. """
        
        self.frequencyPerYear = None
        """ Frequency of this code per patient per year.
        Type `float`. """
        
        super(ClinicalProfileHpo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileHpo, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileMedicationCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileMedicationCorrelatedMedications, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileMedicationCorrelatedPhenotypes, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileMedicationCorrelatedProcedures, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
        ])
        return js


class ClinicalProfileLab(backboneelement.BackboneElement):
    """ Laboratory profile entry.
    """
    
    resource_type = "ClinicalProfileLab"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Lab code (LOINC).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.count = None
        """ Total number of lab tests.
        Type `int`. """
        
        self.fractionOfSubjects = None
        """ Fraction of subjects with this lab.
        Type `float`. """
        
        self.frequencyPerYear = None
        """ Frequency of this lab ordered/reported per patient per year.
        Type `float`. """
        
        self.scalarDistribution = None
        """ Scalar sample summary.
        Type `ClinicalProfileLabScalarDistribution` (represented as `dict` in JSON). """
        
        super(ClinicalProfileLab, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLab, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("count", "count", int, False, None, True),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, False),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("scalarDistribution", "scalarDistribution", ClinicalProfileLabScalarDistribution, False, None, False),
        ])
        return js


class ClinicalProfileLabScalarDistribution(backboneelement.BackboneElement):
    """ Scalar sample summary.
    """
    
    resource_type = "ClinicalProfileLabScalarDistribution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.correlatedLabs = None
        """ Correlated laboratory tests.
        Type `ClinicalProfileLabScalarDistributionCorrelatedLabs` (represented as `dict` in JSON). """
        
        self.decile = None
        """ Decile partitions.
        List of `ClinicalProfileLabScalarDistributionDecile` items (represented as `dict` in JSON). """
        
        self.fractionAboveNormal = None
        """ Fraction of samples above normalized normal range.
        Type `float`. """
        
        self.fractionBelowNormal = None
        """ Fraction of samples below normalized normal range.
        Type `float`. """
        
        self.max = None
        """ Maximum value.
        Type `float`. """
        
        self.mean = None
        """ Mean.
        Type `float`. """
        
        self.median = None
        """ Median.
        Type `float`. """
        
        self.min = None
        """ Minimum value.
        Type `float`. """
        
        self.normalizedHigh = None
        """ Normalize high normal range.
        Type `float`. """
        
        self.normalizedLow = None
        """ Normalize low normal range.
        Type `float`. """
        
        self.stdDev = None
        """ Standard deviation.
        Type `float`. """
        
        self.units = None
        """ Units of scalar result.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(ClinicalProfileLabScalarDistribution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistribution, self).elementProperties()
        js.extend([
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("decile", "decile", ClinicalProfileLabScalarDistributionDecile, True, None, False),
            ("fractionAboveNormal", "fractionAboveNormal", float, False, None, False),
            ("fractionBelowNormal", "fractionBelowNormal", float, False, None, False),
            ("max", "max", float, False, None, True),
            ("mean", "mean", float, False, None, True),
            ("median", "median", float, False, None, True),
            ("min", "min", float, False, None, True),
            ("normalizedHigh", "normalizedHigh", float, False, None, False),
            ("normalizedLow", "normalizedLow", float, False, None, False),
            ("stdDev", "stdDev", float, False, None, True),
            ("units", "units", quantity.Quantity, False, None, True),
        ])
        return js


class ClinicalProfileLabScalarDistributionCorrelatedLabs(backboneelement.BackboneElement):
    """ Correlated laboratory tests.
    
    An ordered list of the laboratory tests  that are most closely correlated.
    This list can be limited by the top "n" labs and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    
    resource_type = "ClinicalProfileLabScalarDistributionCorrelatedLabs"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abscorrelation = None
        """ Minimum absolute value of correlation coefficient.
        Type `float`. """
        
        self.entry = None
        """ Correlated lab.
        List of `ClinicalProfileLabScalarDistributionCorrelatedLabsEntry` items (represented as `dict` in JSON). """
        
        self.topn = None
        """ Number of correlations cutoff (e.g. top 10).
        Type `int`. """
        
        super(ClinicalProfileLabScalarDistributionCorrelatedLabs, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedLabs, self).elementProperties()
        js.extend([
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, True, None, False),
            ("topn", "topn", int, False, None, False),
        ])
        return js


class ClinicalProfileLabScalarDistributionCorrelatedLabsEntry(backboneelement.BackboneElement):
    """ Correlated lab.
    """
    
    resource_type = "ClinicalProfileLabScalarDistributionCorrelatedLabsEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coefficient = None
        """ Correlation coefficient.
        Type `float`. """
        
        self.labcode = None
        """ Lab code (LOINC) or Lab Group Code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, self).elementProperties()
        js.extend([
            ("coefficient", "coefficient", float, False, None, True),
            ("labcode", "labcode", codeableconcept.CodeableConcept, True, None, True),
        ])
        return js


class ClinicalProfileLabScalarDistributionDecile(backboneelement.BackboneElement):
    """ Decile partitions.
    """
    
    resource_type = "ClinicalProfileLabScalarDistributionDecile"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.nth = None
        """ Particular decile (10, 20, …).
        Type `int`. """
        
        self.value = None
        """ Cutoff value for this decile.
        Type `float`. """
        
        super(ClinicalProfileLabScalarDistributionDecile, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionDecile, self).elementProperties()
        js.extend([
            ("nth", "nth", int, False, None, True),
            ("value", "value", float, False, None, True),
        ])
        return js


class ClinicalProfileMedication(backboneelement.BackboneElement):
    """ Medication profile entry.
    """
    
    resource_type = "ClinicalProfileMedication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Indicates the type of medication dispense (for example, where the
        medication is expected to be consumed or administered (i.e.
        inpatient or outpatient)).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.correlatedDiagnoses = None
        """ Correlated diagnosies.
        Type `ClinicalProfileMedicationCorrelatedDiagnoses` (represented as `dict` in JSON). """
        
        self.correlatedMedications = None
        """ Correlated medications.
        Type `ClinicalProfileMedicationCorrelatedMedications` (represented as `dict` in JSON). """
        
        self.correlatedPhenotypes = None
        """ Correlated phenotypes.
        Type `ClinicalProfileMedicationCorrelatedPhenotypes` (represented as `dict` in JSON). """
        
        self.correlatedProcedures = None
        """ Correlated procedures.
        Type `ClinicalProfileMedicationCorrelatedProcedures` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `ClinicalProfileMedicationDosage` (represented as `dict` in JSON). """
        
        self.fractionOfSubjects = None
        """ Fraction of patients in cohort treated with this drug.
        Type `float`. """
        
        self.frequencyPerYear = None
        """ Frequency of treatments per patient per year.
        Type `float`. """
        
        self.medicationCodeableConcept = None
        """ Medication(s) being profiled.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Medication(s) being profiled.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.treatementDuration = None
        """ Duration of treatment (in 1 year).
        Type `float`. """
        
        super(ClinicalProfileMedication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedication, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileMedicationCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileMedicationCorrelatedMedications, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileMedicationCorrelatedPhenotypes, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileMedicationCorrelatedProcedures, False, None, False),
            ("dosage", "dosage", ClinicalProfileMedicationDosage, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("treatementDuration", "treatementDuration", float, False, None, False),
        ])
        return js


class ClinicalProfileMedicationCorrelatedDiagnoses(backboneelement.BackboneElement):
    """ Correlated diagnosies.
    
    An ordered list of  the diagnoses  that are most closely correlated.  This
    list can be limited by the top "n" diagnoses and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedDiagnoses"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abscorrelation = None
        """ Minimum absolute value of correlation coefficient.
        Type `float`. """
        
        self.entry = None
        """ Correlation entry.
        Type `ClinicalProfileMedicationCorrelatedDiagnosesEntry` (represented as `dict` in JSON). """
        
        self.topn = None
        """ Number of diagnoses cutoff (e.g. top 10).
        Type `int`. """
        
        super(ClinicalProfileMedicationCorrelatedDiagnoses, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedDiagnoses, self).elementProperties()
        js.extend([
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileMedicationCorrelatedDiagnosesEntry, False, None, False),
            ("topn", "topn", int, False, None, False),
        ])
        return js


class ClinicalProfileMedicationCorrelatedDiagnosesEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedDiagnosesEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Diagnosis code(s).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.coefficient = None
        """ Correlation coefficient.
        Type `float`. """
        
        super(ClinicalProfileMedicationCorrelatedDiagnosesEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedDiagnosesEntry, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


class ClinicalProfileMedicationCorrelatedMedications(backboneelement.BackboneElement):
    """ Correlated medications.
    
    An ordered list of  the medications  that are most closely correlated.
    This list can be limited by the top "n" medications and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedMedications"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.deviation = None
        """ Deviation cutoff.
        Type `float`. """
        
        self.entry = None
        """ Correlation entry.
        List of `ClinicalProfileMedicationCorrelatedMedicationsEntry` items (represented as `dict` in JSON). """
        
        self.topn = None
        """ Number of medications cutoff (e.g. top 10).
        Type `int`. """
        
        super(ClinicalProfileMedicationCorrelatedMedications, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedMedications, self).elementProperties()
        js.extend([
            ("deviation", "deviation", float, False, None, False),
            ("entry", "entry", ClinicalProfileMedicationCorrelatedMedicationsEntry, True, None, False),
            ("topn", "topn", int, False, None, False),
        ])
        return js


class ClinicalProfileMedicationCorrelatedMedicationsEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedMedicationsEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Indicates the type of medication dispense (for example, where the
        medication is expected to be consumed or administered (i.e.
        inpatient or outpatient)).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.coefficient = None
        """ Correlation coefficient.
        Type `float`. """
        
        self.medicationCodeableConcept = None
        """ Medication code(s).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Medication code(s).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClinicalProfileMedicationCorrelatedMedicationsEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedMedicationsEntry, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("coefficient", "coefficient", float, False, None, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
        ])
        return js


class ClinicalProfileMedicationCorrelatedPhenotypes(backboneelement.BackboneElement):
    """ Correlated phenotypes.
    
    An ordered list of  the phenotypes  that are most closely correlated.  This
    list can be limited by the top "n" phenotypes and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedPhenotypes"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abscorrelation = None
        """ Minimum absolute value of correlation coefficient.
        Type `float`. """
        
        self.entry = None
        """ Correlation entry.
        List of `ClinicalProfileMedicationCorrelatedPhenotypesEntry` items (represented as `dict` in JSON). """
        
        self.topn = None
        """ Number of phenotypes cutoff (e.g. top 10).
        Type `int`. """
        
        super(ClinicalProfileMedicationCorrelatedPhenotypes, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedPhenotypes, self).elementProperties()
        js.extend([
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileMedicationCorrelatedPhenotypesEntry, True, None, False),
            ("topn", "topn", int, False, None, False),
        ])
        return js


class ClinicalProfileMedicationCorrelatedPhenotypesEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    
    List of correlated phenotypes in descending order of the absolute value of
    the correlation coefficient.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedPhenotypesEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Phenotype codes.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.coefficient = None
        """ Correlation coefficient.
        Type `float`. """
        
        super(ClinicalProfileMedicationCorrelatedPhenotypesEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedPhenotypesEntry, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


class ClinicalProfileMedicationCorrelatedProcedures(backboneelement.BackboneElement):
    """ Correlated procedures.
    
    An ordered list of  the procedures  that are most closely correlated.  This
    list can be limited by the top "n" procedures and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedProcedures"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abscorrelation = None
        """ Minimum absolute value of correlation coefficient.
        Type `float`. """
        
        self.entry = None
        """ Correlation entry.
        List of `ClinicalProfileMedicationCorrelatedProceduresEntry` items (represented as `dict` in JSON). """
        
        self.topn = None
        """ Number of rocedures cutoff (e.g. top 10).
        Type `int`. """
        
        super(ClinicalProfileMedicationCorrelatedProcedures, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedProcedures, self).elementProperties()
        js.extend([
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileMedicationCorrelatedProceduresEntry, True, None, False),
            ("topn", "topn", int, False, None, False),
        ])
        return js


class ClinicalProfileMedicationCorrelatedProceduresEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    """
    
    resource_type = "ClinicalProfileMedicationCorrelatedProceduresEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Procedure code(s).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.coefficient = None
        """ Correlation coefficient.
        Type `float`. """
        
        super(ClinicalProfileMedicationCorrelatedProceduresEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationCorrelatedProceduresEntry, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


class ClinicalProfileMedicationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    """
    
    resource_type = "ClinicalProfileMedicationDosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dose = None
        """ Average amount of medication per dose.
        List of `Quantity` items (represented as `dict` in JSON). """
        
        self.method = None
        """ How the drug was administered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Dose quantity per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ Path(s) of substance into body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site(s) administered to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        
        super(ClinicalProfileMedicationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", quantity.Quantity, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, True, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("route", "route", codeableconcept.CodeableConcept, True, None, False),
            ("site", "site", codeableconcept.CodeableConcept, True, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class ClinicalProfileProcedure(backboneelement.BackboneElement):
    """ Procedure profile entry.
    """
    
    resource_type = "ClinicalProfileProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ ICD-10-PCS or CPT procedure code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.correlatedDiagnoses = None
        """ Correlated diagnosies.
        Type `ClinicalProfileMedicationCorrelatedDiagnoses` (represented as `dict` in JSON). """
        
        self.correlatedMedications = None
        """ Correlated medications.
        Type `ClinicalProfileMedicationCorrelatedMedications` (represented as `dict` in JSON). """
        
        self.correlatedPhenotypes = None
        """ Correlated phenotypes.
        Type `ClinicalProfileMedicationCorrelatedPhenotypes` (represented as `dict` in JSON). """
        
        self.correlatedProcedures = None
        """ Correlated procedures.
        Type `ClinicalProfileMedicationCorrelatedProcedures` (represented as `dict` in JSON). """
        
        self.fractionOfSubjects = None
        """ Fraction of patients with this procedure per year.
        Type `float`. """
        
        self.frequencyPerYear = None
        """ Frequency of procedure per patient per year.
        Type `float`. """
        
        super(ClinicalProfileProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileProcedure, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileMedicationCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileMedicationCorrelatedMedications, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileMedicationCorrelatedPhenotypes, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileMedicationCorrelatedProcedures, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
