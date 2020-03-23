# Terraform::AWS::Codepipeline ArtifactStore

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>[ <a href="artifactstore-encryptionkey.md">EncryptionKey</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>
      - <a href="artifactstore-encryptionkey.md">EncryptionKey</a></i>
</pre>

## Properties

#### Location

The location where AWS CodePipeline stores artifacts for a pipeline, such as an S3 bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the artifact store, such as Amazon S3.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: No

_Type_: List of <a href="artifactstore-encryptionkey.md">EncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
