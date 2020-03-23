# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    FunctionName: Optional[str]
    FunctionVersion: Optional[str]
    Id: Optional[str]
    InvokeArn: Optional[str]
    Name: Optional[str]
    RoutingConfig: Optional[Sequence["_RoutingConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            FunctionName=json_data.get("FunctionName"),
            FunctionVersion=json_data.get("FunctionVersion"),
            Id=json_data.get("Id"),
            InvokeArn=json_data.get("InvokeArn"),
            Name=json_data.get("Name"),
            RoutingConfig=json_data.get("RoutingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoutingConfig:
    AdditionalVersionWeights: Optional[Sequence["_AdditionalVersionWeights"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingConfig"]:
        if not json_data:
            return None
        return cls(
            AdditionalVersionWeights=json_data.get("AdditionalVersionWeights"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingConfig = RoutingConfig


@dataclass
class AdditionalVersionWeights:
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalVersionWeights"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalVersionWeights"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalVersionWeights = AdditionalVersionWeights

