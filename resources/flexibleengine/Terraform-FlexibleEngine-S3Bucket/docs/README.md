# Terraform::FlexibleEngine::S3Bucket

CloudFormation equivalent of flexibleengine_s3_bucket

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::S3Bucket",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#bucketdomainname" title="BucketDomainName">BucketDomainName</a>" : <i>String</i>,
        "<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#websitedomain" title="WebsiteDomain">WebsiteDomain</a>" : <i>String</i>,
        "<a href="#websiteendpoint" title="WebsiteEndpoint">WebsiteEndpoint</a>" : <i>String</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;, ... ]</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ &lt;a href=&#34;expiration.md&#34;&gt;Expiration&lt;/a&gt;, ... ]</i>,
        "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ &lt;a href=&#34;noncurrentversionexpiration.md&#34;&gt;NoncurrentVersionExpiration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::S3Bucket
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#bucketdomainname" title="BucketDomainName">BucketDomainName</a>: <i>String</i>
    <a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#websitedomain" title="WebsiteDomain">WebsiteDomain</a>: <i>String</i>
    <a href="#websiteendpoint" title="WebsiteEndpoint">WebsiteEndpoint</a>: <i>String</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;</i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;</i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;</i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;</i>
    <a href="#website" title="Website">Website</a>: <i>
      - &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;</i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>
      - &lt;a href=&#34;expiration.md&#34;&gt;Expiration&lt;/a&gt;</i>
    <a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - &lt;a href=&#34;noncurrentversionexpiration.md&#34;&gt;NoncurrentVersionExpiration&lt;/a&gt;</i>
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

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketDomainName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostedZoneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of &lt;a href=&#34;expiration.md&#34;&gt;Expiration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No

_Type_: List of &lt;a href=&#34;noncurrentversionexpiration.md&#34;&gt;NoncurrentVersionExpiration&lt;/a&gt;

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
