# Terraform::DigitalOcean::SpacesBucket

CloudFormation equivalent of digitalocean_spaces_bucket

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::SpacesBucket",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucketdomainname" title="BucketDomainName">BucketDomainName</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#urn" title="Urn">Urn</a>" : <i>String</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::SpacesBucket
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucketdomainname" title="BucketDomainName">BucketDomainName</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#urn" title="Urn">Urn</a>: <i>String</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketDomainName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Urn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BucketDomainName

Returns the &lt;code&gt;BucketDomainName&lt;/code&gt; value.

#### Urn

Returns the &lt;code&gt;Urn&lt;/code&gt; value.
