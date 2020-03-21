# Terraform::Kubernetes::Ingress Spec Tls

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ String, ... ]</i>,
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hosts" title="Hosts">Hosts</a>: <i>
      - String</i>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
</pre>

## Properties

#### Hosts

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
