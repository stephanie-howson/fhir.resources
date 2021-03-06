#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-17.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import bundle
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)
    
    def testBundle1(self):
        inst = self.instantiate_from("diagnosticreport-hla-genetics-results-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle1(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)
    
    def implBundle1(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("urn:uuid:b0a4b18e-94e7-4b1b-8031-c7ae4bdd8db9"))
        self.assertEqual(force_bytes(inst.entry[0].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[0].request.url), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("urn:uuid:8200dab6-18a2-4550-b913-a7db480c0804"))
        self.assertEqual(force_bytes(inst.entry[1].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[1].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("urn:uuid:7c393185-f15c-45bc-a714-c0fdbea32675"))
        self.assertEqual(force_bytes(inst.entry[2].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[2].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("urn:uuid:65c85f14-c3a0-4b72-818f-820e04fcc621"))
        self.assertEqual(force_bytes(inst.entry[3].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[3].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("urn:uuid:fbba9fe7-0ece-4ec1-9233-a437a8d242a0"))
        self.assertEqual(force_bytes(inst.entry[4].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[4].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("urn:uuid:cbabf93e-1b4b-46f2-ba1e-d84862670670"))
        self.assertEqual(force_bytes(inst.entry[5].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[5].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("urn:uuid:c233ad3d-1572-48d6-93da-0a583535e138"))
        self.assertEqual(force_bytes(inst.entry[6].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[6].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("urn:uuid:05fa52d7-5c67-460a-8722-d3460b24d6fe"))
        self.assertEqual(force_bytes(inst.entry[7].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[7].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[8].fullUrl), force_bytes("urn:uuid:db69e549-6267-4777-b4b9-8813f3329309"))
        self.assertEqual(force_bytes(inst.entry[8].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[8].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.entry[9].fullUrl), force_bytes("urn:uuid:bb55c2bc-5ad2-4bc1-8ff3-c407d06b12d0"))
        self.assertEqual(force_bytes(inst.entry[9].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[9].request.url), force_bytes("Sequence"))
        self.assertEqual(force_bytes(inst.id), force_bytes("hla-1"))
        self.assertEqual(force_bytes(inst.type), force_bytes("transaction"))
    
    def testBundle2(self):
        inst = self.instantiate_from("practitioner-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle2(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)
    
    def implBundle2(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/1"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("1"))
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/13"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("13"))
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/14"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("14"))
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/15"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("15"))
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/16"))
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("16"))
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/17"))
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("17"))
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/18"))
        self.assertEqual(force_bytes(inst.entry[6].resource.id), force_bytes("18"))
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/19"))
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("19"))
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[8].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/20"))
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("20"))
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[9].fullUrl), force_bytes("http://hl7.org/fhir/Practitioner/21"))
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("21"))
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("3ad0687e-f477-468c-afd5-fcc2bf897809"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))
    
    def testBundle3(self):
        inst = self.instantiate_from("xds-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle3(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)
    
    def implBundle3(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("urn:uuid:3fdc72f4-a11d-4a9d-9260-a9f745779e1d"))
        self.assertEqual(force_bytes(inst.entry[0].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[0].request.url), force_bytes("DocumentReference"))
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://localhost:9556/svc/fhir/Patient/a2"))
        self.assertEqual(force_bytes(inst.entry[1].request.ifNoneExist), force_bytes("Patient?identifier=http://acme.org/xds/patients!89765a87b"))
        self.assertEqual(force_bytes(inst.entry[1].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[1].request.url), force_bytes("Patient"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("a2"))
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://localhost:9556/svc/fhir/Practitioner/a3"))
        self.assertEqual(force_bytes(inst.entry[2].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[2].request.url), force_bytes("Practitioner"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("a3"))
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://localhost:9556/svc/fhir/Practitioner/a4"))
        self.assertEqual(force_bytes(inst.entry[3].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[3].request.url), force_bytes("Practitioner"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("a4"))
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("http://localhost:9556/svc/fhir/Binary/1e404af3-077f-4bee-b7a6-a9be97e1ce32"))
        self.assertEqual(force_bytes(inst.entry[4].request.method), force_bytes("POST"))
        self.assertEqual(force_bytes(inst.entry[4].request.url), force_bytes("Binary"))
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("1e404af3-077f-4bee-b7a6-a9be97e1ce32"))
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("xds"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("transaction"))
    
    def testBundle4(self):
        inst = self.instantiate_from("document-example-dischargesummary.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle4(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)
    
    def implBundle4(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://fhir.healthintersections.com.au/open/Composition/180f219f-97a8-486d-99d9-ed631fe4fc57"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("180f219f-97a8-486d-99d9-ed631fe4fc57"))
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://fhir.healthintersections.com.au/open/Practitioner/example"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("example"))
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://fhir.healthintersections.com.au/open/Patient/d1"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("d1"))
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://fhir.healthintersections.com.au/open/Encounter/doc-example"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("doc-example"))
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("urn:uuid:541a72a8-df75-4484-ac89-ac4923f03b81"))
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("urn:uuid:124a6916-5d84-4b8c-b250-10cefb8e6e86"))
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("urn:uuid:673f8db5-0ffd-4395-9657-6da00420bbc1"))
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("urn:uuid:47600e0f-b6b5-4308-84b5-5dec157f7637"))
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("father"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("urn:uuid:0c3151bd-1cbf-4d64-b04d-cd9187a4c6e0"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(force_bytes(inst.signature.contentType), force_bytes("image/jpg"))
        self.assertEqual(force_bytes(inst.signature.type[0].code), force_bytes("1.2.840.10065.1.12.1.1"))
        self.assertEqual(force_bytes(inst.signature.type[0].display), force_bytes("Author's Signature"))
        self.assertEqual(force_bytes(inst.signature.type[0].system), force_bytes("urn:iso-astm:E1762-95:2013"))
        self.assertEqual(inst.signature.when.date, FHIRDate("2015-08-31T07:42:33+10:00").date)
        self.assertEqual(inst.signature.when.as_json(), "2015-08-31T07:42:33+10:00")
        self.assertEqual(force_bytes(inst.type), force_bytes("document"))
    
    def testBundle5(self):
        inst = self.instantiate_from("patient-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle5(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)
    
    def implBundle5(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://hl7.org/fhir/Patient/1"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("1"))
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://hl7.org/fhir/Patient/2"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("2"))
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://hl7.org/fhir/Patient/3"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("3"))
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://hl7.org/fhir/Patient/4"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("4"))
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("http://hl7.org/fhir/Patient/5"))
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("5"))
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("http://hl7.org/fhir/Patient/6"))
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("6"))
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("http://hl7.org/fhir/Patient/7"))
        self.assertEqual(force_bytes(inst.entry[6].resource.id), force_bytes("7"))
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("http://hl7.org/fhir/Patient/8"))
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("8"))
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[8].fullUrl), force_bytes("http://hl7.org/fhir/Patient/9"))
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("9"))
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[9].fullUrl), force_bytes("http://hl7.org/fhir/Patient/10"))
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("10"))
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("b248b1b2-1686-4b94-9936-37d7a5f94b51"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))
    
    def testBundle6(self):
        inst = self.instantiate_from("bundle-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle6(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)
    
    def implBundle6(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("https://example.com/base/MedicationRequest/3123"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("3123"))
        self.assertEqual(force_bytes(inst.entry[0].search.mode), force_bytes("match"))
        self.assertEqual(inst.entry[0].search.score, 1)
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("https://example.com/base/Medication/example"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.entry[1].search.mode), force_bytes("include"))
        self.assertEqual(force_bytes(inst.id), force_bytes("bundle-example"))
        self.assertEqual(force_bytes(inst.link[0].relation), force_bytes("self"))
        self.assertEqual(force_bytes(inst.link[0].url), force_bytes("https://example.com/base/MedicationRequest?patient=347&_include=MedicationRequest.medication"))
        self.assertEqual(force_bytes(inst.link[1].relation), force_bytes("next"))
        self.assertEqual(force_bytes(inst.link[1].url), force_bytes("https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-08-18T01:43:30Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-08-18T01:43:30Z")
        self.assertEqual(inst.total, 3)
        self.assertEqual(force_bytes(inst.type), force_bytes("searchset"))
    
    def testBundle7(self):
        inst = self.instantiate_from("patient-examples-cypress-template.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle7(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)
    
    def implBundle7(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://hl7.org/fhir/Patient/71"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("71"))
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://hl7.org/fhir/Patient/72"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("72"))
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://hl7.org/fhir/Patient/73"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("73"))
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://hl7.org/fhir/Patient/74"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("74"))
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("http://hl7.org/fhir/Patient/75"))
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("75"))
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("http://hl7.org/fhir/Patient/76"))
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("76"))
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("http://hl7.org/fhir/Patient/77"))
        self.assertEqual(force_bytes(inst.entry[6].resource.id), force_bytes("77"))
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("http://hl7.org/fhir/Patient/78"))
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("78"))
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[8].fullUrl), force_bytes("http://hl7.org/fhir/Patient/79"))
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("79"))
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.entry[9].fullUrl), force_bytes("http://hl7.org/fhir/Patient/80"))
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("80"))
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("b0a5e4277-83c4-4adb-87e2-e3efe3369b6f"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))
    
    def testBundle8(self):
        inst = self.instantiate_from("diagnosticreport-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle8(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)
    
    def implBundle8(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/3"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("3"))
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/4"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("4"))
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/5"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("5"))
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/6"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("6"))
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/7"))
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("7"))
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/8"))
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("8"))
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/9"))
        self.assertEqual(force_bytes(inst.entry[6].resource.id), force_bytes("9"))
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/15"))
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("15"))
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[8].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/16"))
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("16"))
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.entry[9].fullUrl), force_bytes("http://hl7.org/fhir/DiagnosticReport/17"))
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("17"))
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("72ac8493-52ac-41bd-8d5d-7258c289b5ea"))
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))
    
    def testBundle9(self):
        inst = self.instantiate_from("location-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle9(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)
    
    def implBundle9(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://hl7.org/fhir/Location/2"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("2"))
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://hl7.org/fhir/Location/3"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("3"))
        self.assertEqual(force_bytes(inst.id), force_bytes("3ad0687e-f477-468c-afd5-fcc2bf897819"))
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))
    
    def testBundle10(self):
        inst = self.instantiate_from("practitionerrole-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle10(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)
    
    def implBundle10(self, inst):
        self.assertEqual(force_bytes(inst.entry[0].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/f003-0"))
        self.assertEqual(force_bytes(inst.entry[0].resource.id), force_bytes("f003-0"))
        self.assertEqual(force_bytes(inst.entry[1].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/example-0"))
        self.assertEqual(force_bytes(inst.entry[1].resource.id), force_bytes("example-0"))
        self.assertEqual(force_bytes(inst.entry[2].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/example-1"))
        self.assertEqual(force_bytes(inst.entry[2].resource.id), force_bytes("example-1"))
        self.assertEqual(force_bytes(inst.entry[3].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/example-2"))
        self.assertEqual(force_bytes(inst.entry[3].resource.id), force_bytes("example-2"))
        self.assertEqual(force_bytes(inst.entry[4].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/f007-0"))
        self.assertEqual(force_bytes(inst.entry[4].resource.id), force_bytes("f007-0"))
        self.assertEqual(force_bytes(inst.entry[5].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/f004-0"))
        self.assertEqual(force_bytes(inst.entry[5].resource.id), force_bytes("f004-0"))
        self.assertEqual(force_bytes(inst.entry[6].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/xcda1-0"))
        self.assertEqual(force_bytes(inst.entry[6].resource.id), force_bytes("xcda1-0"))
        self.assertEqual(force_bytes(inst.entry[7].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/f202-0"))
        self.assertEqual(force_bytes(inst.entry[7].resource.id), force_bytes("f202-0"))
        self.assertEqual(force_bytes(inst.entry[8].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/f201-0"))
        self.assertEqual(force_bytes(inst.entry[8].resource.id), force_bytes("f201-0"))
        self.assertEqual(force_bytes(inst.entry[9].fullUrl), force_bytes("http://hl7.org/fhir/PractitionerRole/f203-0"))
        self.assertEqual(force_bytes(inst.entry[9].resource.id), force_bytes("f203-0"))
        self.assertEqual(force_bytes(inst.id), force_bytes("3ad0687e-f477-468c-afd5-fcc2bf897808"))
        self.assertEqual(force_bytes(inst.type), force_bytes("collection"))

