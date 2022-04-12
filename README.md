# What is this?
It's assignment's solution.
You have set of products. And you have some discount rules. You need to apply rules to each of products. By the time rules may change, so architecture must allow easily adding or changing rules.
## Demo
Checkout [demo](demo.py)
## How to run linter and tests
```bash
python -m pip install -r requirements/lint.txt
make check
```
## Architecture
Rules stores in json format (outside my solution). 
RuleBuilder class is responsible for validation raw json, and building Rule objects.
Each rule consist from Match and Action. Match only checking if this rule applicable to this product.
Action describes how to make a discount to this product.
