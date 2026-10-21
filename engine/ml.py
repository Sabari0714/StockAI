from pathlib import Path
import joblib
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, roc_auc_score
from .indicators import add_indicators, FEATURES
from .data import get_history

MODEL_DIR=Path("models"); MODEL_DIR.mkdir(exist_ok=True)

def make_dataset(symbol,horizon=5,threshold=.01):
    d=add_indicators(get_history(symbol)); d["future_return"]=d.Close.shift(-horizon)/d.Close-1; d["target"]=(d.future_return>=threshold).astype(int); return d.dropna()

def train(symbol):
    d=make_dataset(symbol); X=d[FEATURES].replace([float("inf"),-float("inf")],float("nan")).dropna(); y=d.loc[X.index,"target"]
    split=int(len(X)*.8); Xtr,Xte=X.iloc[:split],X.iloc[split:]; ytr,yte=y.iloc[:split],y.iloc[split:]
    model=HistGradientBoostingClassifier(max_depth=4,learning_rate=.05,max_iter=250,random_state=42); model.fit(Xtr,ytr); p=model.predict_proba(Xte)[:,1]
    out={"symbol":symbol,"accuracy":float(accuracy_score(yte,p>=.5)),"precision":float(precision_score(yte,p>=.5,zero_division=0))}
    try: out["auc"]=float(roc_auc_score(yte,p))
    except Exception: out["auc"]=None
    joblib.dump((model,FEATURES),MODEL_DIR/(symbol.replace(".","_")+".joblib")); return out

def predict(symbol):
    d=add_indicators(get_history(symbol)); model,features=joblib.load(MODEL_DIR/(symbol.replace(".","_")+".joblib")); p=float(model.predict_proba(d[features].iloc[[-1]])[0,1]); return {"symbol":symbol,"up_probability":round(p*100,2)}
