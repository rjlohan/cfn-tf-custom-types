# Terraform::AWS::ApiGatewayGatewayResponse

CloudFormation equivalent of aws_api_gateway_gateway_response

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayGatewayResponse",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>" : <i>[ &lt;a href=&#34;responseparameters.md&#34;&gt;ResponseParameters&lt;/a&gt;, ... ]</i>,
        "<a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>" : <i>[ &lt;a href=&#34;responsetemplates.md&#34;&gt;ResponseTemplates&lt;/a&gt;, ... ]</i>,
        "<a href="#responsetype" title="ResponseType">ResponseType</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayGatewayResponse
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>: <i>
      - &lt;a href=&#34;responseparameters.md&#34;&gt;ResponseParameters&lt;/a&gt;</i>
    <a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>: <i>
      - &lt;a href=&#34;responsetemplates.md&#34;&gt;ResponseTemplates&lt;/a&gt;</i>
    <a href="#responsetype" title="ResponseType">ResponseType</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseParameters

_Required_: No

_Type_: List of &lt;a href=&#34;responseparameters.md&#34;&gt;ResponseParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTemplates

_Required_: No

_Type_: List of &lt;a href=&#34;responsetemplates.md&#34;&gt;ResponseTemplates&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

_Required_: No

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
