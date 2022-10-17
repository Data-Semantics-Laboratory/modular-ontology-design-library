pattern_name = input("Enter name of pattern (include capitalization): ").strip()
file_name = input("Enter name for file (pattern_name used as default): ").strip()
figure_name = input("Enter figurename (Enter nothing for placeholder image): ").strip()

if figure_name == "":
    figure_name = "placeholder"

if file_name == "":
    file_name = pattern_name

file_name = file_name.lower();

loc_file_name = "patterns/{file_name}".format(file_name=file_name)
file_name = "../patterns/" + file_name + ".tex"
barrier = """%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""


with open(file_name, 'w') as f:
    # Create Section Header
    f.write("\\section{"+pattern_name+"}\n")
    label = pattern_name.split(" ")[0]
    f.write("\\label{sec:"+label+"}\n")
    f.write(barrier * 2 + "\n")

    # Create Figure
    f.write("\\begin{figure}[h!]\n")
    f.write("\\begin{center}\n")
    f.write("\\includegraphics[width=.8\\textwidth]{figures/"+figure_name+"}\n")
    f.write("\\end{center}\n")
    f.write("\\caption{Schema Diagram for the " + pattern_name +" Pattern. The visual notation is explained in Chapter \\ref{chap:prelims}.}\n")
    f.write("\\label{fig:"+label+"}\n")
    f.write("\\end{figure}\n")

    # Create Summary
    f.write("\\subsection{Summary}\n")
    f.write("\\label{sum:"+label+"}\n")
    f.write(barrier+"\n")
    f.write("I am some summary text.\n")
    f.write("\n")

    # Create axiomatization
    f.write(barrier * 2 + "\n")
    f.write("\\subsection{Axiomatization}\n")
    f.write("\\label{axs:"+label+"}\n")
    f.write(barrier+"\n")
    f.write("\\begin{align}\n")
    f.write("% General Axioms")
    f.write("\\top &\sqsubseteq \\forall\\textsf{place.Holder} \\\\ \n")
    f.write("\\exists\\textsf{place.Holder} &\sqsubseteq \\top \n")
    f.write("% Domain and Range Restrictions")
    f.write("\\top &\sqsubseteq \\forall\\textsf{place.Holder} \\\\ \n")
    f.write("\\exists\\textsf{place.Holder} &\sqsubseteq \\top \n")
    f.write("% Inverse Aliases (if any)")
    f.write("placeholder &\equiv holderplace^- \n")    
    f.write("\\end{align}\n")
    f.write("\n")

    # Create explanations
    f.write(barrier * 2 + "\n")
    f.write("\\subsection{Explanations}\n")
    f.write("\\label{exp:"+label+"}\n")
    f.write(barrier+"\n")
    f.write("\\begin{enumerate}\n")
    f.write("\\item temporary item\n")
    f.write("\\end{enumerate}\n")
    f.write("\n")

    # Create explanations
    f.write(barrier * 2 + "\n")
    f.write("\\subsection{Competency Questions}\n")
    f.write("\\label{cqs:"+label+"}\n")
    f.write(barrier+"\n")
    f.write("\\begin{enumerate}[CQ1.]\n")
    f.write("\\item temporary item\n")
    f.write("\\end{enumerate}\n")
    f.write("\n")
    f.write("\\newpage\n")

    # Creat end document
    f.write(barrier * 2 + "\n")
    f.write("% End Section" + "\n")
    f.write(barrier * 2 + "\n")
    f.write(barrier * 2)


with open("../patterns.tex",'a') as f:
    f.write("\\input{"+loc_file_name+"}\n")

print(pattern_name)
print(file_name)