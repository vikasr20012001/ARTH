# ARTH AWS

### ARTH-TASK-3 
### TASK DESCRIPTION:
### 1.Create a key pair.
### 2.Create a security group.
### 3.Launch an instance using the above created key pair and security group.
### 4.Create an EBS volume of 1 GB.
### 5.The final step is to attach the above created EBS volume to the instance created in the previous steps.

To use AWS CLI, we need to download and install it on the top of Operating System with which we are working. So, after installing to check whether its successfully installed, use the command:


`` aws --version ``


Here, we need to add the Access-key and Secret-key provided by AWS while creating this IAM User. Also, along with this we need to mention the default output format and the region. Here, region I am using is Mumbai i.e. ap-south-1.

![10 1](https://user-images.githubusercontent.com/64473684/95850722-e5ecd800-0d6e-11eb-8b92-93c8d7f0b092.jpeg)

So, now creating a keypair :
--key-name is an option to give a name to our key.

![10 2](https://user-images.githubusercontent.com/64473684/95851608-17b26e80-0d70-11eb-8860-29eddb3641d4.jpeg)

Now, we have our keypair ready and we can see that on the console too. 'taskkey' is created successfully.

![10 3](https://user-images.githubusercontent.com/64473684/95851900-8a234e80-0d70-11eb-9978-fceecf5faf8b.jpeg)

A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. When you create a security group, you specify a friendly name of your 

choice. You can have a security group for use in EC2-Classic with the same name as a security group for use in a VPC. However, you can't have two security groups for use in EC2-

Classic with the same name or two security groups for use in a VPC with the same name.Now, for creating a security group.

![10 4](https://user-images.githubusercontent.com/64473684/95851920-927b8980-0d70-11eb-8020-d69ac9c6b9d7.jpeg)

![10 5](https://user-images.githubusercontent.com/64473684/95851938-97d8d400-0d70-11eb-926c-132c30d58d93.jpeg)

Now, lets create an EC2 instance. This instance will have the keypair and security groups attached that we created just now.

![10 6](https://user-images.githubusercontent.com/64473684/95851944-9d361e80-0d70-11eb-9f5f-047c00718fcc.jpeg)

Our instance is now launched in ap-south-1a.

![10 8](https://user-images.githubusercontent.com/64473684/95854404-8abde400-0d74-11eb-8157-33c69e9cba38.jpeg)


Now, we will create a 1 GB Volume using EBS. EBS comes under the EC2 service of AWS.The volume type will be general purpose SSD Volume:


![10 9](https://user-images.githubusercontent.com/64473684/95852103-d53d6180-0d70-11eb-9916-5b89814423f7.jpeg)


Our EBS volume is now created and ready. This volume we need to attach to the EC2 instance we have created earlier.

![10 10](https://user-images.githubusercontent.com/64473684/95852117-da9aac00-0d70-11eb-9ff6-6fba9c387f12.jpeg)

Our volume is now successfully attached and we can see that in the Console of AWS:

![10 11](https://user-images.githubusercontent.com/64473684/95852158-edad7c00-0d70-11eb-82e9-a6343ad47f3a.jpeg)

![10 12](https://user-images.githubusercontent.com/64473684/95852216-0453d300-0d71-11eb-880e-5665c970f97a.jpeg)


