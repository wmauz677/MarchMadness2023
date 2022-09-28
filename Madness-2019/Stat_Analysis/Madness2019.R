require(MASS)
Data = read.csv("Desktop/Stat_Analysis/YearStats_Team/2010-11_Stats.csv", row.names = 1)

# Team Stats
TwoPP = Data$X2P.
ThreePP = Data$X3P.
FTP = Data$FT
ORB_G = Data$ORB.G
DRB_G = Data$DRB.G
AST_G = Data$AST.G
STL_G = Data$STL.G
BLK_G = Data$BLK.G
TOV_G = Data$TOV.G
PF_G = Data$PF.G

Ranking = Data$Ranking

# Team Stats
model_fit = lm(Ranking ~ TwoPP + ThreePP + FTP + ORB_G + DRB_G + AST_G + STL_G + BLK_G + TOV_G + PF_G, data = Data)
summary(model_fit)

# Individual Stats
# Data.lm = lm(Ranking ~ i1_TwoPP + i1_FTP + i1_PTS + i1_AST + i1_TOV + i2_TwoPP + i2_FTP + i2_PTS + i2_AST + i2_TOV + i3_TwoPP + i3_FTP + i3_PTS + i3_AST + i3_TOV   

# All Stat Analysis
# model_fit = lm(Ranking ~ TwoPP + ThreePP + FTP + ORB_G + DRB_G + AST_G + STL_G + BLK_G + TOV_G + PF_G + i1_TwoPP + i1_FTP + i1_PTS + i1_AST + i1_TOV + i2_TwoPP + i2_FTP + i2_PTS + i2_AST + i2_TOV + i3_TwoPP + i3_FTP + i3_PTS + i3_AST + i3_TOV, data = Data)

s1 = summary(model_fit)$coefficients[2,1]
s2 = summary(model_fit)$coefficients[3,1]
s3 = summary(model_fit)$coefficients[4,1]
s4 = summary(model_fit)$coefficients[5,1]
s5 = summary(model_fit)$coefficients[6,1]
s6 = summary(model_fit)$coefficients[7,1]
s7 = summary(model_fit)$coefficients[8,1]
s8 = summary(model_fit)$coefficients[9,1]
s9 = summary(model_fit)$coefficients[10,1]
s10 = summary(model_fit)$coefficients[11,1]

a <- c(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
a

# # Player 1 Stats
# i1_TwoPP = Data$i1.2P.
# i1_FTP = Data$i1.FT.
# i1_PTS = Data$i1.PTS
# i1_AST = Data$i1.AST
# i1_TOV = Data$i1.TOV
# 
# # Player 2 Stats
# i2_TwoPP = Data$i2.2P.
# i2_FTP = Data$i2.FT.
# i2_PTS = Data$i2.PTS
# i2_AST = Data$i2.AST
# i2_TOV = Data$i2.TOV
# 
# # Player 3 Stats
# i3_TwoPP = Data$i3.2P.
# i3_FTP = Data$i3.FT.
# i3_PTS = Data$i3.PTS
# i3_AST = Data$i3.AST
# i3_TOV = Data$i3.TOV

# s11 = summary(model_fit)$coefficients[12,1]
# s12 = summary(model_fit)$coefficients[13,1]
# s13 = summary(model_fit)$coefficients[14,1]
# s14 = summary(model_fit)$coefficients[15,1]
# s15 = summary(model_fit)$coefficients[16,1]
# s16 = summary(model_fit)$coefficients[17,1]
# s17 = summary(model_fit)$coefficients[18,1]
# s18 = summary(model_fit)$coefficients[19,1]
# s19 = summary(model_fit)$coefficients[20,1]
# s20 = summary(model_fit)$coefficients[21,1]
# s21 = summary(model_fit)$coefficients[22,1]
# s22 = summary(model_fit)$coefficients[23,1]
# s23 = summary(model_fit)$coefficients[24,1]
# s24 = summary(model_fit)$coefficients[25,1]
# s25 = summary(model_fit)$coefficients[26,1]