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
    Bandwidth: Optional[float]
    BgpAsn: Optional[float]
    BgpAuthKey: Optional[str]
    CreateTime: Optional[str]
    CustomerAddress: Optional[str]
    DcId: Optional[str]
    DcgId: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    RouteFilterPrefixes: Optional[Sequence[str]]
    RouteType: Optional[str]
    State: Optional[str]
    TencentAddress: Optional[str]
    Vlan: Optional[float]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bandwidth=json_data.get("Bandwidth"),
            BgpAsn=json_data.get("BgpAsn"),
            BgpAuthKey=json_data.get("BgpAuthKey"),
            CreateTime=json_data.get("CreateTime"),
            CustomerAddress=json_data.get("CustomerAddress"),
            DcId=json_data.get("DcId"),
            DcgId=json_data.get("DcgId"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            RouteFilterPrefixes=json_data.get("RouteFilterPrefixes"),
            RouteType=json_data.get("RouteType"),
            State=json_data.get("State"),
            TencentAddress=json_data.get("TencentAddress"),
            Vlan=json_data.get("Vlan"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

