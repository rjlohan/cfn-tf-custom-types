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
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    LifecycleDetails: Optional[str]
    NotebookSessionUrl: Optional[str]
    ProjectId: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    NotebookSessionConfigurationDetails: Optional[Sequence["_NotebookSessionConfigurationDetails"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NotebookSessionUrl=json_data.get("NotebookSessionUrl"),
            ProjectId=json_data.get("ProjectId"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            NotebookSessionConfigurationDetails=json_data.get("NotebookSessionConfigurationDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class NotebookSessionConfigurationDetails:
    BlockStorageSizeInGbs: Optional[float]
    Shape: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotebookSessionConfigurationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotebookSessionConfigurationDetails"]:
        if not json_data:
            return None
        return cls(
            BlockStorageSizeInGbs=json_data.get("BlockStorageSizeInGbs"),
            Shape=json_data.get("Shape"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotebookSessionConfigurationDetails = NotebookSessionConfigurationDetails


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts

