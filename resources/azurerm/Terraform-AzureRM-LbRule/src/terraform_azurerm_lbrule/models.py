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
    BackendAddressPoolId: Optional[str]
    BackendPort: Optional[float]
    DisableOutboundSnat: Optional[bool]
    EnableFloatingIp: Optional[bool]
    EnableTcpReset: Optional[bool]
    FrontendIpConfigurationId: Optional[str]
    FrontendIpConfigurationName: Optional[str]
    FrontendPort: Optional[float]
    IdleTimeoutInMinutes: Optional[float]
    LoadDistribution: Optional[str]
    LoadbalancerId: Optional[str]
    Name: Optional[str]
    ProbeId: Optional[str]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackendAddressPoolId=json_data.get("BackendAddressPoolId"),
            BackendPort=json_data.get("BackendPort"),
            DisableOutboundSnat=json_data.get("DisableOutboundSnat"),
            EnableFloatingIp=json_data.get("EnableFloatingIp"),
            EnableTcpReset=json_data.get("EnableTcpReset"),
            FrontendIpConfigurationId=json_data.get("FrontendIpConfigurationId"),
            FrontendIpConfigurationName=json_data.get("FrontendIpConfigurationName"),
            FrontendPort=json_data.get("FrontendPort"),
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            LoadDistribution=json_data.get("LoadDistribution"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            Name=json_data.get("Name"),
            ProbeId=json_data.get("ProbeId"),
            Protocol=json_data.get("Protocol"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts

