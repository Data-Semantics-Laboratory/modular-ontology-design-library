pattern_name = input("Enter name of pattern: ").strip()
file_name = input("Enter name for file (pattern_name used as default): ").strip()

if file_name == "":
    file_name = pattern_name

file_name = "../patterns/" + file_name + ".tex"
barrier = """%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""


with open(file_name, 'w') as f:
    # Create Section Header
    f.write("\\section{"+pattern_name+"}"+"\n")
    label = pattern_name.split(" ")[0]
    f.write("\\label{sec:"+label+"}"+"\n")
    f.write(barrier * 2 + "\n")

    # Create Figure
    f.write("\\begin{figure}[h!]"+"\n")
    f.write("\\begin{center}"+"\n")
    f.write("\\includegraphics[width=.4\\textwidth]{patterns/"+label+"}"+"\n")
    f.write("\\end{center}"+"\n")
    f.write("\\caption{Schema Diagram for " + pattern_name +"."+"\n")
    f.write("\\label{fig:"+label+"}"+"\n")
    f.write("\\end{figure}"+"\n")

    # Create Summary
    f.write("\\subsection{Summary}"+"\n")
    f.write("\\label{sum:"+label+"}"+"\n")
    f.write(barrier+"\n")
    f.write("I am some summary text."+"\n")
    f.write("\n")

    # Create axiomatization
    f.write(barrier * 2 + "\n")
    f.write("\\subsection{Axiomatization}"+"\n")
    f.write("\\label{axs:"+label+"}"+"\n")
    f.write(barrier+"\n")
    f.write("\\begin{align}"+"\n")
    f.write("\\top &\sqsubseteq \\forall\\textsf{hasType.CVType} \\\\"+"\n")
    f.write("\\end{align}"+"\n")
    f.write("\n")

    # Create explanations
    f.write(barrier * 2 + "\n")
    f.write("\\subsection{Explanations}"+"\n")
    f.write("\\label{exp:"+label+"}"+"\n")
    f.write(barrier+"\n")
    f.write("\\begin{enumerate}"+"\n")
    f.write("\\item temporary item"+"\n")
    f.write("\\end{enumerate}"+"\n")
    f.write("\n")

    # Create explanations
    f.write(barrier * 2 + "\n")
    f.write("\\subsection{Competency Question}"+"\n")
    f.write("\\label{cqs:"+label+"}"+"\n")
    f.write(barrier+"\n")
    f.write("\\begin{enumerate}[CQ1.]"+"\n")
    f.write("\\item temporary item"+"\n")
    f.write("\\end{enumerate}"+"\n")
    f.write("\n")


    # Creat end document
    f.write(barrier * 2 + "\n")
    f.write("% End Section" + "\n")
    f.write(barrier * 2 + "\n")
    f.write(barrier * 2)

print(pattern_name)
print(file_name)