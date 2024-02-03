import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

image = Image.open("dna.jpg")

st.image(image, use_column_width=True)

st.write(""" 
# DNA Nucleotide Count Web App
         
This app counts the nucleotide composition of query DNA!
""")

st.header("Enter DNA sequence and press enter to apply")

sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGGATCTTCC"
sequence = st.text_input("Sequence Input",sequence_input,  placeholder="GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGGATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGCTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT")



st.write(""" *** """)

#print the dna sequence
st.header("YOUR DNA")
sequence

#dna nucleotide count
st.header('DNA Nucleotide Count')

def DNA_Nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])

    return d

X = DNA_Nucleotide_count(sequence)

st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

st.subheader("DataFrame")

# // display dataframe
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis = 1)
df.reset_index(inplace=True)
df = df.rename(columns = {"index" : "nucleotide"})
st.write(df)

p = alt.Chart(df).mark_bar().encode(x="nucleotide", y="count")
p = p.properties(width = alt.Step(80))

st.write(p)