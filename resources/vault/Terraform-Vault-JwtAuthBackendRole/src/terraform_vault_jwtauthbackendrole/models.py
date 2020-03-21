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
    AllowedRedirectUris: Optional[Sequence[str]]
    Backend: Optional[str]
    BoundAudiences: Optional[Sequence[str]]
    BoundCidrs: Optional[Sequence[str]]
    BoundClaims: Optional[Sequence["_BoundClaims"]]
    BoundSubject: Optional[str]
    ClaimMappings: Optional[Sequence["_ClaimMappings"]]
    ClockSkewLeeway: Optional[float]
    ExpirationLeeway: Optional[float]
    GroupsClaim: Optional[str]
    GroupsClaimDelimiterPattern: Optional[str]
    MaxTtl: Optional[float]
    NotBeforeLeeway: Optional[float]
    NumUses: Optional[float]
    OidcScopes: Optional[Sequence[str]]
    Period: Optional[float]
    Policies: Optional[Sequence[str]]
    RoleName: Optional[str]
    RoleType: Optional[str]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]
    Ttl: Optional[float]
    UserClaim: Optional[str]
    VerboseOidcLogging: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedRedirectUris=json_data.get("AllowedRedirectUris"),
            Backend=json_data.get("Backend"),
            BoundAudiences=json_data.get("BoundAudiences"),
            BoundCidrs=json_data.get("BoundCidrs"),
            BoundClaims=json_data.get("BoundClaims"),
            BoundSubject=json_data.get("BoundSubject"),
            ClaimMappings=json_data.get("ClaimMappings"),
            ClockSkewLeeway=json_data.get("ClockSkewLeeway"),
            ExpirationLeeway=json_data.get("ExpirationLeeway"),
            GroupsClaim=json_data.get("GroupsClaim"),
            GroupsClaimDelimiterPattern=json_data.get("GroupsClaimDelimiterPattern"),
            MaxTtl=json_data.get("MaxTtl"),
            NotBeforeLeeway=json_data.get("NotBeforeLeeway"),
            NumUses=json_data.get("NumUses"),
            OidcScopes=json_data.get("OidcScopes"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            RoleName=json_data.get("RoleName"),
            RoleType=json_data.get("RoleType"),
            TokenBoundCidrs=json_data.get("TokenBoundCidrs"),
            TokenExplicitMaxTtl=json_data.get("TokenExplicitMaxTtl"),
            TokenMaxTtl=json_data.get("TokenMaxTtl"),
            TokenNoDefaultPolicy=json_data.get("TokenNoDefaultPolicy"),
            TokenNumUses=json_data.get("TokenNumUses"),
            TokenPeriod=json_data.get("TokenPeriod"),
            TokenPolicies=json_data.get("TokenPolicies"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenType=json_data.get("TokenType"),
            Ttl=json_data.get("Ttl"),
            UserClaim=json_data.get("UserClaim"),
            VerboseOidcLogging=json_data.get("VerboseOidcLogging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BoundClaims:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BoundClaims"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoundClaims"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoundClaims = BoundClaims


@dataclass
class ClaimMappings:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClaimMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClaimMappings"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClaimMappings = ClaimMappings

