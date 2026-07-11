from __future__ import annotations

from abc import ABC, abstractmethod

from migration_sdk.contracts.intake import MigrationIntake, TargetContract


class TargetAdapter(ABC):
    platform: str

    @abstractmethod
    def build_contract(self, intake: MigrationIntake) -> TargetContract:
        raise NotImplementedError

    @abstractmethod
    def deployment_plan(self, contract: TargetContract) -> tuple[str, ...]:
        raise NotImplementedError
