"""
This file holds database constants such as paths to the IEMOCAP, CREMA-D,
RAVDESS, and TESS databases.
"""

import os

# GENERAL DATA PATHS
REPO_PATH = r"C:\Users\BT_Lab\Documents\RVST598_Speech-Emotion-Recognition"
DATA_PATH = os.path.join(REPO_PATH, "data")
RAW_DB_PATH = os.path.join(DATA_PATH, "raw")
PROCESS_DB_PATH = os.path.join(DATA_PATH, "processed")
MODEL_PATH = os.path.join(DATA_PATH, "model")
MEL_SPEC_FN = "_{id}-{emo_label}.npy"

# IEMOCAP DATABASE
IEM_DB_PATH = os.path.join(RAW_DB_PATH, "iemocap")
IEM_SAMPLES_CACHE_PATH = os.path.join(
    IEM_DB_PATH, "iemocap_samples_cache.npy")
IEM_LABELS_CACHE_PATH = os.path.join(
    IEM_DB_PATH, "iemocap_labels_cache.npy")
IEM_MEL_SPEC_FN = "IEM{template}".format(template=MEL_SPEC_FN)
IEM_NUM_SAMPLES = 10043

# CREMA-D DATABASE
CRE_DB_PATH = os.path.join(RAW_DB_PATH, "cremad")
CRE_SAMPLES_CACHE_PATH = os.path.join(
    CRE_DB_PATH, "cremad_samples_cache.npy")
CRE_LABELS_CACHE_PATH = os.path.join(
    CRE_DB_PATH, "cremad_labels_cache.npy")
CRE_MEL_SPEC_FN = "CRE{template}".format(template=MEL_SPEC_FN)
CRE_NUM_SAMPLES = 7442

# RAVDESS DATABASE
RAV_DB_PATH = os.path.join(RAW_DB_PATH, "ravdess")
RAV_SAMPLES_CACHE_PATH = os.path.join(
    RAV_DB_PATH, "ravdess_samples_cache.npy")
RAV_LABELS_CACHE_PATH = os.path.join(
    RAV_DB_PATH, "ravdess_labels_cache.npy")
RAV_MEL_SPEC_FN = "RAV{template}".format(template=MEL_SPEC_FN)
RAV_NUM_SAMPLES = 1440

# TESS DATABASE
TES_DB_PATH = os.path.join(RAW_DB_PATH, "tess")
TES_SAMPLES_CACHE_PATH = os.path.join(
    TES_DB_PATH, "tess_samples_cache.npy")
TES_LABELS_CACHE_PATH = os.path.join(
    TES_DB_PATH, "tess_labels_cache.npy")
TES_MEL_SPEC_FN = "TES{template}".format(template=MEL_SPEC_FN)
TES_NUM_SAMPLES = 2800

# The number of standard deviations to include in the data
NUM_STD_CUTOFF = 3
