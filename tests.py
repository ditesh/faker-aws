"""Tests for faker-aws."""

import unittest
import faker_aws
from faker import Faker


class TestAWS(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_aws.Provider)

    def test_arn(self):
        arn = self.fake.arn(service="rds")
        self.assertTrue(isinstance(arn, str))
        self.assertTrue(len(arn) > 0)
        self.assertTrue("db" in arn)

    def test_region(self):
        region = self.fake.region()
        self.assertTrue(isinstance(region, str))
        self.assertTrue(len(region) > 0)

    def test_service(self):
        service = self.fake.service()
        self.assertTrue(isinstance(service, str))
        self.assertTrue(len(service) > 0)


if __name__ == "__main__":
    unittest.main()
