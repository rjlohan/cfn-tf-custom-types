# Terraform::OCI::CoreListingResourceVersionAgreement

CloudFormation equivalent of oci_core_listing_resource_version_agreement

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreListingResourceVersionAgreement",
    "Properties" : {
        "<a href="#listingid" title="ListingId">ListingId</a>" : <i>String</i>,
        "<a href="#listingresourceversion" title="ListingResourceVersion">ListingResourceVersion</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreListingResourceVersionAgreement
Properties:
    <a href="#listingid" title="ListingId">ListingId</a>: <i>String</i>
    <a href="#listingresourceversion" title="ListingResourceVersion">ListingResourceVersion</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ListingId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListingResourceVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EulaLink

Returns the <code>EulaLink</code> value.

#### Id

Returns the <code>Id</code> value.

#### OracleTermsOfUseLink

Returns the <code>OracleTermsOfUseLink</code> value.

#### Signature

Returns the <code>Signature</code> value.

#### TimeRetrieved

Returns the <code>TimeRetrieved</code> value.
