from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.ensemble import HistGradientBoostingClassifier
FEATURES=["EMA20","EMA50","EMA200","RSI14","MACD","MACD_SIGNAL","ATR14","VOLUME_RATIO","MOM_20","MOM_60","DIST_52W_HIGH","EMA20_GAP","EMA50_GAP"]
def walk_forward(df:pd.DataFrame,horizon:int=5,threshold:float=.01,min_train:int=250,test_size:int=60)->dict:
    d=df.copy(); d["future_return"]=d["Close"].shift(-horizon)/d["Close"]-1; d["target"]=(d.future_return>=threshold).astype(int); d=d.dropna(subset=FEATURES+["target"]).reset_index(drop=True)
    if len(d)<min_train+test_size:return {"status":"insufficient_data","rows":len(d),"required":min_train+test_size}
    preds=[]; actual=[]; folds=0
    for end in range(min_train,len(d),test_size):
        test_end=min(end+test_size,len(d)); train=d.iloc[:end]; test=d.iloc[end:test_end]
        if len(test)==0:break
        m=HistGradientBoostingClassifier(max_depth=5,learning_rate=.05,max_iter=250,random_state=42); m.fit(train[FEATURES],train.target); preds.extend(m.predict_proba(test[FEATURES])[:,1].tolist()); actual.extend(test.target.tolist()); folds+=1
    labels=np.array(actual); probs=np.array(preds); out={"status":"ok","folds":folds,"samples":len(actual),"accuracy":float(accuracy_score(labels,probs>=.5))}; out["auc"]=float(roc_auc_score(labels,probs)) if len(np.unique(labels))>1 else None; return out
