#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-9a13c5160d on 2019-04-12.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import measure
from .fhirdate import FHIRDate


class MeasureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Measure", js["resourceType"])
        return measure.Measure(js)
    
    def testMeasure1(self):
        inst = self.instantiate_from("measure-component-b-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure1(inst2)
    
    def implMeasure1(self, inst):
        self.assertEqual(inst.group[0].id, "Main")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "Initial Population")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "Denominator")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "Numerator")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.id, "component-b-example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Screening for Depression")
    
    def testMeasure2(self):
        inst = self.instantiate_from("measure-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure2(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure2(inst2)
    
    def implMeasure2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2014-03-08").date)
        self.assertEqual(inst.date.as_json(), "2014-03-08")
        self.assertEqual(inst.description, "Exclusive breastfeeding measure of outcomes for exclusive breastmilk feeding of newborns.")
        self.assertEqual(inst.group[0].id, "PopulationGroup1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "InitialPopulation1")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "Denominator1")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "denominator-exclusions")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "DenominatorExclusions1")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[3].criteria.expression, "Numerator1")
        self.assertEqual(inst.group[0].population[3].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].id, "PopulationGroup2")
        self.assertEqual(inst.group[1].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[1].population[0].criteria.expression, "InitialPopulation2")
        self.assertEqual(inst.group[1].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[1].population[1].criteria.expression, "Denominator2")
        self.assertEqual(inst.group[1].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].population[2].code.coding[0].code, "denominator-exclusion")
        self.assertEqual(inst.group[1].population[2].criteria.expression, "DenominatorExclusions2")
        self.assertEqual(inst.group[1].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].population[3].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[1].population[3].criteria.expression, "Numerator2")
        self.assertEqual(inst.group[1].population[3].criteria.language, "text/cql")
        self.assertEqual(inst.id, "measure-predecessor-example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "exclusive-breastfeeding-measure")
        self.assertEqual(inst.improvementNotation.coding[0].code, "increase")
        self.assertEqual(inst.improvementNotation.coding[0].system, "http://terminology.hl7.org/CodeSystem/measure-improvement-notation")
        self.assertEqual(inst.library[0], "Library/library-exclusive-breastfeeding-cqm-logic")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.purpose, "Measure of newborns who were fed breast milk only since birth")
        self.assertEqual(inst.relatedArtifact[0].citation, "American Academy of Pediatrics. (2005). Section on Breastfeeding. Policy Statement:Breastfeeding and the Use of Human Milk. Pediatrics.115:496-506.")
        self.assertEqual(inst.relatedArtifact[0].type, "documentation")
        self.assertEqual(inst.relatedArtifact[1].type, "documentation")
        self.assertEqual(inst.relatedArtifact[2].type, "documentation")
        self.assertEqual(inst.relatedArtifact[3].type, "documentation")
        self.assertEqual(inst.relatedArtifact[4].type, "documentation")
        self.assertEqual(inst.relatedArtifact[5].type, "documentation")
        self.assertEqual(inst.relatedArtifact[6].citation, "Kramer, M.S. & Kakuma, R. (2002).Optimal duration of exclusive breastfeeding. [107 refs] Cochrane Database of Systematic Reviews. (1):CD003517.")
        self.assertEqual(inst.relatedArtifact[6].type, "documentation")
        self.assertEqual(inst.relatedArtifact[7].citation, "Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal race/ethnicity and one-month exclusive breastfeeding in association with the in-hospital feeding modality. Breastfeeding Medicine. 2(2):92-8.")
        self.assertEqual(inst.relatedArtifact[7].type, "documentation")
        self.assertEqual(inst.relatedArtifact[8].type, "documentation")
        self.assertEqual(inst.relatedArtifact[9].type, "documentation")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Exclusive Breastfeeding Measure")
        self.assertEqual(inst.topic[0].text, "Exclusive Breastfeeding")
        self.assertEqual(inst.type[0].coding[0].code, "process")
        self.assertEqual(inst.version, "4.0.0")
    
    def testMeasure3(self):
        inst = self.instantiate_from("measure-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure3(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure3(inst2)
    
    def implMeasure3(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-01-01")
        self.assertEqual(inst.author[0].name, "National Committee for Quality Assurance")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://www.ncqa.org/")
        self.assertEqual(inst.date.date, FHIRDate("2017-03-10").date)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(inst.description, "Percentage of children 3-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode.")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2017-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.group[0].id, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "CMS146.InInitialPopulation")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "CMS146.InNumerator")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "CMS146.InDenominator")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code, "denominator-exclusion")
        self.assertEqual(inst.group[0].population[3].criteria.expression, "CMS146.InDenominatorExclusions")
        self.assertEqual(inst.group[0].population[3].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].stratifier[0].code.text, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[0].criteria.expression, "CMS146.AgesUpToNine")
        self.assertEqual(inst.group[0].stratifier[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].stratifier[1].code.text, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[1].criteria.expression, "CMS146.AgesTenPlus")
        self.assertEqual(inst.group[0].stratifier[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].stratifier[2].code.text, "stratifier-gender")
        self.assertEqual(inst.group[0].stratifier[2].criteria.expression, "Patient.gender")
        self.assertEqual(inst.group[0].stratifier[2].criteria.language, "text/fhirpath")
        self.assertEqual(inst.guidance, "This is an episode of care measure that examines all eligible episodes for the patient during the measurement period. If the patient has more than one episode, include all episodes in the measure")
        self.assertEqual(inst.id, "measure-cms146-example")
        self.assertEqual(inst.identifier[0].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "146")
        self.assertEqual(inst.identifier[1].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "0002")
        self.assertEqual(inst.improvementNotation.coding[0].code, "increase")
        self.assertEqual(inst.improvementNotation.coding[0].system, "http://terminology.hl7.org/CodeSystem/measure-improvement-notation")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-09-01").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-09-01")
        self.assertEqual(inst.library[0], "Library/library-cms146-example")
        self.assertEqual(inst.name, "CMS146")
        self.assertEqual(inst.publisher, "National Committee for Quality Assurance")
        self.assertEqual(inst.purpose, "Measure of children with a group A streptococcus test in the 7-day period from 3 days prior through 3 days after the diagnosis of pharyngitis")
        self.assertEqual(inst.relatedArtifact[0].citation, "Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. _Antibiotic treatment of children with sore throat._ JAMA 294(18):2315-2322. ")
        self.assertEqual(inst.relatedArtifact[0].type, "documentation")
        self.assertEqual(inst.relatedArtifact[1].citation, "Infectious Diseases Society of America. 2012. _Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update._ ")
        self.assertEqual(inst.relatedArtifact[1].type, "documentation")
        self.assertEqual(inst.relatedArtifact[2].type, "documentation")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.supplementalData[0].code.text, "supplemental-data-gender")
        self.assertEqual(inst.supplementalData[0].criteria.expression, "Patient.gender")
        self.assertEqual(inst.supplementalData[0].criteria.language, "text/fhirpath")
        self.assertEqual(inst.supplementalData[1].code.text, "supplemental-data-deceased")
        self.assertEqual(inst.supplementalData[1].criteria.expression, "deceasedBoolean")
        self.assertEqual(inst.supplementalData[1].criteria.language, "text/fhirpath")
        self.assertEqual(inst.text.status, "additional")
        self.assertEqual(inst.title, "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.topic[0].coding[0].code, "57024-2")
        self.assertEqual(inst.topic[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.type[0].coding[0].code, "process")
        self.assertEqual(inst.url, "http://hl7.org/fhir/Measure/measure-cms146-example")
        self.assertEqual(inst.useContext[0].code.code, "program")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.text, "eligibile-provider")
        self.assertEqual(inst.useContext[1].code.code, "age")
        self.assertEqual(inst.useContext[1].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueRange.high.unit, "a")
        self.assertEqual(inst.useContext[1].valueRange.high.value, 18)
        self.assertEqual(inst.useContext[1].valueRange.low.unit, "a")
        self.assertEqual(inst.useContext[1].valueRange.low.value, 3)
        self.assertEqual(inst.version, "1.0.0")
    
    def testMeasure4(self):
        inst = self.instantiate_from("measure-component-a-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure4(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure4(inst2)
    
    def implMeasure4(self, inst):
        self.assertEqual(inst.group[0].id, "Main")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "Initial Population")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "Denominator")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "Numerator")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.id, "component-a-example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Screening for Alcohol Misuse")
    
    def testMeasure5(self):
        inst = self.instantiate_from("measure-composite-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure5(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure5(inst2)
    
    def implMeasure5(self, inst):
        self.assertEqual(inst.compositeScoring.coding[0].code, "opportunity")
        self.assertEqual(inst.id, "composite-example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource, "Measure/component-a-example")
        self.assertEqual(inst.relatedArtifact[0].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[1].resource, "Measure/component-b-example")
        self.assertEqual(inst.relatedArtifact[1].type, "composed-of")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Behavioral Assessment Composite Measure")

