# Terraform::AWS::ApiGatewayGatewayResponse

CloudFormation equivalent of aws_api_gateway_gateway_response

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayGatewayResponse",
    "Properties" : {
        "<a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>" : <i>[ <a href="responseparameters.md">ResponseParameters</a>, ... ]</i>,
        "<a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>" : <i>[ <a href="responsetemplates.md">ResponseTemplates</a>, ... ]</i>,
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
    <a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>: <i>
      - <a href="responseparameters.md">ResponseParameters</a></i>
    <a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>: <i>
      - <a href="responsetemplates.md">ResponseTemplates</a></i>
    <a href="#responsetype" title="ResponseType">ResponseType</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### ResponseParameters

_Required_: No

_Type_: List of <a href="responseparameters.md">ResponseParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTemplates

_Required_: No

_Type_: List of <a href="responsetemplates.md">ResponseTemplates</a>

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
