'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''

import streamlit as st
import packaging
import json
from io import StringIO

st.title("Process Package Files")

if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0

uploaded_file = st.file_uploader("Upload package file:", type=["txt"])

if uploaded_file:
    filename = uploaded_file.name
    json_filename = filename.replace(".txt", ".json")
    packages = []

    text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    for line in lines:
        pkg = packaging.parse_packaging(line)
        total = packaging.calc_total_units(pkg)
        unit = packaging.get_unit(pkg)
        packages.append({
            "package": pkg,
            "total_size": total,
            "unit": unit
        })

    count = len(packages)
    with open(json_filename, "w") as f:
        json.dump(packages, f, indent=4)

    summary = f"{count} packages written to {json_filename}"
    st.session_state.summaries.append(summary)
    st.session_state.total_files += 1
    st.session_state.total_lines += count

    for s in st.session_state.summaries:
        st.info(s, icon="💾")
    st.success(f"{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines processed")