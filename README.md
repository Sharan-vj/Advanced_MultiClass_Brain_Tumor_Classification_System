# Advanced_MultiClass_Brain_Tumor_Classification_System

### Project Description
<p align="justify"><b>Advanced MultiClass Brain Tumor Classification System</b> project is designed & developed to efficiently classify brain scan images with and without tumors. In this system user can accurately classify 5 types of tumors namely <b>Astrocytoma</b>, <b>Glioma</b>, <b>Meningioma</b>, <b>Neurocitoma</b>, and <b>Pituitary</b> tumors. And also the system can identify and classify <b>normal brain images</b> too. Over 22000 images were augmented and used in this project. along with that VGG16 architecture was used to train the model and attained 93.2% of overall accuracy. As a user interface, user friendly web application was developed and integrated with the system.</p>

### Project Features &  Advantages
* Work perfectly with both MRI & CT scan images.
* Classifies more types of tumors compared to existing system.
* Reduced misclassification of tumors.
* Easy to use user interface.

### Screenshots
<img width="800" height="400" align="center" src="/screenshots/homepage.png">
<img width="800" height="400" align="center" src="/screenshots/classifypage.png">

### How to run project Locally
1. Download the source code of the project.
2. create a conda virtual environment

    ```bash
    conda create brainproject python=3.8 -y
    ``` 
3. activate the virtual environment.
    ```bash
    conda activate brainproject
    ```
4. change the work directory to project folder.
5. install the requirements file
    ```bash
    pip install -r requirements.txt
    ```
6. run the flask file
    ```bash
    python app.py
    ```
7. open the local host with port number 8080

### How to deploy the Project 

#### Step 1: Create IAM User Account on AWS

Attach below User Policies to IAM user
- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2FullAccess

#### Step 2: Create ECR Repository

1. Create a ECR repository for this project.
2. Note down the URI of the repository. 

3. Example URI : 864136819855.dkr.ecr.ap-south-1.amazonaws.com/repository_name

#### Step 3: Create EC2 Virtual Machine
Use below configuration while creating EC2 virtual machine.

|||
|-|-|
|Operating System|Ubuntu Linux |
|Amazon Machine Image (AMI)| Ubuntu Server 22.04 LTS (HVM), SSD Volume Type|
|Instance type|t2.large|
|Network Settings|Allow HTTP & HTTPS|
|Storage|32GB|

#### Step 4: EC2 Machine Configuration
Using EC2 instance connect, connect to the running virtual machine and execute the below commands one by one.

```bash
sudo apt-get update -y
```
```bash
sudo apt-get upgrade
```
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
```bash
sudo sh get-docker.sh
```
```bash
sudo usermod -aG docker ubuntu
```
```bash
newgrp docker
```

#### Step 5: GitHub Actions Setup
setting>actions>runner>new self hosted runner> choose os> Execute command

1. open repository Settings.
2. on code & automation menus open actions tab.
3. on actions tab click on runners.
4. click new self hosted runners.
5. change the runner image to linux.
6. run the displayed commands on EC2 machine.

#### Step 6: GitHub Actions Secrets Setup
setting>secrets and variables>actions>new repository secret

store the below secrets one by one with your credentials.
```yaml
AWS_ACCESS_KEY_ID
```
```yaml
AWS_SECRET_ACCESS_KEY
```
```yaml
AWS_REGION
```
```yaml
AWS_ECR_LOGIN_URI
```
```yaml
ECR_REPOSITORY_NAME
```