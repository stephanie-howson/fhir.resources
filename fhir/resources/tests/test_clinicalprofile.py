#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-01-17.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import clinicalprofile, identifier, fhirreference
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ClinicalProfileTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ClinicalProfile", js["resourceType"])
        return clinicalprofile.ClinicalProfile(js)

    def test_create_clpr(self):
        clpr = clinicalprofile.ClinicalProfile()
        clpr.id = 'Group/jh-17'
        clpr.identifier = [identifier.Identifier({'value': 'Group/jh-17'})]
        clpr.status = 'draft'
        clpr.population = fhirreference.FHIRReference({'reference': 'Group/jh-18'})
        clpr.reporter = fhirreference.FHIRReference({'reference': 'Organization/JHM'})
        clpr.cohort = fhirreference.FHIRReference({'reference': 'Group/jh-19'})
        js = clpr.as_json()
        print(js)
        self.assertEqual(json.loads("""{
  "resourceType": "Group",
  "id": "lab-ALL-ALL-ALL",
  "type": "person",
  "actual": true
}"""), clpr.as_json())

