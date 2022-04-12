from app.services import RuleBuilder, SerializedRule
from app.domain import Product

raw_rule: SerializedRule = {
        'match': {'attribute_name': 'price', 'condition': 'less', 'attribute_value': 50},
        'action': {'absolute_discount': 10},
}
product = Product('Product', 40, 'black', 'sk', 0, 'abstract')
rule = RuleBuilder().build_rule(raw_rule)
assert rule.apply(product) == 30
