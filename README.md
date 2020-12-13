# faker-aws

Provider for [Faker](https://faker.readthedocs.io/) which adds fake details for the AWS ecosystem.

# Installation

```
pip3 install faker-aws
```

# Usage

## Python

```python
from faker import Faker
from faker_aws import AWSProvider

fake = Faker()
fake.add_provider(AWSProvider)
print(faker.arn(service="rds"))  # prints a fake ARN for RDS
```
