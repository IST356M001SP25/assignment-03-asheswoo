'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
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
    for line in text.split("\n"):
        line = line.strip()
        if line:
            pkg = packaging.parse_packaging(line)
            total = packaging.calc_total_units(pkg)
            unit = packaging.get_unit(pkg)
            packages.append({
                "package": pkg,
                "total_size": total,
                "unit": unit
            })
            st.write(f"Package: {pkg}, Total Size: {total} {unit}")

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