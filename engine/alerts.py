def build_alert(result:dict,min_probability=.65):
    p=result.get("up_probability"); signal=result.get("signal")
    if p is not None and p>=min_probability*100 and signal=="BULLISH": return {"level":"WATCH","reason":"bullish technical + model confirmation","probability":p}
    if result.get("peak_score",0)>=80:return {"level":"CAUTION","reason":"near-peak / extension risk","peak_score":result.get("peak_score")}
    if signal=="BEARISH":return {"level":"RISK","reason":"bearish technical structure"}
    return {"level":"INFO","reason":"no high-priority signal"}
