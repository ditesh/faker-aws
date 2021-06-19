"""Provider for Faker which adds fake names for the AWS ecosystem."""

import random
import faker.providers

SERVICES = [
    "ec2",
    "rds",
    "dynamodb",
]

REGIONS = [
    "us-east-2",
    "us-east-1",
    "us-west-1",
    "us-west-2",
    "af-south-1",
    "ap-east-1",
    "ap-south-1",
    "ap-northeast-3",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-south-1",
    "eu-west-3",
    "eu-north-1",
    "me-south-1",
    "sa-east-1",
]

# From https://github.com/praneshr/project-names/blob/master/src/nouns.js
PROJECT_NAMES = [
    "world",
    "hand",
    "room",
    "face",
    "thing",
    "place",
    "door",
    "woman",
    "house",
    "money",
    "father",
    "government",
    "country",
    "mother",
    "water",
    "state",
    "family",
    "voice",
    "fact",
    "moment",
    "power",
    "city",
    "business",
    "war",
    "school",
    "system",
    "car",
    "number",
    "office",
    "point",
    "body",
    "wife",
    "air",
    "mind",
    "girl",
    "home",
    "company",
    "table",
    "group",
    "boy",
    "problem",
    "bed",
    "hair",
    "child",
    "sense",
    "job",
    "light",
    "question",
    "idea",
    "law",
    "word",
    "party",
    "food",
    "floor",
    "book",
    "reason",
    "story",
    "son",
    "heart",
    "friend",
    "interest",
    "right",
    "town",
    "history",
    "land",
    "program",
    "game",
    "control",
    "matter",
    "policy",
    "oil",
    "window",
    "nation",
    "position",
    "ground",
    "blood",
    "action",
    "wall",
    "street",
    "fire",
    "arm",
    "sound",
    "service",
    "chance",
    "information",
    "price",
    "building",
    "road",
    "paper",
    "court",
    "attention",
    "space",
    "form",
    "society",
]

STORAGE_TYPES = ["io1", "io2", "gp1", "gp2"]
INSTANCE_SIZES = ["micro", "small", "medium", "large", "xlarge", "2xlarge"]
INSTANCE_FAMILIES = ["t3", "m5", "r5"]

# Tag constants
TAG_KEYS_NAME = [
    "name",
    "app_name",
    "project_name",
    "component",
    "component_name",
    "microservice",
    "service",
]
TAG_KEYS_ENV = ["env", "Env", "ENV", "environment", "Environment"]
TAG_VALUES_ENV = [
    "dev",
    "Dev",
    "developer",
    "Developer",
    "development",
    "Development",
    "stage",
    "Stage",
    "staging",
    "Staging",
    "prod",
    "Prod",
    "production",
    "Production",
]
TAG_KEYS_COST = [
    "cost",
    "Cost",
    "costfamily",
    "cost_family",
    "Cost_Family",
    "CostFamily",
    "cost_category",
    "Cost_Category",
    "CostCategory",
]
TAG_KEYS_DEPARTMENT = ["dept", "Dept", "department", "departments"]
TAG_VALUES_DEPARTMENT = ["engineering", "tech", "marketing", "support", "sre"]


class AWSProvider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake names for the AWS ecosystem."""

    def service(self):
        return self.random_element(SERVICES)

    def region(self):
        return self.random_element(REGIONS)

    def storage_type(self):
        return self.random_element(STORAGE_TYPES)

    def instance_class(self, service=None):

        if service == "rds":
            return (
                "db."
                + self.random_element(INSTANCE_FAMILIES)
                + "."
                + self.random_element(INSTANCE_SIZES)
            )

        return "t3.medium"

    def tag(self):

        # Common tags are env, appname, cluster, cost
        r = random.randrange(3)

        # Env
        if r == 0:
            return (
                self.random_element(TAG_KEYS_ENV),
                self.random_element(TAG_VALUES_ENV),
            )

        # Appname
        elif r == 1:
            return (
                self.random_element(TAG_KEYS_NAME),
                self.random_element(PROJECT_NAMES),
            )

        # Cost tag
        elif r == 2:
            return (
                self.random_element(TAG_KEYS_COST),
                self.random_element(TAG_VALUES_DEPARTMENT),
            )

        # Department tag
        else:
            return (
                self.random_element(TAG_KEYS_DEPARTMENT),
                self.random_element(TAG_VALUES_DEPARTMENT),
            )

    def arn(
        self,
        service,
        region=None,
        account_id=None,
        resource_id=None,
        partition="aws",
    ):

        if region is None:
            region = self.region()

        if account_id is None:
            account_id = str(random.randint(100000000000, 999999999999))

        if resource_id is None:
            if service == "rds":
                resource_id = self.random_element(PROJECT_NAMES) + "db"
            else:
                resource_id = random.randint(1000000000000, 9999999999999)

        if service == "rds":
            resource = "db:" + resource_id
        else:
            resource = resource_id

        return "arn:{0}:{1}:{2}:{3}".format(
            partition, region, account_id, resource
        )
