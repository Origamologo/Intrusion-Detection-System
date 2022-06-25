# Intrusion-Detection-System
![portada](https://images.idgesg.net/images/article/2018/02/eye-binary-abstract-100749562-large.jpg?auto=webp&quality=85,70)

# Description
This work has been developed while studing data analitics in Ironhack Madrid as the final project of the bootcamp in the believe that, although cybersecurity is a topic that seldom appears in data analitics studies, the truth is that the mindset of an analist can be extremly useful to face some of the main problems of this field.
The original datasets can be downloaded from here: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

# Objetive
The objetive of this project is to develop a deeper understanding about how the net works, studing the behaviour and features of packets sent by attackers in comparison with those of regular conexions while developing an **Intrusion Detection System** as accurate as possible. This System will efficiency distinguish normal connections from DoS attacks, Probe attacks (pentesting), R2L and U2R.
Another bullet point would be to study different machine learning classification problems, including neuronal networks.

# Working plan
To achive the objetives, we will follow this steps
  1. **Develop a set of hacking:** Following the philosophy of "learn by doing", a number of hacking tools have been build, from spoofing to DoS attacks. The idea is to have a better understanding about how the attacks work designing them AND LEARNING IS THE ONE AND ONLY OBJETIVE, the tools have only been used against virtual machines hosted in my laptop. This set of tools is currently in a privated repository.
  2. **Clean the data:** Clean and prepare the data in order to make in suitable for the machine learning models.
  3. **Launch ML models:** Seven models wil be tried, Gaussian Naive Bayes, Decision Tree Classifier, Random Forest Classifier, Support Vector Machine Classifier, Logistic Regression Classifier, Gradient Boost Classifier, Sequential Neuronal Network in keras.


### Structure of the project files
The structure of this project is composed of:<br/>
  1. **1_clening.ipynb:** contains the study and cleaning of the data.
  2. **2_encoding.ipynb:** prepares the data for the machine learning algorithms
  3. **3_models.ipynb** launch the seven classification models
  4. **data:** a folder containing all the data, the raw and the treated
  5. **images:** a folder containing some of the plots produced during the cleaning
  6. **models:** all seven models trained and ready to use

# Conclusions
About the packets and the attacks:<br/>
- **Normal:** most of normal connection run on TCP protocol, use https service and recieve SF flags (normal stablishment and termination of the connection)
- **DoS:** DoS attacks use mainly ICMP protocol, response service and have mostly SF flags with a signicant 20% of SO (connection attemp seen, no reply)
- **Probe:** two thirds of the probe attacks run on TCP protocol and the other third on ICMP, it uses private and eco/i services and has as many Sf flags as REJected
- **R2L:** runs exclusively on TCP protocol, uses nearly only ftp as service and recieve SF flags
- **U2R:** runs mainly on TCP protocol, two thirds of the conections are through telnet and one third uses ftp service, and recieves mostly SF flags
