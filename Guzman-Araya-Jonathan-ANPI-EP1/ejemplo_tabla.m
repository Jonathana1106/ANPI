clc; clear

pkg load dataframe
a1=5; a2=10; a3=15;
C = {"Patient Name", "Volume", "Quality", "Owner"; 
     "Joe", 200, a1, "MR"; 
     "Dana", 186, a2, "MR"; 
     "Cassidy", 197, a3, "SP"};
dataframe (C)