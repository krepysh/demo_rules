from app.domain import Rule, Action, Match
from typing import Any, Mapping, TypedDict


class SerializedMatch(TypedDict):
    attribute_name: str
    condition: str
    attribute_value: Any


class SerializedAction(TypedDict):
    absolute_discount: int


class SerializedRule(TypedDict):
    match: SerializedMatch
    action: SerializedAction


class RuleBuilder:
    def build_rule(self, jsoned_rule: SerializedRule) -> Rule:
        if not self.is_rule_valid(jsoned_rule):
            self.log_invalid_rule(jsoned_rule)
            raise ValueError(f'Rule {jsoned_rule} is invalid!')
        match = self.create_match(jsoned_rule)
        action = self.create_action(jsoned_rule)
        rule = Rule(match=match, action=action)
        return rule

    def is_rule_valid(self, jsoned_rule: SerializedRule) -> bool:
        return (
            self.is_match_valid(jsoned_rule['match'])
            and self.is_action_valid(jsoned_rule['action'])
        )

    def create_match(self, jsoned_rule: SerializedRule) -> Match:
        serialized_match = jsoned_rule['match']
        match = Match(
            attribute_name=serialized_match['attribute_name'],
            condition=serialized_match['condition'],
            value=serialized_match['attribute_value'],
        )
        return match

    def create_action(self, jsoned_rule: SerializedRule) -> Action:
        action = Action(discount_size=jsoned_rule['action']['absolute_discount'])
        return action

    def is_match_valid(self, serialized_match: SerializedMatch) -> bool:
        return all(
            [
                self.is_key_exist_in_dict('attribute_name', str, serialized_match),
                self.is_key_exist_in_dict('condition', str, serialized_match),
                self.is_key_exist_in_dict('attribute_value', object, serialized_match),
            ],
        )

    def is_action_valid(self, serialized_action: SerializedAction) -> bool:
        return self.is_key_exist_in_dict('absolute_discount', int, serialized_action)

    def is_key_exist_in_dict(self, key: str, key_type: type, dict_to_check: Mapping) -> bool:
        try:
            value = dict_to_check[key]
        except (KeyError, ValueError):
            return False
        return isinstance(value, key_type)

    def log_invalid_rule(self, jsoned_rule: SerializedRule) -> None:
        pass
