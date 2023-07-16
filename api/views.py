from pathlib import Path
import pandas as pd
import os
from django.http import JsonResponse
from django.shortcuts import render
BASE_DIR = Path(__file__).resolve().parent.parent
def pred(request, id = None):
    ans = id
    ans = ans.upper()
    ans = ans.replace(" ", "")
    ans = ans.replace("&", "")
    s1 = 'api/2023 Allotments/' + ans + " 2023.csv"
    path1 = os.path.join(BASE_DIR, s1)
    df = pd.read_csv(path1)
    df["Rank"] = df["Rank"].astype(float)
    oc = df[df['Caste'] ==  "\xa0 \xa0 OC"]
    bcd = df[df['Caste'] ==  "\xa0 \xa0 BC_D"]
    bca = df[df['Caste'] ==  "\xa0 \xa0 BC_A"]
    bcb = df[df['Caste'] ==  "\xa0 \xa0 BC_B"]
    bcc = df[df['Caste'] ==  "\xa0 \xa0 BC_C"]
    bce = df[df['Caste'] ==  "\xa0 \xa0 BC_E"]
    sc = df[df['Caste'] ==  "\xa0 \xa0 SC"]
    st = df[df['Caste'] ==  "\xa0 \xa0 ST"]

    ocf = oc[(oc.Sex == "\xa0 \xa0 F")]
    ocm = oc[(oc.Sex == "\xa0 \xa0 M")]
    bcaf = bca[(bca.Sex == "\xa0 \xa0 F")]
    bcam = bca[(bca.Sex == "\xa0 \xa0 M")]
    bcbf = bcb[(bcb.Sex == "\xa0 \xa0 F")]
    bcbm = bcb[(bcb.Sex == "\xa0 \xa0 M")]
    bccf = bcc[(bcc.Sex == "\xa0 \xa0 F")]
    bccm = bcc[(bcc.Sex == "\xa0 \xa0 M")]
    bcdf = bcd[(bcd.Sex == "\xa0 \xa0 F")]
    bcdm = bcd[(bcd.Sex == "\xa0 \xa0 M")]
    bcef = bce[(bce.Sex == "\xa0 \xa0 F")]
    bcem = bce[(bce.Sex == "\xa0 \xa0 M")]
    scf = sc[(sc.Sex == "\xa0 \xa0 F")]
    scm = sc[(sc.Sex == "\xa0 \xa0 M")]
    stf = st[(st.Sex == "\xa0 \xa0 F")]
    stm = st[(st.Sex == "\xa0 \xa0 M")]

    if bccf.empty:
        bccf.loc[len(bccf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if bccm.empty:
        bccm.loc[len(bccm.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if ocf.empty:
        ocf.loc[len(ocf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if ocm.empty:
        ocm.loc[len(ocm.index)] = [0, 0, 0, 0, 0, 0, 0, 0] 
    if ocf.empty:
        bcaf.loc[len(bcaf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if bcam.empty:
        bcam.loc[len(bcam.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if bcaf.empty:
        bcaf.loc[len(bcaf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]  
    if bcbf.empty:
        bcbf.loc[len(bcbf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if bcbm.empty:
        bcbm.loc[len(bcbm.index)] = [0, 0, 0, 0, 0, 0, 0, 0] 
    if bcdf.empty:
        bcdf.loc[len(bcdf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if bcdm.empty:
        bcdm.loc[len(bcdm.index)] = [0, 0, 0, 0, 0, 0, 0, 0] 
    if bcef.empty:
        bcef.loc[len(bcef.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if bcem.empty:
        bcem.loc[len(bcem.index)] = [0, 0, 0, 0, 0, 0, 0, 0] 
    if scf.empty:
        scf.loc[len(scf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if scm.empty:
        scm.loc[len(scm.index)] = [0, 0, 0, 0, 0, 0, 0, 0] 
    if stf.empty:
        stf.loc[len(stf.index)] = [0, 0, 0, 0, 0, 0, 0, 0]
    if stm.empty:
        stm.loc[len(stm.index)] = [0, 0, 0, 0, 0, 0, 0, 0] 
    return JsonResponse({"ocfb" : min(ocf["Rank"]),
    "ocfl" : max(ocf["Rank"]),
    "ocmb" : min(ocm["Rank"]),
    "ocml" : max(ocm["Rank"]),
    "bcafb" : min(bcaf["Rank"]),
    "bcafl" : max(bcaf["Rank"]),
    "bcamb" : min(bcam["Rank"]),
    "bcaml" : max(bcam["Rank"]),
    "bcbfb" : min(bcbf["Rank"]),
    "bcbfl" : max(bcbf["Rank"]),
    "bcbmb" : min(bcbm["Rank"]),
    "bcbml" : max(bcbm["Rank"]),
    "bccfb" : min(bccf["Rank"]),
    "bccfl" : max(bccf["Rank"]),
    "bccmb" : min(bccm["Rank"]),
    "bccml" : max(bccm["Rank"]),
    "bcdfb" : min(bcdf["Rank"]),
    "bcdfl" : max(bcdf["Rank"]),
    "bcdmb" : min(bcdm["Rank"]),
    "bcdml" : max(bcdm["Rank"]),
    "bcefb" : min(bcef["Rank"]),
    "bcefl" : max(bcef["Rank"]),
    "bcemb" : min(bcem["Rank"]),
    "bceml" : max(bcem["Rank"]),
    "scfb" : min(scf["Rank"]),
    "scfl" : max(scf["Rank"]),
    "scmb" : min(scm["Rank"]),
    "scml" : max(scm["Rank"]),
    "stfb" : min(stf["Rank"]),
    "stfl" : max(stf["Rank"]),
    "stmb" : min(stm["Rank"]),
    "stml" : max(stm["Rank"]),})