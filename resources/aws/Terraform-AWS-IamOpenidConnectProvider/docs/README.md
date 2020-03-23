# Terraform::AWS::IamOpenidConnectProvider

Provides an IAM OpenID Connect provider.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IamOpenidConnectProvider",
    "Properties" : {
        "<a href="#clientidlist" title="ClientIdList">ClientIdList</a>" : <i>[ String, ... ]</i>,
        "<a href="#thumbprintlist" title="ThumbprintList">ThumbprintList</a>" : <i>[ String, ... ]</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IamOpenidConnectProvider
Properties:
    <a href="#clientidlist" title="ClientIdList">ClientIdList</a>: <i>
      - String</i>
    <a href="#thumbprintlist" title="ThumbprintList">ThumbprintList</a>: <i>
      - String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### ClientIdList

A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbprintList

A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL of the identity provider. Corresponds to the _iss_ claim.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.
