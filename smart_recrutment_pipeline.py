import os
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#pytorch for deep learning
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader,TensorDataset

#scikit-learn for ml & preprocessing

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,accuracy_score 

#download nlp essential resources
nltk.download('stopwords')
nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)
nltk.download('wordnet',quiet=True)
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

#=========================================================
#PHASE 1 &2 :SETUP & DATA INGESTION
#=========================================================

print("--- Phase 1 & 2: Setup & Data Ingestion ---")

#simulating an enterprise HR dataset con taining candidate details and raw resume text
np.random.seed(42)
num_candidates=200
skills_pool=["python developer with experience in Django,Flask,Aws cloud infrastructure architecture ",
             "data scientist with expertise in machine learning,deep learning,python,pandas,numpy,matplotlib,seaborn",
             "cloud enginner on Azure,Teraform,Ansible,CI/CD pipelines,kubernetes,Docker and devops",
             "java developer with experience in spring bootsql,,microservices,rest api development and system design pipelines",
]

data={
    "Candidate ID":np.array([1000+i for i in range(num_candidates)]),
    "years_of_experience":np.random.choice([2,3,5,7,8,np.nan,12],size=num_candidates),
    "past_interview_score":np.random.uniform(50.0,100.0,size=num_candidates),
    "resume_text":[np.random.choice(skills_pool) for _ in range(num_candidates)],
    "hired_status":np.random.choice([0,1],size=num_candidates, p=[0.6,0.4]) # a target variable indicating whether the candidate was hired (1) or not (0)
    

}

df=pd.DataFrame(data)
print(f"dataset generated sucessfully.shape:{df.shape}\n")

#==========================================================
#PHASE 7:NATURAL LANGUAGE PROCESSING (NLP) FOR RESUME TEXT
#==========================================================

print("--- Phase 7: Natural Language Processing (NLP) for Resume Text ---")

lemmatizer=WordNetLemmatizer()
stop_words=set(stopwords.words('english'))

def clean_resume_text(text):
    #convert to lowercase &tokenization
    tokens=nltk.word_tokenize(text.lower())
    #remove punctuation and stopwords and perform lemmitization
    cleaned_tokens=[
        lemmatizer.lemmatize(word) for word in tokens 
        if word not in stop_words and word not in string.punctuation
    ]

    return " ".join(cleaned_tokens)

df["cleaned_resume"]=df["resume_text"].apply(clean_resume_text)

#feature extraction using TF-IDF vectorization
tfidf=TfidfVectorizer(max_features=1000)
tfidf_matrix=tfidf.fit_transform(df["cleaned_resume"]).toarray()
tfidf_df=pd.DataFrame(tfidf_matrix,columns=[f"tfidf_{w}" for w in tfidf.get_feature_names_out()])
print("text tokenized,lemmatized and converted via TF-IDF vectorization.\n")

#==========================================================
#3 & 4:MATH & DATA PREPROCESSING
#==========================================================

print("--- Phase 3 & 4: Mathematics,statistics & data preprocessing ---")

mean_exp=df["years_of_experience"].mean()
print(f"calculated dataset mean experience:{mean_exp:.2f}")

#preprocessing:handle missing values and scale numerical features
df["years_of_experience"]=df["years_of_experience"].fillna(mean_exp)

#feature scaling for numerical features
scaler=StandardScaler()
scaled_numerical_features=scaler.fit_transform(df[["years_of_experience","past_interview_score"]])
scaled_num_df=pd.DataFrame(scaled_numerical_features,columns=["scaled_years_of_experience","scaled_past_interview_score"])

#combine processed text feature with numerical features

x=pd.concat([scaled_num_df,tfidf_df],axis=1)
y=df["hired_status"].values

#trian-test split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print(f"data scaled and split.training set :{x_train.shape},test set :{x_test.shape}\n")

#data visualization:

plt.figure(figsize=(6,4))
sns.scatterplot(data=df,x="years_of_experience",y="past_interview_score",hue="hired_status",palette="viridis")
plt.title("candidate distribution :experience vs interview score")
plt.savefig("candidate_distribution.png")
plt.close()

#==============================================================
#phase 5: MACHINE LEARNING ALOGRITHMS
#==============================================================

print("phase 5:applying machine learning algorithms")

#UNSUPRVISEDV LEARNING K MEANS CLUSTRERING TO GROUPS CNADIDATES BAE ON TRATITS

Kmeans=KMeans(n_clusters=3,random_state=42,n_init=10)

df['candidate_cluster']=Kmeans.fit_predict(x)
print("unsupervised learning :candidate grouped into three structured clusters")

#SUPERVISED LEARNING: TRAINING A CLASSIFICATION MODEL
rf_model=RandomForestClassifier(n_estimators=100,random_state=42)
rf_model.fit(x_train,y_train)
rf_pred=rf_model.predict(x_test)

print("[ML Random Forest Performance Evaluation]")
print(classification_report(y_test,rf_pred))

#=============================================================
#PHASE 6:DEEP LEARNING (ANN)
#=============================================================

print("---phase 6:training deep leraning engine(pytorch ann)----")
#convert dataframe to pytorch tensor

x_test_t=torch.tensor(x_test.values,dtype=torch.float32)
y_test_t=torch.tensor(y_test,dtype=torch.float32).unsqueeze(1)


#designing the artificial neural network architecture
class resumeevaluationann(nn.Module):
    def __init__(self, input_dim):
        super(resumeevaluationann, self).__init__()
        self.fc1 = nn.Linear(input_dim,16)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self,x):
        out=self.fc1(x)
        out=self.relu(out)
        out=self.fc2(out)
        out=self.relu(out)
        out=self.fc3(out)
        out=self.sigmoid(out)
        return out
        
#initialize pytorch objects

input_features_dim=x_test_t.shape[1]
ann_model=resumeevaluationann(input_features_dim)
criterion=nn.BCELoss() #binary cross entropy loss
optimizer=optim.Adam(ann_model.parameters(),lr=0.01)

#train data loader

train_loader=DataLoader(TensorDataset(x_test_t,y_test_t),batch_size=16,shuffle=True)

#training loop

ann_model.train()
for epoch in range(20):
    for batch_x,batch_y in train_loader:
        optimizer.zero_grad()
        predictions=ann_model(batch_x)
        loss=criterion(predictions,batch_y)
        loss.backward()
        optimizer.step()

#evaluation
ann_model.eval()
with torch.no_grad():
    raw_ann_preds=ann_model(x_test_t)
    ann_preds=(raw_ann_preds > 0.5).float().numpy()

print(f"[Deep Learning ANN Performance Evaluation]")
print(f"ANN Test Accuracy: {accuracy_score(y_test, ann_preds)*100:.2f}%")
print("---project pipeline execute sucessfully across all 7 modules ---")