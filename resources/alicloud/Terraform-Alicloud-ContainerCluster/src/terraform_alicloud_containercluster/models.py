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
    AgentVersion: Optional[str]
    CidrBlock: Optional[str]
    DiskCategory: Optional[str]
    DiskSize: Optional[float]
    ImageId: Optional[str]
    InstanceType: Optional[str]
    IsOutdated: Optional[bool]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NeedSlb: Optional[bool]
    NodeNumber: Optional[float]
    Nodes: Optional[Sequence["_Nodes"]]
    Password: Optional[str]
    ReleaseEip: Optional[bool]
    SecurityGroupId: Optional[str]
    Size: Optional[float]
    SlbId: Optional[str]
    VpcId: Optional[str]
    VswitchId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AgentVersion=json_data.get("AgentVersion"),
            CidrBlock=json_data.get("CidrBlock"),
            DiskCategory=json_data.get("DiskCategory"),
            DiskSize=json_data.get("DiskSize"),
            ImageId=json_data.get("ImageId"),
            InstanceType=json_data.get("InstanceType"),
            IsOutdated=json_data.get("IsOutdated"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NeedSlb=json_data.get("NeedSlb"),
            NodeNumber=json_data.get("NodeNumber"),
            Nodes=json_data.get("Nodes"),
            Password=json_data.get("Password"),
            ReleaseEip=json_data.get("ReleaseEip"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Size=json_data.get("Size"),
            SlbId=json_data.get("SlbId"),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Nodes:
    Eip: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrivateIp: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            Eip=json_data.get("Eip"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes

